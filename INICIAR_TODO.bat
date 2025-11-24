@echo off
echo ==========================================
echo INICIANDO EL MARKETPLACE DE ARTESANIA
echo ==========================================

:: 1. Abrir Backend en una ventana nueva
start cmd /k "cd backend && venv\Scripts\activate && python -m uvicorn main:app --reload"

:: 2. Abrir Frontend en una ventana nueva
start cmd /k "cd frontend && npm run dev"

echo Todo listo jefe. Las ventanas se abrieron.
timeout 5