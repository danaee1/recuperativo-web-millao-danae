from pathlib import Path
from html import escape

# Obtener la carpeta principal del proyecto.
CARPETA = Path(__file__).resolve().parent.parent

# Archivo HTML que generará Python.
ARCHIVO_SALIDA = CARPETA / "novedades.html"

# Lista de diccionarios con información de las noticias.
noticias = [
    {
        "titulo": "Taller de programación",
        "fecha": "25 de octubre de 2026",
        "descripcion": "Aprende los fundamentos de la programación web."
    },
    {
        "titulo": "Nuevos recursos educativos",
        "fecha": "20 de octubre de 2026",
        "descripcion": "Descubre herramientas digitales para estudiar."
    },
    {
        "titulo": "Ciudadanía digital",
        "fecha": "15 de octubre de 2026",
        "descripcion": "Aprende a utilizar internet de forma segura."
    }
]


def generar_html(lista):
    """Convierte una lista de noticias en contenido HTML."""

    contenido = ""

    # Recorrer cada noticia de la lista.
    for noticia in lista:
        titulo = escape(noticia["titulo"])
        fecha = escape(noticia["fecha"])
        descripcion = escape(noticia["descripcion"])

        contenido += f"""
        <article class="noticia">
            <p class="fecha">{fecha}</p>
            <h2>{titulo}</h2>
            <p>{descripcion}</p>
        </article>
        """

    # Crear el documento HTML completo.
    pagina = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Novedades | EduTech Chile</title>
    <link rel="stylesheet" href="styles/style.css">
</head>
<body>

    <header>
        <h1>Novedades de EduTech Chile</h1>
        <p>Noticias de nuestra comunidad escolar.</p>
        <a class="boton" href="index.html">Volver al inicio</a>
    </header>

    <main>
        <section>
            {contenido}
        </section>
    </main>

    <footer>
        <p>&copy; 2026 EduTech Chile</p>
    </footer>

</body>
</html>
"""

    return pagina


def main():
    """Crear y guardar el archivo HTML."""

    pagina = generar_html(noticias)

    ARCHIVO_SALIDA.write_text(
        pagina,
        encoding="utf-8"
    )

    print("¡Página de novedades generada correctamente!")
    print(f"Archivo guardado en: {ARCHIVO_SALIDA}")


# Ejecutar el programa.
if __name__ == "__main__":
    main()