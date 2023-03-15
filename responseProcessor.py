import hashlib
import json

class ResponseProcessor:

    def __init__(self, response_and_feedback, file_path = "response.json"):
        self.response_and_feedback = response_and_feedback
        self.file_path = file_path
        self.responses = []

    def _get_max_response_id(self):
        try:
            with open(self.file_path, 'r') as f:
                data = json.load(f)
                self.responses = data
        except json.decoder.JSONDecodeError:
            data = []
            with open(self.file_path, 'w') as f:
                json.dump(data, f)
        if not data:
            return 0
        return max(data, key=lambda x: x['response_id'])['response_id']

    def _save_response_to_file(self):
        with open("response.json", "w") as f:
            json.dump(self.responses, f, indent=4)

    def process_response_from_gpt(self):
        response_hash = hashlib.sha256(str(self.response_and_feedback).encode()).hexdigest()
        
        for response in self.responses:
            if response["response_hash"] == response_hash:
                return
                
        response_id = self._get_max_response_id() + 1
        data = {
            "response_id": response_id,
            "response_text": self.response_and_feedback[0],
            "response_hash": response_hash,
            "response_edit": self.response_and_feedback[1]
        }
        self.responses.append(data)
        self._save_response_to_file()

    def clear_repetitive_hashes(self):
        try:
            with open(self.file_path, 'r') as f:
                self.responses = json.load(f)
        except json.decoder.JSONDecodeError:
            self.responses = []

        hashes = []
        filtered_responses = []
        response_id = 0
        for response in self.responses:
            response_hash = response["response_hash"]
            if response_hash not in hashes:
                hashes.append(response_hash)
                response["response_id"] = response_id
                filtered_responses.append(response)
                response_id += 1

        self.responses = filtered_responses
        self._save_response_to_file()