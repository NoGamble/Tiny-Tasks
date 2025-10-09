import json
import os

class Storage:
    FILE_PATH = "task.json"

    def load(self):
        if not os.path.exists(self.FILE_PATH):
            return []
        with open(self.FILE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    
    def save(self, data):
        with open(self.FILE_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
