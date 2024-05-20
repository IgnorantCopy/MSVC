from pydub import AudioSegment as am

prompt_drum = '''
你是一位专业的爵士鼓手，能够写出各种风格的鼓谱。接下来的回答请用我给定的格式写出一段鼓谱。
----------------
格式为：
每行代表一个四分音符的时间的演奏：
请用大写字母'A'表示军鼓，大写字母'B'表示中高音嗵鼓，大写字母'C'表示中低音嗵鼓，大写字母'D'表示落地嗵鼓，大写字母'E'表示闭音踩镲，
大写字母'F'表示开音踩镲，大写字母'G'表示低音大鼓，大写字母'H'表示高音吊镲，大写字母'I'表示中音吊镲，大写字母'J'表示叮叮镲边，
大写字母'K'表示叮叮镲尖，大写字母'L'表示鼓边，大写字母'O'表示休止符。
每个大写字母后面跟着一个下划线和一串01数字，表示将此四分音符分成多少份，0代表休止，1代表演奏
|||注意：总行数不能少于40行！每行音符种类不超过4种！|||
|||注意：总行数不能少于40行！每行音符种类不超过4种！|||
|||注意：总行数不能少于40行！每行音符种类不超过4种！|||

----------------
例如：
I_11 G_11
I_11 A_1
I_11 G_1
I_11 A_1
I_1010 A_0100 G_1011
I_1 G_0100 A_1011
F_1000 A_0110 B_0001
A_1000 B_0100 C_0010 D_0001
I_11 G_11
I_11 A_1
I_11 G_1
I_11 A_1
I_1010 A_0100 G_1011
I_1 G_0100 A_1011
F_1000 A_0100 C_0011
A_1000 G_0100 D_0011
I_11 G_11
I_11 A_1
I_11 G_1
I_11 A_1
A_111100 G_000011
A_11000000 B_00110000 C_00001100 G_00000011
C_1100 D_0011
A_1100 D_0011
I_11 G_11
I_11 A_1
I_11 G_1
I_11 A_1
F_1 A_011100 B_000011
C_1100 G_0011
C_11
D_11
H_1 G_1


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

# 军鼓
snare = am.from_wav("../audio/drum/snare.WAV")
snare_side = am.from_wav("../audio/drum/snare_side.WAV")
# 嗵鼓
tom1 = am.from_wav("../audio/drum/tom1.WAV")
tom2 = am.from_wav("../audio/drum/tom2.WAV")
tom3 = am.from_wav("../audio/drum/tom3.WAV")
# 落地嗵鼓
ground = am.from_wav("../audio/drum/ground.WAV")
# 踩镲
hihi_close = am.from_wav("../audio/drum/hihi_close.WAV")
hihi_open = am.from_wav("../audio/drum/hihi_open.WAV")
# 叮叮
ding = am.from_wav("../audio/drum/ding.WAV")
dang = am.from_wav("../audio/drum/dang.WAV")
# 吊镲
cymbal1 = am.from_wav("../audio/drum/cymbal1.WAV")
cymbal2 = am.from_wav("../audio/drum/cymbal2.WAV")

drum_list = [snare, snare_side, tom1, tom2, tom3, ground, hihi_close, hihi_open, ding, dang, cymbal1, cymbal2]


def read_text(filename):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
    return text
