def main():
    numeros_suma_r = []
    numeros_suma_i = []
    numeros_resta_r = []
    numeros_resta_i = []
    numeros_mult_i = []
    numeros_mult_r = []
    print("1 -> Sumar")
    print("2 -> Restar")
    print("3 -> Multiplicar")
    print("4 -> Al cuadrado")
    x = int(input("Que tipo de operacion va a realizar? "))    
    if( x == 1):
        for i in range(2):
            num1_suma = int(input("Ingresa los numeros reales -> "))
            numeros_suma_r.append(num1_suma)
        for i in range(2):
            num2_suma = int(input("Ingresa los numeros imaginarios-> "))
            numeros_suma_i.append(num2_suma)
        sumas_r_parcial = numeros_suma_r[0]+ numeros_suma_r[1]
        sumas_i_parcial = numeros_suma_i[0] + numeros_suma_i[1]
        
        print(sumas_r_parcial , str(sumas_i_parcial)+"i")
        sumas_totales = sumas_r_parcial , sumas_i_parcial
        #print(sumas_totales)
    if (x ==2):
        for i in range(2):
            num1_resta = int(input("Ingresa los numeros reales -> "))
            numeros_resta_r.append(num1_resta)
        for i in range(2):
            num2_resta = int(input("Ingresa los numeros imaginarios-> "))
            numeros_resta_i.append(num2_resta)

        resta_parcial_r = numeros_resta_r[0] - numeros_resta_r[1]
        resta_parcial_i = numeros_resta_i[0] - abs(numeros_resta_i[1])
        
            
        print(resta_parcial_r,str(resta_parcial_i)+"i")
        

    if (x ==3):
        for i in range(2):
            num1_mult = int(input("Ingresa los numeros reales -> "))
            numeros_mult_r.append(num1_mult)
        for i in range(2):
            num2_mult = int(input("Ingresa los numeros imaginarios-> "))
            numeros_mult_i.append(num2_mult)

        mult_parcial_r = (numeros_mult_r[0] * numeros_mult_r[1]) - (numeros_mult_i[0] * numeros_mult_i[1])
        mult_parcial_i = (numeros_mult_r[0] * numeros_mult_i[1]) + (numeros_mult_i[0] * numeros_mult_r[1])

        print(mult_parcial_r,str(mult_parcial_i)+"i")
            
    if( x ==4):
        num1_sq = int(input("Ingresa el numero reale -> "))
        num2_sq = int(input("Ingresa el numero imaginario -> "))

        square_r = num1_sq * num1_sq - (num2_sq * num2_sq)
        square_i = 2 * num1_sq * num2_sq

        result_parcial_r = square_r * 2
        result_parcial_i = square_i * 2
        
        print(result_parcial_r,str(result_parcial_i)+"i")
            
if __name__ == "__main__":
    main()
    
    
    
