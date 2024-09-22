.PHONY: install test format lint

install:
	pip install -r requirements.txt

test: test-notebook test-script test-lib

test-notebook:
	python -m pytest analysis.ipynb

test-script:
	python -m pytest test_script.py

test-lib:
	python -m pytest test_lib.py

format:
	black .

lint:
	ruff check .