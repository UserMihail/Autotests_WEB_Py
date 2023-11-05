from testpage import OperationsHelper
import logging
import yaml

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)

def teststep1(browser):
    logging.info("Test1 Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata.get("login"))
    testpage.enter_pass(testdata.get("password"))
    testpage.clik_login_button()
    assert testpage.get_error_text() == "401"

def teststep2(browser):
    logging.info("Test2 Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("login")
    testpage.enter_pass("password")
    testpage.clik_login_button()
    assert "hello" in testpage.get_text().lower(), "Failed"

