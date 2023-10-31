import yaml
from module import Site
import pytest

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
site = Site(testdata["address"])
# Переименуем фаил main в test_1 чтобы его видел пайтест

def test_step1():

    x_selector1 = '//*[@id="login"]/div[1]/label/input'
    input1 = site.find_element("xpath", x_selector1)
    input1.send_keys("test")
    x_selector2 = '//*[@id="login"]/div[2]/label/input'
    input2 = site.find_element("xpath", x_selector2)
    input2.send_keys("test")
    btn_selector = "button"
    btn = site.find_element("css", btn_selector)
    btn.click()
    x_selector3 = '//*[@id="app"]/main/div/div/div[2]/h2'
    err_label = site.find_element("xpath", x_selector3)

    assert err_label.text == "401"

if __name__ == "__main__":
    pytest.main(["-vv"])