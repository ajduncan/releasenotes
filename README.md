# release notes #

An example django rest framework api which is used to get/update hardware
information.

## Running #

  $ vagrant up

  Once running, to see a list of release notes:

  $ curl -H 'Accept: application/json; indent=4' -u admin:password123 http://127.0.0.1:8000/releasenotes/

## About ##

release notes provides an API endpoint for remote hooks to report hardware
information.  This is an example application.

## API Endpoints ##

  * POST /releasenotes
  json: {'...', ...}

  Required fields:
  * mac_address: ...

  Optional fields:
  * hardware: ...

## License ##

MIT
