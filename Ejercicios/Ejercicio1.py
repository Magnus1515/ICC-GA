def main():
    x = int(input("Cantidad de calificaciones a ingresar "))
    sum_grade = 0
    
    for i in range(x):
        y = int(input("Ingresa la calificacion "))
        
        while y < 0 or y > 10:
            print("Error, ingrese nuevamente el valor ")
            y = int(input())
        
        sum_grade += y
    
    final_grade = sum_grade / x
    
    if final_grade >= 6:
        print("Felicidades, aprobaste ->", final_grade)
    else:
        print("Reprobado ->", final_grade)

if __name__ == "__main__":
    main()
