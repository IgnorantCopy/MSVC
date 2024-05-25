from pydub import AudioSegment as am
import re
from http import HTTPStatus
import dashscope

dashscope.api_key = 'sk-5a913fba27ec4346a28d8cd0c5bde8da'


prompt_guitar = '''
你是一位专业的吉他手，能够弹出各种风格的吉他和弦伴奏。接下来的回答请用我给定的格式写出一段吉他和弦谱。
注意，你写的曲子必须是C调的。
----------------
格式为：
每行代表一个小节的和弦，由两部分组成：
第一部分代表和弦，表示为 '字母+类型' 的形式，字母代表音高，类型代表和弦类型。
如：C7代表C的大七和弦，F代表F的大三和弦，Am代表A小三和弦，Em7代表E的小七和弦，Asus2代表A的挂二和弦，Fsus4代表F的挂四和弦。
第二部分仅需标注小节编号。
例如：
C 1
C7 2
Fsus2 3
G 4
C 5
Em 6
Am 7
G 8

请注意，这些例子仅供参考，你可以创作出更加复杂、长度更长的谱。

----------------
接下来，请准备开始创作吉他谱：

'''

prompt_piano = '''
你是一位专业的键盘手，能够弹出各种风格的钢琴演奏片段。接下来的回答请用我给定的格式写出一段钢琴谱。
注意，你写的曲子只能是C调的。

---注意，你只能使用C0-B2的音高。
---注意，你只能使用C0-B2的音高。
---注意，你只能使用C0-B2的音高。

----------------
格式为：
每行代表一个四分音符的时长，由三部分组成：
第一部分代表这个音符的音高，类似于简谱，由数字1~7代表一个八度内的音，后面加i代表升高一个八度。
如：1i代表高音C，5代表中音G，7b代表低音B。
第二部分代表这个音符出现在整首曲子的第几拍，从1开始。
第三部分代表音符长度，'s'代表短音符，'ss'代表跳音（即更短的音符），'l'代表长音符，'ll'代表全音符。
在创作时，注意两个音符之间音高差距尽量平缓。

例如：

5b 1 l
1 3 l
4 5 ll
1 8 s
4b 9 s
3b 10 s
2b 11 s
1b 12 s
2b 13 s
3b 14 s
1 15 l
5 17 l
1i 19 l
4i 21 ll
1i 24 s
4i 25 s
3i 26 s
2i 27 s
1i 28 s
2 29 s
3 30 s
5 31 s
3 32 s
1i 33 ll

----------------
接下来，请准备开始创作钢琴谱：
'''

prompt_drum = '''
你是一位专业的爵士鼓手，能够写出各种风格的鼓谱。接下来的回答请用我给定的格式写出一段鼓谱。
----------------
格式为：
每行开头为行号，从零开始编号，每行代表一个四分音符的时间的演奏：
请用大写字母'A'表示军鼓，大写字母'B'表示中高音嗵鼓，大写字母'C'表示中低音嗵鼓，大写字母'D'表示落地嗵鼓，大写字母'E'表示闭音踩镲，
大写字母'F'表示开音踩镲，大写字母'G'表示低音大鼓，大写字母'H'表示高音吊镲，大写字母'I'表示中音吊镲，大写字母'J'表示叮叮镲边，
大写字母'K'表示叮叮镲尖，大写字母'L'表示鼓边，大写字母'O'表示休止符。
每个大写字母后面跟着一个下划线和一串01数字，表示将此四分音符分成多少份，0代表休止，1代表演奏
|||注意：总行数不能少于40行！每行音符种类不超过4种！|||
|||注意：总行数不能少于40行！每行音符种类不超过4种！|||
|||注意：总行数不能少于40行！每行音符种类不超过4种！|||

----------------
例如：
0 I_11 G_11
1 I_11 A_1
2 I_11 G_1
3 I_11 A_1
4 I_1010 A_0100 G_1011
5 I_1 G_0100 A_1011
6 F_1000 A_0110 B_0001
7 A_1000 B_0100 C_0010 D_0001
8 I_11 G_11
9 I_11 A_1
10 I_11 G_1
11 I_11 A_1
12 I_1010 A_0100 G_1011
13 I_1 G_0100 A_1011
14 F_1000 A_0100 C_0011
15 A_1000 G_0100 D_0011
16 I_11 G_11
17 I_11 A_1
18 I_11 G_1
19 I_11 A_1
20 A_111100 G_000011
21 A_11000000 B_00110000 C_00001100 G_00000011
22 C_1100 D_0011
23 A_1100 D_0011
24 I_11 G_11
25 I_11 A_1
26 I_11 G_1
27 I_11 A_1
28 F_1 A_011100 B_000011
29 C_1100 G_0011
30 C_11
31 D_11
32 H_1 G_1


请注意，这些例子仅供参考，你可以创作出更加复杂、长度更长的鼓谱。
请注意，这些例子仅供参考，你可以创作出更加复杂、长度更长的鼓谱。
请注意，这些例子仅供参考，你可以创作出更加复杂、长度更长的鼓谱。

----------------
接下来，请准备开始创作鼓谱：
'''

