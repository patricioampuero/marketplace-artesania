==============================================================================
GUÍA PARA EL EQUIPO: CÓMO DESCARGAR Y EJECUTAR EL PROYECTO
==============================================================================

Hola equipo, aquí están los pasos para clonar el repositorio y dejarlo funcionando en sus computadores.

--- REQUISITOS PREVIOS (Instalar sí o sí) ---
1. Git: https://git-scm.com/downloads
2. Python (3.10 o superior): https://www.python.org/downloads/ (Marcar "Add to PATH" al instalar)
3. Node.js (LTS): https://nodejs.org/es

==============================================================================
PASO 1: DESCARGAR EL CÓDIGO (CLONAR)
==============================================================================

1. Crea una carpeta en tu escritorio donde quieras guardar el proyecto.
2. Haz clic derecho en esa carpeta -> "Open Git Bash here" (o abre una terminal ahí).
3. Ejecuta este comando (reemplaza TU_USUARIO por el usuario de GitHub del proyecto):

   git clone https://github.com/TU_USUARIO/marketplace-artesania.git

4. Entra a la carpeta que se creó:
   cd marketplace-artesania

==============================================================================
PASO 2: CONFIGURAR EL BACKEND (PYTHON)
==============================================================================

1. Abre una terminal dentro de la carpeta "backend".
2. Crea el entorno virtual (haz esto una sola vez):
   python -m venv venv

3. Activa el entorno:
   Windows: .\venv\Scripts\activate
   Mac/Linux: source venv/bin/activate

4. Instala las librerías del proyecto:
   pip install -r requirements.txt
   (Nota: Si no existe requirements.txt, ejecuta: pip install fastapi uvicorn sqlalchemy psycopg2-binary python-dotenv scikit-learn pandas)

5. ¡IMPORTANTE! LA LLAVE MAESTRA (.env)
   Como es un archivo secreto, no está en GitHub. Tienen que crearlo manual:
   
   - Dentro de la carpeta "backend", crea un archivo llamado ".env" (sin comillas).
   - Ábrelo con el Bloc de Notas.
   - Pega EXACTAMENTE esto:

   DB_USER=postgres.beveetgzdzbekzztlnxx
   DB_PASSWORD=Artesania2025
   DB_HOST=aws-1-sa-east-1.pooler.supabase.com
   DB_PORT=6543
   DB_NAME=postgres

   - Guarda y cierra.

==============================================================================
PASO 3: CONFIGURAR EL FRONTEND (REACT)
==============================================================================

1. Abre una terminal en la carpeta "frontend".
2. Instala las dependencias (tarda un poco):
   npm install

==============================================================================
PASO 4: ¡EJECUTAR!
==============================================================================

Si ya hicieron todo lo de arriba UNA VEZ, para trabajar día a día solo hagan esto:

OPCIÓN A (Fácil):
Ve a la carpeta principal y dale doble clic al archivo "INICIAR_TODO.bat".

OPCIÓN B (Manual):
1. Terminal 1 (Backend): python -m uvicorn main:app --reload
2. Terminal 2 (Frontend): npm run dev

Entrar a: http://localhost:5173
