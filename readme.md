## Задание

Напишите на C# или Python библиотеку для поставки внешним клиентам, которая умеет вычислять площадь круга по радиусу и треугольника по трем сторонам. Дополнительно к работоспособности оценим:

- Юнит-тесты
- Легкость добавления других фигур
- Вычисление площади фигуры без знания типа фигуры в compile-time
- Проверку на то, является ли треугольник прямоугольным

## Решение
Реализовано на `Python 3.9.5`.
## Примеры

### Использование функционала

Импорт
```python
from figures.triangle import Triangle
```
Создание треугольника
```python
triangle1 = Triangle(3, 4, 5)
triangle2 = Triangle(1, 2, 3) # raise CreateTriangleException
```
Вычисление площади
```python
triangle1 = Triangle(3, 4, 5)
print(triangle1.area()) # 77.76888838089432
```
Получение типа треугольника
```python
triangle1 = Triangle(3, 4, 5)
print(triangle1.get_type()) # TriangleTypes.RECTANGULAR
```

### Пример добавления своих фигур

Для добавления своей фигуры нужно унаследовать класс от `Figure`
```python
from figures.figure import Figure

class Square(Figure):
    
    def __init__(self, a: float):
        self.a = a
    
    def area(self) -> float:
        return self.a * self.a
```

## Установка библиотеки

```shell
$ pip install git+https://github.com/n-misharin/mindbox-figures#egg=mindbox-figures
```
