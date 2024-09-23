from langchain_core.messages import HumanMessage, SystemMessage
from langchain_aws.chat_models import ChatBedrock

def chat_bedrock(message):
    chat = ChatBedrock(
        model_id = "anthropic.claude-3-5-sonnet-20240620-v1:0",
        model_kwargs={"temperature":1.0},
        region_name="us-east-1",
    )

    messages = [
        SystemMessage("ここにはシステム用のメッセージが入ります。"),
        HumanMessage(message)
    ]

    content=""

    try:
        response = chat.invoke(messages)
        content = response.content
    except Exception as e:
        print(e)

    return content

if __name__ == "__main__":
    message = input("AIに聞きたいことを入力してください！\n")
    result = chat_bedrock(message)
    print(result)
