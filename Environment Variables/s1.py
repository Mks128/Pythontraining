import os
os.environ["DB_HOST"]="postgres://user:pass@localhost:5432/mydb"
print(os.getenv("DB_HOST"))

db_host = os.getenv("DB_HOST", "localhost")
print(db_host)
db_port = os.getenv("DB_PORT", "5432")
print(db_port)
