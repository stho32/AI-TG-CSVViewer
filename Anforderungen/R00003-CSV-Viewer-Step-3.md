

Erweitern Sie die CSV-Viewer-Anwendung wie folgt: Fügen Sie einen zusätzlichen Menüpunkt “S)ort” hinzu. Wenn der Benutzer “S” drückt, wird er aufgefordert, einen Spaltennamen einzugeben. Wenn ein korrekter Spaltenname eingegeben wird, werden die CSV-Daten nach dieser Spalte sortiert. Die aktuelle Seite wird erneut angezeigt, da sich die auf dieser Seite anzuzeigenden Daten aufgrund der Sortierung möglicherweise geändert haben.

Die Anzeige sollte so aussehen:

```
No.|Name |Age|City    |
---+-----+---+--------+ 
 1.|Peter|42 |New York|
 2.|Paul |57 |London  |
 3.|Mary |35 |Munich  |
Page 1 of 3
F)irst page, P)revious page, N)ext page, L)ast page, J)ump to page, S)ort, E)xit

Please enter column name to sort on:
```
