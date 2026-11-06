@echo off
cd /d "%~dp0"
echo ==========================================
echo       ARGUS 4.3 - CINEMATIC WAKE INITIALISATION
echo ==========================================
where py >nul 2>nul
if errorlevel 1 (
  echo Python launcher not found. Install Python 3.12 x64.
  pause
  exit /b 1
)
py -3.12 -m venv .venv
if errorlevel 1 goto failed
call .venv\Scripts\activate.bat
python -m pip install --upgrade pip
if errorlevel 1 goto failed
python -m pip install -r requirements.txt
if errorlevel 1 goto failed
if not exist .env copy .env.example .env
echo.
echo Installing the offline ARGUS wake-word model...
python download_wake_model.py
echo.
echo Setup complete. Open .env and add your Gemini API key.
echo Keep the key private. Never paste it into chat or screenshots.
pause
exit /b 0
:failed
echo Setup failed. Check Python 3.12 x64 and internet connection.
pause
exit /b 1
