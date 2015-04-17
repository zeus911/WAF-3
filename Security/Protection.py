__author__ = 'Raul'

from collections import defaultdict


class Protection:

    def __init__(self):
        self.NumAttacks = 0
        self.NumPetitions = 0
        self.BlackList = defaultdict(int)
        self.XSS = 0
        self.SQLInjection = 0

    def addpetitions(self):
        self.NumPetitions += 1

    def addattacker(self, client):
        self.BlackList[client] += 1

    def isagressor(self, client):
        if client in self.BlackList:
            return True
        else:
            return False

    def addxss(self):
        self.XSS += 1

    def addsqlinjection(self):
        self.SQLInjection += 1