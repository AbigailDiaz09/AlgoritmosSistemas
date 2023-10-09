class SelectionSort:
    arreglo=[6,8,6,9,54,4,88,10,99]
    for i in range(0,len(arreglo)):
        actualpeque=arreglo[i]

        for j in range(i,len(arreglo)):
            if arreglo[j]<arreglo[actualpeque]:
                actualpeque=j
        
        arreglo[i],arreglo[actualpeque]=arreglo[actualpeque],arreglo[i]

    print(arreglo)
