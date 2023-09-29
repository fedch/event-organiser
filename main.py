from event import Event
import storage


def create_event(events):
    name = input("Enter event name: ")
    date = input("Enter event date: ")
    event = Event(name, date)
    events.append(event)
    print(f"Event {event} created successfully!")
    storage.save_events(events)

    
def add_attendee(events):
    list_events(events)
    event_index = int(input("Enter the index of the event to add attendee: "))
    attendee = input("Enter attendee name: ")
    events[event_index].add_attendee(attendee)
    storage.save_events(events)

    
def add_expense(events):
    list_events(events)
    event_index = int(input("Enter the index of the event to add expense: "))
    expense = input("Enter expense description: ")
    events[event_index].add_expense(expense)
    storage.save_events(events)

    
def list_events(events):
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
