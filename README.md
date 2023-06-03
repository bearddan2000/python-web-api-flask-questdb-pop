# python-web-api-flask-questdb-pop

## Description
Creates an api of `pop` table.
Has the ability to query by parameters.

Remotely tested with *testify*.

## Tech stack
- python
  - flask
  - testify
  - requests

## Docker stack
- python:latest
- questdb/questdb

## To run
`sudo ./install.sh -u`
- Get all pops: http://localhost/pop
  - Schema name and color
- Query with params: 
  - http://localhost/pop/name/<name>
  - http://localhost/pop/color/<color>

## To stop
`sudo ./install.sh -d`

## For help
`sudo ./install.sh -h`

## Credits
- [Questdb with python](https://tutswiki.com/setup-access-questdb-python-notebook/)