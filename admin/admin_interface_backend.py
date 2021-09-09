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

        #  Product

    def product_backend_showdata(self):
        product_data = []
        qry = "SELECT * from product"
        product_data = self.my_db.return_data_frmdatabase(qry)
        return product_data

    def product_add(self, pro_name, pro_type, pro_price, pro_company, pro_expiry):
        qry = "INSERT INTO product (Product_name,Product_type,Product_price,Product_company,Product_expiry) VALUES (%s,%s,%s,%s,%s)"
        values = (pro_name, pro_type, pro_price, pro_company, pro_expiry)
        self.my_db.add_update_delete(qry, values)
        return True

    def product_status_update(self, row, pro_name, pro_type, pro_price, pro_company, pro_expiry):
        qry = "UPDATE product SET Product_name=%s, Product_type=%s, Product_price=%s,Product_company=%s,Product_expiry=%s where id=%s"
        values = (pro_name, pro_type, pro_price, pro_company, pro_expiry, row)
        self.my_db.add_update_delete(qry, values)
        return True

    def return_product_search_data(self, search_value, search_by):
        qry = "SELECT * from product where " + search_by + "=%s"
        value = (search_value,)
        req_data = self.my_db.return_data_frmdatabase_wthreturn(qry, value)
        return req_data

    def delete_product(self, row):
        qry = "DELETE FROM product WHERE product.id=%s"
        value = (row,)
        self.my_db.add_update_delete(qry, value)
        return True

        # Customer

    def customer_backend_showdata(self):
        customer_data = []
        qry = "SELECT * from customer_credentials"
        customer_data = self.my_db.return_data_frmdatabase(qry)
        # print(customer_data)
        return customer_data

    def customer_status_update(self, row, name, age, gender, address, email,
                               admin_approval):
        qry = "UPDATE customer_credentials SET Customer_Name=%s,Customer_Age=%s,Customer_Gender=%s,Customer_Address=%s,Customer_Email=%s,Admin_Approval=%s where id=%s"
        values = (name, age, gender, address, email, admin_approval, row)
        self.my_db.add_update_delete(qry, values)
        return True

    def return_customer_search_data(self, search_value, search_by):
        qry = "SELECT * from customer_credentials where " + search_by + "=%s"
        value = (search_value,)
        req_data = self.my_db.return_data_frmdatabase_wthreturn(qry, value)
        return req_data

    def delete_customer(self, row):
        qry = "DELETE FROM customer_credentials WHERE customer_credentials.id=%s"
        value = (row,)
        self.my_db.add_update_delete(qry, value)
        return True

        # Staff

    def staff_backend_showdata(self):
        staff_data = []
        qry = "SELECT * from staff_credentials"
        staff_data = self.my_db.return_data_frmdatabase(qry)
        return staff_data

    def staff_status_update(self, row, name, age, gender, address, admin_approval):
        qry = "UPDATE staff_credentials SET Staff_Name=%s,Staff_Age=%s,Staff_Gender=%s,Staff_Address=%s,Admin_approval=%s where id=%s"
        values = (name, age, gender, address, admin_approval, row)
        self.my_db.add_update_delete(qry, values)
        return True

    def return_staff_search_data(self, search_value, search_by):
        qry = "SELECT * from staff_credentials where " + search_by + "=%s"
        value = (search_value,)
        req_data = self.my_db.return_data_frmdatabase_wthreturn(qry, value)
        return req_data

    def delete_staffs(self, row):
        qry = "DELETE FROM staff_credentials WHERE staff_credentials.id=%s"
        value = (row,)
        self.my_db.add_update_delete(qry, value)
        return True

