"""
Smoke test for stock_alert/main.py.

Checks that main.py executes without errors and defines its entry points
(make_agent, _web, main). No LLM, no network, no API keys required.
"""
import importlib.util
import sys
from pathlib import Path

# Add stock_alert dir to path so we can import main directly
_DEMO_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(_DEMO_DIR))
sys.path.insert(0, str(_DEMO_DIR.parent))  # demo_apps root for _llm.py


# ---------------------------------------------------------------------------
# Module-level import test — ensure no syntax errors
# ---------------------------------------------------------------------------

class TestStockAlertImport:

    def test_module_imports_cleanly(self):
        """main.py loads and defines its entry points (nothing runs at import time)."""
        spec = importlib.util.spec_from_file_location(
            "stock_alert_main", str(_DEMO_DIR / "main.py")
        )
        if spec is None or spec.loader is None:
            raise ImportError(f"could not load {_DEMO_DIR}/main.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        for name in ("make_agent", "_web", "main"):
            assert callable(getattr(module, name)), f"main.py no longer defines {name}()"
