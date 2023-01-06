stu_num = [i for i in range(1, 31)]

for _ in range(28):
    num = int(input()) 
    stu_num.remove(num)

print(min(stu_num))
print(max(stu_num))