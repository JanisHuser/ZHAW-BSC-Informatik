```python
from Scripts.Digitaltechnik.TruthTable import TruthTable

# Mögliche Variablen, werden von rechts nach links gelesen
inputs = ['a', 'b', 'c', 'd']

# Erstellen des TruthTable Objekts
table = TruthTable()

# Gleichung die zu überprüfen gilt
to_check '(d or b) and (a or not c or not d) and (not a or not b or not d)'

# Ausführung, gibt Tabelle in Konsole aus
table.check(to_check)
```