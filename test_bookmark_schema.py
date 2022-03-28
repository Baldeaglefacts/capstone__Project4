import unittest
from unittest import TestCase
from unittest.mock import patch
import sqlite3
import bookmark_schema

class mockDB(TestCase):
    
    @patch('bookmark_schema.insert_data')
    def test_insert_data_2(self, mock_data):

        db = 'test_db.sqlite'

        with sqlite3.connect(db) as conn:
            conn.execute('CREATE TABLE IF NOT EXISTS bookmarks (Name TEXT NOT NULL, Rating TEXT NOT NULL, Address TEXT NOT NULL, City TEXT NOT NULL, Telephone TEXT NOT NULL)')
            example_insert = conn.execute(f'INSERT INTO bookmarks VALUES (?, ?, ?, ?, ?)', ('Coffee', '4', 'Street', 'Houston', '600')) #TODO: figure out data types
        conn.close() # close at end of function

        test = bookmark_schema.insert_data('Coffee', '4', 'Street', 'Houston', '600')

        self.assertEqual(example_insert, test)

if __name__ == '__main__':
    unittest.main()
