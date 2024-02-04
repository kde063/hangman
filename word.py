

# api_key = ""

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

# import openai

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


##완성
# import openai

# openai.api_key = "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"

# messages = []

# while True:
#     user_content = input("user : ")
#     messages.append({"role" : "user", "content" : f"{user_content}"})

#     completion = openai.ChatCompletion.create(model = "gpt-3.5-turbo", messages = messages)

#     assistant_content = completion.choices[0].message["content"].strip()

#     messages.append({"role": "assistant", "content": f"{assistant_content}"})

#     print(f"GPT : {assistant_content}")


import openai

openai.api_key = "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"

messages = []

while True:
    theme = input("테마를 입력해주세요\n")
    user_content = theme + "을 테마로 하는 영단어 10개만 알려줘 그리고 번호와 단어는 빼줘"
    messages.append({"role" : "user", "content" : f"{user_content}"})

    completion = openai.ChatCompletion.create(model = "gpt-3.5-turbo", messages = messages)

    assistant_content = completion.choices[0].message["content"].strip()

    messages.append({"role": "assistant", "content": f"{assistant_content}"})

    print(f"GPT : {assistant_content}")
    print(''.join(assistant_content))
    print([i.split()[1] for i in ''.join(assistant_content).split('\n')])
