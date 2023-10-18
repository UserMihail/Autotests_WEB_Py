from zeep import Client

wsdl = "http://dss.cryptopro.ru/verify/service.svc?wsdl"
sign = ' ' # нужна электронная подпись

client = Client(wsdl=wsdl)

def test_step2(): # запуcтим через pytest, проверка подписи
    assert client.service.VerifySignature('CMS', sign)['Result']