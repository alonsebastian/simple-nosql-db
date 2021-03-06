import os

def create_stack(name):
    if not os.path.exists("." + name + "_meta"):
        result = os.popen('echo "bashDB by Sebastian Alonso 2012" > ' + name).read()
        result = os.popen("touch ." + name + "_meta").read()
        result = os.popen('echo "0" > .' + name + '_meta').read()
        return True
    else:
        return "this stack already exists"

def reset_stack(name):
    result = os.popen('echo "bashDB by Sebastian Alonso 2012" > ' + name).read()
    result = os.popen("touch ." + name + "_meta").read()
    result = os.popen('echo "0" > .' + name + '_meta').read()
    return True

def write_to_db(name, data):
    print os.path.exists("." + name + "_meta")
    if os.path.exists("." + name + "_meta"):
        number = os.popen("cat ." + name + "_meta").read()
        number = int(number) + 1
        result = os.popen("echo " + str(number) + " > ." + name + "_meta").read()
        string = 'echo "' + str(number) + "; " + str(data) + '" >> ' + name
        result = os.popen(string).read()
        return number
    else:
        return "The database has not been created yet. Please use method create_stack()"

def write_previous(name, number, line):
    number = int(number)
    result = os.popen('sed -i "' + str(number+1) + 'c' + str(number) + '; ' + line + '" ' + name).read()
    return result


def query_db(name, query):
    result = os.popen("grep " + str(query) + " " + name).read()
    if "\n" in result:
        results_list = result.split("\n")
        results_list = results_list[:-1] #leave outside the ''
        return results_list
    else:
        return result

def query_id(name, query):
    result = os.popen('grep "^' + str(query) + ';." ' + name).read()
    if result != "":
        return result
    else: return None

if __name__ == "__main__":
    for number in range(100):
        number = str(number) * 5
        write_to_db(number)
