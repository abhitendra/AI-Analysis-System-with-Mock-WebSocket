import unittest
from analysis import AIAnalysisSystem

class TestAIAnalysisSystem(unittest.TestCase):
    def setUp(self):
        self.system = AIAnalysisSystem()

    def test_score_response(self):
        score, feedback = self.system.score_response("neural networks", "Backpropagation is key.")
        self.assertEqual(score, 1)
        self.assertIn("Good job", feedback)

    def test_empty_response(self):
        feedback = self.system.handle_edge_cases("")
        self.assertEqual(feedback, "Empty response detected. Please provide a detailed answer.")

    def test_lengthy_response(self):
        long_response = "word " * 501
        feedback = self.system.handle_edge_cases(long_response)
        self.assertEqual(feedback, "Response too lengthy. Try to be more concise.")

    def test_off_topic_response(self):
        score, feedback = self.system.score_response("machine learning", "Quantum physics is fascinating.")
        self.assertEqual(score, 0)
        self.assertIn("off-topic", feedback)

if __name__ == "__main__":
    unittest.main()
