check:
	cat LOGO
	isort --recursive -c -df .
	isort -v
	yapf --recursive --diff .
	flake8 .
format:
	cat LOGO
	isort -rc .
	yapf --recursive -i .
dev:
	cat LOGO
	ENV=dev python manage.py migrate
	ENV=dev python manage.py runserver 0.0.0.0:8000
test:
	cat LOGO
	ENV=test python manage.py test
help:
	@echo "    check"
	@echo "        Check your code style using flake8 & isort"
	@echo "    format"
	@echo "        Format your code using yapf && isort"
	@echo "    dev"
	@echo "        Start dev server."
	@echo "    test"
	@echo "        Run unit test."