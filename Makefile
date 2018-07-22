#!/usr/bin/env make

.PHONY: all upload download install test

PACKAGE=zero_out
VERSION=$(shell cat VERSION)

# Set FURY_USER and FURY_SECRET environment variables
FURY_UPLOAD=https://$(FURY_SECRET)@push.fury.io/$(FURY_USER)/
FURY_INDEX=https://pypi.fury.io/$(FURY_SECRET)/$(FURY_USER)/

all: install

upload:
	python setup.py sdist
	curl -F package=@dist/$(PACKAGE)-$(VERSION).tar.gz $(FURY_UPLOAD)

download:
	pip install $(PACKAGE)==$(VERSION) --extra-index-url $(FURY_INDEX) --no-cache-dir

install:
	pip install -e .

test:
	python -m unittest discover test/
