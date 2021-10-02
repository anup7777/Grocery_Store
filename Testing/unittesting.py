import unittest
from admin.admin_interface_backend import Adminbackend
from Staff.staff_interface_backend import Staffbackend
from User.user_interface_backend import Customerbackend
from admin.connection import MyDatabase

class Mytest(unittest.TestCase):

    admin_backend = Adminbackend()
    staff_backend = Staffbackend()
    user_backend = Customerbackend()

    def test_check_admin_login_empty_data(self):
        result=self.admin_backend.check_login("","")
        self.assertFalse(result)

    def test_check_admin_login(self):
        result = self.admin_backend.check_login("test", "test")
        self.assertFalse(result)

    def test_check_admin_login_realdata(self):
        result = self.admin_backend.check_login("admin", "admin1234")
        self.assertTrue(result)

    def test_add_services(self):
        result = self.admin_backend.product_add("test_name","test_type","100", "test_company","test_availability")
        self.assertTrue(result)

    def test_add_services_priceistext(self):
        result = self.admin_backend.product_add("test_name","test_type","test_price", "test_company","test_availability")
        self.assertTrue(result)


