import datetime

from flask import Flask, Response, request
from pybadges import badge

app = Flask(__name__)

total_count_hub = {}


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

    repo_id = request.args.get('repo_id')
    if repo_id is None or repo_id == '':
        return invalid_count_resp()

    print("repo_id = ", repo_id)

    original_count = 0
    if repo_id in total_count_hub:
        original_count = total_count_hub[repo_id]

    original_count += 1

    total_count_hub[repo_id] = original_count

    svg = badge(left_text="Total Visitor", right_text=str(original_count))

    expiry_time = datetime.datetime.utcnow() - datetime.timedelta(minutes=10)

    headers = {'Cache-Control': 'no-cache,max-age=0', 'Expires': expiry_time.strftime("%a, %d %b %Y %H:%M:%S GMT")}

    return Response(response=svg, content_type="image/svg+xml", headers=headers)
