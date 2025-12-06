def has_QOCD(s):
    return any(ch in s for ch in "QOCD")

if __name__ == "__main__":
    assert has_QOCD("QuicK") == True
    assert has_QOCD("Odd") == True
    assert has_QOCD("MAC") == True
    assert has_QOCD("WILD") == True
    assert has_QOCD("MATH") == False
    assert has_QOCD("comp123") == False
    print("All tests passed!")
