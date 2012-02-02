import backend
from property_level import stack
import os

class db_connection():
    def __init__(self, db_name = "base.db"):
        self.db_name = db_name

    def create_stack(self, name):
        name = self.db_name + "_" + name
        backend.create_stack(name)

    def reset_stack(self, name):
        name = self.db_name + "_" + name
        return backend.reset_stack(name)

    def connect_stack (self, name):
        name = self.db_name + "_" + name
        self.stack = stack(name)
        return self.stack
