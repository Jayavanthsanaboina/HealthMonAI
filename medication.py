from database import add_medication, get_medications

def add_new_medication(name,time):
    add_medication(name,time)

def list_medications():
    meds = get_medications()
    return meds
