from flask_sqlalchemy import SQLAlchemy
from flaskapp import create_app
from flaskapp.model.model_cloud import db
import config
import unittest


app = create_app(config)
app.config.from_pyfile('../config.py')
app.config['TEMPLATES_AUTO_RELOAD'] = True

db.init_app(app)


@app.cli.command()
def test(input=True):
    """ Runs the unit tests.

    Args:
        input (bool, optional): Whether to run the tests or not. Defaults to True.

    Returns:
        None
    """
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)
