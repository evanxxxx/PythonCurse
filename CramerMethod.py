class CramerMethod(object):

    def filter_system_expresion(self, system='', system2='', system3='') -> list:
        
        matrix = []   
        for e in system:
            try:
                e  = int(e)
                matrix.append(e)
            except ValueError:
                print(f'This caracter [{e}] cannot be converter to int() and value matrix is {matrix}' )
      
            
        for i in system2:
            try:
                i  = int(i)
                matrix.append(i)
            except ValueError:
                print(f'This caracter [{i}] cannot be converter to int()')
   

        for x in system3:
            try:
                x  = int(x)
                matrix.append(x)
            except ValueError:
                print(f'This caracter [{x}] cannot be converter to int()')
        return matrix


if __name__ == "__main__":
    co = CramerMethod()
    print(co.filter_system_expresion('3x+2y+1z=1','2x+0y+1z=2','-1x+1y+2z=4'))

    