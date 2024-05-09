# For prerequisites running the following sample, visit https://help.aliyun.com/document_detail/611472.html
from http import HTTPStatus
import dashscope

dashscope.api_key = 'sk-5a913fba27ec4346a28d8cd0c5bde8da'

prompt = 'You are a professional musician.'

'''
第一行 “x/4” 的格式表示拍号，其中 x 为 3 或 4，例如：“3/4”
第二行为一个整数，表示一共的拍子数 n 
第三行一个整数，表示速度（每分钟节拍数）。
第四行 **仅一个** 字母，表示乐谱的调号，大写表示大调，小写表示小调
接下来 n 行，每行表示 **一个** 音符。'''


prompt = '''
你是一个职业音乐家，
接下来你必须按照我所说的格式输出一份钢琴乐谱。
一共 16 行，每行表示 **一个** 音符。
音符的格式为： X_a ，其中 X 为CDEFBAG中的一个， a 为012中的一个，表示第 a 个八度的 X 音。
注意，你完整的输出中只能有 n + 4 行。

例如：


A_0
A_0
C_1
C_1
E_1
D_1
D_1
C_1
A_0
A_0
C_1
C_1
E_1
D_1
D_1
C_1


注意，你完整的输出中只能有 n + 4 行。
如果你理解我的要求，请输出“是”，反之输出“不是”，并准备输出乐谱。
'''
# 改音符表达方式

def call_with_messages(question):
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


if __name__ == '__main__':
    print(call_with_messages("请写一首哀伤的曲子"))
