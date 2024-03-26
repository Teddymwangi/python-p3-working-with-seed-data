# tests/test_seed.py

import unittest
from app.models import Game
from app.seed import seed_database
from app import session

class TestSeed(unittest.TestCase):
    def setUp(self):
        # Set up any preconditions for testing
        pass

    def tearDown(self):
        # Clean up after each test
        session.query(Game).delete()
        session.commit()

    def test_seed_database(self):
        # Test seeding database
        seed_database()
        games_count = session.query(Game).count()
        self.assertEqual(games_count, 50, "Seed database should add 50 games")

    def test_seed_no_duplicates(self):
        # Test no duplicate records are created
        seed_database()
        seed_database()
        games_count = session.query(Game).count()
        self.assertEqual(games_count, 50, "Seed database should not create duplicate records")

if __name__ == '__main__':
    unittest.main()
