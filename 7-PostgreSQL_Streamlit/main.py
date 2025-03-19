import streamlit as st
import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="my_postgres_container",
    database="testdb",
    user="aaradhya",
    password="secret"
)
cursor = conn.cursor()

# Fetch data
cursor.execute("SELECT * FROM passengers;")
data = cursor.fetchall()

# Streamlit UI
st.title("🚆 Passenger Details")
st.table(data)

# Close connection
cursor.close()
conn.close()
