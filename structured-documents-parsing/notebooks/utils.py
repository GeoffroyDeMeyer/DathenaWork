import re
import copy
from typing import Generator


def split_str2xml(text: str) -> Generator[str, None, None]:
    """
    Split the output of Tika into valid XML strings
    :param text:
        content produced by Apache Tika
    :return:
        an iterator over valid xml string that can be parsed.
    """
    regex = re.compile(r"<html.*?>.*?</html>", re.DOTALL)
    matchs = regex.finditer(text)
    for m in matchs:
        yield m.group()


def json2xml(json_obj: dict) -> str:
    json_obj = copy.deepcopy(json_obj)
    def flat_keys(dic):
        s = ''
        for key, elem in dic.items():
            s+=f'{key}={elem} '
        return s
    xml = '<table>'
    for row in json_obj['data']:
        xml+='<tr>'
        for elem in row:
            text = elem.pop('text')
            xml+=f'<td {flat_keys(elem)}>'
            xml+=text
            xml+='</td>'
        xml+='</tr>'
    xml+='</table>'
    return xml
