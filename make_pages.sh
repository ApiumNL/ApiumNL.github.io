#!/usr/bin/env bash

pipenv run python make_pages.py
cp node_modules/mini.css/dist/*.min.css dist/css/
