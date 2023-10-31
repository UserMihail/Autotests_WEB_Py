import yaml
from module import Site
import pytest

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)

@pytest.fixture()
def selector_login():
    return """// *[ @ id = "login"] / div[1] / label / input"""
@pytest.fixture()
def selector_password():
    return """// *[ @ id = "login"] / div[2] / label / input"""
@pytest.fixture()
def selector_button():
    return "button"
@pytest.fixture()
def selector_error():
    return """//*[@id="app"]/main/div/div/div[2]/h2"""
@pytest.fixture()
def selector_home():
    return """//*[@id="app"]/main/nav/a/span"""

"""Enter element HW_2"""
@pytest.fixture()
def selector_button1():
    return "#create-btn"
@pytest.fixture()
def selector_fistname():
    return """//*[@id="upsert-item"]/div[1]/label/input"""
@pytest.fixture()
def selector_loginprof():
    return """//*[@id="upsert-item"]/div[5]/label/input"""
@pytest.fixture()
def selector_save():
    return "div.submit > button > span"

@pytest.fixture()
def selector_home_name():
    return """//*[@id="app"]/main/div/div/div[1]/div[1]/table/tbody/tr[1]/td[2]"""

@pytest.fixture()
def site():
    site_inst = Site(testdata["address"])
    yield site_inst
    site_inst.my_quit()
