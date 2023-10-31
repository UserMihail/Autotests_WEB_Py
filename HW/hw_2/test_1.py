import yaml
from module import Site
import pytest

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
# site = Site(testdata["address"])
def test_step1(site, selector_login, selector_password,
               selector_button, selector_home, selector_button1,
               selector_fistname, selector_loginprof,
               selector_save, selector_home_name):

    input1 = site.find_element("xpath", selector_login)
    input1.send_keys(testdata.get("username"))

    input2 = site.find_element("xpath", selector_password)
    input2.send_keys(testdata.get("password"))

    btn = site.find_element("css", selector_button)
    btn.click()

    input3 = site.find_element("xpath", selector_home)
    assert input3.text == "Home", "test Fail"

    """Enter element HW_2"""
    btn1 = site.find_element("css", selector_button1)
    btn1.click()

    input4 = site.find_element("xpath", selector_fistname)
    input4.send_keys(testdata.get("fistname"))

    input5 = site.find_element("xpath", selector_loginprof)
    input5.send_keys(testdata.get("login"))

    btn2 = site.find_element("css", selector_save)
    btn2.click()

    input6 = site.find_element("xpath", selector_home_name)
    assert input6.text == "Mihail", "test Fail for home name"




if __name__ == "__main__":
    pytest.main(["-vv"])

