import math

def main():
    n = 50
    lista = []
    konacnaLista = []
    
    for i in range(1, n):
        lista.append(i)
    
    konacnaLista = [x for x in lista if math.sqrt(x).is_integer()]

    print(konacnaLista)

if __name__ == "__main__":
    main()
