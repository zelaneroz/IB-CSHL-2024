import sqlite3
from secure_password import check_password

connection = sqlite3.connect("bitcoin_exchange.db")
cursor = connection.cursor()
query = "SELECT * FROM ledger"
result = cursor.execute(query).fetchall()
res2 = cursor.execute("SELECT MAX(id) FROM ledger").fetchone()[0]

connection.close()

for i in result:
    unhashed = f"id {i[0]},sender_id {i[1]},receiver_id {i[2]},amount {i[3]}"
    if check_password(user_password=unhashed, hashed_password=i[4])==True:
        print(f"Tx(id={i[0]})Signature matches")
    else:
        print(f"Tx(id={i[0]})Error signature")
