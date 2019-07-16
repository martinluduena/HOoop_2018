from main import Fila
from main import FilaPreferencial
from main import FilaGeneral
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



# creo la fila preferencial
Fila_P = FilaPreferencial()

# creo la fila general
Fila_G = FilaGeneral()

Fila_G.insertar(cliente_001)

print(Fila_G.enfila)
print(Fila_P.fila[0].dni)





