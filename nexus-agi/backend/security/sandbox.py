import subprocess


def run_sandboxed_python(code: str) -> dict:
    proc = subprocess.run(['python', '-c', code], capture_output=True, text=True, timeout=30)
    return {'returncode': proc.returncode, 'stdout': proc.stdout, 'stderr': proc.stderr}
