num = int(input ('what is the range you want to check'))
#
# if num > 1 :
#     for i in range(2,num+1):
#         if num % i != 0:
#             print (f'this is a prime Number  {i}')
#         else:
#             print(f'This is not a prime number{i}')
#
# if num > 1:
#
#     for i in range(2, num):
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             print(i, "times", num // i, "is", num)
#             break
#         else:
#             print(num, "is a prime number")
num_list = []
if num > 1:
    for i in range(2,num+1):
        num_list.append(i)
    for p in num_list:
        if p > 1 and i%p != 0:
            print (f'{p} is not a prime number')
        else:
            print(f'{p} is a prime number')