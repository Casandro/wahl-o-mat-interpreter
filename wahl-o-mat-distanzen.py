#!/bin/python3

import csv
import sys
import re

import matplotlib.pyplot as plt
import networkx as nx


class Partei:
    def __init__(self, nummer, kurz, name):
        self.nummer=nummer
        self.kurz=kurz
        self.name=name
        #Ganz kurzen Namen (4 Zeichen) bereichnen
        self.ganzkurz=re.sub("(der|die|das) ?", "", kurz, flags=re.IGNORECASE)[:4]
        self.positionen={}

    def add_position(self, these, position):
        if (position=="stimme zu"):
            self.positionen[these]=2;
            return
        if (position=="stimme nicht zu"):
            self.positionen[these]=0;
            return
        self.positionen[these]=1;

    def vergleich(self, partei):
        thesen={} #Wir machen eine kombinierte Liste an Thesen
        for p in self.positionen:
            thesen[p]=1;
        for p in partei.positionen:
            thesen[p]=1;
        summe=0
        for t in thesen:
            if not (t in self.positionen):
                print("Fehler in Daten bei These %s" %(t));
            if not (t in partei.positionen):
                print("Fehler in Daten bei These %s" %(t));
            summe=summe+abs(self.positionen[t]-partei.positionen[t]);
        return summe;

parteien={}
thesen={}

with open(sys.argv[1]) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        partei_nr=row["Partei: Nr."]
        partei_kurz=row["Partei: Kurzbezeichnung"]
        partei_name=row["Partei: Name"]
        these_nr=row["These: Nr."]
        position=row["Position: Position"];
        if not partei_nr in parteien:
            parteien[partei_nr]=Partei(partei_nr, partei_kurz, partei_name);
        parteien[partei_nr].add_position(these_nr, position);
        if not these_nr in thesen:
            thesen[these_nr]=1


anzahl_thesen=len(thesen)

print("Unterschiede zwischen Meinungen, je These 2 Punkte, also bei %s Thesen maximal %s Unterschiedspunkte" % (anzahl_thesen, anzahl_thesen*2))
print(" \033[1;32mgrün\033[0m sind die kleinsten Meinungsunterschiede innerhalb der Zeile")
print(" \033[1;31mrot\033[0m sind die größten Meinungsunterschiede innerhalb der Zeile")
# Tabelle mit allen Unterschieden ausg
print("     ", end="")
for pb in parteien:
    print("%4s "%(parteien[pb].ganzkurz), end="")
print("")
for pa in parteien:
    partei_a=parteien[pa]
    print("%4s "%(parteien[pa].ganzkurz), end="")
    minimum=999
    maximum=0
    for pb in parteien:
        if (pa==pb):
            continue
        partei_b=parteien[pb]
        vergleich=partei_a.vergleich(partei_b)
        if vergleich<minimum:
            minimum=vergleich
        if vergleich>maximum:
            maximum=vergleich
    for pb in parteien:
        if (pa==pb):
            print("  -- ", end="")
            continue
        partei_b=parteien[pb]
        vergleich=partei_a.vergleich(partei_b)
        if vergleich==minimum: # Die kleinsten Unterschiede werden grün eingefärbt
            print("\033[1;32m",end="")
        if vergleich==maximum: # Die kleinsten Unterschiede werden rot eingefärbt
            print("\033[1;31m", end="")
        print("%4s " %(vergleich), end="")
        print("\033[0m", end="")
    print("")


print("Legende:")
for p in parteien:
    partei=parteien[p]
    print("  %4s: %s"%(partei.ganzkurz, partei.name))


if len(sys.argv)>2:
    # Graphen mit Zusammenhängen als dotviz Graph generieren
    G = nx.Graph()
    for pa in parteien:
        partei_a=parteien[pa]
        for pb in parteien:
            if pa==pb:
                continue
            partei_b=parteien[pb]
            vergleich=partei_a.vergleich(partei_b)
            penwidth=0
            label=""
            rel_unterschiede=vergleich*0.5/anzahl_thesen;
            if rel_unterschiede<0.4: 
                penwidth=1
                label="%2.0f"%(vergleich*0.5/anzahl_thesen*100)+"%"
            if rel_unterschiede<0.25:
                penwidth=2
            if rel_unterschiede<0.125:
                penwidth=4
            if rel_unterschiede<0.0625:
                penwidth=8

            G.add_edge(parteien[pa].kurz, parteien[pb].kurz,weight=0.5, len=vergleich*0.2, penwidth=penwidth, label=label)

    nx.nx_pydot.write_dot(G, sys.argv[2])

