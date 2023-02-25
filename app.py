from flask import Flask


def create_app() -> Flask:
    """
    Holds the specifications to create the Flask app.

    Returns:
        Flask: application object.
    """

    app = Flask(__name__)
    app.secret_key = "c@tgram"

    # Avoids circular import
    from routes import auth

    app.register_blueprint(auth)

    return app


if __name__ == "__main__":
    app = create_app()
    app.app_context().push()

    app.run(debug=True)
