.PHONY: clean check

SHELL := bash

all: clean
	find . -name profile.yml | while read f; do d="$$(dirname $$f)"; tar -C "$$d" -czf "profiles/$$(basename $$d).tar.gz" .; done

clean:
	rm -f profiles/*.tar.gz
	find . -name clean.sh -exec bash {} \;

check:
	find . -name profile.yml | bin/check_profiles.py
