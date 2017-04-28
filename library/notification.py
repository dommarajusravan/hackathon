# from plugins/callback/slack.py
"""
Call Back class
"""

from ansible.plugins.callback import CallbackBase
#from ansible import constants as C
import psycopg2

class CallbackModule(CallbackBase):
    """
    update data to db
    """
    def update_db(self, task_name, description, state):
        try:
            print task_name
            weightage = {'Gathering Facts':10, 'POST_task_1':5, 'debug':10, \
            'Create_script':30, 'POST_task_2':5, 'POST_task_3':5, \
            'Launch VM':25, 'Verify vm':10, 'assert':0}
            conn_string = "host='localhost' dbname='my_database' user='opsimple' \
            password='opsimple'"
            conn = psycopg2.connect(conn_string)
            cursor = conn.cursor()
            query = "INSERT INTO progress (name,progress,status,description) VALUES \
            ('{}', {},'{}', '{}' );".format( \
            task_name, weightage.get(task_name), state, description);
            cursor.execute(query)
            conn.commit()
            cursor.close()
        except Exception:
            print "I am unable to connect to the database"

    """
    executes on failure of task

    """
    def v2_runner_on_failed(self, result, ignore_errors=False):
        #import pdb;pdb.set_trace();
        self.update_db(result._task.get_name(), result._result.get('msg'), "FAILED")
        #import pdb;pdb.set_trace()
        #print(result._result['exception'].strip().split('\n')[-1])
    """
    executes on successfully completed task
    """
    def v2_runner_on_ok(self, result):
        self.update_db(result._task.get_name(), "Successfully Executed.", "SUCCESS")
        #print(result._task.get_name())
        #print(result._host)
        #import pdb;pdb.set_trace()
        #print(result._task.dump_attrs())
        #print(result._task.dump_me(1))
        #self.update_db(result._task.get_name())
        #if result._task.action:
        #self._display.display("%s | SUCCESS => %s" % (result._host.get_name(), \
        #self._dump_results(result._result, indent=0).replace('\n','')), color=C.COLOR_OK)
