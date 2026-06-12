from backend.database import engine
from sqlalchemy import inspect

inspector = inspect(engine)

for table in inspector.get_table_names():
    print(table)