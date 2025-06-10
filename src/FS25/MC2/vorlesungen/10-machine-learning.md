# 🤖 Embedded Machine Learning

## 🎯 Ziel

Verständnis für die Anwendung von Machine Learning (ML) auf Embedded-Systemen mit eingeschränkten Ressourcen.

## 🧠 Grundlagen Neuronaler Netze

### Feed Forward Netze

* Bestehen aus: Eingabeschicht, versteckten Schichten, Ausgabeschicht
* Verbindungen zwischen allen Neuronen jeder Schicht
* Können beliebige stetige Funktionen approximieren

### Aktivierungsfunktionen

| Funktion   | Formel / Verhalten                  | Verwendung                      |
| ---------- | ----------------------------------- | ------------------------------- |
| Sigmoid    | $\frac{1}{1 + e^{-x}}$              | Klassisch, nicht mehr empfohlen |
| Tanh       | $\frac{e^x - e^{-x}}{e^x + e^{-x}}$ | Besser als Sigmoid              |
| ReLU       | $\max(0, x)$                        | Standard für hidden layers      |
| Leaky ReLU | $\max(\alpha x, x)$                 | Vermeidet "Dead Neurons"        |

## 📝 Beispiel: MNIST Dataset

* Handgeschriebene Ziffern (0–9)
* 28×28 Pixel, Graustufen
* Trainingsdaten: 60'000 Bilder, Testdaten: 10'000
* In Keras integriert: `keras.datasets.mnist.load_data()`

## ⚙️ Trainingsablauf

1. **Initialisierung**: Gewichtung & Architektur definieren
2. **Forward Pass**: Input → Output berechnen
3. **Loss berechnen**: z. B. mit `categorical_crossentropy`
4. **Backpropagation**: Gradienten berechnen
5. **Optimierung**: z. B. mit `Adam`, `SGD`, `RMSprop`
6. **Wiederholung** über viele Epochen

### Codebeispiel mit Keras

```python
model = keras.Sequential([
    keras.Input(shape=(28, 28, 1)),
    layers.Flatten(),
    layers.Dense(16, activation="relu"),
    layers.Dense(16, activation="relu"),
    layers.Dense(10, activation="softmax"),
])
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
model.fit(x_train, y_train, batch_size=50, epochs=5, verbose=1)
```

## ⚙️ Training vs. Inferenz

| Phase    | Beschreibung                                             |
| -------- | -------------------------------------------------------- |
| Training | Nur auf leistungsstarken Systemen                        |
| Inferenz | Optimiert für Embedded (z. B. Raspberry Pi, Jetson Nano) |

## 🧰 Frameworks

| Framework  | Beschreibung                     |
| ---------- | -------------------------------- |
| TensorFlow | Marktführer, weit verbreitet     |
| Keras      | High-Level API auf TensorFlow    |
| PyTorch    | Flexibel & beliebt bei Forschung |
| TFLite     | Optimiert für Embedded Inferenz  |

## 🖼️ Praxisszenario

* Kamera → Bild → OpenCV-Preprocessing → TensorFlow-Modell → Klassifikation

## 🧪 Lab Setup

* Eingabegerät: USB-Kamera
* Hardware: Raspberry Pi
* Training auf PC, Deployment auf Pi

## 🪄 Optimierungen für Embedded

* Quantisierung (8-bit statt 32-bit)
* Pruning (Entfernung unwichtiger Gewichte)
* Model Compression (z. B. mit TFLite Converter)

---

Embedded Machine Learning macht es möglich, KI in kleine Geräte zu bringen – lokal, datensparsam und reaktiv.
