from main import Fila
from main import cliente


cliente_001 = cliente(32994917)


cliente_001.modificarcategoria("Preferencial")

print(cliente_001.categoria)

lista_clientes = []

n=20
for i in range(0,n):
    dni = i+10
    lista_clientes.append( cliente(dni) )
    if i<10:
        lista_clientes[i].modificarcategoria("Preferencial")
    else:
        lista_clientes[i].modificarcategoria("General")
    
    print(lista_clientes[i].dni,lista_clientes[i].categoria )







