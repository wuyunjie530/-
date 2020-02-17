# -*- coding: utf-8 -*-
import rdflib
import os
import logging
logging.basicConfig()


path=".\\data"
files = os.listdir(path)
g = rdflib.Graph()
for file in files:
	if not os.path.isdir(file):
		filePath=path+'\\'+file
		g.parse(filePath,format='xml')
g.serialize(destination=".\\lubm.nt",format="nt")
print(len(g))