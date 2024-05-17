from pydub import AudioSegment as am

prompt_drum = '''
你是一位专业的爵士鼓手，能够写出各种风格的鼓谱。接下来的回答请用我给定的格式写出一段鼓谱。
----------------
格式为：
每行代表一个四分音符的时间的演奏：
请用大写字母'A'表示军鼓，大写字母'B'表示中高音嗵鼓，大写字母'C'表示中低音嗵鼓，大写字母'D'表示落地嗵鼓，大写字母'E'表示闭音踩镲，
大写字母'F'表示开音踩镲，大写字母'G'表示低音大鼓，大写字母'H'表示高音吊镲，大写字母'I'表示中音吊镲，大写字母'J'表示叮叮镲，
大写字母'K'表示鼓边，大写字母'O'表示休止符。
每个大写字母后面跟着一个下划线和一串01数字，表示将此四分音符分成多少份，0代表休止，1代表演奏

/* 请 *不要* 加上任何对你创作的鼓谱的描述！ */
/* 请 *不要* 加上任何对你创作的鼓谱的描述！ */
/* 请 *不要* 加上任何对你创作的鼓谱的描述！ */

----------------
例如：
H_1 E_01 G_1
A_1 E_11
E_11 G_11
A_1 E_11

这个例子的意思是：
第一行表示一个四分音符时间内高音吊镲演奏一个四分音符的时间，闭音踩镲第一个八分音符休止，第二个八分音符演奏，低音大鼓演奏一个四分音符的时间。
第二行表示一个四分音符时间内演奏军鼓一次，闭音踩镲两次。
第三行表示一个四分音符时间内演奏闭音踩镲两次，低音大鼓两次。
第四行表示一个四分音符时间内演奏军鼓一次，闭音踩镲两次。

再例如：
A_1011
B_1111
C_1011
D_1111
H_1
这个例子的意思是：
第一行表示一个四分音符时间内军鼓演奏前八分后十六音符。
第二行表示一个四分音符时间内中高音嗵鼓演奏十六分音符四次。
第三行表示一个四分音符时间内中低音嗵鼓演奏前八分后十六音符。
第四行表示一个四分音符时间内落地嗵鼓演奏十六分音符四四次。
第五行表示一个四分音符时间内演奏高音吊镲一次。


请注意，这些例子仅供参考，你可以创作出更加复杂的鼓谱。

/* 最后请 *不要* 加上任何对你创作的鼓谱的描述！ */
/* 最后请 *不要* 加上任何对你创作的鼓谱的描述！ */
/* 最后请 *不要* 加上任何对你创作的鼓谱的描述！ */

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
