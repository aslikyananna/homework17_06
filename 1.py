import string
x = input("write something")
z = str()
for i in x:
    if i not in string.punctuation:
        z = z + i
z = z.lower()
z = z.split()
d = {}
y = []
for i in range(len(z)):
    result = z.count(z[i])
    y.append(result)
d = dict(zip(z, y))
print(d)
