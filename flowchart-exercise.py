num_a = float(input('Please give me a number a : '))
num_b = float(input('Please give me a number b : '))
num_c = float(input('Please give me a number c : '))

if (num_a > num_b): 
    if (num_a > num_c):
        print(num_a)
    else: 
        print(num_c)
else:
    if num_b > num_c:
        print(num_b)
    else:
        print(num_c)
