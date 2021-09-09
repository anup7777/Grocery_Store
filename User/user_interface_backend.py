from admin.connection import MyDatabase

class Customerbackend:
    def __init__(self):
        self.my_db = MyDatabase()

    # changing credentials
    def return_customer_search_data(self, search_value):
        qry = "SELECT customer_credentials.password FROM customer_credentials where username =%s"
        value = (search_value,)
        req_data = self.my_db.return_data_frmdatabase_wthreturn(qry, value)
        return req_data

    # update customer login credential
    def update_customer_login_data(self, providedpassword, search_value):
        qry = "UPDATE customer_credentials SET password=%s where username =%s"
        value = (providedpassword, search_value,)
        self.my_db.add_update_delete(qry, value)
        return True


