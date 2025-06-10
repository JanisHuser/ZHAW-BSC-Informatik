# 📜 Linux Lizenzen

## 🎯 Ziel

Verständnis für die wichtigsten Open-Source-Lizenzmodelle, deren Unterschiede und Bedeutung im Linux-/Embedded-Kontext.

## 🧾 Bedeutung von Lizenzen

* Schutz geistigen Eigentums bei gleichzeitiger Offenlegung des Quellcodes
* Definieren Nutzungs-, Weitergabe- und Veränderungsrechte

## 🗃️ Wichtige Lizenzen im Linux-Umfeld

### 🟩 GPL (GNU General Public License)

* **Copyleft-Lizenz**: Änderungen müssen ebenfalls unter GPL veröffentlicht werden
* Dynamisches und statisches Linken verpflichten zur Offenlegung des Quellcodes
* Bekannte Projekte: Linux-Kernel, BusyBox, GCC

### 🟨 LGPL (Lesser GPL)

* Schwächere Version der GPL
* **Dynamisches Linken erlaubt proprietären Code**
* Änderungen an der Bibliothek müssen veröffentlicht werden
* Beispiel: glibc

### 🟦 MIT-Lizenz

* **Sehr permissiv**
* Erlaubt proprietäre Nutzung, Veränderung und Weitergabe
* Nur Urheberrechtshinweis muss erhalten bleiben

### 🟥 BSD-Lizenz (Berkeley Software Distribution)

* Ähnlich wie MIT, aber mit zusätzlicher Klausel zur Namensnennung
* Frei in kommerziellen Produkten verwendbar

### ⛔️ Tivoization

* Hardwarehersteller verhindern Ausführung modifizierter Software
* **GPLv3** verbietet dies explizit
* GPLv2 erlaubt es noch → daher bleibt Linux-Kernel bei GPLv2

## ⚖️ Lizenzkonflikte & Praxis

* Vermischen inkompatibler Lizenzen kann rechtliche Probleme verursachen
* Beispiel: MIT (libA) + GPL (libB) → gesamtes Werk wird GPL

## 🔍 Lizenz-Check & Tools

| Tool           | Beschreibung                         |
| -------------- | ------------------------------------ |
| `licensecheck` | Erkennung von Lizenztypen in Dateien |
| `reuse lint`   | Prüfung auf konforme Lizenzierung    |
| `FOSSology`    | Web-Tool für Lizenzanalyse           |

## 📦 Praxis: Lizenz für eigene Applikation

```c
/* SPDX-License-Identifier: GPL-2.0 */
```

* Empfehlung: SPDX-Identifier verwenden
* Quellcode-Kopfzeile mit klarer Lizenzangabe

---

Die Wahl der richtigen Lizenz ist entscheidend für Open-Source-Kompatibilität und Rechtssicherheit – insbesondere bei kommerzieller Nutzung und Distribution.
