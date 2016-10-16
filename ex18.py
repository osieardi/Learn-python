#this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print("arg1: %r, arg2: %r" % (arg1, arg2))

#ok, that *args is accually pointles, we can just do this
def print_two_again(arg1, arg2):
    print("arg1: %r, arg2: %r" % (arg1, arg2))

#only 1 argument
def print_one(arg1):
    print("arg1: %r" % arg1)

def print_none():
    print("I got nothing.")

print_two("Ossie","Ardi")
print_two_again("Ossie","Ardi")
print_one("First!")
print_none()
