import math

def nova_lista(n):
    return [i for i in range(1, n)]

def lista_korena(l):
    return [x for x in l if math.sqrt(x).is_integer()]

def main():
    n = 50
    lista = []
    
    lista = nova_lista(n)
    
    konacna_lista = lista_korena(lista)

    print(konacna_lista)

if __name__ == "__main__":
    main()
