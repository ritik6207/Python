lang = set()
lang.add("java")
lang.add("python")
lang.add("ruby")
print(lang)
lang.update(["c++"])
print(lang)


# Join Python Sets Using "|" Operator
s1={1,2,3,4,5}
s2={4,5,6,7,8}
s3 = s1|s2
print (s3)