from database import add_medication, get_medications

def add_new_medication(name,time):
    add_medication(name,time)

def list_medications():
    meds = get_medications()
    return meds
interaction_pairs = [
    ("Aspirin", "Ibuprofen"),
    ("Paracetamol", "Alcohol")
]

def check_interaction(med1, med2):
    if (med1, med2) in interaction_pairs or (med2, med1) in interaction_pairs:
        return "⚠ Possible interaction detected"
    return "No known interaction"
