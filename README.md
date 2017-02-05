
#### About this project

This project is a single page application that allows users to see the current temperature at a certain address.

[![Deploy](http://www.herokucdn.com/deploy/button.png)](https://quiet-badlands-78231.herokuapp.com/)

#### How to setup environment (development mode)

This application architecture is separated in two parts: frontend and backend.

##### Backend (server folder)

Create a virtualenv - virtualenv is a tool to create isolated Python environments - We recommend using [pyenv](https://github.com/yyuu/pyenv) to management python versions and virtualenvs.

Create a virtualenv using Python 3.6.

```
pyenv install 3.6.0
pyenv virtualenv 3.6.0 venv-tramsdaol-3.6.0
pyenv activate venv-tramsdaol-3.6.0 
```

After the virtualend was created install all dependencies `cd server && pip install -r requiriments.txt`

Ready, run the project `python manage.py runserver`.

##### Frontend (client fodler)

You need to install [nodejs](https://nodejs.org/en/download/) and [Typescript](https://www.typescriptlang.org/#download-links).

We chose Angular 2 to write this application, so you need to install [Angular CLI](https://cli.angular.io/) to management angular apps.

Just it, now run the command `ng serve`.

#### Database Configuration 

First steps after PostgresSQL installation you need to create a user, type the following command `createuser -P -s <user>`, in sequence create a database `createdb <db>`.

Do not forget to set the environment variable `DATABASE_URL`.

```
export DATABASE_URL=postgres://tramsdaol:123456@localhost:5432/tramsdaol
```

Running Postgres in Mac `postgres -D /usr/local/var/postgres`.

#### Running tests

This application was developed with the best practices of software development.  So don't forget, Write tests for everything 🕵 .

Run backend tests: `python manage.py test`.
Run frontend tests: `ng test`.

**NO TEST NO BEER**

#### Deploy like a boss

This application is separated into two parts: `client` and `server` .  So you need to set up two repository in Heroku.

```
git remote add heroku-client https://git.heroku.com/quiet-badlands-78231.git
git remote add heroku-server https://git.heroku.com/guarded-coast-40901.git
```

You need to build the frontend files. Run the following command:
```
cd client/
ng build --prod
```

After build the folder `dist` was created. This folder contais the minified/concatenated files.

Affter each push you need to rename the correct `Procfile`, see `Procfile.server` and `Procfile.client`.

```
git push heroku-client master
git push heroku-server master
```

Server running in: https://guarded-coast-40901.herokuapp.com/
Client running in: https://quiet-badlands-78231.herokuapp.com/ 

Django Admin `user/password` : `loadsmart/1234qwer`.

#### Future improvements

* Support to tracking by IPv6
* Use Meinheld (http://meinheld.org/) - `--worker-class=meinheld.gmeinheld.MeinheldWorker`
* Improvement error response API
* API returns some unfriendly error messages
* Add unit test for ExportTracking service (other services have tests)

#### References:

I've read a few articles to develop this project and improve my code.

* https://docs.python.org/3/whatsnew/3.6.html
* http://klen.github.io/py-frameworks-bench/
* https://devcenter.heroku.com/articles/using-multiple-buildpacks-for-an-app
* https://kendaleiv.com/angular-2-mockbackend-service-testing-template-using-testbed/
* https://medium.com/google-developer-experts/angular-2-unit-testing-with-jasmine-defe20421584#.4k7g5aczp
* http://www.codexworld.com/get-zipcode-from-address-using-google-maps-api-php/
* http://gis.stackexchange.com/questions/33966/google-geocoder-lookup-get-postal-code-by-* country-and-city
* http://stackoverflow.com/questions/311627/how-to-print-date-in-a-regular-format-in-python
* https://en.wikipedia.org/wiki/Helios

