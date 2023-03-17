"""
engine =
"""

from sqlalchemy import create_engine


host = "127.0.0.1"
user = "root"
port = 3306
database = "starwarsDB"
password = "yogi1807"


def get_connection():
    return create_engine(
        url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database
        )
    )


if __name__ == "__main__":
    connection = get_connection()

    if connection:
        print("[ INFO ] connection has been created successfully")

    else:
        print("[ ERROR ] please check your DB username and password")
