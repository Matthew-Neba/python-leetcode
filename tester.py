# can slice strings using this notation s[start:stop:step], returns a new string since strings are immutable
s = "asdas"
s_new = s[::-1]
print(s_new)

print([s_new])