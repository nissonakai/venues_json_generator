# coding:utf-8

import csv
from pathlib import Path

def read_csv(csv_data, encode="cp932"):
    data = open(csv_data, "r", encoding=encode, newline="")
    return csv.reader(
        data,
        delimiter=",",
        doublequote=True,
        lineterminator="\n",
        quotechar='"',
        skipinitialspace=True,
    )
