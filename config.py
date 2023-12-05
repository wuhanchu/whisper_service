import os


class Config:
    """
    配置信息
    """

    MODEL = os.getenv("MODEL", "medium")  # 调用的模型
    TEMP_FOLDER = os.getenv("TEMP_FOLDER", "items_temp")
