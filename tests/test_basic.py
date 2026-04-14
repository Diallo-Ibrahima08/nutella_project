import sys
from pathlib import Path

# Ajoute src/ et la racine au path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))


def test_placeholder():
    assert True


def test_loader_importable():
    from loaders.base_loader import BaseLoader

    assert BaseLoader is not None


def test_evaluator_importable():
    from evaluators.evaluator import Evaluator

    assert Evaluator is not None


def test_config():
    import config

    assert config.DATA_DIR is not None
    assert config.OUTPUT_DIR is not None
