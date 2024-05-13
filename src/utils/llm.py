# For prerequisites running the following sample, visit https://help.aliyun.com/document_detail/611472.html
from http import HTTPStatus
import dashscope
import common

dashscope.api_key = 'sk-5a913fba27ec4346a28d8cd0c5bde8da'


def call_with_messages(question):
    messages = [{'role': 'system', 'content': common.prompt_drum},
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


def text_to_drum(text):
    lines = text.split('\n')
    signature = lines[0]
    speed = lines[1]
    song = []
    for i in range(2, len(lines)):
        line = lines[i]
        notes = line.split(' ')
        for note in notes:
            if note[0] == 'A':
                song.append(common.snare)
            elif note[0] == 'B':
                song.append(common.tom1)
            elif note[0] == 'C':
                song.append(common.tom2)
            elif note[0] == 'D':
                song.append(common.tom3)

    print(lines)


if __name__ == '__main__':
    text_to_drum(call_with_messages("请写一个摇滚风格的鼓谱。"))