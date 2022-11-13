# Balanced Tree

Der absolute Höhenunterschied der linken sowie rechten Seite dürfen nicht grösser als 1 sein. Dies bei jeder Node.


# Algorithmus

1. Berechne für jede Node die linke und rechte Höhe.
2. Rekusriv zur niedrigsten Node gehen, und beim zurückgehen den Höhenunterschied von links zu rechts überprüfen.

### Problem
Bei jeder Node wird die Höhe rekursiv berechnet.


### Behebung

1. Zuerst niedrigstes Level erreichen, und danach die Höhe in die Node eintragen und berechnen.