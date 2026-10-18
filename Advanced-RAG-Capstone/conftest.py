"""
Makes `import config` and `import src...` work when running pytest.

pytest adds the folder containing this file to Python's import path, so the
tests in `tests/` can import modules from the project root without any
packaging setup.
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
