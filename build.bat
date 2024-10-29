@echo off

:: Create a virtual environment
python -m venv venv

:: Activate the virtual environment
call venv\Scripts\activate

:: Install requirements
pip install -r requirements.txt

:: Run PyInstaller with the specified options
pyinstaller --onefile --name=fun --icon=icon.ico main.py --add-data "CAPCHA/*;CAPCHA" --noconsole

:: Deactivate the virtual environment
call venv\Scripts\deactivate

:: Ensure the destination directory exists
if not exist "%ProgramFiles%\fun" (
    mkdir "%ProgramFiles%\fun"
)

:: Copy the executable to Program Files
xcopy /y /i "dist\fun.exe" "%ProgramFiles%\fun\"

:: Schedule the task to run on workstation unlock
schtasks /create /sc ONLOGON /tn "fun" /tr  "\"C:\Program Files\fun\fun.exe\"" /ru System /rl HIGHEST
