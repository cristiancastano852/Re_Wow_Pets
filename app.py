import flaskapp
import config
import unittest


app = flaskapp.create_app(config)

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