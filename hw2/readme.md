Источник https://geekbrains.ru/posts/

Необходимо обойти все записи в блоге и извлеч из них информацию следующих полей:

    url страницы материала
    Заголовок материала
    Первое изображение материала
    Дата публикации (в формате datetime)
    имя автора материала
    ссылка на страницу автора материала

пример словаря:

{
"url": "str",
"title": "str",
"image": "str",
"writer_name": "str", 
"writer_url": "str",
"pub_date": datetime object,

}

полученые материалы сохранить в MongoDB

предусмотреть метод извлечения данных из БД за период передаваемый в качестве параметров