# -*- coding: utf-8 -*-

"""
Documents: https://github.com/openai/whisper
"""
import os
import time

import whisper

from stable_whisper import modify_model
from zhconv import convert
from flask import request, jsonify, Flask
from config import Config

app = Flask(__name__, root_path=os.getcwd())
model = whisper.load_model(Config.MODEL)
modify_model(model)

# 创建临时文件夹
temp_folder = Config.TEMP_FOLDER
os.makedirs(temp_folder, exist_ok=True)


def save_file(file):
    file_path = os.path.join(
        temp_folder, str(time.time()) + os.path.splitext(file.filename)[-1]
    )
    file.save(file_path)
    return file_path


def convert_to_simplified_chinese(content: dict):
    """
    中文繁体转中文简体
    """
    content["text"] = convert(content["text"], "zh-cn")
    content["segments"] = [
        {**segment, "text": convert(segment["text"], "zh-cn")}
        for segment in content["segments"]
    ]


@app.route("/asr", methods=["POST"])
def asr():
    """
    whisper transcribe
    """
    param = {**request.files}

    if "file" not in param:
        return jsonify({"message": "invalid file param", "code": "-1"})

    file_path = save_file(param["file"])
    try:
        result = model.transcribe(file_path)

        # 处理时间不要重叠
        last_end = None
        for item in result.get("segments", []):
            if item.get("start") and item.get("start") == last_end:
                item["start"] = float(item.get("start")) + 0.01

            last_end = item.get("end")

        # 转换简体繁体
        if result.get("language") == "zh":
            convert_to_simplified_chinese(result)

        return jsonify({"message": "success", "code": "0", "result": result})
    finally:
        import os
        os.remove(file_path)


# 运行
if __name__ == "__main__":
    print(app.url_map)
    app.run("0.0.0.0", port=5000)
