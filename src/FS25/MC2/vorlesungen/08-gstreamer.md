# 🎥 Multimedia mit GStreamer

## 🎯 Ziel

Verständnis des GStreamer-Frameworks zur Verarbeitung von Audio- und Videodaten in Embedded-Linux-Systemen.

## 📦 Was ist GStreamer?

* Framework zur Erstellung von Multimedia-Pipelines
* Unterstützt Audio, Video, Netzwerk, Codecs, Filter, Effekte
* Modularer Aufbau: Einzelne Verarbeitungsschritte als "Elemente"

## 🧱 Aufbau einer GStreamer-Pipeline

```text
Quelle → Filter → Codec → Ausgabe
```

Beispiel:

```bash
gst-launch-1.0 audiotestsrc ! audioconvert ! audioresample ! autoaudiosink
```

## 🔧 Wichtige GStreamer-Komponenten

| Komponente        | Beschreibung                          |
| ----------------- | ------------------------------------- |
| `gst-launch-1.0`  | CLI-Werkzeug zum Testen von Pipelines |
| `gst-inspect-1.0` | Zeigt Infos über Plugins & Elemente   |
| `filesrc`         | Liest Datei von Datenträger           |
| `v4l2src`         | Kameraeingang (Video4Linux2)          |
| `alsasrc`         | Mikrofoneingang                       |
| `alsasink`        | Audioausgabe über ALSA                |
| `ximagesink`      | Videoausgabe im Fenster               |

## 🔄 Datenfluss mit `caps`

* `capabilities` definieren Datenformat zwischen Elementen
* Beispiel: `video/x-raw,format=YUY2,width=640,height=480`

## 🧪 Praxisbeispiele

### 📺 Video anzeigen

```bash
gst-launch-1.0 v4l2src ! videoconvert ! autovideosink
```

### 🎙 Audio aufnehmen und abspielen

```bash
gst-launch-1.0 alsasrc ! audioconvert ! audioresample ! autoaudiosink
```

### 📼 Video speichern

```bash
gst-launch-1.0 v4l2src ! videoconvert ! x264enc ! mp4mux ! filesink location=video.mp4
```

### 🔄 Kamera → Grayscale-Bild → JPEG speichern

```bash
gst-launch-1.0 v4l2src ! videoconvert ! imagefreeze ! jpegenc ! filesink location=bild.jpg
```

## 📚 GStreamer in eigenen Programmen

```c
#include <gst/gst.h>

int main(int argc, char *argv[]) {
  gst_init(&argc, &argv);
  GstElement *pipeline = gst_parse_launch("videotestsrc ! autovideosink", NULL);
  gst_element_set_state(pipeline, GST_STATE_PLAYING);
  g_main_loop_run(g_main_loop_new(NULL, FALSE));
  gst_element_set_state(pipeline, GST_STATE_NULL);
  gst_object_unref(pipeline);
  return 0;
}
```

## 📋 Fehleranalyse

* Umgebungsvariable setzen: `GST_DEBUG=3` (bis 5 für detaillierter)
* Logdatei schreiben: `GST_DEBUG_DUMP_DOT_DIR=/tmp`
* Visualisierung mit Graphviz möglich

---

GStreamer bietet eine mächtige Grundlage zur Audio-/Videoverarbeitung auf Embedded-Systemen und ist hochgradig modular erweiterbar.
