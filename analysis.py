import re
from typing import Dict, Tuple

class AIAnalysisSystem:
    def __init__(self):
        self.concepts = {
            "neural networks": ["backpropagation", "activation function", "weights"],
            "machine learning": ["supervised", "unsupervised", "reinforcement"],
            "natural language processing": ["tokenization", "embedding", "transformer"],
        }

    def score_response(self, question: str, response: str) -> Tuple[int, str]:
        """
        Score the student's response and return feedback.

        :param question: AI concept question.
        :param response: Student's response to the question.
        :return: Tuple of score and feedback.
        """
        response_lower = response.lower()
        related_keywords = self.concepts.get(question.lower(), [])
        score = sum(1 for word in related_keywords if word in response_lower)

        if score == 0:
            feedback = "Your answer is off-topic. Review the basics of the topic."
        elif score < len(related_keywords) // 2:
            feedback = "You mentioned some relevant points. Consider exploring key areas further."
        else:
            feedback = "Good job! You covered the essential points."

        return score, feedback

    def handle_edge_cases(self, response: str) -> str:
        """
        Handle cases like empty responses or overly verbose answers.
        
        :param response: Student's response.
        :return: Feedback for the edge case.
        """
        if not response.strip():
            return "Empty response detected. Please provide a detailed answer."
        if len(response.split()) > 500:
            return "Response too lengthy. Try to be more concise."
        return None
