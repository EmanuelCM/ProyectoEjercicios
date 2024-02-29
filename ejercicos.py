op=3

def calcularIva(precio):
    precio=precio*1.19
    return precio

def calculoDesc(precio,descuento):
    precioFinal= (precio-(precio*(descuento/100)))
    return precioFinal

def calculoImc(peso,estatura):
    condicion=""
    imc=peso/(estatura**2)
    if imc < 18.5:
        condicion="Bajo Peso"
    elif imc >= 18.5 and imc<=24.9:
        condicion="Adecuado"
    elif imc >= 25 and imc<=29.9:
        condicion="Obesidad"    
    elif imc >= 30.0 and imc<=34.9:
        condicion="Obesidad Grado 1"
    elif imc >= 35 and imc<=39.9:
        condicion="Obesidad Grado 2"
    else:
        condicion="Obesidad Grado 3" 
    return imc,condicion    
   

    
    
    

while op != 4:
    print("       Menu      " )
    print("**"*10 )
    print("1. Calcular Iva")
    print("2. Calcular Descuento")
    print("3. Calcular IMC")
    print("4. Salir")
    op= int(input("Ingresar la opcion:(1-4)"))
    
    if op == 1:
        precio=int(input("Ingrese el valor del producto: "))
        precio= calcularIva(precio)    
        print(precio)
    
    if op ==2:
        precio=int(input("Ingrese el valor del producto: "))
        descuento=int(input("Ingrese el '%' de descuento: "))
        precioFinal=calculoDesc(precio,descuento)
        print(f"El valor final del producto es S/.{precioFinal} y tiene un descuento del {descuento}%")
    
    if op==3:
        imc=[]
        peso= float(input("Ingrese su peso: "))
        estatura= float(input("Ingrese su estatura: "))
        imc,condicion=calculoImc(peso,estatura)
        print(f"Su IMC es: {imc} y se encuentra con {condicion}")
            
        