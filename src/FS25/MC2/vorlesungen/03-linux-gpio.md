# 🔌 Linux GPIO (General Purpose Input/Output)

## 🚀 Ziel

Zugriff auf die GPIO-Pins unter Linux, sowohl aus Userspace als auch im Kernelmodul, verstehen und umsetzen.

## 🔧 Methoden des GPIO-Zugriffs

### 1. Pseudo-Dateisystem (`/sys/class/gpio`)

* Nutzerfreundlich & portabel
* Benötigt GPIO-Treiber im Kernel

#### Typische Befehle:

```bash
echo 340 > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio340/direction
echo 1 > /sys/class/gpio/gpio340/value
echo 340 > /sys/class/gpio/unexport
```

### 2. Speicher-Mapping (Memory Map)

* Direktzugriff auf Register
* Benötigt Root-Rechte und Kenntnis der physischen Adressen
* Schnell, aber nicht portabel

#### Beispiel-Code:

```c
#define GPIO_BASE_ADDR 0xfe200000
#define GPIO_SET0      0x1c
#define GPIO_CLR0      0x28

void *virtual_gpio_base;
uint32_t *gpio_reg = (uint32_t *)(virtual_gpio_base + GPIO_SET0);
*gpio_reg = (0x1 << gpio);
```

## 🗋 Register des BCM2711 (Raspberry Pi 4)

| Register  | Funktion                      |
| --------- | ----------------------------- |
| GPFSEL0-5 | Pin-Funktionsauswahl (In/Out) |
| GPSET0-1  | GPIO auf HIGH setzen          |
| GPCLR0-1  | GPIO auf LOW setzen           |
| GPLEV0-1  | Pegel lesen (Input-Zustand)   |

### Beispiel: GPFSEL für GPIO-Richtung setzen

```c
#define FSELX_OFFSET(pin) ((pin % 10) * 3)
*gpio_reg &= ~(0x7 << FSELX_OFFSET(gpio));  // Clear Bits
*gpio_reg |= (1 << FSELX_OFFSET(gpio));     // Set Output
```

## 🧰 Device Tree

* Deklaration der GPIO-Adressen und Kompatibilität

```dts
soc {
  gpio@7e200000 {
    compatible = "brcm,bcm2711-gpio";
    reg = <0x7e200000 0xb4>; // legacy addr + size
  };
};
```

## ⚖️ mmap-Zugriff in C

```c
int m_mfd = open("/dev/mem", O_RDWR);
virtual_gpio_base = mmap(NULL, 4096, PROT_READ|PROT_WRITE,
                         MAP_SHARED, m_mfd, GPIO_BASE_ADDR);
close(m_mfd);
```

## 🔺 Legacy vs. ARM View Adressen

| Typ               | Adresse      |
| ----------------- | ------------ |
| Legacy (32-bit)   | `0x7e200000` |
| ARM View (35-bit) | `0xfe200000` |

## 🔔 Praxis

* LED an GPIO12 einschalten:

```bash
echo 12 > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio12/direction
echo 1 > /sys/class/gpio/gpio12/value
```

* Button an GPIO22 auslesen:

```bash
echo 22 > /sys/class/gpio/export
echo in > /sys/class/gpio/gpio22/direction
cat /sys/class/gpio/gpio22/value
```

---

Diese GPIO-Kenntnisse bilden die Grundlage für Kernelmodule, Interruptsteuerung und weitere eingebettete Hardwareinteraktionen.
