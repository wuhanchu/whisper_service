# whisper 服务

基于 [whisper](https://github.com/openai/whisper) 封装函数提供 API 服务

## 环境要求

1. python 3.7+

## 环境变量

| 分组    | 配置项        | 说明                                                                                                      |
| ------  | ------------ | -------------------------------------------------------------------------------------------------------- |
| 模型参数 | MODEL        | 需要调用的模型名称 默认 base                                                                                |
| 文件参数 | TEMP_FOLDER  | 临时文件夹                                                                                                |

## 文件目录说明

```filetree
├── README.md -- 项目说明
├── run.py -- 程序运行文件
├── run.sh -- 容器运行脚本
├── requirements.txt -- 项目使用到的依赖包
├── config.py -- 项目配置文件
├── Dockerfile -- 项目镜像构建文件
```

## 编译

初始化编译
`docker build  . -t whisper_server`

更新编译
`docker build -f ./Dockerfile.continue . -t whisper_server`
