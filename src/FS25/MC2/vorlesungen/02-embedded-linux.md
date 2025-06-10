# 📦 Embedded Linux System

## 🪑 Ziel

Ein minimales Linux-System für eingebettete Hardware verstehen, erstellen und analysieren.

## 🔢 Grundlegende Linux-Kommandos

| Kommando                  | Funktion                         |
| ------------------------- | -------------------------------- |
| `ls`, `cd`, `pwd`         | Navigation im Dateisystem        |
| `cp`, `mv`, `rm`          | Dateioperationen                 |
| `grep`, `find`            | Suchen nach Inhalten und Dateien |
| `chmod`, `chown`, `chgrp` | Rechteverwaltung                 |
| `df -h`, `du -skh`        | Speicherplatz anzeigen           |
| `tar`, `gzip`             | Archivieren & Komprimieren       |
| `mount`, `umount`         | Einhängen von Dateisystemen      |

## 📀 Linux-Dateisystem

* Wurzelverzeichnis: `/`
* Wichtige Verzeichnisse:

  * `/bin`, `/sbin`, `/lib`: essentielle Programme und Bibliotheken
  * `/etc`: Konfigurationsdateien
  * `/dev`: Gerätedateien
  * `/proc`, `/sys`: Pseudo-Dateisysteme zur Kernelkommunikation

## 🚗 Zielplattformen

* Plattformen mit und ohne MMU (Memory Management Unit)
* ✅ Anforderungen:

  * mind. 8 MB RAM (besser 32 MB)
  * 4 MB Flash oder Ramdisk

## 💻 Hardwaretypen

| Typ                 | Beschreibung                             |
| ------------------- | ---------------------------------------- |
| Component on Module | Nur CPU, RAM, Flash mit Steckkontakten   |
| Evaluation Board    | Voll ausgestattete Entwicklungsplattform |
| Custom Platform     | Selbst entwickelte Hardware              |

## ⚙️ Toolchain für Embedded Linux

* Trennung zwischen **Host** (Entwicklung) und **Target** (Zielsystem)
* Typen:

  * **Native Toolchain** (nur für Host)
  * **Cross-Compiler**: Kompiliert auf Host für Zielarchitektur (z. B. ARM)

### Toolchain-Komponenten

* **GCC** (Compiler)
* **Binutils** (Linker, Assembler)
* **C-Library** (z. B. glibc, uClibc, musl)
* **Debugger** (gdb, gdbserver)

## ⚡ Bootloader & Startprozess

* Typisch: **U-Boot** auf Embedded Systemen
* Aufgaben:

  * Initialisierung der HW
  * Laden des Kernels
  * Übergabe von Kernelparametern (root=...)

## 📆 Praktischer Ablauf

### Lab1: Yocto SD-Image

* Erstellung eines kompletten Images mit eigener Applikation
* Befehl: `bitbake core-image-minimal`
* Ergebnis: bootfähiges System auf SD-Karte

### Lab2-12: NFS-basiertes System

* Kernel & U-Boot auf SD-Karte, Rest über Netzwerk (NFS RootFS)
* Entwicklung & Debugging über SSH, GDB, Serial Console

## 🚤 Root-Benutzer & sudo

* Root darf alles, Standardbenutzer nicht
* `sudo` ermöglicht Ausführung privilegierter Kommandos als normaler Benutzer

## 🚪 Startprozess

* Erster Prozess: `/sbin/init`
* Verwaltet Runlevel (z. B. 0 = Shutdown, 3 = Multi-User)
* Tools: `shutdown`, `reboot`, `halt`

---

Dies bildet die Grundlage für alle weiteren Themen wie GPIO, Kernelmodule, Scheduling und Realtime.
