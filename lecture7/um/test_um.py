from um import count

def test_count():
    assert count('um') == 1
    assert count('') == 0
    assert count('um?') == 1
    assert count('Um, thanks for the album.') == 1
    assert count('Um, thanks, um...') == 2
def test_count_upper():
    assert count('UM') == 1
    assert count('') == 0
    assert count('aUma') == 0
    assert count('aUmaauMa') == 0
