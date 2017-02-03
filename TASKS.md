[X] Create a virtualenv to development this project
    We recomendate to use lates version pyenv and pip
    Use Python 3.6.0

[X] How define python version in requirements
    It is not possible

[x] Create a comectiom with PostgreSQL
 	postgres -D /usr/local/var/postgres
	Create a user to access with psql - createuser --pwprompt postgres
	createuser -P -s <user>
	createdb <db>
    export DATABASE_URL=postgres://tramsdaol:123456@localhost:5432/tramsdaol

[] BUG in find 
    For example, when find to Barra Bonita - State of Santa Catarina, Brazil return Guaraciaba

[] API
    Validations
    Error check

https://github.com/t4joel/get-address-by-google-maps-api/blob/master/scripts/geoLocationFactory.js

[] unittests

Requirements

● Assume the temperature doesn’t vary within the same Zipcode

● Assume the temperature for a Zipcode doesn’t vary within 1­hour windows

● Must track service usage by IP (how many times did this IP use the service). Think of it

as a company monitoring users usage. Design the database appropriately.

● Create a tool that exports usage by IP (csv, json, you pick the format). This export may

be fast even in scale (e.g. 10,000 unique IP addresses and 10,000 uses per IP).

Heat map ()

Usar CDN para escalar