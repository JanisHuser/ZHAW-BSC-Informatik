# 👁️‍🗨️ Computer Vision mit OpenCV

## 🎯 Ziel

Grundlagen der Bildverarbeitung mit OpenCV verstehen und anwenden, insbesondere im Kontext von Embedded Linux und Python.

## 📦 Was ist OpenCV?

* **Open Source Computer Vision Library**
* Seit 1999 (Intel), heute plattformübergreifend
* Programmiersprachen: C++, Python, Java
* Plattformen: Linux, Windows, macOS, Android, iOS
* GPU-Unterstützung mit CUDA, OpenCL

## 🐍 Python-Basics für OpenCV

```python
import cv2
import numpy as np
```

### Bild einlesen und anzeigen

```python
img = cv2.imread('bild.jpg')
cv2.imwrite('ausgabe.jpg', img)
```

### Argumente per Kommandozeile

```python
import sys
img = cv2.imread(sys.argv[1])
```

## 🧱 Bildstruktur

* Farbige Bilder: 3D-Array (Höhe × Breite × Kanäle)
* Graustufenbilder: 2D-Array

## 🎨 Bildmanipulationen

### Eigenschaften abfragen

```python
h, w, c = img.shape
img.dtype, img.size
```

### Pixelzugriff

```python
px = img[100, 100]       # Zugriff auf BGR-Werte
img[100, 100] = [255, 0, 0]  # Setzt Pixel blau
```

### Farbkanäle splitten/mergen

```python
b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))
```

### Kanäle nullsetzen

```python
img[:, :, 1] = 0  # Kein Grün
```

## 📸 Video mit OpenCV

### Kamera-Zugriff

```python
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
cv2.imwrite('grau.jpg', gray)
cap.release()
```

## 🖍 Zeichenfunktionen

```python
cv2.line(img, (0, 0), (100, 100), (255, 0, 0), 3)
cv2.rectangle(img, (10, 10), (50, 50), (0, 255, 0), 2)
cv2.circle(img, (60, 60), 20, (0, 0, 255), -1)
```

## 🧠 Bildverarbeitung

### Farbraumkonvertierung

```python
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
```

### Convolution

* Anwenden von Filtern (z. B. Weichzeichnen, Kanten finden)

### Beispiel: Median Blur

```python
cv2.medianBlur(img, 5)
```

## 📚 Weitere Features

### Texterkennung (OCR)

* Integration mit Tesseract

### Bar-/QR-Code-Erkennung

* z. B. mit `pyzbar` oder OpenCV-Funktionalität

### Objekterkennung

* Haar-Cascades: Gesichtserkennung uvm.

## 📈 Performance

```python
t1 = cv2.getTickCount()
# Verarbeitung
elapsed = (cv2.getTickCount() - t1) / cv2.getTickFrequency()
print(f"Dauer: {elapsed:.4f} s")
```

### Optimierung aktivieren

```python
cv2.setUseOptimized(True)
```

---

OpenCV ist das zentrale Werkzeug für Bildverarbeitung im Embedded-Bereich – effizient, flexibel und plattformunabhängig einsetzbar.
