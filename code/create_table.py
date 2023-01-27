import psycopg2

#connect to postgresql
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=1234")
cur = conn.cursor()

#create table
cur.execute("""
                CREATE TABLE IF NOT EXISTS all_ticket(
                    no_ticket text PRIMARY KEY,
                    title text,
                    body text,
                    created_on date,
                    ticket_status text,
                    file_name text,
                    date_insert date
                )

"""
)
conn.commit()

print("Create Table Success")
