# flask app with template demo

:bread: :bread: :bread: :bread: :bread:

Here's an example of a flask app serving up some simple HTML templates.
In this example, we're running a quiz to identify some naughty blobs. People want to
get better at identifying the naughty blobs so they can help people, and that's very nice.

# before running: create a config file

In the repo root:

`touch config.py`

In the config file:

```
class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = b'your-secret-key'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
```

# to run:

```
pipenv install
pipenv shell
python app.py
```

Open link in browser (usually http://127.0.0.1:5000/)



