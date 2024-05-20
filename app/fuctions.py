from pathlib import Path
from rest_framework.response import Response
BASE_DIR = Path(__file__).resolve().parent.parent

def lines():
    file_path = f"{BASE_DIR}/app/otm.txt"
    lines = []

    # Faylni ochish va har bir qatorni listga kiritish
    with open(file_path, 'r') as file:
        for line in file:
            lines.append((line.strip(),line.strip()))

    return tuple(lines)

