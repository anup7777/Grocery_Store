from admin.connection import MyDatabase

class Adminbackend:
    def __init__(self):
        self.my_db = MyDatabase()

    def check_login(self,username,password):
        if len(username)==0 or len(password)==0:
            return False
        else:
            values = self.my_db.fetchingdata_login()
            if (username ==values[0][0] and password==values[0][1]):
                return True
            else:
                return False

    """# SERVICES
    
    def service_backend_showdata(self):
        customer_data=[]
        qry = "SELECT * from services"
        service_data = self.my_db.return_data_frmdatabase(qry)
        return service_data
    
    def service_add(self, product_name, product_type, product_price,product_availability):"""
