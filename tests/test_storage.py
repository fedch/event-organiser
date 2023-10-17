import unittest
from unittest.mock import mock_open, patch
from event import Event
import storage

class TestStorage(unittest.TestCase):
    
    def setUp(self):
        self.mock_data = [
            {
                "name": "Meeting",
                "date": "2022-01-01",
                "attendees": [],
                "expenses": [],
                "category": "General"
            }
        ]


    def test_load_events_no_file(self):
        m = mock_open()
        m.side_effect = FileNotFoundError
        with patch('builtins.open', m):
            events = storage.load_events()
        self.assertEqual(events, [])


if __name__ == '__main__':
    unittest.main()
