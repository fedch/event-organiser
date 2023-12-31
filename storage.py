import json
from event import Event

def load_events():
    try:
        with open('events.json', 'r') as file:
            data = json.load(file)
            return [Event.from_dict(event_data) for event_data in data]    
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_events(events):
    with open('events.json', 'w') as file:
        json.dump([event.to_dict() for event in events], file)
