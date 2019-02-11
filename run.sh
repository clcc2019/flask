#!/bin/sh
uwsgi -s /tmp/webquery.sock --manage-script-name --mount /webquery=webapp:app
