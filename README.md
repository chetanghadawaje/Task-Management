
### Token API
curl --location 'http://127.0.0.1:8000/api/token/' \
--header 'Content-Type: application/json' \
--data '{
    "username": "admin",
    "password": "admin"
}'

{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczMDk3MTUzNCwiaWF0IjoxNzMwODg1MTM0LCJqdGkiOiI3ODQ4MjY5YmRhNjU0ZmI5YjI5OGI2MzQ2MmY0YTI5NSIsInVzZXJfaWQiOjF9.a13Ga4BIDTSbGL6fZ0llM80J85CTmbOyVjWPfjcMNQU",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMwODg4NzM0LCJpYXQiOjE3MzA4ODUxMzQsImp0aSI6Ijc2ZDBiZTRiNjdlNjRmOWRhYmY4YWJlMzhiNTcxYjdkIiwidXNlcl9pZCI6MX0.RkRhurle7kgkfnCvVI7x-5PQjlod10g2L7IntgFC5EI"
}


### Task POST API
curl --location 'http://127.0.0.1:8000/api/tasks/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMwODg4NzM0LCJpYXQiOjE3MzA4ODUxMzQsImp0aSI6Ijc2ZDBiZTRiNjdlNjRmOWRhYmY4YWJlMzhiNTcxYjdkIiwidXNlcl9pZCI6MX0.RkRhurle7kgkfnCvVI7x-5PQjlod10g2L7IntgFC5EI' \
--data '{
    "title": "Test1",
    "description": "Test description",
    "due_date": "2024-11-10T15:30:00Z",
    "status": "Pending"
}'

{
    "id": 1,
    "title": "Test1",
    "description": "Test description",
    "due_date": "2024-11-10T15:30:00Z",
    "status": "Pending",
    "created_at": "2024-11-06T09:32:13.268266Z",
    "updated_at": "2024-11-06T09:32:13.268286Z"
}


### Task GET API
curl --location 'http://127.0.0.1:8000/api/tasks/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMwODg4NzM0LCJpYXQiOjE3MzA4ODUxMzQsImp0aSI6Ijc2ZDBiZTRiNjdlNjRmOWRhYmY4YWJlMzhiNTcxYjdkIiwidXNlcl9pZCI6MX0.RkRhurle7kgkfnCvVI7x-5PQjlod10g2L7IntgFC5EI'

[
    {
        "id": 1,
        "title": "Test1",
        "description": "Test description",
        "due_date": "2024-11-10T15:30:00Z",
        "status": "Pending",
        "created_at": "2024-11-06T09:32:13.268266Z",
        "updated_at": "2024-11-06T09:32:13.268286Z"
    }
]



### Task Single GET API
curl --location 'http://127.0.0.1:8000/api/tasks/1' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMwODg4NzM0LCJpYXQiOjE3MzA4ODUxMzQsImp0aSI6Ijc2ZDBiZTRiNjdlNjRmOWRhYmY4YWJlMzhiNTcxYjdkIiwidXNlcl9pZCI6MX0.RkRhurle7kgkfnCvVI7x-5PQjlod10g2L7IntgFC5EI'

{
    "id": 1,
    "title": "Test1",
    "description": "Test description",
    "due_date": "2024-11-10T15:30:00Z",
    "status": "Pending",
    "created_at": "2024-11-06T09:32:13.268266Z",
    "updated_at": "2024-11-06T09:32:13.268286Z"
}

{
    "detail": "No Task matches the given query."
}



### Task PUT API
curl --location --request PUT 'http://127.0.0.1:8000/api/tasks/1/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMwODg4NzM0LCJpYXQiOjE3MzA4ODUxMzQsImp0aSI6Ijc2ZDBiZTRiNjdlNjRmOWRhYmY4YWJlMzhiNTcxYjdkIiwidXNlcl9pZCI6MX0.RkRhurle7kgkfnCvVI7x-5PQjlod10g2L7IntgFC5EI' \
--data '{
    "title": "Test update",
    "description": "Test description",
    "due_date": "2024-11-10T15:30:00Z",
    "status": "Pending"
}'

{
    "id": 1,
    "title": "Test update",
    "description": "Test description",
    "due_date": "2024-11-10T15:30:00Z",
    "status": "Pending",
    "created_at": "2024-11-06T09:32:13.268266Z",
    "updated_at": "2024-11-06T09:35:02.483710Z"
}



### Task DELETE API
curl --location --request DELETE 'http://127.0.0.1:8000/api/tasks/1/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMwODg4NzM0LCJpYXQiOjE3MzA4ODUxMzQsImp0aSI6Ijc2ZDBiZTRiNjdlNjRmOWRhYmY4YWJlMzhiNTcxYjdkIiwidXNlcl9pZCI6MX0.RkRhurle7kgkfnCvVI7x-5PQjlod10g2L7IntgFC5EI'

