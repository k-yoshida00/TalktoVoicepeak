import os
import subprocess
import winsound


def playVoicePeak(response , narrator = "Koharu Rikka", hightension=80, livid=10, lamenting=10, despising=10, narration=10):
    
    """
    任意のテキストをVOICEPEAKのナレーターに読み上げさせる関数
    script: 読み上げるテキスト（文字列）
    narrator: ナレーターの名前（文字列）
    happy: 嬉しさの度合い
    sad: 悲しさの度合い
    angry: 怒りの度合い
    fun: 楽しさの度合い
    """
    print('\r音声変換中...',  end='')

    # voicepeak.exeのパス設定
    exepath = "YOUR-VOICEPEAK-PATH"
    # wav出力先
    outpath = "YOUR-WAV-OUTPUT-PATH"

    # 引数を作成
    args = [
        exepath,
        "-s", response,
        "-n", narrator,
        "-o", outpath,
        "-e", f"hightension={hightension},livid={livid},lamenting={lamenting},despising={despising},narration={narration}"
    ]

    # プロセスを実行
    process = subprocess.Popen(args)

    # プロセスが終了するまで待機
    process.communicate()
    
    # 音声を再生
    winsound.PlaySound(outpath, winsound.SND_FILENAME)

    # wavファイルを削除
    os.remove(outpath)
