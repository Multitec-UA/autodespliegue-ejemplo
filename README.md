# Ejemplo · Autodespliegue MT

La aplicación más pequeña que funciona en [despliega.multitecua.com](https://despliega.multitecua.com):
una página que cuenta sus visitas en la base de datos Firestore del propio servicio.

Úsala como plantilla: **Use this template** en GitHub, cambia `main.py`, y conecta tu
copia desde el panel. Lo que importa está en tres sitios:

- `Dockerfile`: escucha en `0.0.0.0:$PORT`.
- `main.py`: `firestore.Client(database=os.environ["FIRESTORE_DATABASE"])`, nunca la base de datos por defecto.
- `autodespliegue.yaml`: opcional, rellena el formulario del panel.

Antes de hacer push, tu agente puede comprobarlo con la skill
[autodespliegue-skills](https://github.com/Multitec-UA/autodespliegue-skills):
`python3 check_service.py --build .`
