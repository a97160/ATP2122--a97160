def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n > 1:
        return fib(n-1) + fib(n-2)
    else:
        return 0 

lista = []   
for i in range(20):
    lista.append(fib(i)) #append junta 
print(lista)

def fib_iterativa(n):
    lista = []
    for i in range(n):
        if i == 0:
            lista.append(1)

        elif i == 1:
            lista. append(1)

        elif i > 1:
            lista.append(lista[-1] + lista[-2])

    return lista[-1]
    
