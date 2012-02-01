import os

def write_to_db(data):
    number = os.popen("cat .basedb_meta").read()
    number = int(number) + 1
    result = os.popen("echo " + str(number) + " > .basedb_meta").read()
    string = 'echo "' + str(number) + "; " + str(data) + '" >> base.db'
    result = os.popen(string).read()
    return True

def create_db():
    result = os.popen("touch base.db").read()
    result = os.popen('echo "bashDB by Sebastian Alonso 2012" > base.db').read()
    result = os.popen("touch .basedb_meta").read()
    result = os.popen('echo "0" > .basedb_meta').read()
    return True

def query_db(query):
    result = os.popen("grep " + str(query) + " base.db").read()
    if "\n" in result:
        results_list = result.split("\n")
        results_list = results_list[:-1] #leave outside the ''
    return results_list

def query_id(query):
    result = os.popen('grep "^' + str(query) + ';." base.db').read()
    return result
