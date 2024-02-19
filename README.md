# Leon_HOTEL
Руководство по запуску проекта:
Для начала работы нужно указать переменные окружения в файле .env  
Пример:
```
#GOOGLE
export GOOGLE_CLIENT_ID=ВАШ_КЛЮЧ
export GOOGLE_CLIENT_SECRET=ВАШ_КЛЮЧ
```
Запустить docker compose.
```
docker compose up --build -d
```
Перейти по http://127.0.0.1:8000/admin/ и войти используя admin/admin.  
Пароль можно изменить после входа.  

В админ панели присутствуют:  
CRUD, Пользователи, Отели, Города, Сети(google), Русский язык.

Ссылка на задание:  
https://docs.google.com/document/d/1wHnPeOMGrHysfiiiiENqm5jwRlM2GXOtAp0mTF_7ZzU/edit?pli=1#heading=h.8853u49snklu

Описание эндпоинтов:  
"user/create/":   
Операция - создание пользователя   
Параметры - 
```
{"first_name":"Lev", "last_name":"Sergeev", "password":"asgqwg215ssa", "email":"testmail@mail.ru"}
```   
"user/auth/":  
Операция - авторизация пользователя  
Параметры -  
```
{"email":"testmail@mail.ru", "password":"asgqwg215ssa"}  
```  
"hotels/":  
Операция - список отелей в формате json  
Параметры - 
```  
?city_id=<city_id>&from_id=<hotel_id>&limit=<number>
```  
city_id: Есть возможность фильтровать по городу если передан GET параметр;  
from_id: Если передан GET параметр то все отели id которых больше указанного;  
limit: Если передан GET параметр то вернуть не больше указанного числа;    
"accounts/":  
Операция - google авторизация/регистрация/деавторизация  
Параметры - отсутствуют  