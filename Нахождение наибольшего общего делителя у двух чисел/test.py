def test_positive():
    assert evc(10, 5) == 5, "evc(10, 5) should be 5"
    assert evc(10, 50) == 10, "evc(10, 50) should be 10"
    assert evc(15, 27) == 3, "evc(15, 27) should be 3"
    assert evc(6, 14) == 2, "evc(6, 14) should be 2"
    assert evc(150, 120) == 30, "evc(150, 120) should be 30"
    assert evc(17, 120) == 1, "evc(17, 120) should be 1"


def test_negative():
    assert evc(0, 5) == 0, "Testing 0 failed..."
    assert evc(3, 0) == 0, "Testing 0 failed..."
    assert evc(0, 0) == 0, "Testing 0 failed..."
    assert evc(1, 0) == 0, "Testing 0 failed..."
    assert evc(0, 1) == 0, "Testing 0 failed..."
    assert evc(-1, 1) == 0, "Testing negative failed..."
    assert evc(-17, 17) == 0, "Testing negative failed..."
    assert evc(-22, -25) == 0, "Testing negative failed..."
    assert evc(0.5, 0.5) == 0, "Testing not natural failed..."
    assert evc(1, 0.5) == 0, "Testing not natural failed..."
    assert evc(10, 0.5) == 0, "Testing not natural failed..."
    assert evc(10.7, 355) == 0, "Testing not natural failed..."


def evc(a: int, b: int) -> int:
    if a <= 0 or b <= 0 or not type(a) == int or not type(b) == int:
        return 0
    while b != 0:
        a, b = b, a % b
    return a


if __name__ == "__main__":
    test_positive()
    test_negative()
    print("Everything passed")
