Тестовый проэкт написаный на Django.

Frameworks: Django, Scrapy, Django REST Framework
1. В папке parserproduct - Парсер на Scrapy. Парсит ссылку 'https://bt.rozetka.com.ua/coffee_machines/c80164/
и сохраняет информацию в product.json файл.

2. В 1 html "шаблоне" выполняется проверка на наличие объектов в БД и если они не 
приходят из представления отображается простая ссылка на представление запускающее 
скрипт выгрузки товаров из .json файла сгенерированого парсером в БД.

3. Для таблицы product в БД создан API на основе Django REST Framework.
	api/products/ - get запрос на получение информации о всех продуктах БД
	api/products/<pk>/ - get запрос на получение информации о ghjlernt c id=pk
	api/products/create/ - post запрос на создание нового продукта, требует авторизации
	api/products/update/<pk>/ - put запрос на обновление информации о товаре с id=pk, требует авторизации
	api/products/destroy/<pk>/ - delete запрос на удаление с БД товара с id=pk, требует авторизации
4. /admin - админ панель, login: admin, password: admin.
5. Поля name и adress, phone - имеют ограничения по длине вводимой информации.
	Поле email - стандартная валидация django.
        Поле shipping_options - чекбокс с 4 вариантами выбора. Если сумма менее 300 - 3 варианта.
Нажатие на кнопку Pay - сохраняе информацию по заказу в БД.




