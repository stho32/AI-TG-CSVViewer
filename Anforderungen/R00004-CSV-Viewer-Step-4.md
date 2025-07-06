

Der CSV-Viewer soll nun riesige CSV-Dateien anzeigen, bspw. die 3-fache Menge an GB des Arbeitsspeichers Ihres Computers. Ja, der CSV-Viewer sollte in der Lage sein, Milliarden von Datensätzen zu verarbeiten, oder zumindest viel mehr Datensätze, als in den Speicher passen würden.

Dennoch sollte beim Start der Anwendung sofort die erste Seite angezeigt werden. Aber die maximale Seitenzahl kann dann natürlich noch nicht ermittelt werden. Solange [1] dies der Fall ist, geben Sie hinter der Anzahl der Seiten einfach ein „?“ aus:

No.|Name |Age|City    |
---+-----+---+--------+
1. |Peter|42 |New York|
2. |Paul |57 |London  |
3. |Mary |35 |Munich  |
Page 1 of 3?
F)irst page, P)revious page, N)ext page, L)ast page, J)ump to page, S)ort, E)xit

Das Sortieren der Daten soll natürlich auch jetzt noch möglich sein. Bei riesigen Datenmengen keine einfache Aufgabe, aber lösbar 😉

[1] Dies impliziert, dass eine Hintergrundverarbeitung stattfindet. Die Datei muss nach Anzeige der ersten Seite weiterverarbeitet werden, da der Benutzer die genaue Anzahl der Seiten wissen möchte und sofort zu einer beliebigen Seite (die bereits verarbeitet wurde) springen möchte. Im Hinblick auf eine hohe Benutzerfreundlichkeit ist es keine Option, erst mit dem Lesen aus der Datei zu beginnen, wenn der Benutzer eine Seitennummer eingegeben hat, zu der er springen kann.
