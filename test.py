cookie = 5

def test_nonlocal():
    global cookie
    cookie += 1

test_nonlocal()

print(cookie)