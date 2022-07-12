

### Развертывание
1) `poetry install` или  `pip install -r requirements.txt`
2) запусти бд (можно прост юзануть `docker run -p 5432:5432 -e POSTGRES_USER=gallery -e POSTGRES_DB=photo_album_db -e POSTGRES_PASSWORD=12345 --name gallery postgres`)
3) ./manage.py runserver`

### Развертывание прод
1) `docker-compose up --build`
2) `sudo docker exec -it app bash -c "sh /app/entrypoint.sh"` - если бд была снеcена
