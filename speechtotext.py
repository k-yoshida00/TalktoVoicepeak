import azure.cognitiveservices.speech as speechsdk

# configの設定
speech_key = "YOUR-SPEECH-KEY"
service_region = "YOUR-RESION"
language = "ja-JP"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region, speech_recognition_language=language)

# recognizerの設定
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

# 録音する
def recordvoice():
    print('\r録音中...',  end='')

    result = speech_recognizer.recognize_once()

    # 結果の確認
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        return result.text
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("音声が録音されませんでした: {}".format(result.no_match_details))
        return "exit"
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("録音がキャンセルされました: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
            return "exit"
