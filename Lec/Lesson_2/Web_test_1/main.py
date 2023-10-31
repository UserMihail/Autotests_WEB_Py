import yaml
from module import Site

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
site = Site(testdata["address"])


css_selector = 'span.mdc-text-field__ripple'
print(site.get_element_property("css", css_selector, "height"))


xpath_selector = '//*[@id="login"]/div[3]/button/div'
print(site.get_element_property("xpath", xpath_selector, "color"))
