from json.encoder import py_encode_basestring_ascii
from typing import List
import fasttext
import fasttext.util
from virtex import RequestHandler
from virtex import http_server

# You will need to download a pretrained FastText model.bin file
model_filepath = "../../.local/datasets/wiki/wiki.en.bin" 


class MatchingService(RequestHandler):

    def __init__(self):
        self.model = fasttext.load_model(model_filepath)

    def process_request(self, data):
        return [sent.strip().lower() for sent in data]

    def run_inference(self, model_input):
        matches = [self.model.get_nearest_neighbors(q) for q in model_input]
        return matches

    def process_response(self, model_output_item):
        return model_output_item


app = http_server(
    name='fasttext_word_matcher',
    handler=MatchingService(),
    max_batch_size=128,
    max_time_on_queue=0.005
)
