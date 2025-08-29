# tests/conftest.py
import sys
from pathlib import Path

# adiciona a RAIZ do repositório ao sys.path, assim "src" vira um pacote top-level
REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))
