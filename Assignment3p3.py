def string_test(s):
    d={"Upper_case":0,"Lower_case":0}
    for c in s:
        if c.isupper():
          d["Upper_case"]+=1
        elif c.islower():
            d["Lower_case"]+=1
        else:
            pass
    print(f"original string",s)
    print("number of Upere case alphabets:",d["Upper_case"])
    print("number of Lower case alphabets:",d["Lower_case"])
string_test("The quick Brow Fox")

