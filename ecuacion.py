import math

a = int ( input ( ' Introduce el valor de a : ' ) )
b = int ( input ( ' Introduce el valor de b : ' ) )
c = int ( input ( ' Introduce el valor de c : ' ) )

d = ( b * b ) -4 * a * c

if d < 0 :
    print ( ' No existen soluciones Reales !! ' )
    x1 = ( - b + math.sqrt ( d ) ) / ( 2 * a )
    x2 = ( - b - math.sqrt ( d ) ) / ( 2 * a )
else :
        print ('solucion de x1 es:')
        print ('solucion de x2 es:')