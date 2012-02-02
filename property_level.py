import backend

def property_write(property_, value, id_ = None):
    property_ = str(property_)
    value = str(value)
    id_ = str(id_)
    if id_ != None:
        register = backend.query_id(id_)
        start = register.find(";")+2
        register = register[start:-1] + "; " + property_ + ":" + value
        backend.write_previous(id_, register)
        return id_
    else:
        register = property_ + ":" + value
        id_ = backend.write_to_db(register)
        return id_
   
def property_query(property_, value):
    property_ = str(property_)
    value = str(value)
    results = backend.query_db(property_ + ":" + value)
    return results

def return_object(id_):
    id_ = str(id_)
    return backend.query_id(id_)[:-1]

def multi_property_query(property_list):    #[(property1, value1), (property2, value2), (propertyN, valueN)]
                                            # User must provide strings
    results = property_query(property_list[0][0], property_list[0][1])
    answer = []
    if len(results) == 1:
        return results
    else:
        for result in results:
            for item in property_list:
                if not item[0] + ":" + item[1] in result:
                    break
            #every item is in result
            answer.append(result)
        return answer
