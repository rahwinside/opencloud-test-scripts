import pymysql
from app import app, forbidden
from db_config import mysql
from flask import jsonify, request


@app.route('/linear-sql-smoke', methods=['GET'])
def linear_sql_smoke():
    pass_count = 0
    fail_count = 0
    total_count = 0

    while True:
        try:
            print("CONNECT...      ", end=" ")
            cnx = mysql.connect()
            print("OK      ", end=" ")

            cursor = cnx.cursor()
            sql = "SELECT * FROM linear_smoke"
            print("SELECT...      ", end=" ")
            cursor.execute(sql)
            cursor.close()
            print("OK      ", end=" ")

            cursor = cnx.cursor()
            sql = "INSERT INTO `opencloud`.`linear_smoke` (status) VALUES ('pass')"
            print("INSERT...      ", end=" ")
            cursor.execute(sql)
            cnx.commit()
            print("OK      ", end=" ")

            print("DISCONNECT...      ", end=" ")
            cnx.close()
            print("OK      ", end=" ")
            pass_count += 1
            print("iter# " + str(total_count + 1) + " PASS")

        except KeyboardInterrupt as e:
            print("Total Attempts: " + str(total_count))
            print("Passed: " + str(pass_count))
            print("Failed: " + str(fail_count))
            print("Hit Rate: " + str(pass_count / total_count * 100) + "%")
            print("Miss Rate: " + str(fail_count / total_count * 100) + "%")
            break
            exit(o)

        except Exception as e:
            print(e)
            fail_count += 1
            print("iter# " + str(total_count + 1) + " FAIL")

        finally:
            total_count += 1


linear_sql_smoke()
