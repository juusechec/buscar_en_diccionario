#!/usr/bin/python3
import re

#filename = 'libreoffice-dic-es_ANY.txt'
filename = 'phpstorm-dict.txt'
#filename = 'listado-general.txt'
length = 0 # is for no limits
#length = 7
noletters = ['t']
# politica
# impactos
# aspecto
# inorganicos
# organicos
# adaptacion
# aprovechables
# internas (condiciones internas o del entorno)
# desarrollo sostenible
# economia sostenible
# producción sostenible
# consumo sostenible 
# objetivos de desarrollo sostenible

#regex = re.compile(r'^.?[o].*$')
#regex = re.compile(r'^[a-zA-Z][oó].?[i][t][i][c].*$')
#regex = re.compile(r'^[a-zA-Z]{2}[oó][r].*$')
#regex = re.compile(r'^[aá][a-z][aá][a-z]{2}[aá][a-z][ií].*$')
#regex = re.compile(r'^[aá][a-z]{2}[oó][a-z]{4}[aá].*$')
#regex = re.compile(r'^[f][a-záéíóúý]{4}[c][aá][n][t].*$')
#regex = re.compile(r'^[a-záéíóúý][oó][l][aá][g][aá][s].*$')
regex = re.compile(r'^[f][b].*$')
#regex = re.compile(r'^[i][a-z]{3}[ií][a-z][a].*$')
#regex = re.compile(r'^[i][a-záéíóúý][aá][a-záéíóúý][ií][a-záéíóúý][aá].*$')
#regex = re.compile(r'^[ií][a-záéíóúý]{4}[v][aá].*$')
#regex = re.compile(r'^[ií][a-záéíóúý]{4}[v][aá].*$')


textfile = open(filename, 'r')
matches = []
for line in textfile:
    if length > 0 and len(line) != length + 1:
        continue
    match = regex.findall(line)
    for letter in noletters:
        if str(match).find(letter) > -1:
            continue
    matches += match
textfile.close()
print(matches)
print('longitud', length)
