__author__ = 'Raul'

import re
import Attacks
import AnalyzeHTTP

patternfirst = re.compile(u'(.*) (.*) (.*)')
patternvarspost = re.compile(u'(.*)=(.*)&(.*)')
#Comprobar que no sean valores vacios


class Request:

    def __init__(self, request):

        self.vars = None
        self.message = request

        petition = re.match(patternfirst, self.message)

        if petition is not None:
            self.type = petition.group(1)
            if self.type.upper() == 'POST':
                self.vars = self.getitempost()
            if self.type.upper() == 'GET':
                ob = AnalyzeHTTP.HTTP(self.message)
                ob.analyzeheader()
            #    self.vars = self.getitemget()
                #Hacer lo mismo del POST con el GET

    def getitempost(self):
        match = re.search(patternvarspost, self.message)
        if match is not None:
            dictitems = {match.group(1): match.group(2)}
            dictitems2 = self.__analyze(match.group(3))
            dictitems.update(dictitems2)
            return dictitems

    def analyzevalues(self):
        if self.vars is not None:
            for value in self.vars.values():
                if value in Attacks.TAGSSQL:
                    return 'Attack SQLInjection'
                elif value in Attacks.TAGSXSS:
                    return 'Attack XSS'
        return True

    @staticmethod
    def __analyze(items):
        diccionario = None
        values = items.split('&')
        for tupple in values:
            par = tupple.split('=')
            diccionario = {par[0]: par[1]}
        return diccionario
