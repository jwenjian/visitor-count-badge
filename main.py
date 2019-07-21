import datetime

import psycopg2
from flask import Flask, Response, request
from pybadges import badge
from os import environ

app = Flask(__name__)


def invalid_count_resp() -> Response:
    """
    Return a svg badge with error info when cannot process repo_id param from request
    :return: A response with invalid request badge
    """
    svg = badge(left_text="Error", right_text='Cannot get repo_id param from request!',
                whole_link="https://github.com/jwenjian/visitor-count-badge")
    expiry_time = datetime.datetime.utcnow() - datetime.timedelta(minutes=10)

    headers = {'Cache-Control': 'no-cache,max-age=0', 'Expires': expiry_time.strftime("%a, %d %b %Y %H:%M:%S GMT")}

    return Response(response=svg, content_type="image/svg+xml", headers=headers)


@app.route("/total.svg")
def total_count_svg() -> Response:
    """
    Return a svg badge with latest visitor count of 'repo_id'

    :return: A svg badge with latest visitor count
    """

    repo_id = request.args.get('repo_id')
    if repo_id is None or repo_id == '':
        return invalid_count_resp()

    print("repo_id = ", repo_id)

    conn = psycopg2.connect(environ['DATABASE_URL'])
    cursor = conn.cursor()

    new_count = 1

    cursor.execute('SELECT id, count FROM TOTAL_COUNT_RECORD WHERE repo_id = %s', (repo_id,))
    doc = cursor.fetchone()

    try:
        if doc is not None:
            # 0: id, 1: count
            original_count = doc[1]
            new_count = original_count + 1
            cursor.execute('UPDATE TOTAL_COUNT_RECORD SET count = %s WHERE id = %s', (new_count, doc[0]))
            conn.commit()
        else:
            cursor.execute('INSERT INTO TOTAL_COUNT_RECORD(repo_id, count) VALUES(%s, %s)', (repo_id, new_count))
            conn.commit()
    except Exception as e:
        print('execute sql error', e)
    finally:
        cursor.close()
        conn.close()

    svg = badge(left_text="Total Visitor", right_text=str(new_count))

    expiry_time = datetime.datetime.utcnow() - datetime.timedelta(minutes=10)

    headers = {'Cache-Control': 'no-cache,max-age=0,no-store,s-maxage=0,proxy-revalidate',
               'Expires': expiry_time.strftime("%a, %d %b %Y %H:%M:%S GMT")}

    return Response(response=svg, content_type="image/svg+xml", headers=headers)


@app.route('/today.svg')
def current_day_visitor_count_svg() -> Response:
    """
    Return a svg badge with latest visitor count of 'repo_id' in current day only, this will NOT increase the total count of the 'repo_id'

    :return: A svg badge with latest visitor count in current day
    """

    repo_id = request.args.get('repo_id')
    if repo_id is None or repo_id == '':
        return invalid_count_resp()

    print("repo_id = ", repo_id)

    conn = psycopg2.connect(environ['DATABASE_URL'])
    cursor = conn.cursor()

    visit_date = datetime.datetime.now().strftime('%Y%m%d')
    print('visit date is ', visit_date)

    new_count = 1

    cursor.execute('SELECT id, count FROM CURRENT_DAY_COUNT_RECORD WHERE repo_id = %s and visit_date = %s',
                   (repo_id, visit_date))
    doc = cursor.fetchone()

    try:
        if doc is not None:
            # 0: id, 1: count
            original_count = doc[1]
            new_count = original_count + 1
            cursor.execute('UPDATE CURRENT_DAY_COUNT_RECORD SET count = %s WHERE id = %s', (new_count, doc[0]))
            conn.commit()
        else:
            cursor.execute('INSERT INTO CURRENT_DAY_COUNT_RECORD(repo_id, count, visit_date) VALUES(%s, %s, %s)',
                           (repo_id, new_count, visit_date))
            conn.commit()
    except Exception as e:
        print('execute sql error', e)
    finally:
        cursor.close()
        conn.close()

    svg = badge(left_text="Visitors in today", right_text=str(new_count))

    expiry_time = datetime.datetime.utcnow() - datetime.timedelta(minutes=10)

    headers = {'Cache-Control': 'no-cache,max-age=0,no-store,s-maxage=0,proxy-revalidate',
               'Expires': expiry_time.strftime("%a, %d %b %Y %H:%M:%S GMT")}

    return Response(response=svg, content_type="image/svg+xml", headers=headers)


if __name__ == '__main__':
    app.run()
