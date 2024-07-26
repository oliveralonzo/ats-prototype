from django.db import models
import json, os


# This is the model that grabs a corresponding simplification object
# from sample.json for a given text
class Replacer(models.Model):

    def __init__(self):
        script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
        rel_path = "sample.json"
        abs_file_path = os.path.join(script_dir, rel_path)
        json_file = open(abs_file_path, "r")
        self.sentences = json.load(json_file)
        json_file.close()

    def replaceSentence(self, to_replace):
        print("Sentence to be replaced -----> ", to_replace)
        try:
            sentence = self.sentences[to_replace]
            print(sentence)
            return sentence
        except Exception as ex:
            print(ex)
            print("failed")
            return {}