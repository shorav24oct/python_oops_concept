from loguru import logger
import psycopg2
import configparser

config = configparser.ConfigParser()
config.read(r'C:\Users\sharm\.vscode\python_programming\src\resources\config_file.ini')

connector = psycopg2.connect(
    host=config.get('postgre_database', 'host'),
    port=config.get('postgre_database', 'port'),
    database=config.get('postgre_database', 'database'),
    user=config.get('postgre_database', 'user'),
    password=config.get('postgre_database', 'password')
)

cursor = connector.cursor()

logger.info("Executing query...")
cursor.execute("SELECT winner FROM icc_world_cup")

results = cursor.fetchall()
logger.info("Query results: {}", results)

insert_query = "INSERT INTO Labour (first_name, last_name, wage, role, email) VALUES (%s, %s, %s, %s, %s)"
cursor.execute(insert_query, ("John", "Doe", 50000, "Engineer", "john.doe@example.com"))
connector.commit()
logger.info("Inserted new record into Labour table.")

cursor.close()
connector.close()