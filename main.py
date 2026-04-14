import sys
from pathlib import Path

# Ajoute src/ au path Python
sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from orchestrator.orchestrator import Orchestrator

if __name__ == "__main__":
    orch = Orchestrator(
        data_path="big.csv",
        output_dir="output",
        translation_model="Helsinki-NLP/opus-mt-fr-en",
        metric="bleu",
    )
    orch.run()
