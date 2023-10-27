//
//  main.c
//  Practica_1
//
//  Created by David Roldan Machado on 18/08/23.
//

#include <stdio.h>


//int a;
//int b;
//    int maximo_comun_divisor_recursivo(int a, int b) {
//    if (b == 0) return a;
//    return maximo_comun_divisor_recursivo(b, a % b);
//
//        }
//int main(void) {
//    printf("%d\n",maximo_comun_divisor_recursivo(24,36));
//    return 0;
//
//}
//#include <stdio.h>
//
//int main(void)
//{
//    int pisos=0;
//    int filas=0;
//    int columnas=0;
//    printf("Ingresa el numero de pisos para la piramide -> ");
//    scanf("%d",&pisos);
//
//    for(filas = 1; filas <= pisos; filas++)
//    {
//        for(columnas=1; columnas <= 2*pisos-1; columnas++)
//        {
//            if(columnas >= pisos-(filas-1) && columnas <= pisos+(filas-1) ){
//                printf("*");
//
//            }else
//            {
//                printf(" ");
//            }
//        }
//
//        printf("\n");
//    }
//    return 0;
//}

//2,43, 3, 1, 9, 23, 12, 8, 56, 12, 21

void selectionSort(int array[]){
    
    int n = 10;
    
    for(int i = 0; i < n -1; i++){
        
        int min_indice = i;
        
        for (int j = i + 1; j < n; j++) {
            
            if(array[j] < array[min_indice]){
                
                min_indice = j;
            }
        }
        int temp = array[i];
        array[i] = array[min_indice];
        array[min_indice] = temp;
    }
}
//2,43, 3, 1, 9, 23, 12, 8, 56, 12, 21

int main(void){
    int arr[] = {2, 43, 3, 1, 9, 23, 12, 8, 56, 12, 21};
    selectionSort(arr);
    
    int n = 10;
    for (int i = 0; i < n; i++) {
            printf("%d ", arr[i]);
        }
    return 0;
}
