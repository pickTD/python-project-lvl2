install:
	poetry install
package-install:
	pip install --no-cache-dir --user dist/*.whl
build:
	poetry build
publish:
	poetry publish -r testpypi
lint:
	poetry run flake8 gendiff
diff:
	poetry run gendiff