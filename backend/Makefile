
all: check coverage

.PHONY: \
		all \
		check \
		clean \
		coverage \
		format \
		green \
		init \
		install \
		linter \
		red \
		refactor \
		setup \
		tests

module = finance_module

define lint
	pylint \
        --disable=bad-continuation \
        --disable=missing-class-docstring \
        --disable=missing-function-docstring \
        --disable=missing-module-docstring \
        ${1}
endef

check:
	black --check --line-length 100 ${module}
	black --check --line-length 100 tests
	flake8 --max-line-length 100 ${module}
	flake8 --max-line-length 100 tests
	mypy ${module}
	mypy tests

clean:
	rm --force --recursive .*_cache
	rm --force --recursive ${module}.egg-info
	rm --force --recursive ${module}/__pycache__
	rm --force --recursive tests/__pycache__


format:
	black --line-length 100 ${module}
	black --line-length 100 tests

init: setup tests

install:
	pip install --editable .

linter:
	$(call lint, ${module})
	$(call lint, tests)

setup: clean install

tests:
	pytest --verbose

red: format
	git restore $(module) \
	&& (pytest --verbose tests/*.py) \
	&& git restore tests/*.py \
	|| (git add tests/*.py && git commit -m "🛑🧪 Fail tests")
	chmod g+w -R .

green: format
	git restore tests/*.py \
	&& (pytest --verbose tests/*.py) \
	&& (git add $(module)/*.py && git commit -m "✅ Pass tests") \
	|| git restore $(module)/*.py
	chmod g+w -R .

refactor: format
	pytest --verbose tests/*.py \
	&& (git add $(module)/*.py tests/*.py && git commit -m "♻️  Refactor") \
	|| git restore $(module)/*.py tests/*.py
	chmod g+w -R .
