install:
	poetry install

build:
	poetry build

project:
	poetry run project

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install dist/*.whl