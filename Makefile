install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt
	python -m textblob.download_corpora

test:
	python -m pytest -vv *.py
	

format:
	black *.py

lint:
	pylint --disable=R,C *.py my_lib/*.py 

all: install lint test