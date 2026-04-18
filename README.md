# lyrics-furigana

A CLI tool that automatically annotates Japanese lyrics with furigana using `<ruby>` / `<rt>` HTML tags.

```
食べる　→　<ruby>食</ruby><rt>たべ</rt></ruby>る
```

## Requirements

- Python 3.8+
- [fugashi](https://github.com/polm/fugashi) + a MeCab dictionary

## Installation

```bash
pip install fugashi unidic-lite
```

## Usage

Run the script and paste your lyrics, then type `END` on a new line to finish:

```bash
python main.py
```

```
貼上歌詞（輸入 END 結束）：

夜に駆ける
END

=== 結果 ===

<ruby>夜</ruby><rt>よる</rt></ruby>に<ruby>駆</ruby><rt>か</rt></ruby>ける
```

The output is ready to paste into any HTML file — wrap it in a `<p>` tag and the browser will render the furigana automatically.

## How it works

Each token from MeCab includes a surface form and a kana reading. The `align()` function uses the kana characters within the surface as anchors to correctly slice the reading onto each kanji, rather than splitting it evenly.
