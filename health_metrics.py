from database import connect
from datetime import date

def add_metrics(steps,heart_rate):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO health_metrics(steps,heart_rate,date) VALUES (?,?,?)",
        (steps,heart_rate,str(date.today()))
    )

    conn.commit()
    conn.close()


def get_metrics():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM health_metrics")

    data = cursor.fetchall()

    conn.close()

    return data