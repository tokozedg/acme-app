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

### Database
**Assumed Dependencies**:
* psql

**TLDR**
```
createdb hello-world
export DATABASE_URL=postgresql://postgres:postgres@localhost/hello-world
python initDB.py
# now start/restart the server and it should use Postgres database
```
To use a Postgres database first install [Postgres](https://www.postgresql.org/download/) and would recommend [PgAdmin](https://www.pgadmin.org/download/). Create a database with some name `createdb hello-world`. Export your database URL using something like `export DATABASE_URL=postgresql://postgres:postgres@localhost/hello-world`. If you used a different user and password protected then using the following form `postgresql://<user>:<password>@localhost/<database-name>`. Now just need to initiate the database using `python initDB.py` and the table entity should be created. Should be able to verify using PgAdmin or from command line: `psql hello-world` and `select * from entity;`.

### Testing
```
# unit-tests
pytest --cov-report=html --cov=app app/testing
#user interface end-to-end tests
cd ui-testing
npm install
npm run cypress:test
# manually run cypress file
npm run cypress:open
```
**Pytest**
For unit testing [Pytest](https://docs.pytest.org/en/latest/) is being used. [Coverage](https://coverage.readthedocs.io/en/coverage-5.3.1/) is used to generate code coverage report. To run the unit tests use `pytest --cov-report=html --cov=app app/testing` and it will produce a HTML code coverage report as well.

**User Interface Testing**
There is a `README` in ui-testing folder that dives into all the details.

# Github CI
A Github action is run on pull requests to the main branch. This action could be used as CI to ensure testing is ran and code consistency using linting. The following is performed on
1.  [flake8](https://flake8.pycqa.org/en/latest/) is used to lint the files to ensure code consistency
2. Unit tests are ran - all tests must pass and code coverage criteria level met
3. code coverage report uploaded to codecov
4. Starts the flask server and cypress tests against it
5. Upload cypress testing video as an artifact
6. Upload code coverage report from Cypress E2E testing
