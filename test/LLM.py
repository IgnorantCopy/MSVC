# For prerequisites running the following sample, visit https://help.aliyun.com/document_detail/611472.html
from http import HTTPStatus
import dashscope

dashscope.api_key = 'sk-5a913fba27ec4346a28d8cd0c5bde8da'


def call_with_messages(question):
    messages = [{'role': 'system', 'content': 'You are a professional musician.'},
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
    print(call_with_messages("如何做西红柿炒鸡蛋"))
