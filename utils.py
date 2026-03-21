from datetime import datetime
from todo import PRIORITIES

def validate_deadline(deadline_str):
    try:
        datetime.strptime(deadline_str, "%Y-%m-%d %H:%M")
        return True
    except:
        return False

def validate_priority(priority):
    return priority in PRIORITIES