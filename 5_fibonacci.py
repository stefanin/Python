#F1=1 F2=2 Fn = Fn-1 + Fn-2 (per ogni n>2)

def fibonacci(numero):
    F=[1,1]
    for n in range(2,numero):
        F.append(F[n-1]+F[n-2])
    return F




F=fibonacci(10)
for L in range(0,len(F)):
    print(str(F[L])+" ",end="")
     

