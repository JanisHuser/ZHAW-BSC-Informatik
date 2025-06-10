# 🧬 Linux Kernel

## 🏗 Architektur

### 📦 Kerneltypen

| Typ          | Beschreibung                                           |
| ------------ | ------------------------------------------------------ |
| Monolithisch | Alles in einem Kernelimage, inkl. Treiber              |
| Modular      | Monolithisch mit ladbaren Modulen (\*.ko) zur Laufzeit |

Linux ist modular **und** monolithisch – es erlaubt dynamisches Nachladen von Modulen, behält aber die monolithische Struktur.

### 🧱 Architektur-Übersicht

```text
Anwendungen
 └─ Systembibliotheken (libc)
     └─ System Call Interface (SYSCALL)
         └─ Kernelspace:
             ├─ Prozessverwaltung
             ├─ Speicherverwaltung (MMU)
             ├─ Gerätetreiber
             ├─ Dateisysteme
             └─ Netzwerkschnittstellen
```

## 🕳 System Calls

* Ermöglichen Übergang von Userspace in Kernelspace
* Beispiel: `read()`, `write()`, `open()`, `ioctl()`

## 🗃 Kernel-Sourcen

* Bezugsquelle: [https://www.kernel.org](https://www.kernel.org)
* Verzeichnisstruktur:

```text
/usr/src/linux
 ├── arch/      # Architektur-spezifisch (z. B. arm, x86)
 ├── drivers/   # Gerätetreiber
 ├── fs/        # Dateisysteme
 ├── include/   # Headerdateien
 ├── kernel/    # Kernelkern: Scheduler, Signals
 └── net/       # Netzwerkstack
```

## ⚙️ Konfiguration & Kompilierung

### Konfigurationstools:

* `make menuconfig` (Textoberfläche)
* `make xconfig` (GUI)

### Konfigurationsdateien:

* `.config`: Ergebnis der Konfiguration
* Mit Yocto: `bitbake -c menuconfig virtual/kernel`

### Kernel bauen:

```bash
make ARCH=arm CROSS_COMPILE=arm-linux-gnueabi- zImage
```

### Module installieren:

```bash
make INSTALL_MOD_PATH=/pfad/ modules_install
```

## 📦 Kernelmodule

* Dynamisch ladbare Erweiterungen (\*.ko)
* Einbindung in Kernel zur Laufzeit mit `insmod`, `modprobe`

### Minimalbeispiel:

```c
#include <linux/module.h>
#include <linux/init.h>

static int __init hello_init(void) {
    pr_info("Hello Kernel\n");
    return 0;
}
static void __exit hello_exit(void) {
    pr_info("Bye Kernel\n");
}
module_init(hello_init);
module_exit(hello_exit);
MODULE_LICENSE("GPL");
```

## 🧪 Kernel starten & Debugging

* Erster Prozess: `/sbin/init`
* Runlevel steuern Startverhalten
* Tools:

  * `dmesg` – Kernelmeldungen
  * `lsmod`, `modinfo`, `insmod`, `rmmod` – Modulinformationen

---

Diese Grundlagen bereiten auf die Entwicklung eigener Kernelmodule, Platform-Driver und Device-Tree-Integration vor.
