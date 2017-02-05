* about this project

* install dependences

* setup DB

* statup project (developlent mode)

Dont forget you need to set the DATABASE_URL

 run application

 run tests


* referencias

How to setup this project 

Fisrt off all you nedd to create a virtualenv with as dependeces.

    * Python 3.6 or lastes

We recomendete do to use pyend to management many python versions and virutaevns

 ```
 pyenv install 3.6.0
 pyenv virtualenv 3.6.0 venv-tramsdaol-3.6.0
 pyenv activate venv-tramsdaol-3.6.0 
 ```

Install all dependences

pip install -r requiriments.txt

Database conection

You need to define a envarioment varible called DATABASE_URL, with as:

```
DATABASE_URL=postgres://tramsdaol:123456@localhost:5432/tramsdaol
```

Deploy like a boss

git remote set-url heroku-client https://git.heroku.com/quiet-badlands-78231.git
git remote set-url heroku-server https://git.heroku.com/guarded-coast-40901.git


Fetures futuras

IPv6


References:



I dont make this project alone,
I use some content to undestand some things and imprmenvetm my conde
I choice the best content that I used

https://docs.python.org/3/whatsnew/3.6.html
http://klen.github.io/py-frameworks-bench/
https://devcenter.heroku.com/articles/using-multiple-buildpacks-for-an-app
https://kendaleiv.com/angular-2-mockbackend-service-testing-template-using-testbed/
https://medium.com/google-developer-experts/angular-2-unit-testing-with-jasmine-defe20421584#.4k7g5aczp
http://www.codexworld.com/get-zipcode-from-address-using-google-maps-api-php/
http://gis.stackexchange.com/questions/33966/google-geocoder-lookup-get-postal-code-by-country-and-city
http://stackoverflow.com/questions/311627/how-to-print-date-in-a-regular-format-in-python
https://en.wikipedia.org/wiki/Helios

