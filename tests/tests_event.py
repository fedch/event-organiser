import unittest
from event import Event

class TestEvent(unittest.TestCase):
    
    def test_event_creation(self):
        event = Event("Meeting", "2022-01-01", ["Alice", "Bob"], ["Lunch", "Stationery"], "Work")
        
        self.assertEqual(event.name, "Meeting")
        self.assertEqual(event.date, "2022-01-01")
        self.assertEqual(event.attendees, ["Alice", "Bob"])
        self.assertEqual(event.expenses, ["Lunch", "Stationery"])
        self.assertEqual(event.category, "Work")
        
    def test_event_default_values(self):
        event = Event("Party", "2022-01-10")
        
        self.assertEqual(event.attendees, [])
        self.assertEqual(event.expenses, [])
        self.assertEqual(event.category, "General")
        
    def test_event_to_dict(self):
        event = Event("Meeting", "2022-01-01")
        expected_dict = {
            "name": "Meeting",
            "date": "2022-01-01",
            "attendees": [],
            "expenses": [],
            "category": "General"
        }
        self.assertEqual(event.to_dict(), expected_dict)

    def test_event_from_dict(self):
        data = {
            "name": "Meeting",
            "date": "2022-01-01",
            "attendees": ["Alice"],
            "expenses": ["Coffee"],
            "category": "Work"
        }
        event = Event.from_dict(data)
        self.assertEqual(event.name, "Meeting")
        self.assertEqual(event.date, "2022-01-01")
        self.assertEqual(event.attendees, ["Alice"])
        self.assertEqual(event.expenses, ["Coffee"])
        self.assertEqual(event.category, "Work")

if __name__ == '__main__':
    unittest.main()
