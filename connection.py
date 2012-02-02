import backend
import propertyLayer
import os

class db_connection():
    def __init__(self, db_name = "base.db"):
        self.db_name = db_name

    def create_db(self):
        backend.create_db(self.db_name)

    def reset_db(self):
        return backend.reset_db(self.db_name)






    def create_object(self, property_, value):
        return propertyLayer.property_write(property_, value)

    def add_to_object(self, property_, value, id_):
        return propertyLayer.property_write(property_, value, id_)

    def single_query(self, property_, value):
        return propertyLayer.property_query(property_, value)

    def multi_query(self, property_list):
        return propertyLayer.multi_property_query(property_list)

    def id_query(self, id_):
        return propertyLayer.return_object(id_)

