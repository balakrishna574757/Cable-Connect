number=5
fact=1


for i   in  range(1,number+1):
 fact=fact*i

print("factorial:",fact)

print("----------------------------")

a=10
b=20
c=30

if a >=b and  a>=c:
 print("a is grater")
elif b>=a and b>=c:
 print("b is grater")

else:
 print("c is grater")  

 print("------------------")
name = "student"
reverse = ""

for i in name:
    reverse = i + reverse

if name == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")

print("-----------------------")
name = "banana"

for i in name:
    count = 0

    for j in name:
        if i == j:
            count += 1

    print(i, count)


print("---------------")
numbers = [10, 20, 10, 30, 20, 40]

new_list = []

for i in numbers:
    if i not in new_list:
        new_list.append(i)

print(new_list)