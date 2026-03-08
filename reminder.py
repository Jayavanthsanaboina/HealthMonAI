import schedule
import time
from medication import get_medications


def send_reminder(medicine):

    print(f"Reminder: Time to take your medicine - {medicine}")


def schedule_reminders():

    meds = get_medications()

    for med in meds:

        name = med[1]
        med_time = med[2]

        schedule.every().day.at(med_time).do(send_reminder,name)


def start_reminder_service():

    schedule_reminders()

    while True:

        schedule.run_pending()
        time.sleep(1)