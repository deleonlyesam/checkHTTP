import  uuid
import yaml

class ParseYAML(object):
	""" 
	This class is responsible to parse data based from 
		YAML as input.

	"""
	def __set__(self, instance, filepath):
		try: 
			with open(filepath, 'r') as contents:
				self.contents = contents.read()
		except Exception, err:
			print err

	def __get__(self, instance, owner):
		
		try:
			self.contents = yaml.load(self.contents)
			return dict(self.contents)
		except Exception, err:
			print err

class ParseContent(ParseYAML):
	"""
		Gathers data based from key value pair on the YAML file.
		Im thinking some revisions here to allow fetching the data
		in a more simple, dynamic as possible. Eliminate static data
	"""
	def __init__(self, contents):
		super(ParseContent, self).__init__()
		self.contents = contents
		self.root = dict(self.contents['task'])
		self.definition_tree = dict(self.root["definition"])
		self.run_tree = dict(self.root["run"])

	def get_id(self, key="definition_id"):
		if key == "definition_id": return self.get_definition("id")
		if key == "run_id": 
			return uuid.uuid4().get_hex()

	def get_definition(self, key):
		"""Gets all key value pairs from definition tree"""
		try:
			for each in self.definition_tree:
				self.definition_tree[key]
		except KeyError, err:
			raise Exception("{0} can't be recognized as a key element. \
				Info: {1}".format(key, err))
			
	def get_url_params(self, key):
		try:
			parameters = self.definition_tree["parameters"]
			return parameters[key]
		except KeyError, err:
			raise Exception("{0} can't be recognized as a key element. \
				Info: {1}".format(key, err))

		
	def get_run(self, key):
		"""Gets all key value pairs from run tree"""
		if key == "run_id": return uuid.uuid4().get_hex()
		for each in self.run_tree:
			if key == "logging": return self.run_tree[key]["config"]