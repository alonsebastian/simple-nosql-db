import backend

def property_write(property_, value, id_ = None):
    if id_ != None:
        register = backend.query_id(id_)
        start = register.find(";")+2
        register = register[start:-1] + "; " + property_ + ":" + value
        print "register: " + register
        backend.write_previous(id_, register)
        return True
    else:
        register = property_ + ":" + value
        backend.write_to_db(register)
        return True
