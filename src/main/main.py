from database.postgre_connection import execute_query
from loguru import logger
import configparser

config = configparser.ConfigParser()
config.read(r'C:\Users\sharm\.vscode\python_programming\src\resources\config_file.ini')

def main():
    query = "SELECT winner FROM icc_world_cup"
    results = execute_query(config, query)
    logger.info("Query results: {}", results)

if __name__ == "__main__":
    main()