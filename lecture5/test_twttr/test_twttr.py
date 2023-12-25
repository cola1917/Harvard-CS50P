import pytest
from twttr import shorten


# def test_shorten():
#     assert shorten("aeiouAEIOU0.bB") == "0.bB"

# def test_empty():
#     assert shorten('') == 'Output: '

# def test_a_vowel():
#     assert shorten('a') == 'Output: '

# def test_a_vowel_and_a_normal():
#     assert shorten('ab') == 'Output: b'

# def test_normal():
#     assert shorten('In the text editor window') == 'Output: n th txt dtr wndw'
def test_shorten():
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""
    assert shorten("Twitter") == "Twttr"
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("CS50PDF") == "CS50PDF"

# def test_error():
#     assert shorten('In') == 'Output: In'



