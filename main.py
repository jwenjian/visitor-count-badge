import datetime

from flask import Flask, Response, request
from pybadges import badge
from tinydb import TinyDB, Query

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
    global total_count_hub
    db = TinyDB('db.json')
    total_count_table = db.table('total_count')
    record = Query()

    repo_id = request.args.get('repo_id')
    if repo_id is None or repo_id == '':
        return invalid_count_resp()

    print("repo_id = ", repo_id)

    original_count = 0
    doc = None
    docs = total_count_table.search(record.repo_id == repo_id)
    if docs is not None and len(docs) > 0:
        doc = docs[0]
        original_count = doc['count'] if doc['count'] is not None else 0
    else:
        doc = {'repo_id': repo_id, 'count': 0}

    original_count += 1

    doc['count'] = original_count

    total_count_table.upsert(doc, record.repo_id == repo_id)

    svg = badge(left_text="Total Visitor", right_text=str(original_count))

    expiry_time = datetime.datetime.utcnow() - datetime.timedelta(minutes=10)

    headers = {'Cache-Control': 'no-cache,max-age=0,no-store,s-maxage=0,proxy-revalidate',
               'Expires': expiry_time.strftime("%a, %d %b %Y %H:%M:%S GMT")}

    return Response(response=svg, content_type="image/svg+xml", headers=headers)


if __name__ == '__main__':
    app.run()
