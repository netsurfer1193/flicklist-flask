from flask import Flask
import random

app = Flask(__name__)

page_header = """
<!DOCTYPE html>
<html>
    <head>
        <h1>FlickList</h1>
    </head>
    <body>
        <h1>FlickList</h1>
"""

page_footer = """
    </body>
</html>
"""


@app.route("/")
def index():
    # choose a movie by invoking our new function
    todays_movie = getRandomMovie()
    tomorrows_movie = getRandomMovie()

    # build the response string
    content = page_header
    content += "<h1>Movie of the Day</h1>"
    content += "<ul>"
    content += "<li>" + todays_movie + "</li>"
    content += "</ul>"

    content += "<h1>Tomorrow's Movie of the Day</h1>"
    content += "<ul>"
    content += "<li>" + tomorrows_movie + "</li>"
    content += "</ul>"
    content += page_footer

    return content

def getRandomMovie():
    return random.choice(["The Big Lebowski", "The Royal Tenenbaums", "Princess Mononoke", "The Princess Bride", "Star Trek IV: The Voyage Home"])


app.run()