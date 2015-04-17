__author__ = 'Raul'

import re
from bs4 import BeautifulSoup
import urllib2

ParamHeaderRequest = ['Accept', 'Accept-Charset', 'Accept-Encoding', 'Accept-Language', 'Accept-Datetime',
                      'Authorization', 'Cache-Control', 'Cache-Control', 'Connection', 'Cookie', 'Content-Lenght',
                      'Content-MD5', 'Content-type', 'Date', 'Expect', 'From', 'Host', 'If-Match', 'If-Modified-Since',
                      'If-None-Match', 'If-Range', 'If-Unmodified-Since', 'Max-Forwards', 'Origin', 'Pragma',
                      'Proxy-Authorization', 'Range', 'Referer', 'TE', 'User-Agent', 'Upgrade', 'Via', 'Warning']

ParamHeaderResponse = ['Access-Control-Allow-Origin', 'Accept-Patch', 'Accept-Ranges', 'Age', 'Allow', 'Cache-Control',
                       'Connection', 'Content-Disposition', 'Content-Encoding', 'Content-Language', 'Content-Length',
                       'Content-Location', 'Content-MD5', 'Content-Range', 'Content-Type', 'Date', 'ETag', 'Expires',
                       'Last-Modified', 'Link', 'Location', 'P3P', 'Pragma', 'Proxy-Authenticate', 'Refresh',
                       'Retry-After', 'Server', 'Set-Cookie', 'Status', 'Strict-Transport-Security', 'Trailer',
                       'Transfer-Encoding', 'Upgrade', 'Vary', 'Via', 'Warning', 'WWW-Authenticate', 'X-Frame-Options']

DictReqRes = {'Request': ParamHeaderRequest, 'Response': ParamHeaderResponse}

TAGSHTTP = ['GET', 'POST', 'HEAD', 'PUT', 'DELETE', 'TRACE', 'OPTIONS', 'CONNECT']


class HTTP:

    def __init__(self, message):

        self.HeaderMessageHTTP = {}
        self.message = message
        self.typemessage = None
        self.typemess = None
        self.parametersPetition = {}
        self.typeheader = None

        self.inputshtml = {}

        self.analyzeheader()

    def analyzeheader(self):

        self.typemessage = re.search(ur'(.*) (.*) (.*)', self.message)
        validmessage = self.__typemessagehttp()

        if validmessage:
            for word in self.typeheader:
                match = re.search(ur''+word+':(.*)', self.message)
                if match is not None:
                    self.HeaderMessageHTTP[word] = match.group(1).replace('\r', '')

        #print self.HeaderMessageHTTP

    def __typemessagehttp(self):
        self.typemess = 'Request'
        if self.typemessage is not None:
            if self.typemessage.group(1) in TAGSHTTP:
                method = self.typemessage.group(1).replace('\r', '')
                if method not in TAGSHTTP:
                    return False
                self.HeaderMessageHTTP['Method'] = method
                self.HeaderMessageHTTP['Path'] = self.typemessage.group(2).replace('\r', '')
                self.HeaderMessageHTTP['HTTP-Version'] = self.typemessage.group(3).replace('\r', '')
            else:
                version = self.typemessage.group(1).replace('\r', '')
                if 'HTTP' not in version:
                    return False
                self.HeaderMessageHTTP['HTTP-Version'] = version
                self.HeaderMessageHTTP['Status-Code'] = self.typemessage.group(2).replace('\r', '')
                self.HeaderMessageHTTP['Reason-Phrase'] = self.typemessage.group(3).replace('\r', '')
                self.typemessage = 'Response'
                self.getinputsbody()
        self.typeheader = DictReqRes[self.typemess]
        return True

    def getparam(self):

        if len(self.HeaderMessageHTTP) > 0:
            if self.typemess == 'Request' and 'Method' in self.HeaderMessageHTTP and \
                            self.HeaderMessageHTTP['Method'] == 'GET':
                path = self.HeaderMessageHTTP['Path']
                parameters = re.search(ur'[?](.*)', path)
                if parameters is not None:
                    param = parameters.group(0)[1:]
                    values = param.replace('&', '=').split('=')
                    for pos in range(0, len(values), 2):
                        self.parametersPetition[values[pos]] = values[pos+1]
            elif self.typemess == 'Request' and 'Method' in self.HeaderMessageHTTP \
                    and self.HeaderMessageHTTP['Method'] == 'POST':
                pass
            if len(self.parametersPetition) > 0: print self.parametersPetition
            return self.parametersPetition

    def getinputsbody(self):
        html = urllib2.urlopen('http://localhost/prueba/').read()
        soup = BeautifulSoup(html)
        for input in soup.find_all('input'):
            print input
            if input.get('type') != 'submit':
                self.inputshtml[input.get('name')] = input.get('value')
        print self.inputshtml