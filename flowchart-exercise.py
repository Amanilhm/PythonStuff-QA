num_a = float(input('Please give me a number a : '))
num_b = float(input('Please give me a number b : '))
num_c = float(input('Please give me a number c : '))

if (num_a > num_b): 
    if (num_a > num_c):
        print('a')
    else: 
        print('c')
else:
    if num_b > num_c:
        print('b')
    else:
        print('c')