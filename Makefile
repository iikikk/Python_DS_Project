.PHONY: install test format lint

install:
	pip install -r requirements.txt

test: test-notebook test-script test-lib
	pytest

test-notebook:
	pytest analysis.ipynb

test-script:
	pytest test_script.py

test-lib:
	pytest test_lib.py

format:
	black .

lint:
	ruff check .
