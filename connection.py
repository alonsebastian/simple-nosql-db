import backend
from stacks import stack
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

    def delete_stack(self, name):
        os.remove(self.db_name + "_" + name)
        os.remove("." + self.db_name + "_" + name + "_meta")

def test():
    conn = db_connection()
    conn.create_stack("family")
    stack = conn.connect_stack("family")
    return conn, stack
