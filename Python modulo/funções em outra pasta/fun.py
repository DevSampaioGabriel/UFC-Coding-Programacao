
def contador (n):
     n = int(input('Digite um número: '))
    temp = n
    i = 0
    cont = 0

    while temp > 0:
        i += 1
        temp -= temp%(10**i)
        x = ((n%(10**i)) - ((n%(10**(i-1)))/(10**(i-1)))
        if x == 2:
            cont += 1
    print(f'O número {n} aparece %d vezes' %cont)'''
