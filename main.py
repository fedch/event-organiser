import re
from event import Event
import storage

def validate_date(date):
    return re.match(r'\d{4}-\d{2}-\d{2}', date)

def create_event(events):
    name = input("Enter event name: ")
    date = input("Enter event date (YYYY-MM-DD): ")

    if not validate_date(date):
        print("Invalid date format. Please use YYYY-MM-DD.")
        return
    
    event = Event(name, date)
    events.append(event)
    print(f"Event {event} created successfully!")
    storage.save_events(events)


def update_event(events):
    list_events(events)
    if not events: return
    
    event_index = int(input("Enter the index of the event to update: "))
    
    if event_index < 0 or event_index >= len(events):
        print("Invalid event index.")
        return
    
    name = input("Enter new event name (press enter to skip): ")
    date = input("Enter new event date (YYYY-MM-DD, press enter to skip): ")
    
    if date and not validate_date(date):
        print("Invalid date format. Please use YYYY-MM-DD.")
        return
    
    if name:
        events[event_index].name = name
    if date:
        events[event_index].date = date
    
    storage.save_events(events)
    print("Event updated successfully!")


def search_events(events):
    search_term = input("Enter search term (name or date): ").lower()
    found_events = [event for event in events if search_term in event.name.lower() or search_term in event.date.lower()]
    list_events(found_events)
    
def add_attendee(events):
    list_events(events)
    if not events: return

    event_index = int(input("Enter the index of the event to add attendee: "))
    if event_index < 0 or event_index >= len(events):
        print("Invalid event index.")
        return
    
    attendee = input("Enter attendee name: ")
    events[event_index].add_attendee(attendee)
    storage.save_events(events)

    
def add_expense(events):
    list_events(events)
    if not events: return

    event_index = int(input("Enter the index of the event to add expense: "))
    if event_index < 0 or event_index >= len(events):
        print("Invalid event index.")
        return
    
    expense = input("Enter expense description: ")
    events[event_index].add_expense(expense)
    storage.save_events(events)

    
def list_events(events):
    if not events:
        print("No events available.")
        return
    
    print("Events:")
    for index, event in enumerate(events):
        print(f"{index}. {event}")


if __name__ == "__main__":
    events = storage.load_events()
    while True:
        print("1. Create Event")
        print("2. Add Attendee")
        print("3. Add Expense")
        print("4. List Events")
        print("5. Exit")
        try:
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
                print("Invalid choice, please enter a number between 1 and 5.")

        except ValueError:
            print("Invalid input, please enter a number.")
