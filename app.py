from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

# Pfad zur JSON-Datei, in der unsere Aufgaben gespeichert werden.
TASKS_FILE = Path("tasks.json")


def load_tasks() -> list[dict[str, Any]]:
    """
    Lädt Aufgaben aus tasks.json.

    Fehlerbehandlung:
    - Wenn die Datei fehlt: Eine neue leere Datei wird erstellt.
    - Wenn JSON kaputt ist oder kein Listenformat hat: Leere Liste zurückgeben.
    """
    if not TASKS_FILE.exists():
        save_tasks([])
        return []

    try:
        with TASKS_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)

        # Wir erwarten eine Liste von Aufgaben.
        if not isinstance(data, list):
            return []

        # Zusätzliche Sicherheitsprüfung: Nur gültige Aufgaben übernehmen.
        valid_tasks: list[dict[str, Any]] = []
        for task in data:
            if (
                isinstance(task, dict)
                and isinstance(task.get("id"), int)
                and isinstance(task.get("text"), str)
                and isinstance(task.get("done"), bool)
            ):
                valid_tasks.append(task)
        return valid_tasks

    except (json.JSONDecodeError, OSError):
        # JSON kaputt oder Lesefehler -> sichere Fallback-Liste.
        return []


def save_tasks(tasks: list[dict[str, Any]]) -> None:
    """Speichert Aufgaben als JSON in tasks.json."""
    with TASKS_FILE.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=2)


@app.route("/")
def index() -> str:
    """Startseite: Zeigt Formular + alle Aufgaben."""
    tasks = load_tasks()
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add_task() -> Any:
    """Fügt eine neue Aufgabe hinzu."""
    text = request.form.get("text", "").strip()

    # Leere Eingaben ignorieren.
    if text:
        tasks = load_tasks()

        # Neue ID: max vorhandene ID + 1 (oder 1, wenn Liste leer ist).
        next_id = max((task["id"] for task in tasks), default=0) + 1

        tasks.append({"id": next_id, "text": text, "done": False})
        save_tasks(tasks)

    return redirect(url_for("index"))


@app.route("/done/<int:task_id>", methods=["POST"])
def mark_done(task_id: int) -> Any:
    """Markiert eine Aufgabe als erledigt."""
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            break

    save_tasks(tasks)
    return redirect(url_for("index"))


@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id: int) -> Any:
    """Löscht eine Aufgabe."""
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    return redirect(url_for("index"))


if __name__ == "__main__":
    # Cloud-Umgebungen (z. B. Codespaces/Replit) brauchen oft host=0.0.0.0
    # und einen Port aus der Umgebungsvariable PORT.
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
