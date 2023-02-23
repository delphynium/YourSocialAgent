import os
import json
from pathlib import Path

class ChatlogManager:
    def __init__(self, dir=Path("./data")):
        self.dir = dir

    def add(self, text, person, send):
        filename = str(self.dir / (person + ".json"))
        data = []
        if os.path.exists(filename):
            try:
                with open(filename, 'r', encoding="utf8") as f:
                    data = json.load(f)
            except EnvironmentError:
                print("Loading json failed!")
        data.append({"from": "I" if send else "They", "text": text})
        try:
            with open(filename, 'w', encoding="utf8") as f:
                json.dump(data, f, ensure_ascii=False)
        except EnvironmentError:
            print("Dumping json failed!")

    def read_all(self, person):
        filename = str(self.dir / (person + ".json"))
        data = []
        if os.path.exists(filename):
            try:
                with open(filename, 'r', encoding="utf8") as f:
                    data = json.load(f)
            except EnvironmentError:
                print("Loading json failed!")
        return data

    def clear(self, person):
        filename = str(self.dir / (person + ".json"))
        if os.path.exists(filename):
            try:
                os.remove(filename)
            except EnvironmentError:
                print("Clearing chatlog failed!")