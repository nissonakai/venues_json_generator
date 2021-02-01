# coding:utf-8
from __future__ import unicode_literals

import csv
import json

from util import read_csv
from constant import prefectures

def convert(path_name, path_home):
    data = read_csv(path_name)
    next(data)
    next(data)
    next(data)
    data_arr = [{"prefecture": d[0], "venue": d[1], "adress": d[2], "url": d[-1]} for d in data if d[0] in prefectures]
    target_arr = []
    for d in data_arr:
        if d not in target_arr:
            target_arr.append(d)
    text = json.dumps(target_arr, sort_keys=True, ensure_ascii=False, indent=2)
    with open(f"{path_home}/Desktop/area_venue.json", "wb") as fh:
        fh.write(text.encode("utf-8"))
    return [
        f"出力会場件数：{len(target_arr)}件",
        "デスクトップにarea_venue.jsonを出力しました。"
        ]
