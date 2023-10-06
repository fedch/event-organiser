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
    
    category = input("Enter event category (e.g., Work, Personal, Vacation, etc.): ")
    
    event = Event(name, date, category=category)
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


def delete_event(events):
    list_events(events)
    if not events: return
    
    event_index = int(input("Enter the index of the event to delete: "))
    
    if event_index < 0 or event_index >= len(events):
        print("Invalid event index.")
        return
    
    events.pop(event_index)
    storage.save_events(events)
    print("Event deleted successfully!")


def view_event_details(events):
    list_events(events)
    if not events: return
    
    event_index = int(input("Enter the index of the event to view: "))
    
    if event_index < 0 or event_index >= len(events):
        print("Invalid event index.")
        return
    
    event = events[event_index]
    print("\nEvent Details:")
    print(f"Name: {event.name}")
    print(f"Date: {event.date}")
    print("Attendees:", ", ".join(event.attendees) or "None")
    print("Expenses:", ", ".join(event.expenses) or "None")


def search_events(events):
    search_term = input("Enter search term (name or date): ").lower()
    found_events = [event for event in events if search_term in event.name.lower() or search_term in event.date.lower()]
    list_events(found_events)


def advanced_search(events):
    print("1. Search by name")
    print("2. Search by date range")
    print("3. Search by category")
    choice = int(input("Choose a search method: "))

    if choice == 1:
        search_events(events)
    elif choice == 2:
        start_date = input("Enter start date (yyyy-mm-dd): ")
        end_date = input("Enter end date (yyyy-mm-dd): ")

        for event in events:
            if start_date <= event.date <= end_date:
                print(event)
    elif choice == 3:
        category = input("Enter category to search: ")
        for event in events:
            if event.category.lower() == category.lower():
                print(event)
    else:
        print("Invalid choice!")


def summary_view(events):
    upcoming_events = [event for event in events if event.date >= datetime.today().date()]
    total_expenses = sum(len(event.expenses) for event in upcoming_events)

    print(f"Total upcoming events: {len(upcoming_events)}")
    print(f"Total expenses for upcoming events: {total_expenses}")

    
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


def update_expense(events):
    list_events(events)
    if not events: return
    
    event_index = int(input("Enter the index of the event to update an expense: "))
    if event_index < 0 or event_index >= len(events):
        print("Invalid event index.")
        return

    event = events[event_index]
    if not event.expenses:
        print("There are no expenses for this event.")
        return

    for idx, expense in enumerate(event.expenses):
        print(f"{idx}. {expense}")

    expense_index = int(input("Enter the index of the expense to update: "))
    if expense_index < 0 or expense_index >= len(event.expenses):
        print("Invalid expense index.")
        return

    new_expense = input("Enter the new description for the expense: ")
    event.expenses[expense_index] = new_expense
    storage.save_events(events)
    print("Expense updated successfully!")


def delete_expense(events):
    list_events(events)
    if not events: return
    
    event_index = int(input("Enter the index of the event to delete an expense: "))
    if event_index < 0 or event_index >= len(events):
        print("Invalid event index.")
        return

    event = events[event_index]
    if not event.expenses:
        print("There are no expenses for this event.")
        return

    for idx, expense in enumerate(event.expenses):
        print(f"{idx}. {expense}")

    expense_index = int(input("Enter the index of the expense to delete: "))
    if expense_index < 0 or expense_index >= len(event.expenses):
        print("Invalid expense index.")
        return

    event.expenses.pop(expense_index)
    storage.save_events(events)
    print("Expense deleted successfully!")
    
def list_events(events):
    events.sort(key=lambda x: x.date)  # Sorting events based on date
    if not events:
        print("No events available.")
        return
    
    print("Events:")
    for index, event in enumerate(events):
        print(f"{index}. {event}")


if __name__ == "__main__":
    events = storage.load_events()
    try:
        while True:
            print("\nEvent Organizer")
            print("1. Create Event")
            print("2. Update Event")
            print("3. Delete Event")
            print("4. View Event Details")
            print("5. Add Attendee")
            print("6. Add Expense")
            print("7. Update Expense")
            print("8. Delete Expense")
            print("9. Search Events")
            print("10. List Events")
            print("11. Advanced Search")
            print("12. Summary View")
            print("13. Exit")
            try:
                choice = input("Enter your choice: ")

                if choice == '1':
                    create_event(events)
                elif choice == '2':
                    update_event(events)
                elif choice == 3:
                        delete_event(events)
                elif choice == 4:
                    view_event_details(events)
                elif choice == 5:
                    add_attendee(events)
                elif choice == 6:
                    add_expense(events)
                elif choice == 7:
                    update_expense(events)
                elif choice == 8:
                    delete_expense(events)
                elif choice == 9:
                    search_events(events)
                elif choice == 10:
                    list_events(events)
                elif choice == 11:
                    advanced_search(events)
                elif choice == 12:
                    summary_view(events)
                elif choice == 13:
                    break
                else:
                    print("Invalid choice, please enter a number between 1 and 11.")

            except ValueError:
                print("Invalid input, please enter a number.")

    except Exception as e:
        print(f"An error occurred: {e}")
