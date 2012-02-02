import os

def create_db(name):
    result = os.popen("touch " + name).read()
    result = os.popen('echo "bashDB by Sebastian Alonso 2012" > ' + name).read()
    result = os.popen("touch ." + name + "_meta").read()
    result = os.popen('echo "0" > .' + name + '_meta').read()
    return True

def reset_db(name):
    temp = os.popen("rm " + name + " ; rm ." + name + "_meta")
    return True



def write_to_db(data):
    returned = os.popen('if [ -e ".basedb_meta" ]; then echo "ok"; fi').read()
    if returned == "ok\n":
        number = os.popen("cat .basedb_meta").read()
        number = int(number) + 1
        result = os.popen("echo " + str(number) + " > .basedb_meta").read()
        string = 'echo "' + str(number) + "; " + str(data) + '" >> base.db'
        result = os.popen(string).read()
        return number
    else:
        return "The database has not been created yet. Please use method create_db()"

def write_previous(number, line):
    number = int(number)
    result = os.popen('sed -i "' + str(number+1) + 'c' + str(number) + '; ' + line + '" base.db').read()
    return result

def create_db(name):
    result = os.popen("touch " + name).read()
    result = os.popen('echo "bashDB by Sebastian Alonso 2012" > ' + name).read()
    result = os.popen("touch ." + name + "_meta").read()
    result = os.popen('echo "0" > .' + name + '_meta').read()
    return True

def query_db(query):
    result = os.popen("grep " + str(query) + " base.db").read()
    if "\n" in result:
        results_list = result.split("\n")
        results_list = results_list[:-1] #leave outside the ''
        return results_list
    else:
        return result

def query_id(query):
    result = os.popen('grep "^' + str(query) + ';." base.db').read()
    if result != "":
        return result
    else: return None

if __name__ == "__main__":
    for number in range(100):
        number = str(number) * 5
        write_to_db(number)
