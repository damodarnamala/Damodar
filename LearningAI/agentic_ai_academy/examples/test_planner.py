"""Run: python -m unittest discover -s examples -p 'test_*.py'"""
import unittest
from importlib.machinery import SourceFileLoader
from pathlib import Path

MODULES = Path(__file__).parent
planner = SourceFileLoader("planner", str(MODULES / "04_planner.py")).load_module()

class TestPlanner(unittest.TestCase):
    def test_order(self):
        order = planner.schedule({"build": ["plan"], "plan": []})
        self.assertEqual(order, ["plan", "build"])

    def test_cycle(self):
        with self.assertRaises(ValueError):
            planner.schedule({"a": ["b"], "b": ["a"]})

if __name__ == "__main__":
    unittest.main()
