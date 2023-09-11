# API Documentation

## Endpoints

### POST `/api`

This endpoint creates a user resource. It expects a JSON request strictly in the following format:

```json
{
  "name": "Harry Potter"
}
```

#### Response

Status Code: **201 Created**

```json
{
  "id": 1,
  "name": "Harry Potter"
}
```

For requests with extra fields like this:

```json
{
  "name": "Draco Malfoy",
  "house": "Slytherin"
}
```

an error message will be returned (example below):

Status Code: **422 Unprocessable Entity**

```json
{
  "detail": [
    {
      "loc": ["body", "house"],
      "msg": "extra fields not permitted",
      "type": "value_error.extra"
    }
  ]
}
```

### GET `/api/{user_id}`

This endpoint gets a user with the provided ID in the path parameter.

Sample Request: `/api/1`

#### Response

Status Code: **200 OK**

```json
{
  "id": 1,
  "name": "Harry Potter"
}
```

The following error is returned when a request is made with an ID that does not exist in the database:

Status Code: **404 Not Found**

```json
{
  "detail": "User does not exist."
}
```

### PATCH `/api/{user_id}`

This endpoint updates a user with the provided ID in the path parameter. It expects a JSON request containing the new data in the following format:

Sample Request: `/api/1`

```json
{
  "name": "Hermione Granger"
}
```

#### Response

Status Code: **200 OK**

```json
{
  "id": 1,
  "name": "Hermione Granger"
}
```

For requests with extra fields like this:

```json
{
  "name": "Luna Lovegood",
  "house": "Ravenclaw"
}
```

an error message will be returned (example below):

Status Code: **422 Unprocessable Entity**

```json
{
  "detail": [
    {
      "loc": ["body", "house"],
      "msg": "extra fields not permitted",
      "type": "value_error.extra"
    }
  ]
}
```

### DELETE `api/{user_id}`

This endpoint deletes a user with the provided ID in the path parameter.

#### Response

Status Code: **204 No Content**
