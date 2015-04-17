__author__ = 'Raul'

import re

'# Valores predefinidos del inicio del ReverseProxy'
pred_init_IP = 'localhost'
pred_init_Port = 9090
pred_init_language = 'ES'  # Lenguaje predefinido de la aplicacion
pred_pet_max = 200 # Numero de peticiones maximas que aceptara el servidor simultaneamente
'# Inicializacion con los valores del fichero'
conf_init_IP = None
conf_init_Port = None
conf_init_language = None
conf_pet_max = None

'# Valores predefinidos para la direccion real de la web'
pred_url = 'localhost'
pred_port = 80
'# Inicilizacion de los valores desde fichero'
conf_url = None
conf_port = None

'# Variable que mantienen a las dos opciones validas'

'#TRUE=Indica que ha obtenido los valores correctamente, FALSE en caso contrario'
Values = False

'# FALSE = 0, TRUE = 1'
init_IP = [pred_init_IP, conf_init_IP]
init_Port = [pred_init_Port, conf_init_Port]
init_language = [pred_init_language, conf_init_language]
init_pet_max = [pred_pet_max, conf_pet_max]
init_web_url = [pred_url, conf_url]
init_web_port = [pred_port, conf_port]

'#Posibles Lenguajes'
TAGSLANGUAGE = ['ES', 'EN']


class Settings:
    def __init__(self, path):
        self.path = path
        self.readsettings = None

    def loadsettings(self):
        exist = True

        try:
            self.readsettings = open(self.path, 'r').read()
        except IOError:
            exist = False
            self.__writefileconfig()

        if exist:
            self.__getfileconfig()
            Values = self.__checkvalues()
        else:
            self.__writefileconfig()

    def __getfileconfig(self):

        conf_init_IP = re.findall(u'init_IP=(.*)', self.readsettings)
        conf_init_Port = re.findall(u'init_Port=(.*)', self.readsettings)
        conf_init_language = re.findall(u'init_language=(.*)', self.readsettings)
        conf_pet_max = re.findall(u'init_pet_max=(.*)', self.readsettings)
        conf_url = re.findall(u'init_web_url=(.*)', self.readsettings)
        conf_port = re.findall(u'init_web_port=(.*)', self.readsettings)

    def __writefileconfig(self):
        tags = {'init_IP': init_IP[Values], 'init_Port': init_Port[Values], 'init_language': init_language[Values],
                'init_pet_max': init_pet_max[Values], 'init_web_url': init_web_url[Values],
                'init_web_port': init_web_port[Values]}

        writeconfig = open(self.path, 'w')
        for key in tags:
            writeconfig.write(key + '=' + str(tags[key]) + '\n')
        writeconfig.close()

    @staticmethod
    def __checkvalues():
        pass