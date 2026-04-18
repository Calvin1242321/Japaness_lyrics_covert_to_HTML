# align.py

import re


def is_kanji(ch):
    return '\u4e00' <= ch <= '\u9fff'


def to_hiragana(s):
    return ''.join(
        chr(ord(c) - 0x60) if '\u30A1' <= c <= '\u30F6' else c
        for c in s
    )


def align(surface, reading):
    segments = []
    i = 0
    while i < len(surface):
        if is_kanji(surface[i]):
            j = i
            while j < len(surface) and is_kanji(surface[j]):
                j += 1
            segments.append(('kanji', surface[i:j]))
            i = j
        else:
            j = i
            while j < len(surface) and not is_kanji(surface[j]):
                j += 1
            segments.append(('kana', surface[i:j]))
            i = j

    reading_h = to_hiragana(reading)
    result = ""
    pos = 0 

    for seg_idx, (kind, text) in enumerate(segments):
        if kind == 'kana':
            result += text
            text_h = to_hiragana(text)
            idx = reading_h.find(text_h, pos)
            if idx != -1:
                pos = idx + len(text_h)
            else:
                pos += len(text)
        else:
            next_kana = None
            for k in range(seg_idx + 1, len(segments)):
                if segments[k][0] == 'kana':
                    next_kana = to_hiragana(segments[k][1])
                    break

            if next_kana is None:
                kanji_reading = reading[pos:]
                pos = len(reading)
            else:
                anchor_idx = reading_h.find(next_kana, pos)
                if anchor_idx == -1:
                    kanji_reading = reading[pos:]
                    pos = len(reading)
                else:
                    kanji_reading = reading[pos:anchor_idx]
                    pos = anchor_idx

            kanji_list = list(text)
            n = len(kanji_list)
            r_len = len(kanji_reading)

            for k_idx, ch in enumerate(kanji_list):
                start = round(r_len * k_idx / n)
                end = round(r_len * (k_idx + 1) / n)
                rt = kanji_reading[start:end]
                result += f"<ruby>{ch}<rt>{to_hiragana(rt)}</rt></ruby>"

    return result