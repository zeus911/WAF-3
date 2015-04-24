__author__ = 'Raul'

import re
import HTTPPage
from bs4 import BeautifulSoup
import urllib2


class HTTP:

    def __init__(self, message):

        self.message = message
        self.typemessage = None
        self.typemess = None
        self.typeheader = None
        self.parametersPetition = {}
        self.HeaderMessageHTTP = {}

        self.analyzeheader()

    def analyzeheader(self):

        self.typemessage = re.search(ur'(.*) (.*) (.*)', self.message)
        validmessage = self.__typemessagehttp

        if validmessage:
            for word in self.typeheader:
                match = re.search(ur''+word+':(.*)', self.message)
                if match is not None:
                    self.HeaderMessageHTTP[word] = match.group(1).strip()

    def __typemessagehttp(self):
        self.typemess = 'Request'
        if self.typemessage is not None:
            if self.typemessage.group(1) in HTTPPage.TAGSHTTP:
                method = self.typemessage.group(1).strip()
                if method not in HTTPPage.TAGSHTTP:
                    return False
                self.HeaderMessageHTTP['Method'] = method
                self.HeaderMessageHTTP['Path'] = self.typemessage.group(2).strip()
                self.HeaderMessageHTTP['HTTP-Version'] = self.typemessage.group(3).strip()
                self.__getinputsbody()
            else:
                version = self.typemessage.group(1).strip()
                if 'HTTP' not in version:
                    return False
                self.HeaderMessageHTTP['HTTP-Version'] = version
                self.HeaderMessageHTTP['Status-Code'] = self.typemessage.group(2).strip()
                self.HeaderMessageHTTP['Reason-Phrase'] = self.typemessage.group(3).strip()
                self.typemess = 'Response'
            self.typeheader = HTTPPage.DictReqRes[self.typemess]

        return True

    def getparameters(self):

        if len(self.HeaderMessageHTTP) > 0:

            if self.typemess == 'Request' and 'Method' in self.HeaderMessageHTTP \
                            and self.HeaderMessageHTTP['Method'] == 'GET':

                path = self.HeaderMessageHTTP['Path']
                parameters = re.search(ur'[?](.*)', path)
                if parameters is not None:
                    param = parameters.group(0)[1:]
                    self.__getparamfromrequest(param)

            elif self.typemess == 'Request' and 'Method' in self.HeaderMessageHTTP \
                    and self.HeaderMessageHTTP['Method'] == 'POST':

                lines = str(self.message).splitlines()
                for line in range(1, len(lines)):
                    key = lines[line].split(':')
                    if key[0] not in self.HeaderMessageHTTP and len(lines[line]) > 0:
                        self.__getparamfromrequest(lines[line])

            return self.parametersPetition

    def __getparamfromrequestget(self, vars):
        values = vars.replace('&', '=').split('=')
        for pos in range(0, len(values), 2):
            self.parametersPetition[values[pos]] = values[pos+1]

    def __getinputsbody(self):
        host = self.HeaderMessageHTTP['Host']
        if self.HeaderMessageHTTP['Path'] not in HTTPPage.ParametersAllPages:
            if host is not None:
                host = host.replace(':9090', ':80')
                page = urllib2.urlopen(host+self.HeaderMessageHTTP['Path']).read()
                soup = BeautifulSoup(page)
                for input in soup.find_all('input'):
                    if input.get('type') != 'submit':
                        HTTPPage.ParametersAllPages[self.HeaderMessageHTTP['Path']] = {[input.get('name')]:
                                                                                           input.get('value')}