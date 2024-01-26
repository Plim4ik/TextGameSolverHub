# Определение переменных
VENV_NAME := .venv
REQUIREMENTS := requirements.txt
PYTHON := python3

# При помощи этой цели создается виртуальное окружение
venv:
	$(PYTHON) -m venv $(VENV_NAME)

# Цель для активации виртуального окружения
activate:
	. $(VENV_NAME)/bin/activate

# Цель для установки зависимостей из requirements.txt
install:
	. $(VENV_NAME)/bin/activate && $(PYTHON) -m pip install -r $(REQUIREMENTS)


# Цель для очистки виртуального окружения
clean:
	rm -rf $(VENV_NAME)

tree:
	tree -I '.venv|__pycache__' -L 3


# По умолчанию выполняется цель help, чтобы вывести информацию о доступных целях
help:
	@echo "\033[1mДоступные команды:\033[0m"
	@echo "\033[1m  \033[33mmake venv\033[0m            - Создать виртуальное окружение"
	@echo "\033[1m  \033[33mmake activate\033[0m        - Активировать виртуальное окружение"
	@echo "\033[1m  \033[33mmake install\033[0m         - Установить зависимости из requirements.txt"
	@echo "\033[1m  \033[33mmake clean\033[0m           - Очистить виртуальное окружение"
	@echo "\033[1m  \033[33mmake tree\033[0m            - Построить дерево проекта (игнорируя системные файлы)"