# 解混淆
import re
import requests


def get_jsfile(file):
    """
    传入一个js文件
    :param file: 以字符串的形式传入
    :return:
    """
    unicode_part = file.replace(r'\u', '\\u').encode('utf-8').decode('unicode_escape')  # 解unicode部分的混淆
    hex_pattern = r'\\x([0-9a-fA-F]{2})'  # 解hex编码部分的混淆
    hex_matches = re.findall(hex_pattern, unicode_part)

    for match in hex_matches:
        hex_value = match
        ascii_char = chr(int(hex_value, 16))
        unicode_part = unicode_part.replace(f'\\x{hex_value}', ascii_char)

    return unicode_part
def upload_jsfile():
    url = 'https://spa13.scrape.center/js/main.js'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0",
    }
    res = requests.get(url, headers=headers)
    print(get_jsfile(res.text))

upload_jsfile()