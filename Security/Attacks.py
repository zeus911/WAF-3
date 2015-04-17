__author__ = 'Raul'

'#Etiquetas para posibles ataques XSS'
TAGSXSS = ['%3Cscript%3E', '%3Cobject%3E', '%3Capplet%3E', '%3Cembed%3E']
# %3C = <
# %3E = >
'#Etiquetas para posibles Ataques SQLInjection (KeyWords SQL)'
TAGSSQL = ['SELECT', 'DROP', 'INSERT', 'DELETE', '%3B', '--', ' OR ']
# %3B = ;
'#Etiquetas HTTP'