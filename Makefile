PYTHON=python2.7

ENV_DIR=.env_$(PYTHON)

ifeq ($(OS),Windows_NT)
	IN_ENV=. $(ENV_DIR)/Scripts/activate &&
else
	IN_ENV=. $(ENV_DIR)/bin/activate &&
endif

all: test flake8 lint docs sdist rpm

env: $(ENV_DIR)

test: build
	$(IN_ENV) nosetests -v --with-xunit --xunit-file=test_results.xml --with-coverage --cover-erase --cover-xml  --cover-package plotie

artifacts: build rpm sdist

$(ENV_DIR):
	virtualenv -p $(PYTHON) $(ENV_DIR)

build_reqs: env
	$(IN_ENV) pip install herodotus sphinx flake8 coverage nose

build: build_reqs
	$(IN_ENV) pip install -U --pre -e .

sdist: build
	$(IN_ENV) python setup.py sdist

rpm: build
	$(IN_ENV) rpmbuild --define '_topdir '`pwd` -bb SPECS/*.spec

lint: pep8

pep8: build_reqs
	- $(IN_ENV) pep8 src/plotie > pep8.out

flake8: build_reqs
	- $(IN_ENV) flake8 src/plotie > flake8.out

docs: build
	$(IN_ENV) pip install -r docs/requirements.txt
	$(IN_ENV) $(MAKE) -C docs html man

freeze: env
	- $(IN_ENV) pip freeze

clean:
	- @rm -rf BUILD
	- @rm -rf BUILDROOT
	- @rm -rf RPMS
	- @rm -rf SRPMS
	- @rm -rf SOURCES
	- @rm -rf docs/build
	- @rm -rf src/*.egg-info
	- @rm -rf build
	- @rm -rf dist
	- @rm -f .coverage
	- @rm -f test_results.xml
	- @rm -f coverage.xml
	- @rm -f pep8.out
	- @rm -f flake8.out
	- @find ./src ./docs -name '*.pyc' | xargs -r rm

env_clean: clean
	- @rm -rf $(ENV_DIR)
