### Баг-репорт: Фильтрация "по дороже" не работает корректно

### Описание: При использовании фильтрации "по дороже" на странице результатов поиска Авито, записи не фильтруются корректно. Некоторые записи с более низкой ценой отображаются выше записей с более высокой ценой.

### Шаги для воспроизведения:

1. Зайти на страницу результатов поиска Авито
2. Выбрать фильтр "по дороже"
3. Проверить список записей

### Ожидаемый результат: Записи должны быть отсортированы по убыванию цены, т.е. самые дорогие записи должны быть в начале списка.

### Фактический результат: Некоторые записи с более низкой ценой отображаются выше записей с более высокой ценой.

### Приоритет: High

### Тип бага: Функциональный баг