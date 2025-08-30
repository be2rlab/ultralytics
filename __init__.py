# Ultralytics YOLO 🚀, AGPL-3.0 license

__version__ = "8.0.120"

import sys
from pathlib import Path

# Add parent directory of 'ultralytics' to path to allow absolute imports
# like 'from ultralytics.yolo.utils import ...'
ultralytics_parent_dir = str(Path(__file__).parent.parent.resolve())
if ultralytics_parent_dir not in sys.path:
    sys.path.insert(0, ultralytics_parent_dir)

from ultralytics.hub import start
from ultralytics.vit.rtdetr import RTDETR
from ultralytics.vit.sam import SAM
from ultralytics.yolo.engine.model import YOLO
from ultralytics.yolo.nas import NAS
from ultralytics.yolo.utils.checks import check_yolo as checks

__all__ = (
    "__version__",
    "YOLO",
    "NAS",
    "SAM",
    "RTDETR",
    "checks",
    "start",
)  # allow simpler import
