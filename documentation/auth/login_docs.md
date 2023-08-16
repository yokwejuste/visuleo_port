# Login API Documentation

## Endpoint: `/api/v0/login`

### Description
The Login API allows users to authenticate and obtain an access token for accessing protected resources.

### Request
- HTTP Method: `POST`
- URL: `/api/v0/login`
- Content-Type: `application/json`

#### Request Body
The request body should be a JSON object with the following properties:

```json
{
  "email": "string",
  "password": "string"
}
```