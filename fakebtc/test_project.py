from project import purchase, parser, overview
def test_purchase():
    assert purchase(1, 0) == '0 do not need purchase'
    assert purchase(2, 0.0) == '0.0 do not need purchase'
    assert purchase(-1,0.1) == '0.1 BTC has purchased, cost -0.1$'
    assert purchase(3, 1.0) == '1.0 BTC has purchased, cost 3.0$'
    assert purchase(1, -0.1) == '0.1 BTC has sold, get -0.1$'

def test_parser():
    assert parser(0, 1)['price'] == 0
    assert parser(100, 2)['amount'] == 2
    assert parser(100, -1)['amount'] == -1
    assert parser(100, 0)['price'] == 100
    assert parser(-100, 1)['price'] == -100


def test_overview():
    assert overview() == 'no record'


# def test_function_n():
#     ...
