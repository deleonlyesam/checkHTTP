import os
import sys

import logging
import logging.config
import requests
import argparse

import parse_config 


class CheckHTTP(object):
	"""
		Main class to check http status based from request presented
		on YAML config config_file

	"""
	config_file = parse_config.ParseYAML( )

	def __init__(self, config_file): 
		self.config_file = config_file
		self.contents = parse_config.ParseContent(self.config_file)

	def request(self):

		url = self.contents.get_url_params("url")
		method = self.contents.get_url_params("method")
		follow_redirects = self.contents.get_url_params("follow_redirects")
		timeout = self.contents.get_url_params("timeout")
		
		if method.upper() != "GET": 
			raise Exception("Only accepts GET as method")

		# Try catch must be implemented here
		# ConnectionError, HTTPError, Timeout, TooManyRedirects
		# requests.exceptions.RequestException
		response = requests.get(url,  
				allow_redirects=follow_redirects,
				timeout=timeout)


if __name__ == '__main__':
	cmd = argparse.ArgumentParser()
	cmd.add_argument("--config", help="Accepts YAML file as parameter")

	config_file_path = cmd.parse_args().config

	a = CheckHTTP(config_file_path)
	print a.request()