�������� ������ ��������� �� Django.

Frameworks: Django, Scrapy, Django REST Framework
1. � ����� parserproduct - ������ �� Scrapy. ������ ������ 'https://bt.rozetka.com.ua/coffee_machines/c80164/
� ��������� ���������� � product.json ����.

2. � 1 html "�������" ����������� �������� �� ������� �������� � �� � ���� ��� �� 
�������� �� ������������� ������������ ������� ������ �� ������������� ����������� 
������ �������� ������� �� .json ����� ��������������� �������� � ��.

3. ��� ������� product � �� ������ API �� ������ Django REST Framework.
	api/products/ - get ������ �� ��������� ���������� � ���� ��������� ��
	api/products/<pk>/ - get ������ �� ��������� ���������� � ghjlernt c id=pk
	api/products/create/ - post ������ �� �������� ������ ��������, ������� �����������
	api/products/update/<pk>/ - put ������ �� ���������� ���������� � ������ � id=pk, ������� �����������
	api/products/destroy/<pk>/ - delete ������ �� �������� � �� ������ � id=pk, ������� �����������
4. /admin - ����� ������, login: admin, password: admin.
5. ���� name � adress, phone - ����� ����������� �� ����� �������� ����������.
	���� email - ����������� ��������� django.
        ���� shipping_options - ������� � 4 ���������� ������. ���� ����� ����� 300 - 3 ��������.
������� �� ������ Pay - �������� ���������� �� ������ � ��.




