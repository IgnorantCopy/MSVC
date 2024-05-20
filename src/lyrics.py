from utils import llm
from utils import common


if __name__ == '__main__':
    print(llm.call_with_messages(common.prompt_lyrics, "请写一段赞美友情的歌词"))