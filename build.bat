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
