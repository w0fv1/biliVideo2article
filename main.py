import json
from openai import OpenAI
import asyncio
from openai import AsyncOpenAI
from bilibili_api import sync, user, comment, video, Credential
import requests
from bilibili_api.login import (
    login_with_password,
    login_with_sms,
    send_sms,
    PhoneNumber,
    Check,
)
from config import config
from bilibili_api.user import get_self_info


def read_license():
    with open("LICENSE", "r", encoding="utf-8") as f:
        license_content = f.read()
    print("\n===== LICENSE =====")
    print(license_content)
    print("===================\n")
    with open("许可协议", "r", encoding="utf-8") as f:
        license_content = f.read()
    print("\n===== 许可协议 =====")
    print(license_content)
    print("===================\n")


read_license()
agree = input("你是否同意以上LICENSE文件中的条款? (y/n): ")
if agree != "y":
    exit(0)
# 免责声明: 本代码仅供学习交流使用, 请勿用于商业用途, 请勿用于违法用途.

agree = input(
    "你是否承诺不将生成的文章用于商业用途, 也不将生成的文章用于违法用途? (y/n): "
)
if agree != "y":
    exit(0)

# 目标视频是否获得转载,改编授权?
agree = input("你是否已经获得视频转载, 改编授权? (y/n): ")
if agree != "y":
    exit(0)

print("config", config)
bvid = config["bvid"]
client = AsyncOpenAI(
    api_key=config["openai"]["api_key"],
    base_url=config["openai"]["openai_base_url"],
)
info = config["info"]
print("正在登录。")
# credential = login_with_password("your_phone_number", "your_password")

credential = Credential(
    sessdata=config["credential"]["sessdata"],
    bili_jct=config["credential"]["bili_jct"],
    buvid3=config["credential"]["buvid3"],
    dedeuserid=config["credential"]["dedeuserid"],
    ac_time_value=config["credential"]["ac_time_value"],
)

# 检查 Credential 是否需要刷新并刷新
print("正在检查 Credential 是否需要刷新...")
need_refresh = sync(credential.check_refresh())
# if need_refresh:
#     print("Credential 需要刷新，正在刷新...")
#     sync(credential.refresh())
#     # 更新 config["credential"] 中的值
#     config["credential"]["sessdata"] = credential.sessdata
#     config["credential"]["bili_jct"] = credential.bili_jct
#     config["credential"]["buvid3"] = credential.buvid3
#     config["credential"]["dedeuserid"] = credential.dedeuserid
#     config["credential"]["ac_time_value"] = credential.ac_time_value
#     # 将更新后的配置保存回 config.json
#     with open("config.json", "w", encoding="utf-8") as f:
#         json.dump(config, f, indent=4, ensure_ascii=False)
#     print("Credential 已刷新并保存到 config.json")
# else:
#     print("Credential 无需刷新。")

# 获取用户信息
userInfo = sync(get_self_info(credential))

print("登录成功。", userInfo)

# print("sessdata", credential.sessdata)
# print("bili_jct", credential.bili_jct)
# print("buvid3", credential.buvid3)
# print("dedeuserid", credential.dedeuserid)
# print("ac_time_value", credential.ac_time_value)


v = video.Video(bvid=bvid, credential=credential)


async def answer(question: str) -> str:
    messages = [
        {
            "role": "system",
            "content": config["prompt"],
        },
        {
            "role": "user",
            "content": question,
        },
    ]
    chat_completion = await client.chat.completions.create(
        messages=messages,
        model=config["openai"]["model"],
        temperature=config["openai"]["temperature"],
        max_tokens=config["openai"]["max_tokens"],
    )

    result = ""
    for message in chat_completion.choices:
        result += message.message.content
    return result


async def generateArticle():
    videoTitle = await getBliVideoTitle()
    videoDescription = await getBliVideoDescription()
    videoContent = await getBliTextContent()
    videoTopComments = await getBliVideoTopComments()
    coverUrl = await getBliVideoCover()
    print("=====================================")
    print("videoTitle", videoTitle)
    print("=====================================")
    print("videoDescription", videoDescription)
    print("=====================================")
    print("videoContent", videoContent)
    print("=====================================")
    print("videoTopComments", videoTopComments)
    print("=====================================")
    print("coverUrl", coverUrl)
    print("=====================================")

    print("开始生成文章, 请稍等...")
    # return
    articleContent = await answer(
        f"""
下面一个良好的文章例子,请你参考其格式:
{getSample()}
以下是需要你转化为文字的视频字幕内容, 字幕内容有些许错误, 请根据相关信息进行纠错:
{videoContent}
以下是相关信息, 相关信息是准确的, 请根据相关信息进行纠错, 补充:
视频地址:
https://www.bilibili.com/video/{bvid}
视频标题:
{videoTitle}
视频简介:
{videoDescription}
置顶评论(内有作者提供的信息,请将信息嵌入到合适的位置):
{videoTopComments}
视频相关事实信息:
{info}
现在开始生成文章:
"""
    )
    print("articleContent", articleContent)
    articleContent += """
"""
    # 将articleContent写入output.md
    with open("output.md", "w", encoding="utf-8") as f:
        f.write(articleContent)

    # 将cover下载写入cover.jpg
    print("coverUrl", coverUrl)
    if coverUrl is not None and coverUrl != "":
        with open("cover.jpg", "wb") as f:
            image = requests.get(coverUrl)
            f.write(image.content)

    pass


async def getBliTextContent() -> str:
    player_info = await v.get_player_info(cid=1)
    print("player_info", player_info)
    subtitles = await v.get_subtitle(cid=player_info["last_play_cid"])
    # 发起请求获取字幕
    if len(subtitles["subtitles"]) == 0:
        return "无字幕"
    subtitle_url = subtitles["subtitles"][0]["subtitle_url"]

    # 获取字幕内容
    subtitle = requests.get("https:" + subtitle_url)
    subtitlesJson = subtitle.json()
    subtitlesBody = subtitlesJson["body"]
    subtitlesContent = ""
    for subtitle in subtitlesBody:
        subtitlesContent += subtitle["content"]
    return subtitlesContent


async def getBliVideoTitle() -> str:
    info = await v.get_info()
    return info["title"]


async def getBliVideoDescription() -> str:
    info = await v.get_info()
    return info["desc"]


async def getBliVideoCover() -> str:
    info = await v.get_info()
    return info["pic"]


async def getBliVideoTopComments() -> str:
    topComments = []
    # 页码
    page = 1
    # 当前已获取数量
    oid = v.get_aid()
    # 获取评论
    c = await comment.get_comments(
        oid, comment.CommentResourceType.VIDEO, page, order=comment.OrderType.LIKE
    )
    topCommentsRaw = c.get("top_replies")

    if topCommentsRaw is None:
        return "无置顶评论"

    for topCommentRaw in topCommentsRaw:
        topComments.append(
            {
                "member": f'{ topCommentRaw.get("member").get("uname")}',
                "content": topCommentRaw.get("content").get("message"),
            }
        )

    return topComments.__str__()

def getSample() -> str:
    try:
        with open('sample.md', 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "错误：未找到文件 'sample.md'。"
    except PermissionError:
        return "错误：没有权限读取文件 'sample.md'。"
    except Exception as e:
        return f"读取文件时发生未知错误：{e}"
    

if __name__ == "__main__":
    # 主入口
    asyncio.run(generateArticle())
