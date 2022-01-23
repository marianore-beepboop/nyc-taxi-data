from pathlib import Path

from pkg_resources import resource_filename

_p = Path(resource_filename("project", "/"))

PROJECT_PATH = _p / "project"
REPO_ROOT = _p.parent
RESOURCES_PATH = _p / "resources"
DATA_DIR = RESOURCES_PATH / "data"
