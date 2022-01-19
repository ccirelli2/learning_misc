from sqlalchemy.engine import URL
from sqlalchemy import create_engine

connection_string="DRIVER={ODBC Driver 17 for SQL Server};SERVER=yde2xj08jm.database.windows.net;DATABASE=SwyfftAnalyticsSARDev;UID=UnderwritingReadOnly;PWD=Oper92iU84%k*le"

connection_url=URL.create("mssql+pyodbc", query={"odbc_connect":connection_string})

engine=create_engine(connection_url)

print(engine)
print(help(engine))
