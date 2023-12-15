from huggingface_hub import login, hf_hub_download
import json


""" # Get model api key """
def load_api_key_from_file(file_path):
    with open(file_path, 'r') as file:
        api_key = file.read().strip()
    return api_key


def util_setup():
    token_file_path='api_key_huggingface.txt'
    login(token=load_api_key_from_file(token_file_path))

    repo_id = "huggingface/label-files"
    filename = "imagenet-22k-id2label.json"
    id2label = json.load(open(hf_hub_download(repo_id, filename, repo_type="dataset"), "r"))
    LABELS = {int(k):v for k,v in id2label.items()}
    return LABELS