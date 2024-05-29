# biliVideo2article

## 项目介绍

`biliVideo2article`
是一个将哔哩哔哩视频转换为文章的小项目。本项目利用哔哩哔哩的API获取视频信息和评论，通过OpenAI的API生成文章，并将生成的文章保存为Markdown格式。

## 使用说明

### 环境设置

1. 请确保你的系统已安装 Python 3.7 及以上版本。
2. 建议使用 `venv` 来创建虚拟环境，以确保依赖不会与系统的其他项目发生冲突。

```bash
python -m venv venv
source venv/bin/activate  # Unix系统
venv\Scripts\activate     # Windows系统
```

3. 安装依赖库：

```bash
pip install -r requirements.txt
```

### 配置文件

1. 复制 `config.sample.json` 文件并重命名为 `config.json`。

```bash
cp config.sample.json config.json

# Windows系统
copy config.sample.json config.json
```

2. 打开 `config.json` 文件，根据你的需求填写相应的配置信息：

```json
{
  "bvid": "视频的bvid",
  "openai": {
    "api_key": "你的OpenAI API密钥",
    "openai_base_url": "OpenAI API的基础URL",
    "model": "填写你的LLM MODEL",
    "temperature": 1,
    "max_tokens": 4096
  },
  "credential": {
    "sessdata": "请参考https://nemo2011.github.io/bilibili-api/#/get-credential获得sessdata",
    "bili_jct": "请参考https://nemo2011.github.io/bilibili-api/#/get-credential获得bili_jct",
    "buvid3": "请参考https://nemo2011.github.io/bilibili-api/#/get-credential获得buvid3",
    "dedeuserid": "请参考https://nemo2011.github.io/bilibili-api/#/get-credential获得dedeuserid",
    "ac_time_value": "请参考https://nemo2011.github.io/bilibili-api/#/get-credential获得ac_time_value"
  },
  "prompt": "生成文章时的提示信息",
  "info": "这是视频的额外事实信息, 当视频的信息不足以生成一篇文章的时候, 在这里补充事实信息, 如果不需要, 请删除留空."
}
```

### 使用步骤

1. 运行脚本之前，请先阅读并同意免责声明。

2. 确认你已获得视频的转载和改编授权。

3. 运行主脚本生成文章：

```bash
python main.py
```

### 注意事项

- 本代码仅供学习交流使用，请勿用于商业用途。
- 使用本代码前，请确保你已获得视频的转载和改编授权。
- 生成的文章请勿用于违法用途。

### 免责声明

请在运行脚本时，确认你不会将生成的文章用于商业用途或违法用途。如果不同意，请不要继续运行脚本。

请确认你已获得视频的转载和改编授权。如果没有，请不要继续运行脚本。

## 其他说明

如有任何问题或建议，请发Issue或联系我。

该项目依赖上游项目
[nemo2011/bilibili-api](https://github.com/Nemo2011/bilibili-api)，感谢原作者的贡献。另外当`nemo2011/bilibili-api`项目更新时，本项目也需要更新，以保持正常运行。

---

请根据实际情况调整配置和说明内容。祝使用愉快！
