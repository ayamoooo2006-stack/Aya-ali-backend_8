num = int(input("Enter num (0 - 10) : "))
# p = 5
# if num == p :
#     print("good")
# elif num-p < 2:
#     print(num, p)
# else:
#     print("XXXX")

# for i in range(2,11): # [2,3,4,5,6,7,8,9,10]
#     print(i)

print(2>1)

l = []
for i in range(0,9):  # [0,1,2,3,4,5,6,7,8]
    l.append(i)
print(l)

l2 = [i for i in range(2, 11)]
s2 = {a for a in range(2,11)}
print(l2, s2)
print(s2)