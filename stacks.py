import backend

class stack():
    def __init__(self, name):
        self.name = name

    def write_property(self, property_, value, id_ = None):
        property_ = str(property_)
        value = str(value)
        if id_ == None:
            register = property_ + ":" + value
            id_ = backend.write_to_db(self.name, register)
            return id_
        else:
            register = backend.query_id(self.name, id_)
            if register is not None:
                start = register.find(";")+2
                register = register[start:-1] + "; " + property_ + ":" + value
                backend.write_previous(self.name, id_, register)
                return id_
            else: return
       
    def query_property(self, property_, value):
        property_ = str(property_)
        value = str(value)
        results = backend.query_db(self.name, property_ + ":" + value)
        return results

    def return_object(self, id_):
        id_ = str(id_)
        answer = backend.query_id(self.name, id_)
        if answer != None:
            return answer[:-1]
        else: return None


    def query_multi_property(self, property_list):    #[(property1, value1), (property2, value2), (propertyN, valueN)]
                                                # User must provide strings
        results = self.property_query(property_list[0][0], property_list[0][1])
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





