name = input("what's your name")
sname = input("and what's your surname?")
#removes the white space from the name and capialise
name=name.strip().capitalize()
sname=sname.strip().capitalize()

print(f"hello, " + name + " " + sname)
