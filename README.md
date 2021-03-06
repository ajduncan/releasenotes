# release notes #

An example django rest framework api which is used to get/update hardware
information.

Users should be able to use the admin (authenticated) to associcate an HTML response with the app_version, app_platform and language.

Unauthenticated remote clients should be able to post their and receive the HTML response encapsulated in JSON.


## Running #

  $ vagrant up

  Once running, to see a list of release notes:

  $ curl -H 'Accept: application/json; indent=4' -u admin:password123 http://127.0.0.1:8000/release-note/

  Or visit:

  http://localhost:8000/release-note/

  With admin / password123 for the username and password.

## About ##

release notes provides an API endpoint for remote hooks to report hardware
information.  This is an example application.

## API Endpoints ##

  * POST /release-note
  json: {'...', ...}

  Required fields:
  * mac_address: ...

  Optional fields:
  * hardware: ...

## License ##

MIT
