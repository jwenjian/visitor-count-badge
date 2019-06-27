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

    return Response(response=svg, content_type="image/svg+xml")
