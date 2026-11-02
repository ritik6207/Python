# Binary to Int

myStr = '01000101'

def strtoint(myStr):
    for x in myStr:
        if x not in '01': return "Error. String with non-binary character"
    num = int(myStr, 2)
    return num
print ("binary:{} integer: {}".format(myStr,strtoint(myStr)))

digits = [str(x) for x in range(10)]
print(digits)
mystr = 'He12llo, Py00th55on!'
chars = []
for x in mystr:
   if x not in digits:
      chars.append(x)
newstr = ''.join(chars)
print (newstr)