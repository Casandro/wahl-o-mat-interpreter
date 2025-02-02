# wahl-o-mat-interpreter
Ein kleines Programm, welches die Rohdaten des Wahl-o-Maten in Unterschiede zwischen Parteien umwandelt.

Das hier ist _nicht_ von der [Bundeszentrale für politische Bildung](https://www.bpb.de/), das ist ein kleines Privatprojekt.

# Anwendung

  * Hole Dir die Rohdaten für die Wahl die Du verarbeiten möchtest. Du findest Sie im [Archiv](https://www.bpb.de/themen/wahl-o-mat/45484/archiv/) der [Bundeszentrale für politische Bildung](https://www.bpb.de/themen/wahl-o-mat/556865/datensaetze-des-wahl-o-mat/) Dort findest Du ZIP-Archive der entsprechenden Wahlen. (Die Bundestagswahl 2025 ist dort, Stand 2.2.2025 noch nicht zu finden)
  * Die ZIP-Archive enthalten ein Excel-Sheet, welches sich zum Beispiel leicht mit Libreoffice öffnen lässt
  * Wähle das Tabellenblatt mit der gewünschten Wahl und speichere die Datei als CSV-Datei
  * Führe das Programm hier zum Beispiel mit `./wahl-o-mat-distanzen.py <CSV-Datei` aus. Es gibt Dir eine Tabelle der Meinungsverschiedenheit aus.


# Funktionsweise
Das Programm bewertet die Antworten jeder Partei. Für eine Zustimmung werden 2 Punkte gegeben, für eine Ablehnung 0, und eine neutrale Position wird mit einem Punkt bewertet.

Beim Vergleich zweier Parteien wird der Absolutwert der Differenz jeder These über alle Thesen aufsummiert.

Ein Beispiel:

| | Partei A | Partei B |
These 1 | Zustimmung | Ablehnung |
These 2 | Ablehung | Zustimmung |
These 3 | Ablehnung | neutral |
These 4 | Zustimmung | neutral |


Das wird intern wie folgt gespeichert:


| | Partei A | Partei B |
These 1 | 2 | 0 |
These 2 | 0 | 2 |
These 3 | 0 | 1 |
These 4 | 2 | 1 |

Somit ergeben sich die Absolutwerte der Differenzen zu 2, 2, 1 und 1. Die Summe der Meinungsunterschiede ist somit 6.

Sind zwei Parteien eher einer Meinung, so sind die Werte klein. Sind die Parteien eher unterschiedlicher Meinung, so sind die Werte hoch.


# Beispiel Bundestagswahl 2021
Hier ist als Beispiel die Ausgabe für die Bundestagswahl 2021

<pre>Unterschiede zwischen Meinungen, je These 2 Punkte, also bei 38 Thesen maximal 76 Unterschiedspunkte
 <span style="color:#8AE234"><b>grün</b></span> sind die kleinsten Meinungsunterschiede innerhalb der Zeile
 <span style="color:#EF2929"><b>rot</b></span> sind die größten Meinungsunterschiede innerhalb der Zeile
     GRÜN  CDU  AfD  SPD  FDP LINK  ÖDP PIRA PART FREI MENS Bünd  DKP Basi  DiB Eine Klim Huma Gesu W202 Volt 
GRÜN   --   31 <span style="color:#EF2929"><b>  45 </b></span><span style="color:#8AE234"><b>  17 </b></span>  36   26   31   33   21   37   34   41   35   43   25   43   22   25   33   37   23 
 CDU   31   --   24   34 <span style="color:#8AE234"><b>  15 </b></span>  51   42   42   46   18   45   20 <span style="color:#EF2929"><b>  56 </b></span>  40   44   24   45   34   36   30   38 
 AfD   45   24   --   44   27   59   40   52   58   30   41 <span style="color:#8AE234"><b>  18 </b></span><span style="color:#EF2929"><b>  62 </b></span>  38   54   28   51   42   34   28   54 
 SPD   17   34 <span style="color:#EF2929"><b>  44 </b></span>  --   37   21   30   32 <span style="color:#8AE234"><b>  16 </b></span>  36   33 <span style="color:#EF2929"><b>  44 </b></span>  30   38   24   34   23   20   38   38 <span style="color:#8AE234"><b>  16 </b></span>
 FDP   36 <span style="color:#8AE234"><b>  15 </b></span>  27   37   --   54   45   45   49   27   52   21 <span style="color:#EF2929"><b>  59 </b></span>  45   49   33   48   33   37   37   39 
LINK   26   51   59   21   54   --   29   15 <span style="color:#8AE234"><b>   5 </b></span>  43   26 <span style="color:#EF2929"><b>  61 </b></span>   9   31   11   41   16   21   35   41   21 
 ÖDP   31   42   40   30 <span style="color:#EF2929"><b>  45 </b></span>  29   --   38   28   38   29   38   30   38   30   34 <span style="color:#8AE234"><b>  23 </b></span>  38   34   36   34 
PIRA   33   42 <span style="color:#EF2929"><b>  52 </b></span>  32   45 <span style="color:#8AE234"><b>  15 </b></span>  38   --   20   36   35   48   18   24   18   36   25   22   30   34   26 
PART   21   46   58   16   49 <span style="color:#8AE234"><b>   5 </b></span>  28   20   --   38   27 <span style="color:#EF2929"><b>  60 </b></span>  14   34   10   38   15   18   38   40   16 
FREI   37 <span style="color:#8AE234"><b>  18 </b></span>  30   36   27   43   38   36   38   --   43   32 <span style="color:#EF2929"><b>  50 </b></span>  40   40   26   41   32   34   34   38 
MENS   34   45   41   33 <span style="color:#EF2929"><b>  52 </b></span>  26   29   35   27   43   --   41   25   29   25   25   30   39   27 <span style="color:#8AE234"><b>  19 </b></span>  35 
Bünd   41   20 <span style="color:#8AE234"><b>  18 </b></span>  44   21 <span style="color:#EF2929"><b>  61 </b></span>  38   48   60   32   41   --   58   44   52   26   49   44   34   24   44 
 DKP   35   56 <span style="color:#EF2929"><b>  62 </b></span>  30   59 <span style="color:#8AE234"><b>   9 </b></span>  30   18   14   50   25   58   --   26   16   42   21   30   38   40   26 
Basi   43   40   38   38 <span style="color:#EF2929"><b>  45 </b></span>  31   38 <span style="color:#8AE234"><b>  24 </b></span>  34   40   29   44   26   --   28   36   31   30   28   28   34 
 DiB   25   44 <span style="color:#EF2929"><b>  54 </b></span>  24   49   11   30   18 <span style="color:#8AE234"><b>  10 </b></span>  40   25   52   16   28   --   36   13   24   30   34   24 
Eine <span style="color:#EF2929"><b>  43 </b></span>  24   28   34   33   41   34   36   38   26   25   26   42   36   36   --   39   38   36 <span style="color:#8AE234"><b>  20 </b></span>  42 
Klim   22   45 <span style="color:#EF2929"><b>  51 </b></span>  23   48   16   23   25   15   41   30   49   21   31 <span style="color:#8AE234"><b>  13 </b></span>  39   --   27   25   39   25 
Huma   25   34   42   20   33   21   38   22   18   32   39 <span style="color:#EF2929"><b>  44 </b></span>  30   30   24   38   27   --   34   36 <span style="color:#8AE234"><b>  16 </b></span>
Gesu   33   36   34 <span style="color:#EF2929"><b>  38 </b></span>  37   35   34   30 <span style="color:#EF2929"><b>  38 </b></span>  34   27   34 <span style="color:#EF2929"><b>  38 </b></span>  28   30   36 <span style="color:#8AE234"><b>  25 </b></span>  34   --   34 <span style="color:#EF2929"><b>  38 </b></span>
W202   37   30   28   38   37 <span style="color:#EF2929"><b>  41 </b></span>  36   34   40   34 <span style="color:#8AE234"><b>  19 </b></span>  24   40   28   34   20   39   36   34   --   40 
Volt   23   38 <span style="color:#EF2929"><b>  54 </b></span><span style="color:#8AE234"><b>  16 </b></span>  39   21   34   26 <span style="color:#8AE234"><b>  16 </b></span>  38   35   44   26   34   24   42   25 <span style="color:#8AE234"><b>  16 </b></span>  38   40   -- 
Legende:
  GRÜN: BÜNDNIS 90/DIE GRÜNEN
   CDU: Christlich Demokratische Union Deutschlands
   AfD: Alternative für Deutschland
   SPD: Sozialdemokratische Partei Deutschlands
   FDP: Freie Demokratische Partei
  LINK: DIE LINKE
   ÖDP: Ökologisch-Demokratische Partei / Familie und Umwelt
  PIRA: Piratenpartei Deutschland
  PART: Partei für Arbeit, Rechtsstaat, Tierschutz, Elitenförderung und basisdemokratische Initiative
  FREI: FREIE WÄHLER
  MENS: Menschliche Welt - für das Wohl und Glücklichsein aller
  Bünd: Bündnis C - Christen für Deutschland
   DKP: Deutsche Kommunistische Partei
  Basi: Basisdemokratische Partei Deutschland
   DiB: DEMOKRATIE IN BEWEGUNG
  Eine: Eine für Alle - Partei
  Klim: Klimaliste Baden-Württemberg
  Huma: Partei der Humanisten
  Gesu: Partei für Gesundheitsforschung
  W202: Partei WIR2020
  Volt: Volt Deutschland
</pre>
