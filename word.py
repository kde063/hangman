

api_key = "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"

# from openai import OpenAI

# client = OpenAI(api_key=api_key)

# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#     {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
#   ]
# )

# print(completion.choices[0].message.content)

# import openai #이거 된듯 #할당량초과

# OpenAI API 키 설정
# openai.api_key = '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'

# # GPT-3에 텍스트 전달
# response = openai.Completion.create(
#     engine="gpt-3.5-turbo",  # 엔진 선택
#     prompt="hi",
#     max_tokens=150  # 최대 토큰 수 설정
# )

# # GPT-3의 응답 출력
# print(response.choices[0].text.strip())

import openai #요놈아도 할당량 초과인듯

openai.api_key = "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"

messages = []

while True:
    user_content = input("user : ")
    messages.append({"role" : "user", "content" : f"{user_content}"})

    completion = openai.ChatCompletion.create(model = "gpt-3.5-turbo", message = messages)

    assistant_content = completion.choices[0].message["content"].strip()

    messages.append({"role": "assistant", "content": f"{assistant_content}"})

    print(f"GPT : {assistant_content}")