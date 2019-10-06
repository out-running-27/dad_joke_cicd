import unittest
from app.dad_jokes import get_dad_joke


class TestJokes(unittest.TestCase):
    def test_joke_whittle(self):
        word = "whittle"
        joke = get_dad_joke("AI6pbUSnbh")
        self.assertIn(word, joke)

    def test_joke_flamingo(self):
        word = "When my wife told me to stop impersonating a flamingo, I had to put my foot down."
        joke = get_dad_joke("ORK6UDA5hqc")
        self.assertEqual(word, joke)


if __name__ == "__main__":
    unittest.main()
