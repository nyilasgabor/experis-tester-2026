import unittest

from Fish import Fish
from Plant import Plant

class TestAquarium(unittest.TestCase):

    def test_goldfish(self):
        # Arrange
        goldfish = Fish("Goldfish", 0)

        # Act
        goldfish.update_food_level(20)

        # Assert
        self.assertEqual(goldfish.food_level, 12)

    def test_seeweed(self):
        seeweed = Plant("Seeweed", 0)
        seeweed.update_food_level(16)
        self.assertEqual(seeweed.food_level, 8)


if __name__ == "__main__":
    unittest.main()


