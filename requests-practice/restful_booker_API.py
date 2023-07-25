from requests import request, Response
from typing import Dict, Any
import requests

# Docs: https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request
API_URL = "https://restful-booker.herokuapp.com"


# API endpoints
def health_check() -> Response:
	url = API_URL + "/ping"
	response = request(url=url, method="GET")
	return response


# def health_checker() -> Response:
# 	response2 = requests.get(API_URL + "/ping")
# 	return response2


def create_booking(request_payload: Dict[str, Any]) -> Response:
	url = API_URL + "/booking"
	headers = {"Content-Type": "application/json"}
	response = request(url=url, method="POST", data=request_payload, headers=headers)
	return response


def delete_booking(booking_id: str, headers: Dict[str, str]) -> Response:
	url = API_URL + "/booking/1"
	response = request(url=url, method="DELETE", headers=headers)
	return response


# def get_booking_by_id():
# 	pass


# def get_list_of_bookings():
# 	pass


# You can have two separate functions to call different update-endpoints or one to handle both based on a condition
# def update_booking():
# 	pass