req = '''
接下来你必须按照我所说的格式输出乐谱。
第一行 “x/4” 的格式表示拍号，其中 x 为 3 或 4，例如：“3/4”
第二行为一个整数，表示一共的小节数 n 
第三行一个整数，表示速度（每分钟节拍数）。
接下来 n * x 行，每行一个数字表示音高。
如果你理解我的要求，请输出“不是”，反之输出“是”，并准备输出乐谱。
'''

prompt_lyrics = '''
你是一个专业的作词家，能够创作出各种风格的歌词。接下来的回答请用我给定的格式写出一首歌词。
----------------
Main
'主歌的内容'

Refrain
'合唱的内容'

Bridge
'过渡段的内容'

Ending
'尾声的内容'

----------------
例如：
Main
让我掉下眼泪的 不止昨夜的酒
让我依依不舍的 不止你的温柔
余路还要走多久 你攥着我的手
让我感到为难的 是挣扎的自由

Main
分别总是在九月 回忆是思念的愁
深秋嫩绿的垂柳 亲吻着我额头
在那座阴雨的小城里 我从未忘记你
成都带不走的 只有你

Refrain
和我在成都的街头走一走 喔…
直到所有的灯都熄灭了也不停留
你会挽着我的衣袖 我会把手揣进裤兜
走到玉林路的尽头 坐在小酒馆的门口


再例如：
Main
到了某个年纪你就会知道
一个人的日子真的难熬
渐渐开始尝到孤单的味道
时间在敲打着你的骄傲

Main
过了某个口你就会感到
彻夜陪你聊天的越来越少
厌倦了被寂寞追着跑
找个爱你的人就想托付终老

Bridge
能陪我走一程的人有多少
愿意走完一生的更是寥寥
是否刻骨铭心并没那么重要
只想在平淡中体会爱的味道

Refrain
终于等到你 还好我没放弃
幸福来得好不容易
才会让人更加珍惜
终于等到你 差点要错过你
在最好的年纪遇到你
才算没有辜负自己
终于等到你

'''

prompt_default = '你是一个音乐知识专家。'


def call_with_messages(prompt, question):
    messages = [{'role': 'system', 'content': prompt},
                {'role': 'user', 'content': question}]

    response = dashscope.Generation.call(
        dashscope.Generation.Models.qwen_turbo,
        messages=messages,
        result_format='message',  # set the result to be "message" format.
    )
    if response.status_code == HTTPStatus.OK:
        return response.output.choices[0].message.content
    else:
        return 'Request id: %s, Status code: %s, error code: %s, error message: %s' % (
            response.request_id, response.status_code,
            response.code, response.message
        )


def read_text(filename):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
    return text


def llm_to_text(question, instrument, max_len):
    prompt = ''
    rules = {
        'guitar': r'[a-zA-Z0-9]',
        'piano': r'^[1-7]',
        'drum': r'\d+',
        'lyrics': r''
    }
    if instrument == 'guitar':
        max_len /= 4
        prompt = prompt_guitar
    elif instrument == 'piano':
        prompt = prompt_piano
    elif instrument == 'drum':
        prompt = prompt_drum
    elif instrument == 'lyrics':
        filename = '../data/cache/text/{}_text.txt'.format(instrument)
        filename.write(call_with_messages(prompt_lyrics, question))
        return filename
    else:
        return 'Invalid instrument'
    origin = call_with_messages(prompt, question)
    text_list = origin.split('\n')
    result = []
    count = 0
    for line in text_list:
        test = line.split(' ')[0]
        if re.match(rules[instrument], test):
            result.append(line)
            count += 1
            if count >= max_len:
                break
    filename = '../data/cache/text/{}_text.txt'.format(instrument)
    with open(filename, 'w') as f:
        for line in result:
            f.write(line + '\n')
    return filename


def modify_text(filename, text_dict):
    with open(filename, "r", encoding="utf-8") as f:
        old_text = f.read()
    new_text = old_text.split('\n')
    for k, v in text_dict.items():
        if 0 <= k < len(new_text):
            new_text[k] = str(k) + ' ' + v
    result = ''
    with open(filename, "w", encoding="utf-8") as f:
        for line in new_text:
            f.write(line + '\n')
            result += line + '\n'
    return result
