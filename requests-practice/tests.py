import json

from restful_booker_API import health_check, create_booking

X = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }


# API tests
def test_health_check():
    response = health_check()
    assert response.status_code == 201
    assert response.url == "https://restful-booker.herokuapp.com/ping"

# assert response. == "GET"


def test_create_booking():
    payload = X
    response = create_booking(request_payload=payload)
    assert response.url == "https://restful-booker.herokuapp.com/booking"
    # json_response = response.json()
    # assert "bookingid" in json_response
    # assert "application/json" in response.headers["Content-Type"]
    # assert response.status_code == 200
