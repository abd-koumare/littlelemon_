# littlelemon_


HTML STATIC VIEW

127.0.0.1:8000/restaurant/

User API endpoints:

    127.0.0.1:8000/auth/users/ [POST]  # to create a new user using username and password as formdata
    127.0.0.1:8000/api/api-token-auth/ # username and password required to get token you of user created


*Note*: all these endpoint are protected don't forget to include Bearer Token before making request. 
MenuItem API endpoints:
    127.0.0.1:8000/api/menu [GET, POST]
    127.0.0.1:8000/api/menu/<int:pk> [GET, PUT, PATCH, DELETE]

Booking API endpoints:

    127.0.0.1:8000/api/booking [GET, POST]
    127.0.0.1:8000/api/booking/<int:pk> [GET, PUT, PATCH, DELETE]




