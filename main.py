"""Autodespliegue MT example: a page that counts its visits in the service's own Firestore."""
import html
import os

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from google.cloud import firestore

app = FastAPI()
_db = None


def db():
    global _db
    if _db is None:
        # Always the database the platform gave this service, never "(default)".
        _db = firestore.Client(database=os.environ["FIRESTORE_DATABASE"])
    return _db


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    who = request.headers.get("x-goog-authenticated-user-email", "").split(":")[-1]
    ref = db().collection("visits").document("counter")
    ref.set({"n": firestore.Increment(1)}, merge=True)
    n = ref.get().to_dict().get("n", 0)
    return f"""<!doctype html><html lang="es"><meta charset="utf-8">
<title>Ejemplo · Autodespliegue MT</title>
<body style="font-family:sans-serif;max-width:40rem;margin:4rem auto;padding:0 1rem">
<h1>Funciona</h1><p>Hola {html.escape(who) or "socio"}. Esta página se ha visto <b>{n}</b> veces.</p>
<p>Desplegada con Autodespliegue MT. El contador vive en la base de datos Firestore de este servicio.</p>
</body></html>"""


@app.get("/_ok")
def ok():
    return {"ok": True}
