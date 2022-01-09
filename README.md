### Голосовой помощник на для линукса на питоне

* Требует подключения к интернету для распознавания речи
* Подразумеватеся запуск под raspberry pi (в принципе под линуксом)
* Пока что прорабатывается простой но рабочий функционал, шлифовать код буду как функционала прибавится

_____

Коротко о структуре:

- Anekdoter
  - `auth_data.py` [Файл исключительно для хранения токена вк]
  - `main.py` [Может сохранять свежие анекдоты и читать их из базы]
  - `i_have_reached_comedy.db` [База]
- weather
  - `weather.py` [Скрит для получения, парсинга и вывода отформатированных данных о погоде]
- `recognizer.py` [Всё, что отвечает за распознование речи и передачи результата в *response.py*]
- `response.py` ["Мозг", принимающий решение, какой фукнкционал вызывать в зависимости от запроса пользователя]

_____

*Синтез голоса*: с синтезом голоса в линуксе всё довольно грустно, плюс к тому бот обладает некоторой своеобразной сущностью, поэтому хочется пойти не по лёгкому пути, а по странно-кастомному - озвучить его самостоятельно. 

_____

> Для корректной работы рассказывания ботом анекдотов в папке `/Anekdoter/auth_data.py` требуется заменить переменную `token` на ваш токен вк!

> Для работы с погодой в `weather/weather.py` в функции `get_weather` замените значение параметра `city` на ваш город 

Пока бот сыроват и в разработке, и имеющийся функционал скорее тестовый.
Справляется с простенькими задачами: здороваться, подсказывать время, пошутить, сказать температуру процессора, вывести погоду в заданном городе.

Но так как основа готова - доработка модулей намного проще.

Будем работать

_____

![Sound](https://cdn.dribbble.com/users/6190/screenshots/4263671/browserpreview_tmp-1.gif "Оно такое тыц-тыц")

_____
