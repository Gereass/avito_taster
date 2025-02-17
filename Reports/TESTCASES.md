### Тест-кейсы: Функциональность доски объявлений
#### Назначение:Проверка функциональности доски объявлений, включая создание, редактирование и поиск объявлений.
#### Тест-кейсы:
1. **Создание новой записи**:
    #### ID: TC-001
    #### Название: Создание нового объявления
    #### Предусловие: Пользователь имеет доступ к доске объявлений и может создавать новые объявления.
    #### Шаги: 
    1. Открыть доску объявлений.
    2. Нажать кнопку "Создать".
    3. Ввести данные для новой записи.
    4. Нажать кнопку "Сохранить".
    6. Нажать кнопку "Сохранить" без заполненых полей.
    7. Повторить пункты 1-4 с суммой 0.
    8. Повторить пункты 1-4 с суммой -0.
    9. Повторить пункты 1-4 с суммой 99999999999999999999999999999999999999999999999999999999.
    10. Добавить два объявления с большим названием (например, более 50 символов) на доску объявлений.
    12. Добавить два объявления с очень коротким названием (например, с 1 символом) на доску объявлений.
    13. Повторить пункты 1-4, в поле "Ссылка на изображение" вставить случайные символы. 
    #### Ожидаемый результат:
    * При вводе нормальных данных:
        + Система должна отобразить успешность записи сохранять новую запись.
    * При пустых полях:
        + Система должна отображать ошибку.
    * При вводе 0 суммы (0):
        + Система должна сохранить не новую запись с 0 суммой.
        + Система должна отображать ошибку.
    * При вводе отрицательной 0 суммы (-0):
        + Система должна отобразить ошибку и не сохранять новую запись.
        + Ошибка должна содержать сообщение о том, что сумма не может быть отрицательной.
    * При вводе 99999999999999999999999999999999999999999999999999999999 суммы (99999999999999999999999999999999999999999999999999999999):
        + Система должна отобразить ошибку и не сохранять новую запись.
        + Ошибка должна содержать сообщение о том, что сумма выходит за рамки граничных значений.
    * При добавлении двух объявлений с большим названием:
        + Фрейм второго объявления не должен отображаться частично поверх первого объявления.
        + Оба объявления должны быть полностью видимы и не должны перекрывать друг друга.
    * При добавлении двух объявлений с очень коротким названием:
        + Отображение объявлений не должно быть слишком маленьким.
        + Объявления должны быть легко читаемы и не должны быть слишком плотно расположены.
    * Поле с изображением:
        + Должна быть проверка на корректность урла изображения
    #### Проверка:
    * Проверить, что созданная запись отображается на доске объявлений.
    * Проверить, что новая запись не была создана в базе данных при вводе отрицательной суммы (-100).
    * Проверить, что новая запись была создана в базе данных при вводе 0 суммы (0).
    * Проверить, что новая запись не была создана в базе данных при вводе отрицательной 0 суммы (-0).
    * Проверить, что система отобразила ошибку и сообщение о том, что сумма не может быть отрицательной при вводе отрицательной суммы (-100) и отрицательной 0 суммы (-0).
    * Проверить, что при вводе суммы 99999999999999999999999999999999999999999 система отображает ошибку и не сохраняет новую запись, поскольку такая сумма превышает максимально допустимое значение и не может существовать в реальности.
    * Проверить, что фреймы объявлений не перекрывают друг друга.
    * Проверить, что объявления с большим названием отображаются полностью и не обрезаются.
    * Проверить, что объявления с очень коротким названием отображаются с достаточным размером шрифта и не слишком плотно расположены.
    * Проверить, что при корректной ссылке на изображение она отображается верно.
    #### Критерии приемки:
    * Запись создана успешно и отображается на доске объявлений.
    * Данные записи введены правильно.
    * Система не позволяет создать новую запись с отрицательной суммой (-100).
    * Система позволяет создать новую запись с 0 суммой (0).
    * Система не позволяет создать новую запись с отрицательной 0 суммой (-0).
    * Система позволяет создать новую запись с 99999999999999999999999999999999999999999 суммой (99999999999999999999999999999999999999999).
    * Система отображает ошибку и сообщение о том, что сумма не может быть отрицательной при вводе отрицательной суммы (-100) и отрицательной 0 суммы (-0).
    * Объявления с большим названием должны отображаться полностью и не должны перекрывать друг друга.
    * Объявления с очень коротким названием должны отображаться с достаточным размером шрифта и не слишком плотно расположены.
    * Фреймы объявлений не должны перекрывать друг друга.
    * Изображение объявление отображается корректно.
2. **Редактирование объявления**:
    #### ID: TC-002
    #### Название: Редактирование существующего объявления
    #### Предусловие: Пользователь имеет доступ к доске объявлений и может редактировать существующие объявления.
    #### Шаги:
    1. Открыть доску объявлений.
    2. Найти существующую запись и нажать на нее.
    3. Нажать кнопку "Редактировать".
    4. Внести изменения в данные записи (например, изменить название, описание, цену).
    5. Нажать кнопку "Сохранить".
    #### Ожидаемый результат:
    * Запись отредактирована успешно и отображается на доске объявлений.
    * Данные записи изменены правильно.
    #### Проверка:
    * Проверить, что созданная запись отображается на доске объявлений.
    * Проверить, что отредактированная запись отображается на доске объявлений с измененными данными.
    #### Критерии приемки:
    * Запись отредактирована успешно и отображается на доске объявлений.
    * Данные записи изменены правильно.
3. **Фильтрация записей**:
    #### ID: TC-003
    #### Название: Поиск объявлений по ключевым словам
    #### Предусловие: Пользователь имеет доступ к доске объявлений и может искать объявления.
    #### Шаги:
    1. Открыть доску объявлений.
    2. Нажать кнопку с пиктограммой фильтрации.
    3. Выбрать критерии фильтрации (например: цена, просмотры, лайки).
    4. Нажать нужный фильтр.
    5. Повторить пункты 1-4, нажать на пиктограмму сортировки по убыванию/возростанию .
    6. Повторить пункт 1, ввести ключевые слова в поле поиска.
    7. Нажать кнопку "Найти".
    8. Повторить пункты 1-4, нажать на пиктограмму" Items on page:" выбрать "25".
    9. Нажимать на кнопку "Следующая".
    #### Ожидаемый результат:
    * Записи отфильтрованы правильно в соответствии с выбранными критериями.
    * Отображается только записи, в правильной последовательности критериям фильтрации.
    * Найдена запись по кнопке "Найти".
    * Результаты будут циклически пролистываться.
    #### Критерии приемки:
    * Записи отфильтрованы правильно в соответствии с выбранными критериями.
    * Отображается только записи, в правильной последовательности критериям фильтрации.
    * Отображается толдько результат поиска.
    * Не возникает ошибок при перелистывании элементов.

#### Примечания:
* Этоти тест-кейсы проверяют функциональность доски объявлений, включая создание, редактирование и фильтрацию записей.
* Тест-кейсы должен быть выполнены для разных типов записей и критериев фильтрации.