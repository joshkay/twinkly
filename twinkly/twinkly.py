# -*- coding: utf-8 -*-

"""Main module."""

import requests
import json

class Twinkly(object):

	HTTP = "http://"
	TWINKLY_URL = "/xled/v1/"
	LOGIN_URL = "login"
	VERIFY_URL = "verify"
	MODE_URL = "led/mode"

	AUTH_HEADER = 'X-Auth-Token'

	AUTHENTICATION_TOKEN = 'authentication_token'
	CHALLENGE_RESPONSE = 'challenge-response'
	MODE = 'mode'
	MODE_ON = 'movie'
	MODE_OFF = 'off'

	HEADERS = {'Content-Type': 'application/json'}
	LOGIN_PAYLOAD = {'challenge': 'AAECAwQFBgcICQoLDA0ODxAREhMUFRYXGBkaGxwdHh8='}
	TURN_ON_PAYLOAD = {MODE: MODE_ON}
	TURN_OFF_PAYLOAD = {MODE: MODE_OFF}

	def __init__(self, host):
		self._request_base_url = Twinkly.HTTP + host + Twinkly.TWINKLY_URL
		self._request_headers = Twinkly.HEADERS

	def login_auth(self):
		loginData = requests.post(
			self._request_base_url + Twinkly.LOGIN_URL,
			data = json.dumps(Twinkly.LOGIN_PAYLOAD),
			headers = self._request_headers
		).json()
		
		challengeResponse = loginData[Twinkly.CHALLENGE_RESPONSE]
		authToken = loginData[Twinkly.AUTHENTICATION_TOKEN]

		self._request_headers[Twinkly.AUTH_HEADER] = authToken
		
		verifyPayload = {Twinkly.CHALLENGE_RESPONSE: challengeResponse}

		verifyData = requests.post(
			self._request_base_url + Twinkly.VERIFY_URL,
			data = json.dumps(verifyPayload),
			headers = self._request_headers
		).json()

		print(verifyData)

	def turn_on(self):
		requests.post(
			self._request_base_url + Twinkly.MODE_URL,
			data = json.dumps(Twinkly.TURN_ON_PAYLOAD),
			headers = self._request_headers
		)

	def turn_off(self):
		requests.post(
			self._request_base_url + Twinkly.MODE_URL,
			data = json.dumps(Twinkly.TURN_OFF_PAYLOAD),
			headers = self._request_headers
		)

	def get_state(self):
		modeData = requests.get(
			self._request_base_url + Twinkly.MODE_URL,
			headers = self._request_headers
		).json()

		return modeData[Twinkly.MODE] != Twinkly.MODE_OFF