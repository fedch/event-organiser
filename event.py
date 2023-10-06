class Event:
    def __init__(self, name, date, attendees=None, expenses=None, category=None):
        self.name = name
        self.date = date
        self.attendees = attendees if attendees else []
        self.expenses = expenses if expenses else []
        self.category = category or "General"

    def add_attendee(self, attendee):
        self.attendees.append(attendee)

    def add_expense(self, expense):
        self.expenses.append(expense)

    def to_dict(self):
        return {
            "name": self.name,
            "date": self.date,
            "attendees": self.attendees,
            "expenses": self.expenses,
        }

    @staticmethod
    def from_dict(data):
        return Event(data['name'], data['date'], data.get('attendees', []), data.get('expenses', []))

    def __str__(self):
        return f"{self.name} - {self.date}"
