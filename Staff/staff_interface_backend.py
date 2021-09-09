#  Importing all the necessary modules
from admin.connection import MyDatabase

class Staffbackend:
    def __init__(self):
        self.my_db = MyDatabase()

    # changing credentials
    def return_staff_search_data(self, search_value):
        qry = "SELECT staff_credentials.password FROM staff_credentials where username =%s"
        value = (search_value,)
        req_data = self.my_db.return_data_frmdatabase_wthreturn(qry, value)
        return req_data

    # update staff login credential
    def update_staff_login_data(self,providedpassword,search_value):
        qry = "UPDATE staff_credentials SET password=%s where username =%s"
        value = (providedpassword,search_value,)
        self.my_db.add_update_delete(qry, value)
        return True

