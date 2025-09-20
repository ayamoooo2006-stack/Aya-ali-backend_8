# student info
f_name = 'Aya'
l_name = "Ali"
age = 19
major = 'Computer'
GPA = 3.5

# list example
g = [80, 50, 5, 35, 54, 'Aya', [1, 2, 3]]
print(g[:5])
print(g)

# set example
x = {1, 9, 8, 87}
print(x)
x.add('Aya')
print(x)
x.add('Ali')
print(x)

# dictionary example
std_1 = {
    "f_name": "Aya",
    "l_name": "Ali",
    'gpa': 3.5,
    'major': 'Computer',
    "G": [80, 50, 5, 35, 54, 'Aya', [1, 2, 3], {'1': "2"}]
}
print(std_1['major'])
print(std_1['G'][3])

# tuple examples
p = (0, 1, 6, 6)
USER_TYPE = ('admin', 'user', 'dev')
color = (
    ('#000', 'black'),
)
r = ("a")
r2 = ('username',)
print(type(r), type(r2))