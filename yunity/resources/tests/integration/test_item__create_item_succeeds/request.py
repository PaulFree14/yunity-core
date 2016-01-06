from .initial_data import request_user

request = {
    "endpoint": "/api/items",
    "method": "post",
    "body": {
        "description": "my lovely test item",
        "latitude": 50.827845,
        "longitude": 12.921370
    },
    "user": request_user,
}
