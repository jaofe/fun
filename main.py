import time
import subprocess

def run_script():
    while True:
        # Execute the CAPCHA.py script
        subprocess.run(['python', 'CAPCHA.py'])
        
        # Wait for 30 seconds
        time.sleep(30)

if __name__ == '__main__':
    run_script()
