import os
from typing import TextIO, Dict, Any

import yaml

def load_profile(profile_file : TextIO) -> Dict[str, Any]:
    return yaml.safe_load(profile_file)

def env_constructor(loader, node):
    """Expands !env STRING to replace environment variables in STRING."""
    return os.path.expandvars(node.value)


yaml.SafeLoader.add_constructor("!env", env_constructor)
