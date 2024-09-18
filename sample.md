# HackNews 周报 708

**便捷日志查看工具；AMD GPU 运行 CUDA；开源 LLMOps 平台**

了解科技资讯、把握行业脉搏。欢迎收看科技周报。本期我们将介绍几个实用的科技工具，包括便捷的日志查看工具、开源的 HTML 邮件设计工具、动画创作工具、AMD GPU 运行 CUDA 的工具包，以及一个开源的 LLMOps 平台。

---

## 科技周报｜便捷日志查看工具；AMD GPU 运行 CUDA；开源 LLMOps 平台

### Logdy｜便捷日志查看工具

**Logdy** 是一个非常实用的日志查看工具，它将终端日志搬到了网页上，并加入了一些智能的功能。安装非常简单，只需一行命令即可完成。使用起来也很方便，只需将日志通过管道传给 Logdy，它就会在本地开启一个网页界面，让你可以实时查看日志。

Logdy 的强大之处在于它结合了多个常用工具的优点。它像 `tail` 一样能实时更新，像 `grep` 那样可以搜索，还能像 `jq` 那样处理 JSON。而且，它的界面非常直观，让你能更加轻松地浏览和分析日志。此外，它支持各种格式的日志，你还可以用 TypeScript 写解析规则，让灵活性大大增加。如果你经常需要查看和分析日志，Logdy 绝对值得一试。

[Logdy｜便捷日志查看工具](https://logdy.dev/)

---

### SENDUNE｜开源 HTML 邮件设计工具

**SENDUNE** 是一个开源的 HTML 邮件设计工具，让制作精美的邮件模板变得简单又高效。它提供了拖拽设计器、HTML 代码编辑器和纯文本邮件三种创建模板的方式，满足了不同用户的需求，从零基础到专业开发者都能够用得顺手。

SENDUNE 遵循了一些邮件设计的基本原则，确保生成的邮件能在各种客户端正常显示。我们认为邮件目前仍然是营销和发送通知常用的方式，但许多开发者初次开发邮件 HTML 模板时还是会因为兼容性等问题遇到困难。这个简单又精致的工具对帮助大家走出这一困境十分实用。

[SENDUNE｜开源 HTML 邮件设计工具](https://github.com/SendWithSES/Drag-and-Drop-Email-Designer)

---

### Motion Canvas｜动画创作工具

**Motion Canvas** 是一个有趣的动画创作工具，将代码编辑与可视化编辑巧妙融合。用户可以用 TypeScript 描述动画，实时预览，再在编辑器中进行微调。该项目基于 Web 构建，支持实时更新，提升效率。

我们之前介绍的 REVIDEO 项目就是基于 Motion Canvas 实现，用代码编辑视频。这一技术思路可以批量高效渲染视频，也可以将视频模板化，让无视频编辑能力的使用者通过配置参数定制自己的专属视频。相信在未来还有更大的发展潜力。

[Motion Canvas｜动画创作工具](https://motioncanvas.io/)

---

### SCALE｜AMD GPU 运行 CUDA

**SCALE** 是一个野心勃勃的 GPU 编程工具包，它让开发者可以将 CUDA 程序直接编译运行在 AMD GPU 上。SCALE 最大的亮点是它的兼容性，你不需要修改现有的 CUDA 代码或构建系统，甚至支持内联的 PTX 汇编代码。SCALE 编译器还与 nvcc 的命令行选项保持一致，目标是直接替换 NVIDIA 的构建工具链。

目前，SCALE 主要支持 AMD 的新一代 GPU 架构如 RDNA 2.0 和 3.0。它已经通过了多个知名开源项目的测试，包括大家关注的 LLaMA.cpp 大语言模型项目。我们认为 SCALE 的出现是否能让 AMD GPU 突破 NVIDIA GPU 基于库的构建的护城河，在保持兼容性的情况下性能如何，都值得进一步关注。

[SCALE｜AMD GPU 运行 CUDA](https://docs.scale-lang.com/)

---

### Pezzo｜开源 LLMOps 平台

如果你在基于 LLM 开发应用时，发现代码越来越多无法维护，那你可能需要考虑使用 **Pezzo** 这样一个开源的 LLMOps 平台。它提供了一系列强大功能，支持对代码的集中管理，并增加版本控制、实时监控和排查 AI 操作中的问题。通过缓存等方式优化成本，也支持团队协作管理和迭代相关资产。

Pezzo 还支持多种客户端，包括 Node.js、Python 和 LangChain。开发者可以通过 Docker Compose 轻松在本地运行完整的 Pezzo 服务。你可以使用他们提供的云服务。随着 LLM 上层应用开发的蓬勃发展，各类开发工具也会逐渐成熟，Pezzo 等同类工具具有很大的发展潜力，开源发布也是这类工具成功的最佳途径。

[Pezzo｜开源 LLMOps 平台](https://github.com/pezzolabs/pezzo)

---

### Zed｜代码编辑器登陆 Linux

之前备受关注的代码编辑器 **Zed** 正式登陆 Linux 平台了。这是一款用 Rust 打造的现代开源代码编辑器，拥有 GPU 加速渲染引擎，目标是保持轻量化和高性能。该项目之前已经在 macOS 平台上获得了不少早期用户，而在 Linux 上运行也一直是呼声最高的需求。如今在社区的一同努力下，该功能终于完成。Z 团队特别感谢了社区的贡献，有 133 位贡献者提交了 447 个 PR，大大加快了 Linux 版本的开发进度。

[Zed｜代码编辑器登陆 Linux](https://zed.dev/blog/zed-on-linux)

---

以上就是本期科技周报的全部内容，谢谢您的收看。如果内容对您有帮助，请一键三连支持我们。更多详细信息和项目链接，请访问本期 [Hacker Newsletter](https://www.hackernewsletter.com)。

---

## 视频信息

**视频标题:** 科技周报｜便捷日志查看工具；AMD GPU 运行 CUDA；开源 LLMOps 平台

**视频地址:**  
[Bilibili](https://www.bilibili.com/video/BV1Wz421B7cB)

---

**本期项目链接：**

- [Logdy](https://logdy.dev/)
- [SENDUNE](https://github.com/SendWithSES/Drag-and-Drop-Email-Designer)
- [Motion Canvas](https://motioncanvas.io/)
- [SCALE](https://docs.scale-lang.com/)
- [Pezzo](https://github.com/pezzolabs/pezzo)
- [Zed](https://zed.dev/blog/zed-on-linux)
