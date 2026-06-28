from loguru import logger
import psycopg2

def execute_query(config, query):
    try:
        connector = psycopg2.connect(
            host=config.get('postgre_database', 'host'),
            port=config.get('postgre_database', 'port'),
            database=config.get('postgre_database', 'database'),
            user=config.get('postgre_database', 'user'),
            password=config.get('postgre_database', 'password')
        )

        cursor = connector.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        return results

    except Exception as e:
        logger.info("Error occurred while executing query: {}", e)
        raise e

    finally:
        cursor.close()
        connector.close()

