def printName(first_name, last_name, reverse = False):
  '''
  Use Keyword arguments and default value
  reverse parameter is given explicit value of false
  OR I can leave reverse value to be implicit, in that case, I have to make it explicit 
  when calling printName function as shown in line 14
  '''
  if reverse:
    print(last_name + " " + first_name)
  else:
    print(first_name + " " + last_name)

printName("Tunde",  "Hammed")
printName("Tunde", "Hammed", True)

def foos(x, y = 5):
    def bar(x):
        return x + 1
        
    return bar(y * 2)

print(foos(3))

def foo(x, y = 5):
    def bar(x):
        return x + 1
        
    return bar(y * 2)

print(foo(3, 0))