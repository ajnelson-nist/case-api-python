#!/usr/bin/make -f

# This software was developed at the National Institute of Standards
# and Technology by employees of the Federal Government in the course
# of their official duties. Pursuant to title 17 Section 105 of the
# United States Code this software is not subject to copyright
# protection and is in the public domain. NIST assumes no
# responsibility whatsoever for its use by other parties, and makes
# no guarantees, expressed or implied, about its quality,
# reliability, or any other characteristic.
#
# We would appreciate acknowledgement if the software is used.

SHELL = /bin/bash

PYTHON ?= python3.5

all: \
  check

check: \
  verify_output.log
	@echo "Unit tests pass!"

clean:
	@rm -f from_readme.json verify_from_readme.log

output.json: \
  example.py
	$(PYTHON) example.py || rm -f output.json

verify_output.log: \
  output.json \
  verify_output.py
	$(PYTHON) verify_output.py --debug output.json
	touch $@
