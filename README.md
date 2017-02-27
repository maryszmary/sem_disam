# Word Sense Disambiguation for RNC

Этот проект – попытка сделать семантическую дизамбигуацию для НКРЯ с помощью метода контекстного пересечения.
"Sence contexts" взяты из МАС (из определений и примеров к значениям словаря).
Метод контекстного пересечения слегка улучшен в том, что алгоритм не просто смотрит на размер пересечения "смыслового мешка" и "контекстного мешка", но учитывает количество встреченных слов. Так, если в определении слова "мягкий" в 1-ом значении слово "тёплый" встретилось 2 раза, а слово "уютный" 1 раз, то его вхождение в контестный мешок при принятии решения будет весить больше.

## Описание скриптов:

* **MAS_parser.py** обрабатывает МАС в формате .dsl и достаёт из него все омонимичные прилагательные, для которых контексты разделены на первое и не-первое.
Я использую его следующи образом:

*$ python3 MAS_parser.py > hom.adj.csv*

* **create_sense_bags.py** отсеивает шум, выкидывает стоп-слова и создаёт файл с "мешками смыслов" (**sense_bags.json**)

* **cont_intersection.py** является реализацией алгоритма. Для использования скрипта для дизамбигуации нужно указать в путь к файлу с контестами омонимичного прилагательного и прилагательное (переменные (FNAME и ADJ). Скрипт умеет работать с контекстами только одного прилагательного. Использование: 

*$ python3 cont_intersection.py*

Скрипт использует mystem и nltk.

* **accuracy_estimation.py** обрабатывает файл csv с примерами, размеченными алгоритмом, и золотым стандартом, и выдаёт оценку точности, полноты и f-score.

## Оценка работы алгоритма

Работа программы оценивается на данных НКРЯ для прилагательного мягкий. Для оценки было размеченно 100 примеров из корпуса.

||Presicion|Recall|f-score|
|------|:--:|:--:|:--:|
|мягкий|0.79|0.72|0.69|
|------|:--:|:--:|:--:|
|мягкий|0.88|0.81|0.83|

## Главные недостатки (что нужно исправить в первую очередь)

В данный момент **MAS_parser.py** делит смысловые контесты на две группы: "контекст первого значения" и "контекст всех отальных значений". Это является одной из весомых причин низкой точности: из-за того, что в группу всех остальных значений попадают определения и примеры сразу нескольких значний, контексты для них больше, и поэтому перевешивают в большинстве случаев, что сильно искажает результаты.

Как вариант продолжения, имеет смысл подумать, как можно расширить мешок смыслов (найти ещё один источник). 

