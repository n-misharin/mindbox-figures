tests:
	python -m pytest

dist:
	python setup.py sdist bdist_wheel
