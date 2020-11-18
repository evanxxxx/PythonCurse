'''
Title: Class Example
Autor: Edgar
Fecha 04/11/2020
'''

class Car ():

    _color = None
    _num_llantas = 4
    _num_puertas = None
    _transmision = None
    _enmarcha = False

    def __init__(self, color, num_llantas, num_puertas, trasmision):
        self._color = color
        self._num_llantas = num_llantas
        self._num_puertas = num_puertas
        self._transmision = trasmision
    
    def arrancar(self):
        self._enmarcha = True
        print(f'Tu auto ha arrancado, la marcha esta en : {self._enmarcha}')

    def apagar(self):
        self._enmarcha = False
        print(f'Tu auto ahora esta apagado, la marcha esta en {self._enmarcha}')

    def info_auto(self):
        print(f'Tu auto es de color {self._color}, tiene  {self._num_llantas} llantas y su trasmision es {self._transmision}, con {self._num_puertas} puertas ')

if __name__ == "__main__":
    oc = Car('rojo', 4, 4 , 'automatico')
    oc.info_auto()
    oc.apagar()
