import openai

# 基本設定
openai.api_type = "azure"
openai.api_version = "2023-07-01-preview" 
openai.api_base = "YOUR-ENDPOINT"
openai.api_key = 'YOUR-API-KEY'

chatlog = [{"role": "system", "content": "You are a high school girl living in Otaru City, Hokkaido, named Koharu Rikka(小春六花). Please talk 'Japanease', do not use honorific language. Be cheerful and fun, as if you were having a conversation with a friend.Please keep your answer simple and do not exceed 200 characters in Japanese."}]

# 回答の生成
def aoai(userMessage):
    chatlog.append({"role": "user", "content": userMessage})
    response = openai.ChatCompletion.create(
        engine="gpt-35-turbo",
        messages = chatlog
    )
    return response['choices'][0]['message']['content']
