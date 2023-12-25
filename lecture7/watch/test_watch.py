from watch import parse
# def test_parse_out_iframe():
#     assert parse('http://youtube.com/embed/xvFZjo5PgG0') == 'https://youtu.be/xvFZjo5PgG0'
#     assert parse('https://youtube.com/embed/xvFZjo5PgG0') == 'https://youtu.be/xvFZjo5PgG0'
#     assert parse('https://www.youtube.com/embed/xvFZjo5PgG0') == 'https://youtu.be/xvFZjo5PgG0'

def test_parse_in_iframe():
    assert parse('<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>') == 'https://youtu.be/xvFZjo5PgG0'
    assert parse('<iframe width="560" src="https://www.youtube.com/embed/xvFZjo5PgG0" frameborder="0"></iframe>') == 'https://youtu.be/xvFZjo5PgG0'
