import json


class Event:
    def __init__(self, name, date, attendees=None, expenses=None):
        self.name = name
        self.date = date
        self.attendees = attendees if attendees else []
        self.expenses = expenses if expenses else []

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


def load_events():
    try:
        with open('events.json', 'r') as file:
            data = json.load(file)
            return [Event.from_dict(event) for event in data]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def save_events(events):
    with open('events.json', 'w') as file:
        json.dump([event.to_dict() for event in events], file)


def create_event(events):
    name = input("Enter event name: ")
    date = input("Enter event date: ")
    event = Event(name, date)
    events.append(event)
    print(f"Event {event} created successfully!")
    save_events(events)

    
def add_attendee(events):
    list_events(events)
    event_index = int(input("Enter the index of the event to add attendee: "))
    attendee = input("Enter attendee name: ")
    events[event_index].add_attendee(attendee)
    save_events(events)

    
def add_expense(events):
    list_events(events)
    event_index = int(input("Enter the index of the event to add expense: "))
    expense = input("Enter expense description: ")
    events[event_index].add_expense(expense)
    save_events(events)

    
def list_events(events):
    print("Events:")
    for index, event in enumerate(events):
        print(f"{index}. {event}")


if __name__ == "__main__":
    events = load_events()
    while True:
        print("1. Create Event")
        print("2. Add Attendee")
        print("3. Add Expense")
        print("4. List Events")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            create_event(events)
        elif choice == '2':
            add_attendee(events)
        elif choice == '3':
            add_expense(events)
        elif choice == '4':
            list_events(events)
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")
