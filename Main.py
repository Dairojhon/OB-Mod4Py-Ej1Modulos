import Operaciones

def main():
    a=int(input("Por favor digite el primer numero a operar: "))
    b=int(input("Por favor digite el segundo numero a operar, en caso de la división sera el divisor: "))
    sum=Operaciones.suma(a,b)
    res=Operaciones.resta(a,b)
    prod=Operaciones.producto(a,b)
    if b==0:
        div= "Syntax Error; esta operación no se puede realizar"
    else:
        div=Operaciones.division(a,b)

    print("El resultado de la suma es",sum)
    print("El resultado de la resta es",res)
    print("El resultado de la multiplicación es",prod)
    print("El resultado de la división es",div)

if __name__ =="__main__":
    main()