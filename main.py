import re
from event import Event
import storage
from datetime import datetime


class EventManager:
    def __init__(self):
        # Load events at initialization
        self.events = storage.load_events()


    @staticmethod
    def validate_date(date):
        """Validates the date format."""
        return re.match(r'\d{4}-\d{2}-\d{2}', date)

    def create_event(self):
        """Creates a new event."""
        name = input("Enter event name: ")
        date = input("Enter event date (YYYY-MM-DD): ")

        if not self.validate_date(date):
            print("Invalid date format. Please use YYYY-MM-DD.")
            return
        
        category = input("Enter event category (e.g., Work, Personal, Vacation, etc.): ")
        
        event = Event(name, date, category=category)
        self.events.append(event)
        self.save()
        print(f"Event {event} created successfully!")


    def update_event(self):
        """Updates an existing event."""
        self.list_events(events)
        if not self.events: return
        
        try:
            event_index = int(input("Enter the index of the event to update: "))
            event = self.events[event_index]
            
            name = input("Enter new event name (press enter to skip): ")
            date = input("Enter new event date (YYYY-MM-DD, press enter to skip): ")
            
            if date and not self.validate_date(date):
                print("Invalid date format. Please use YYYY-MM-DD.")
                return
            
            if name:
                event.name = name
            if date:
                event.date = date

            self.save()
            print("Event updated successfully!")

        except IndexError:
            print("Invalid event index.")
        except ValueError:
            print("Please enter a valid number.")


    def delete_event(self):
        """Deletes an existing event."""
        self.list_events()
        if not self.events: return
        
        try:
            event_index = int(input("Enter the index of the event to delete: "))
            self.events.pop(event_index)
            self.save()
            print("Event deleted successfully!")

        except IndexError:
            print("Invalid event index.")


    def view_event_details(self):
        """Displays the details of an event."""
        self.list_events()
        if not self.events: return
        
        try:
            event_index = int(input("Enter the index of the event to view: "))
            event = self.events[event_index]

            print("\nEvent Details:")
            print(f"Name: {event.name}")
            print(f"Date: {event.date}")
            print("Attendees:", ", ".join(event.attendees) or "None")
            print("Expenses:", ", ".join(event.expenses) or "None")

        except IndexError:
            print("Invalid event index.")


    def search_events(self):
        """Searches for events by name or date."""
        search_term = input("Enter search term (name or date): ").lower()
        found_events = [event for event in self.events if search_term in event.name.lower() or search_term in event.date.lower()]
        self.list_events(found_events)


    def advanced_search(self):
        """Searches for events by name, date range, or category."""
        print("1. Search by name")
        print("2. Search by date range")
        print("3. Search by category")
        choice = int(input("Choose a search method: "))

        if choice == 1:
            self.search_events()
        elif choice == 2:
            start_date = input("Enter start date (yyyy-mm-dd): ")
            end_date = input("Enter end date (yyyy-mm-dd): ")

            for event in self.events:
                if start_date <= event.date <= end_date:
                    print(event)
        elif choice == 3:
            category = input("Enter category to search: ")
            for event in self.events:
                if event.category.lower() == category.lower():
                    print(event)
        else:
            print("Invalid choice!")


    def summary_view(self):
        upcoming_events = [event for event in self.events if event.date >= datetime.today().date()]
        total_expenses = sum(len(event.expenses) for event in upcoming_events)

        print(f"Total upcoming events: {len(upcoming_events)}")
        print(f"Total expenses for upcoming events: {total_expenses}")

        
    def add_attendee(self):
        self.list_events()
        if not self.events: return

        event_index = int(input("Enter the index of the event to add attendee: "))
        if event_index < 0 or event_index >= len(self.events):
            print("Invalid event index.")
            return
        
        attendee = input("Enter attendee name: ")
        self.events[event_index].add_attendee(attendee)
        self.save()

        
    def add_expense(self):
        self.list_events()
        if not self.events: return

        event_index = int(input("Enter the index of the event to add expense: "))
        if event_index < 0 or event_index >= len(self.events):
            print("Invalid event index.")
            return
        
        expense = input("Enter expense description: ")
        self.events[event_index].add_expense(expense)
        self.save()


    def update_expense(self):
        self.list_events()
        if not self.events: return
        
        event_index = int(input("Enter the index of the event to update an expense: "))
        if event_index < 0 or event_index >= len(self.events):
            print("Invalid event index.")
            return

        event = self.events[event_index]
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
        self.save()
        print("Expense updated successfully!")


    def delete_expense(self):
        self.list_events()
        if not self.events: return
        
        event_index = int(input("Enter the index of the event to delete an expense: "))
        if event_index < 0 or event_index >= len(self.events):
            print("Invalid event index.")
            return

        event = self.events[event_index]
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
        self.save()
        print("Expense deleted successfully!")

    def save(self):
        """Saves the events to a file."""
        storage.save_events(self.events)
        
    def list_events(self, events=None):
        """Lists all events."""
        events_to_list = events or self.events
        events_to_list.sort(key=lambda x: x.date)  # Sorting events based on date
        if not events_to_list:
            print("No events available.")
            return
        
        print("\nEvents:")
        for index, event in enumerate(events_to_list):
            print(f"{index}. {event}")


if __name__ == "__main__":
    manager = EventManager()

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
        choice = input("Enter your choice: ")
        
        try:

            if choice == '1':
                manager.create_event()
            elif choice == '2':
                manager.update_event()
            elif choice == '3':
                manager.delete_event()
            elif choice == '4':
                manager.view_event_details()
            elif choice == '5':
                manager.add_attendee()
            elif choice == '6':
                manager.add_expense()
            elif choice == '7':
                manager.update_expense()
            elif choice == '8':
                manager.delete_expense()
            elif choice == '9':
                manager.search_events()
            elif choice == '10':
                manager.list_events()
            elif choice == '11':
                manager.advanced_search()
            elif choice == '12':
                manager.summary_view()
            elif choice == '13':
                break
            else:
                print("Invalid choice, please enter a number between 1 and 13.")

        except ValueError:
            print("Invalid input, please enter a number.")
