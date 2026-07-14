.PHONY: test check lab-start lab-status lab-stop

PYTHON ?= python3

test:
	$(PYTHON) tests/run_tests.py

check:
	$(PYTHON) tests/run_tests.py

lab-start:
	$(PYTHON) scripts/lab.py start

lab-status:
	$(PYTHON) scripts/lab.py status

lab-stop:
	$(PYTHON) scripts/lab.py stop
