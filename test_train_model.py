import unittest
from pathlib import Path

import train_model


class TrainModelTests(unittest.TestCase):
    def test_main_creates_model_file(self):
        model_path = Path(__file__).resolve().parent / "model.pkl"
        if model_path.exists():
            model_path.unlink()

        train_model.main()

        self.assertTrue(model_path.exists())
        self.assertTrue(model_path.is_file())


if __name__ == "__main__":
    unittest.main()
