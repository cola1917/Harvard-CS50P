from response import validemail

def test_validemail():
    assert validemail('malan@harvard.edu') == 'Valid'
    assert validemail('abc@@a..com') == 'Invalid'
    assert validemail('malan@@@harvard.edu') == 'Invalid'
    assert validemail('abc@a.com') == 'Valid'
