# ToDo-Webanwendung mit Flask (für absolute Anfänger)

Dieses Mini-Projekt zeigt dir Schritt für Schritt, wie du mit **Python + Flask** eine einfache ToDo-App baust.

## Projektstruktur

```text
.
├── app.py
├── tasks.json
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── README.md
```

## Voraussetzungen

- Python 3.10 oder neuer
- Terminal (PowerShell, CMD, macOS Terminal oder Linux Shell)

## Ich will **nicht lokal** arbeiten – geht das in der Cloud?

Ja, geht. Am einfachsten mit **GitHub Codespaces**.

- **Wichtig:** Nur die normale GitHub-Webseite (Dateien ansehen/ändern) kann Python nicht ausführen.
- Du brauchst eine Laufzeit-Umgebung. Für dich nehmen wir: **Codespaces**.

### Cloud-Start mit GitHub Codespaces (ohne lokale Installation)

#### Schritt 1: Repository auf GitHub öffnen
1. Öffne dein Repository auf github.com.
2. Klicke auf den grünen Button **Code**.
3. Gehe auf den Tab **Codespaces**.
4. Klicke **Create codespace on main** (oder auf deinem Branch).

Jetzt startet ein Cloud-Editor (VS Code im Browser) – das kann 1–2 Minuten dauern.

#### Schritt 2: Terminal im Codespace öffnen
- Menü: **Terminal → New Terminal**

#### Schritt 3: Flask im Codespace installieren
```bash
python -m venv .venv
source .venv/bin/activate
pip install flask
```

#### Schritt 4: App starten
```bash
python app.py
```

#### Schritt 5: App im Browser öffnen (Port freigeben)
- Nach dem Start erkennt Codespaces den Port `5000` automatisch.
- Unten im Bereich **Ports** erscheint ein Eintrag für `5000`.
- Klicke auf **Open in Browser** (oder auf die URL).

Damit läuft deine Flask-App vollständig in der Cloud.

#### Hinweis zu Kosten
- GitHub Codespaces hat ein Freikontingent (abhängig vom GitHub-Tarif).
- Wenn Kontingent aufgebraucht ist, stoppt der Codespace oder wird kostenpflichtig.

---

## Alternative Cloud-Option (Replit, kurz)

Wenn du lieber Replit nutzt:
1. Neues Python-Repl erstellen.
2. Projektdateien hochladen (`app.py`, `templates`, `static`, `tasks.json`).
3. `pip install flask`.
4. `python app.py` starten.
5. Replit-Web-URL öffnen.

---

## Lokaler Weg (optional)

Falls du später doch lokal starten willst, nutze die Schritte unten.

## 1) Projektordner öffnen

Wechsle im Terminal in den Projektordner:

```bash
cd /pfad/zu/deinem/projekt
```

## 2) Virtuelle Umgebung erstellen (venv)

Eine virtuelle Umgebung hält Projekt-Abhängigkeiten getrennt vom Rest deines Systems.

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Wenn es funktioniert, siehst du meistens `(.venv)` am Anfang deiner Eingabezeile.

## 3) Flask installieren

```bash
pip install flask
```

Optional prüfen:

```bash
pip show flask
```

## 4) App starten

```bash
python app.py
```

Du solltest im Terminal etwas sehen wie:

```text
* Running on http://127.0.0.1:5000
```

## 5) Im Browser öffnen

Öffne diese Adresse im Browser:

- http://127.0.0.1:5000

Jetzt kannst du Aufgaben hinzufügen, als erledigt markieren und löschen.

---

## Optionaler Schnelltest im Terminal

Ja, du kannst diesen Befehl zum Testen verwenden:

```bash
python -m py_compile app.py
```

Was macht das?
- Prüft, ob `app.py` **Syntaxfehler** hat.
- Es startet die Web-App **nicht**.
- Wenn **keine Ausgabe/kein Fehler** kommt, ist die Syntax okay.

Wichtig:
- Das ist nur ein Basis-Test.
- Danach die App normal starten mit:

```bash
python app.py
```

---

## Wie die Daten gespeichert werden

Die Datei `tasks.json` enthält eine Liste von Aufgaben. Beispiel:

```json
[
  {"id": 1, "text": "Milch kaufen", "done": false}
]
```

- `id`: eindeutige Nummer
- `text`: Aufgabe
- `done`: `true` oder `false`

---

## Typische Fehler + Lösungen

### Fehler 1: `ModuleNotFoundError: No module named 'flask'`

**Ursache:** Flask ist nicht installiert (oder falsche Python-Umgebung aktiv).

**Lösung:**

1. Prüfen, ob venv aktiv ist (`(.venv)` sichtbar).
2. Dann installieren:

```bash
pip install flask
```

### Fehler 2: `python` funktioniert nicht

**Ursache:** Auf manchen Systemen heißt der Befehl `python3`.

**Lösung:** Nutze stattdessen:

```bash
python3 app.py
```

### Fehler 3: Port 5000 ist schon belegt

**Ursache:** Eine andere App läuft bereits auf Port 5000.

**Lösung 1:** Andere App beenden.

**Lösung 2:** In `app.py` den Start ändern:

```python
app.run(debug=True, port=5001)
```

Dann im Browser öffnen: http://127.0.0.1:5001

### Fehler 3b: Seite lässt sich nicht öffnen (vor allem in Codespaces/Replit)

**Typische Ursachen:**
- App läuft nicht (Terminal zeigt Fehler).
- Falscher Host/Port.
- In Codespaces wurde der Port nicht geöffnet.

**So prüfst du es:**

1. Starte die App und achte auf die Ausgabe:

```bash
python app.py
```

2. In Codespaces: Tab **Ports** öffnen und Port `5000` (oder den angezeigten Port) im Browser öffnen.
3. Wenn `PORT` von der Cloud gesetzt ist, nutzt die App ihn automatisch.

Hinweis: In `app.py` ist bereits `host=\"0.0.0.0\"` gesetzt, damit die App auch aus der Cloud erreichbar ist.

### Fehler 4: `tasks.json` ist kaputt (ungültiges JSON)

**Ursache:** Datei wurde manuell falsch bearbeitet.

**Lösung:**

- Dateiinhalt auf `[]` setzen und speichern.
- Oder löschen: Die App erstellt sie beim nächsten Start neu.

### Fehler 5: `python: can't open file ... app.py: [Errno 2] No such file or directory`

**Bedeutung:** Du bist im falschen Ordner **oder** der Dateiname/Pfad passt nicht.

**Schnelllösung (in Codespaces-Terminal):**

```bash
pwd
ls
```

Wenn bei `ls` keine `app.py` steht, wechsle in den richtigen Projektordner:

```bash
cd /workspaces/Test
ls
python app.py
```

Wichtig:
- Linux/Codespaces unterscheidet Groß-/Kleinschreibung (`Test` ist nicht `test`).
- Achte auch auf den Pfad: häufig ist es `/workspaces/...` (mit **s**), nicht `/workspace/...`.
- Die pip-`[notice]` Meldung ist **kein Fehler** und verhindert den Start nicht.

---

## Kurz erklärt: Was macht jede Datei?

- `app.py`: Flask-Server + Logik (Routen, Lesen/Schreiben von Aufgaben)
- `tasks.json`: gespeicherte Aufgaben
- `templates/index.html`: HTML-Seite
- `static/style.css`: Design der Seite
- `README.md`: Anleitung

Viel Spaß beim Lernen! 🚀
