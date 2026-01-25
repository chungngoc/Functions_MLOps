install:
	pip install --upgrade pip && \
		pip install -r requirements.txt
test:
	python -m pytest -vv test_1.py
format:
	black *.py
lint:
	pylint --disable=R,C statement.py
all:
	install test format lint
