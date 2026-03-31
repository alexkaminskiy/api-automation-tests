import os
from typing import Optional
import yaml


def load_config(path: Optional[str] = None) -> dict:
    """Load YAML config. If path not provided, load from config/config.yaml."""
    cfg_path = path or os.path.join(os.path.dirname(os.path.dirname(__file__)), "config", "config.yaml")
    try:
        with open(cfg_path, "r", encoding="utf-8") as f:
            cfg = yaml.safe_load(f) or {}
    except FileNotFoundError:
        cfg = {}

    # Allow environment variable overrides
    base_url = os.getenv("API_BASE_URL")
    if base_url:
        cfg["base_url"] = base_url

    return cfg
