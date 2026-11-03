'''
# Basic Commands in pdb Terminal

n (next) − Execute the next line of code.
s (step) − Step into a function call.
c (continue) − Continue execution until the next breakpoint.
l (list) − List the current location in the code.
p (print) − Print the value of a variable.
q (quit) − Quit the debugger and exit the program.
b (break) − Set a breakpoint at a specified line number or function.
'''



import pdb

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b


# pdb.set_trace() # Tracing
result = add(10, 20)
print("Addition Result", result)

# pdb.set_trace()
result = subtract(10, 20)
print("Subtraction Result", result)


# Checking Variable Type at Runtime (whatis command)
'''
> /mnt/work/py/ Errors&Exceptions/exp5.py(37)<module>()->None
-> pdb.set_trace()
(Pdb) whatis a
<class 'int'>
(Pdb) wahtis b
*** SyntaxError: invalid syntax
(Pdb) whatis b
<class 'float'>
(Pdb) whatis c
<class 'str'>
(Pdb) 
'''
a = 10
b = 20.5
c = "Hello, World!"

pdb.set_trace()
