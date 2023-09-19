tests:
	python -m pytest

lib:
	python setup.py sdist bdist_wheel
