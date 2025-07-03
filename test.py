cookie = 5

def test_nonlocal():
    cookie += 1

test_nonlocal()

print(cookie)