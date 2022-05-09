## Основы работы с изображениями
### Задание №1 в рамках спецсеминара «Математические методы обработки изображений»

Программа реализует следующий функционал:
* отражение изображения относительно горизонтальной, вертикальной и диагональных осей
* извлечение фрагмента изображения
* поворот изображений по и против часовой стрелки на произвольное число градусов, кратное 90
* автоматический поворот изображения, исходя из того, что на всех фотографиях верхняя часть изображения (небо, облака) светлее нижней. 

### Запуск из командной строки:
Программа поддерживает запуск из командной строки со строго определённым форматом команд:

``` bash
python main.py command parameters input_file output_file
```

Аргументы:
* command     — команда из списка ниже
* parameters  — параметры для `command`, прописанные в списке ниже
* input_file  — входное изображение (имя файла)
* output_file — выходное изображение (имя файла)

Список команд:
* `mirror` {h|v|d|cd}                         — отражение относительно горизонтальной оси (h), вертикальной оси (v), главной диагонали (d), побочной диагонали (cd)
* `extract` left_x top_y width height — извлечение фрагмента изображения с параметрами: отступ слева (left_x, целое), отступ сверху (top_y, целое), ширина фрагмента (width, положительное), высота фрагмента (height, положительное)
* `rotate` {cw|ccw} angle                 — поворот по (cw) или против (ccw) часовой стрелки на заданное количество градусов angle
* `autorotate`		                          — автоматический поворот на угол 0, 90, 180 или 270 градусов