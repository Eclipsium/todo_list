
###REST API списка задач
Тестовое задание для [ReTechLabs](www.ReTechLabs.com "ReTechLabs")

Медоты работы с организациями
------------
- **/api/v1/org/**

Метод GET возвращает организации пользователя, к которым имеет доступ
 - **/api/v1/org/create/**
 
Метод POST получает параметр `name` и создает организацию с таким именем.
Пользователь может создать только одну организацию
- **/api/v1/org/detail/pk/** 

Редактирование и удаление отдельных организаций.

Методы работы с пользователями
------------
- **/api/v1/users/** 

Получение текущего пользователя
- **/api/v1/users/detail/pk** 
 
Удаление и редактирование отдельных пользователей
- **/api/v1/users/invite** 

Метод GET возвращает приглашенных в организацию пользователей, в которой вы являетесь создателем

Метод POST получает параметр `email` и добавляет пользователя в органищацию

Метод DELETE получает параметр `email` и удаляет пользователя из организации

- **/api/v1/users/create/

Метод POST создает нового пользователя. Принимает `email` и `password`. Пароль хешируется

Методы работы с задачами
------------

- **/api/v1/org/**

Метод GET возвращает организации пользователя, к которым он имеет доступ

- **/api/v1/org/detail/pk/**

Метод для удаления и редактирования отдельных задач

- **/api/v1/org/create/** 

Метод POST получает параметр `text` и создает задачу для компании, создателем которой вы являетесь

