# -*- coding: utf-8 -*-

"""
Documents: https://github.com/openai/whisper
"""
import os
import time

import whisper
from flask import request, jsonify, Flask
from config import Config

app = Flask(__name__, root_path=os.getcwd())
model = whisper.load_model(Config.MODEL)

# 创建临时文件夹
temp_folder = Config.TEMP_FOLDER
os.makedirs(temp_folder, exist_ok=True)


def save_file(file):
    file_path = os.path.join(temp_folder, str(time.time()) + os.path.splitext(file.filename)[-1])
    file.save(file_path)
    return file_path


@app.route("/asr", methods=["POST"])
def asr():
    """
    whisper transcribe
    """
    param = {**request.files}

    if "file" not in param:
        return jsonify({"message": "invalid file param", "code": "-1"})
    
    file_path = save_file(param["file"])
    result = model.transcribe(file_path)

    return jsonify({"message": "success", "code": "0", "result": result})


# 运行
if __name__ == "__main__":
    print(app.url_map)
    app.run("0.0.0.0", port=5000)
