# ♟️ CheckMate

> **Tu escudo contra la desinformación.**

CheckMate es una herramienta de verificación de noticias ("Fact-Checking") que permite contrastar titulares o enlaces sospechosos directamente con la base de datos oficial de **Google Fact Check Tools**.

Desarrollado para combatir las Fake News de manera rápida, visual y sencilla.

---

## ✨ Características

* 🔍 **Detección Inteligente:** Pega un link y CheckMate extraerá el titular automáticamente (Web Scraping).
* 🚦 **Semáforo de Verdad:** Interfaz visual que resalta si una noticia es VERDADERA, FALSA o ENGAÑOSA.
* 📱 **Diseño Moderno:** Interfaz web limpia y responsiva (gracias a Pico.css).
* ⚡ **Motor de Búsqueda:** Conexión directa con APIs de verificación globales (AFP, EFE, Maldita.es, etc.).

---

## 🛠️ Tecnologías Utilizadas

Este proyecto fue construido con:

* **Python 3.x**: Lógica del backend.
* **Flask**: Servidor web ligero.
* **BeautifulSoup4**: Para el scraping de metadatos en URLs.
* **Pico.css**: Framework CSS minimalista para la interfaz.
* **Google Fact Check API**: Fuente de datos de verificación.

---

## 🚀 Instalación y Uso

Si quieres correr este proyecto en tu máquina local:

1.  **Clona el repositorio:**
    ```bash
    git clone [https://github.com/FreeFlowLabsCL/check-mate.git](https://github.com/FreeFlowLabsCL/check-mate.git)
    cd check-mate
    ```

2.  **Crea un entorno virtual (Recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Linux/Mac
    # venv\Scripts\activate   # En Windows
    ```

3.  **Instala las dependencias:**
    ```bash
    pip install Flask requests beautifulsoup4 colorama
    ```

4.  **Configura tu API Key:**
    Necesitas una API Key de Google Cloud Platform con acceso a "Fact Check Tools API".
    ```bash
    export google_API="TU_CLAVE_AQUI"
    ```

5.  **Ejecuta la aplicación:**
    ```bash
    python app.py
    ```

6.  **Abre tu navegador:**
    Visita `http://127.0.0.1:5000`

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT - siéntete libre de usarlo y mejorarlo.

---
Hecho con ☕ y Python por **[FreeFlowLabsCL]**.