def inverterstring(s):
    if (len(s.split()) == 0):
        return("")
    else:
        return f"{s[-1]}{inverterstring(s[0:len(s)-1])}"
print(inverterstring("ABCD"))