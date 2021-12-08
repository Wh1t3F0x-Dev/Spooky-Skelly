#import random

#Clase para poner atributos de colores 
class colors:
    #Aqui irian los diferentes atributos para poner los colores y tal

    '''
    DIFERENTES TIPOS DE COLORES
    '''
    #Color: Morado
    purple = '\033[95m'

    #Color: Naranjito Claro (se ve fuerte)
    lightorange = '\033[33m'

    #Color: Azul oscuro (se ve poco)
    blue = '\033[94m'

    #Color: cyan (se ve fuerte)
    prompt = '\033[1;97m'

    #Color:
    banner = '\033[1;90m'

    title= '\033[1;96m'

    subtitle= '\033[1;92m'
    '''
    METODOS DE LA CLASE    
    '''
    '''
    #Getter para conseguir la lista de colores.
    def getLC (self):
        return self.listColor
    
    #Metodo para conseguir un color de la lista de forma aleatoria
    def getRC (self):
        LC=self.getLC()
        #Para que tenga mas aleatoriedad
        for x in range(5):
            random.shuffle(LC)
        #Devuelve el primer valor de la lista
        return LC[0]
    '''
    
