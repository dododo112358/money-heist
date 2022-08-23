import pandas as pd
import numpy as np
from hashlib import sha1
from threading import Thread
from datetime import datetime
import os
from sqlalchemy import create_engine, types
import joblib
import schedule
import time


# con = create_engine("oracle+cx_Oracle://")
ALL_USERS = list(map(str, range(100)))
joblib.dump([], "lst.zlib")


def create_log(username="admin"):
    log = pd.DataFrame({"id": [sha1(os.urandom(32)).hexdigest()],
                        "insertion_time": datetime.now(),
                        "user": [username]})
    # log.to_sql("table_name", if_exists="append", dtype={
    #            c: types.VARCHAR(256) for c in log.columns if c.dtype == "object"})
    print(log)


# def erase_log(username):
#     con.exceute(f"DELETE FROM TABLE WHERE user = '{username}'")


def add_authorized_user():
    username = np.random.choice(ALL_USERS)
    authorized_users = joblib.load("lst.zlib")
    authorized_users.append(username)
    print(authorized_users)
    create_log(username)
    joblib.dump(authorized_users, "lst.zlib")
    time.sleep(10)
    authorized_users = joblib.load("lst.zlib")
    authorized_users.remove(username)
    joblib.dump(authorized_users, "lst.zlib")
    print(authorized_users)
    # erase_log(username)


def run_thread():
    t = Thread(target=add_authorized_user)
    t.start()


schedule.every(1).seconds.do(create_log)
schedule.every(3).to(6).seconds.do(run_thread)

while True:
    schedule.run_pending()
