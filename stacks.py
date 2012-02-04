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
            return db_object(id_ + "; " + register, self)
        else:
            register = backend.query_id(self.name, id_)
            if register is not None:
                start = register.find(";")+2
                register = register[start:-1] + "; " + property_ + ":" + value
                backend.write_previous(self.name, id_, register)
                return db_object(id_ + "; " + register, self)
            else: return

    def write_full_object(self, id_, register):
        #does not return db_object, cause it's mainly used by it
        backend.write_previous(self.name, id_, register)
        return

    def query_property(self, property_, value):
        property_ = str(property_)
        value = str(value)
        results = backend.query_db(self.name, property_ + ":" + value)
        for result in results:
            result = db_object(result, self)
        return results

    def return_object(self, id_):
        id_ = str(id_)
        answer = backend.query_id(self.name, id_)
        if answer != None:
            return db_object(answer[:-1], self)
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

class db_object():
    def __init__(self, record, stack):
        self.stack = stack
        self.record = record
        print "record: " + self.record
        self.property_list = self.record.split(";")
        print "list: "
        print self.property_list
        self.id_ = self.property_list[0]
        print "id: " + self.id_

    def __getitem__(self, property_):
        self.answer = False
        for self.property_record in self.property_list:
            if property_ in self.property_record:
                self.answer = self.property_record.split(":")[1]
                break
        return self.answer

    def __setitem__(self, property_, value):
        for self.property_record in self.property_list:
            if property_ in self.property_record:
                self.temp = self.property_record.split(":")
                print "aca va temp: "
                print self.temp
                self.temp[1] = value
                self.record = ""
                count = 0
                for property__ in self.property_list:
                    if property__ != self.property_record and count > 0:
                        self.record += property__
                    count += 1
                print "registro: " + self.record
                self.record += self.temp[0] + ":" + self.temp[1]
                self.stack.write_full_object(self.id_, self.record)
                self.property_list = self.record.split(";")
                return
                
        self.stack.write_property(property_, value, self.id_)
        self.property_list.append(property_ + ":" + value)
        print "record: " + self.record
        print "list: "
        print self.property_list
        return True
                




















