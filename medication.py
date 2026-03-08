from database import connect

def add_medication(name,time):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO medication(name,time) VALUES (?,?)",
        (name,time)
    )

    conn.commit()
    conn.close()


def get_medications():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM medication")

    data = cursor.fetchall()

    conn.close()

    return data