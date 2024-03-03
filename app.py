import speechtotext
import answer_generate
import talk2voicepeak

# アシスタント名を設定
assistant = "小春六花"

while True:
    # ユーザーからの音声入力
    userMessage = speechtotext.recordvoice()

    # exitで終了、それ以外は入力を文字出力
    if userMessage == "exit":
        print("system exit.")  
        break
    else: print("\rUser:"+userMessage)

    print('\r回答出力中...',  end='')

    # answer_generateから回答文を取得
    response = answer_generate.aoai(userMessage)

    # 音声出力-voicepeak
    talk2voicepeak.playVoicePeak(response)

    # 文章でも出力
    print("\r"+assistant+":"+response)

    # 会話履歴に追加
    answer_generate.chatlog.append({"role": "assistant", "content": response})