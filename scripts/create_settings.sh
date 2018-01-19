#!/bin/bash

cat "[settings]" > settings.ini
cat "APP_UID=$APP_UID" >> settings.ini
cat "APP_SECRET=$APP_SECRET" >> settings.ini
cat "TOKEN_FILE=$TOKEN_FILE" >> settings.ini