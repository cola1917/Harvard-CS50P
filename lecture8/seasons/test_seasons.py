from seasons import convert


def test_date():
    assert convert(10477) == "Fifteen million, eighty-six thousand, eight hundred eighty minutes"
    assert convert(365) == "Five hundred twenty-five thousand, six hundred minutes"
    assert convert(364) == "Five hundred twenty-four thousand, one hundred sixty minutes"
    assert convert(363) == "Five hundred twenty-two thousand, seven hundred twenty minutes"
