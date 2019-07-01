import datetime

from flask import Flask, Response
from pybadges import badge

app = Flask(__name__)

total_visitor_count = 0


@app.route("/")
def hello():
    global total_visitor_count

    total_visitor_count += 1

    svg = badge(left_text="Total Visitor", right_text=str(total_visitor_count),
                whole_link="https://github.com/jwenjian/ghiblog")

    expiry_time = datetime.datetime.utcnow() - datetime.timedelta(minutes=10)

    headers = {'Cache-Control': 'no-cache,max-age=0', 'Expires': expiry_time.strftime("%a, %d %b %Y %H:%M:%S GMT")}

    return Response(response=svg, content_type="image/svg+xml", headers=headers)
