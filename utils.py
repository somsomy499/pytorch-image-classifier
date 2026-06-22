"""Utility functions."""
import os
import json
import hashlib
import logging
from pathlib import Path
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)

def setup_logging(level: str = "INFO"):
    logging.basicConfig(
        level=getattr(logging, level.upper()),
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )

def load_config(path: str) -> Dict[str, Any]:
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Config not found: {path}")
    with open(path) as f:
        if path.suffix in (".yaml", ".yml"):
            import yaml
            return yaml.safe_load(f)
        elif path.suffix == ".json":
            return json.load(f)
        elif path.suffix == ".toml":
            import tomllib
            return tomllib.loads(f.read())
    raise ValueError(f"Unsupported config format: {path.suffix}")

def save_config(data: Dict, path: str):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2, default=str)

def hash_text(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()[:16]

def retry(fn, max_attempts: int = 3, delay: float = 1.0, backoff: float = 2.0):
    import time
    last_exc = None
    for attempt in range(max_attempts):
        try:
            return fn()
        except Exception as e:
            last_exc = e
            if attempt < max_attempts - 1:
                time.sleep(delay * (backoff ** attempt))
    raise last_exc

def chunk_list(lst, size):
    for i in range(0, len(lst), size):
        yield lst[i:i+size]

def ensure_dir(path: str):
    Path(path).mkdir(parents=True, exist_ok=True)
