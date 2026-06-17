import os
import subprocess
import json

def generate_build_diagnostics():
    try:
        result = subprocess.run(['cmake', '--build', '.', '--config', 'Release'], check=True, capture_output=True, text=True)
        with open('diagnostic/build-XXX.logd', 'w') as f:
            f.write(result.stdout + result.stderr)
        with open('diagnostic/build-XXX.json', 'w') as f:
            json.dump({'status': 'success'}, f)
    except subprocess.CalledProcessError as e:
        with open('diagnostic/build-XXX.logd', 'w') as f:
            f.write(e.stdout + e.stderr)
        with open('diagnostic/build-XXX.json', 'w') as f:
            json.dump({'status': 'failure', 'error': str(e)}, f)

if __name__ == '__main__':
    generate_build_diagnostics()