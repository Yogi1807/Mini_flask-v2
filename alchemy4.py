import sqlalchemy
from pymysql.err import Error
from sqlalchemy import create_engine
import sqlalchemy as db  # alias for sqlalchemy is `db`


user = "root"
password = "yogi1807"
host = "127.0.0.1"
port = 3306
database = "starwarsDB"


def get_connection():
    try:
        engine = create_engine(
            "mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
            "".format(
                user=user,
                password=password,
                host=host,
                port=int(port),
                database=database,
            )
        )

    except Error as ex:
        print(f"[ ERROR ] details {ex}")

    return engine


if __name__ == "__main__":
    engine = get_connection()
    meta_data_obj = db.MetaData()

    profile_ = db.Table(
        "newprofile",
        meta_data_obj,
        db.Column("name", db.String(250)),
        db.Column("email", db.String(250)),
        db.Column("contact", db.Integer),
    )
    meta_data_obj.create_all(bind=engine)

    stmt = profile_.insert().values(
        name="randomname1234", email="prashant@vctcpune.co.in"
    )
    bar = engine.connect()
    bar.execute(stmt)
    bar.commit()
