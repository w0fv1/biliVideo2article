# biliVideo2article

## 项目介绍

**`biliVideo2article`** 是一个将哔哩哔哩视频转换为文章的小项目。本项目利用哔哩哔哩的 API 获取视频信息和评论，通过 OpenAI 的 API 生成文章，并将生成的文章保存为 Markdown 格式。

## 使用说明

### 环境设置

1. **安装 Python**

   请确保你的系统已安装 Python 3.7 及以上版本。你可以通过以下命令检查 Python 版本：

   ```bash
   python --version
   ```

2. **创建虚拟环境**

   建议使用 `venv` 来创建虚拟环境，以确保依赖不会与系统的其他项目发生冲突。

   ```bash
   python -m venv venv
   source venv/bin/activate  # Unix 系统
   venv\Scripts\activate     # Windows 系统
   ```

3. **安装依赖库**

   使用以下命令安装项目所需的依赖库：

   ```bash
   pip install -r requirements.txt
   ```

### 配置文件

1. **复制配置模板**

   复制 `config.sample.json` 文件并重命名为 `config.json`。

   ```bash
   cp config.sample.json config.json

   # Windows 系统
   copy config.sample.json config.json
   ```

2. **编辑配置文件**

   打开 `config.json` 文件，根据你的需求填写相应的配置信息：

   ```json
   {
     "bvid": "视频的 bvid",
     "openai": {
       "api_key": "你的 OpenAI API 密钥",
       "openai_base_url": "OpenAI API 的基础 URL",
       "model": "填写你的 LLM MODEL",
       "temperature": 1,
       "max_tokens": 4096
     },
     "credential": {
       "sessdata": "请参考 https://nemo2011.github.io/bilibili-api/#/get-credential 获得 sessdata",
       "bili_jct": "请参考 https://nemo2011.github.io/bilibili-api/#/get-credential 获得 bili_jct",
       "buvid3": "请参考 https://nemo2011.github.io/bilibili-api/#/get-credential 获得 buvid3",
       "dedeuserid": "请参考 https://nemo2011.github.io/bilibili-api/#/get-credential 获得 dedeuserid",
       "ac_time_value": "请参考 https://nemo2011.github.io/bilibili-api/#/get-credential 获得 ac_time_value"
     },
     "prompt": "生成文章时的提示信息",
     "info": "这是视频的额外事实信息，当视频的信息不足以生成一篇文章的时候，在这里补充事实信息，如果不需要，请删除留空。"
   }
   ```

### 使用步骤

1. **阅读并同意免责声明**

   在运行脚本之前，请先阅读并同意免责声明。

2. **确认授权**

   确认你已获得视频的转载和改编授权。

3. **运行主脚本生成文章**

   使用以下命令运行主脚本：

   ```bash
   python main.py
   ```

4. **创建示例文件（可选）**

   为了更好地了解生成的文章格式，你可以创建一个 `sample.md` 文件作为参考。你可以使用以下内容作为模板：

   ```markdown
   # 示例文章标题

   ## 引言

   这是一个示例文章的引言部分，用于展示生成文章的基本结构和格式。

   ## 正文

   这里是文章的主要内容部分，你可以根据需要添加更多的段落和小节。

   ## 结论

   这是文章的结论部分，总结主要观点和内容。
   ```

   将上述内容保存为 `sample.md`，你可以根据实际生成的内容进行调整和参考。

### 生成结果

- **生成文章**

  脚本运行完成后，会在当前目录下生成一个 `output.md` 文件，即为生成的文章。

- **生成封面**

  脚本运行完成后，会在当前目录下生成一个 `cover.jpg` 文件，即为视频的封面。

### 注意事项

- 本代码仅供学习交流使用，请勿用于商业用途。
- 使用本代码前，请确保你已获得视频的转载和改编授权。
- 生成的文章请勿用于违法用途。

### 免责声明

- 请在运行脚本时，确认你不会将生成的文章用于商业用途或违法用途。如果不同意，请不要继续运行脚本。
- 请确认你已获得视频的转载和改编授权。如果没有，请不要继续运行脚本。

## 其他说明

- **项目依赖**

  本项目依赖上游项目 [nemo2011/bilibili-api](https://github.com/Nemo2011/bilibili-api)，感谢原作者的贡献。另外，当 `nemo2011/bilibili-api` 项目更新时，本项目也需要更新，以保持正常运行。

- **无 UI**

  本项目不会制作易用性 UI，以免被滥用，请自行修改代码以适应自己的需求。（对于程序员来说，这不是什么难事）

- **支持与反馈**

  闲聊可加QQ群: [w0fv1.dev / 编程小屋](https://qm.qq.com/q/tqTsZ39nGM)。但有项目相关的反馈请发 [Issue](https://github.com/你的仓库/issues)。

## 许可证

本项目使用 [Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/deed.zh) 许可证。您可以自由地共享和修改本项目的内容，但仅限于非商业用途，且必须遵守许可证的条款。

---
```

---

**备注：**

- **示例文件 (`sample.md`)**：已在“使用步骤”中添加了创建 `sample.md` 的说明，提供了一个基本模板供用户参考生成的文章格式。
  
- **Issue 链接**：请确保将 `[Issue](https://github.com/你的仓库/issues)` 中的 `你的仓库` 替换为你实际的 GitHub 仓库地址，以便用户能够正确提交问题反馈。

- **进一步自定义**：根据项目需求，你可以进一步完善和自定义 `sample.md` 的内容，以更好地展示生成文章的样式和结构。