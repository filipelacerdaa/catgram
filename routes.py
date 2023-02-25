from flask import Blueprint, render_template


auth = Blueprint("auth", __name__)


#===============================================#
#                                               #
#                   Index page                  #
#                                               #
#===============================================#

@auth.route("/", methods=["POST", "GET"])
def index() -> str:
    with open("content.txt", "r") as file:
        lines = file.readlines()

        for i in range(len(lines)):
            lines[i] = lines[i].replace(
                "\n", "/?utm_source=ig_embed&amp;utm_campaign=loading"
            )

    return render_template("index.html", lines=lines)
