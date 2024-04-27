# <center> Приложение для анализа данных на Python </center>
## Разделы
1. [Описание проекта](#Описание-проекта)
2. [Особенности](#Особенности)
3. [Зависимости](#Зависимости)
4. [Установка проекта](#Установка-проекта)
5. [Использование проекта](#Использование-проекта)
6. [Авторы](#Авторы)
7. [Вывод](Использование-проекта)

## Описание проекта

> Этот проект разрабатывался с целью создать приложение по анализу данных на языке программирования Python для дипломной работы.

**О структуре проекта:**
* [extends](./extends) - папка с дополнительными функциями
* [tabs](./tabs) - папка с модулями, каждый из которых представляет собой отдельную вкладку в приложении
* [leftframe.py](./leftframe.py) - модуль левого блока в приложении
* [main_tabs.py](./main_tabs.py) - основной модуль вкладок приложения
* [options_window.py](./options_window.py) - модуль окна настроек
* [main.py](./main.py) - основной модуль проекта


## Особенности
- Возможность загрузки данных в формтах .csv и .xlsx.
- Реализация различных методов и функций для анализа данных, таких как вывод данных в таблицу, построение графиков, фильтрация и сортировка, проведение статистического анализа и нахождение выбросов в данных.
- Графический интерфейс пользователя для удобного взаимодействия с данными и результатами анализа.
- Поддержка сохранения результатов анализа, графики и данные.

## Используемые зависимости
* Python (3.10):
    * [customtkinter_(5.2.2)](https://customtkinter.tomschimansky.com/)
    * [ctkcomponents_(0.4)](https://github.com/rudymohammadbali/ctk_components/wiki)
    * [pandas_(2.2.2)](https://pandas.pydata.org/)
    * [pandastable_(0.13.1)](https://pandastable.readthedocs.io/en/latest/description.html)
    * [numpy_(1.26.4)](https://numpy.org/)
    * [matplotlib_(3.8.2)](https://matplotlib.org/)
    * [seaborn_(0.13.2)](https://seaborn.pydata.org/)

## Установка проекта

Клонируйте репозиторий:
```
git clone https://github.com/kirillgt33/DataAnalysisApp.git
```
Установите зависимости:
```
pip install -r requirements.txt
```

## Использование
Вся информация о работе с приложением находится в приложении на вкладке **Документация**.

## Авторы

* [Кирилл](https://t.me/KirillGT)

## Вывод

Получилось функциональное и удобное приложение. Оно позволяет просматривать данные, строить графики с различными настройками, фильтровать и сортировать данные, проводить расширенный анализ с использованием статистических методов, а так же производить сохранение графиков и данных.
