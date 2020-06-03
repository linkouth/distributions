# distributions
Преобразование ПСЧ к заданному распределению

## Требования к окружению
Python 3.6+

## Установка
> git clone https://github.com/linkouth/distributions.git <projectName>

## Использование
> python3 main.py -h

## Пример запуска
> python3 main.py -f "example inputs/gm_input.txt" -d gm -a 0 -b 1 -c 1.5 -m 100

## Описание файлов
- main.py – точка входа в программу, отвечает за обработку ввода и вызов генераторов.
- dists – папка с реализацией функций распределений
- example inputs – папка с примерами входных файлов

## TODO
- Добавить юнит-тесты и интеграционные тесты
