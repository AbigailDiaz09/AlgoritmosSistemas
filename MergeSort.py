def mergeSort(arr): #arreglo máximo
    if len(arr)== 1:
        return arr
    middle= len(arr)//2
    arrIzq=arr[:middle]
    arrDer=arr[middle:]   #O(n)

    #resolver de forma recursiva
    izqOrdenado=mergeSort(arrIzq)
    derOrdenado=mergeSort(arrDer)
    #T(n)= 2T(n/2) + O(n)  metodo master, metodo de arbol recursivo  
    #=T([n/2]+T([n2])+O(n)
    #O(Log(n))
    #O(nlog(n'))
    
    #juntar los resultados de la solucion final
    finalOrdenado=Junta(izqOrdenado,derOrdenado)
    return finalOrdenado                               #O(n)

def Junta(izq,der):
    resultado=[]
    apuntizq=0
    apuntder=0

    while(apuntizq<len(izq)and apuntder<len(der)):
        if izq[apuntizq]<der[apuntder]:
            resultado.append(izq[apuntizq])
            apuntizq+=1
        else:
            resultado.append(der[apuntder])
            apuntder+=1
    #O(izq+der-1)
    while apuntder<len(der):
        resultado.append(der[apuntder])
        apuntder+=1
    #O(der)
    while apuntizq<len(izq):
        resultado.append(izq[apuntizq])
        apuntizq+=1
    return resultado
    #O(izq)

if __name__=="__main__":
    arr=[4,5,3,6,8,8,90,5,7,55,4,753,23]
    arrOrd=mergeSort(arr)
    print(arr)
    print(arrOrd)
