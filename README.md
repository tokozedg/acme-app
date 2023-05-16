# acme-app

## Development Locally

```
# install all python requirements
pip install -r requirements.txt
# export following if plan on testing locally
export TESTING=True
export DEBUG=True
python runserver.py
```

This will use an in-memory database. To actually test with a PostGres database one just needs to setup the appropriate environment variables.

### Environment Variables
The following variables are used by the app and the defaults are in brackets:
* DATABASE_URL: the database url to connect to ("sqlite://")
* SECRET_KEY: the secret key for the app (random uuid1)
* TESTING: True if testing setup (default False)
* DEBUG: True if debugging is to be enabled (default False)
* LOGGING: the level of logging - debug, info, warning, error, critical (default info)

**Pytest**
For unit testing [Pytest](https://docs.pytest.org/en/latest/) is being used. [Coverage](https://coverage.readthedocs.io/en/coverage-5.3.1/) is used to generate code coverage report. To run the unit tests use `pytest --cov-report=html --cov=app app/testing` and it will produce a HTML code coverage report as well.