

arreglo = [1,2,3, 4, 5, 6, 7, 8, 9, 10]

def sumArray(array):
    sumatoria = 0; 
    for i in range(len(array) ): 
        sumatoria += array[i];
    return sumatoria
        
print(f"La sumatoria de los numeros del 1 al 10 es:  { sumArray(arreglo)}")