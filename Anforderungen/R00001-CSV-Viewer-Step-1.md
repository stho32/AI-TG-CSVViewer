# CSV-Viewer Step 1

Ursprung: https://kurse.ccd-akademie.de/csv-viewer-i/
Zielsprache: dotnet
Zielordner : ./Source

----------

Schreiben Sie eine Anwendung, um CSV-Dateien auf der Konsole anzuzeigen. [1] Es soll ein sehr einfaches Programm sein: Rufen Sie es einfach so über die Befehlszeile auf:

C:\>csvviewer.exe persons.csv

…und der Inhalt der Datei wird nun wie folgt angezeigt: [2]

```
Name |Age|City    |
-----+---+--------+ 
Peter|42 |New York|
Paul |57 |London  |
Mary |35 |Munich  |
F)irst page, P)revious page, N)ext page, L)ast page, E)xit
```

Seiten mit Datensätzen werden als Tabelle mit einer Kopfzeile und Zellenrändern wie abgebildet angezeigt. Die entsprechende Datei sieht wie folgt aus; bei einer Seitenlänge von 3 Datensätzen würden diese als drei Seiten dargestellt:

```
Name;Age;City 
Peter;42;New York
Paul;57;London
Mary;35;Munich
Jaques;66;Paris
Yuri;23;Moscow
Stephanie;47;Stockholm
Nadia;29;Madrid
```

Jede Zeile enthält einen Datensatz; die erste Zeile enthält die Spaltennamen; Spalten werden durch “;” getrennt. Der Inhalt der Datensatzfelder ist einfach: keine Zeilenumbrüche, keine Feldtrenner, keine Verarbeitung von Werten in “”. Die Codierung der CSV-Textdateien ist UTF-8.

ACHTUNG: natürlich ist dies nur ein Beispiel! Konkrete CSV Dateien können durchaus unterschiedlich aussehen (mehr oder weniger Spalten, andere Spaltenüberschriften). Insofern ist es NICHT die Lösung, eine Klasse Person mit den Properties Name, Age und City anzulegen.

Die Seitenlänge sollte einen angemessenen Standard für die Konsolenfenster Ihrer Plattform haben, kann aber auch wie folgt an die Anwendung übergeben werden:

C:\>csvviewer.exe persons.csv 40

Die Seitentabelle sollte Spalten mit fester Breite haben, die dem längsten Wert für jede Spalte innerhalb einer Seite entsprechen.

[1] Für diese Übung wird ein Konsolen-Frontend verwendet, da dies der kleinste gemeinsame Nenner in Bezug auf das Frontend für alle Plattformen ist. Egal, ob Sie Python oder C# oder Java verwenden, Sie sollten in der Lage sein, ein Konsolen-Frontend über jede Geschäftslogik zu legen. Sicher wäre eine GUI stylischer, aber sie würde auch von den Hauptherausforderungen der Übung ablenken.

[2] Gehen Sie davon aus, dass alle CSV-Dateien nur Zeilen enthalten mit einer Länge, die einer Anzeigezeile entspricht. Es ist daher kein horizontales Scrollen erforderlich. Sehr wahrscheinlich sind jedoch alle Zeilen unterschiedlich lang.
