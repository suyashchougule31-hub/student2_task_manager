import mysql.connector

def get_database_connection():
    connection = mysql.connector.connect(
        host = 'gateway01.ap-southeast-1.prod.aws.tidbcloud.com',
        user = '3a52Z1LwuFrPCnW.root',
        password = 'IyfL7E6mkfqQnFRr',
        database = 'student2_task_manager',
        port = 4000
    )
    return connection