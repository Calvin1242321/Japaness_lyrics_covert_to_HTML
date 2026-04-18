# main.py

from fugashi import Tagger
from align import align

tagger = Tagger()


def convert(text):
    lines = text.split("\n")
    output_lines = []

    for line in lines:
        tokens = tagger(line)
        new_line = ""

        for token in tokens:
            surface = token.surface

            reading = token.feature.kana
            if not reading or reading == "*":
                new_line += surface
            else:
                new_line += align(surface, reading)

        output_lines.append(new_line)

    return "<br>\n".join(output_lines)


if __name__ == "__main__":
    print("貼上歌詞（輸入 END 結束）：\n")

    lines = []
    while True:
        try:
            line = input()
            if line.strip() == "END":
                break
            lines.append(line)
        except EOFError:
            break

    text = "\n".join(lines)
    result = convert(text)

    print("\n=== 結果 ===\n")
    print(result)