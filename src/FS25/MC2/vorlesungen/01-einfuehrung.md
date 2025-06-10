Hier ist eine Zusammenfassung zum Thema **„Einführung & Yocto Projekt“** aus dem Modul *Microcomputer Systems 2 (MC2)*:

---

# 📦 Einführung & Yocto-Projekt

## 🔍 Was ist Embedded Linux?

* **Embedded Linux**: Nutzung des Linux-Kernels in eingebetteten Systemen (Router, TVs, Steuergeräte).
* Kombiniert Kernel mit Open-Source-Komponenten (glibc, busybox, etc.).
* Vorteile:

  * Keine Lizenzkosten
  * Wiederverwendbarkeit von Komponenten
  * Große Community-Unterstützung
  * Viele verfügbare Bibliotheken und Treiber

## 💡 Warum ein Build-System?

### Ohne Build-System:

* Manuelles Bauen jeder Komponente
* Abhängigkeiten müssen händisch aufgelöst werden
* Schwer wart- und reproduzierbar

### Mit Build-System:

* Automatisierter Download, Konfiguration, Kompilierung
* Bessere Wartbarkeit und Anpassbarkeit
* Reproduzierbare Builds

## 🧰 Bekannte Build-Systeme:

| Name          | Eigenschaften                                                  |
| ------------- | -------------------------------------------------------------- |
| **Buildroot** | Einfach, für kleine Systeme geeignet                           |
| **PTXdist**   | Von Pengutronix, für Industrieeinsatz                          |
| **OpenWRT**   | Ursprunglich für Router, sehr flexibel                         |
| **Yocto**     | Sehr anpassbar, Layer-basiert, Standard bei Industrieprojekten |

---

## 🧱 Das Yocto-Projekt

### 📌 Definition:

* Sammlung von Werkzeugen, Vorlagen und Methoden
* Ziel: Erzeugung angepasster Embedded-Linux-Distributionen
* Initiator: **Linux Foundation** (seit 2010)

### 📦 Hauptkomponenten:

* **Poky**: Referenzdistribution (besteht aus BitBake, OpenEmbedded Core etc.)
* **BitBake**: Build-Engine (interpretiert Rezepte `.bb`)
* **Layers**: Sammlungen von Rezepten & Konfigurationen

### 📁 Verzeichnisstruktur (vereinfacht):

```
poky/
 ├── bitbake/          # Build-Engine
 ├── meta/             # OpenEmbedded Core Layer
 ├── meta-yocto/       # Yocto-spezifische Erweiterungen
 ├── meta-yocto-bsp/   # Board Support Packages (BSPs)
```

### 📐 Layer hinzufügen:

* Konfiguration über:

  * `bblayers.conf`: Aktivierte Layer
  * `local.conf`: Zielarchitektur, Build-Optionen, Anwendungen

### 🧪 Beispiel: Raspberry Pi

* Layer `meta-raspberrypi` einfügen
* Applikationen via eigener Layer z. B. `meta-student`, `meta-mc2` einbinden

---

## 🗓 Semesterplan FS25 (Auszug)

| Woche | Thema                  | Labor                         |
| ----- | ---------------------- | ----------------------------- |
| 1     | Embedded Linux & Yocto | Lab1: BitBake & Layerstruktur |
| 2     | Embedded Linux System  | Lab2: Softwareentwicklung     |
| ...   | ...                    | ...                           |

---

Wenn du möchtest, kann ich dir diese Zusammenfassung auch als Markdown-Datei exportieren.
