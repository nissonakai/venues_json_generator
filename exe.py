# coding:utf-8

import PySimpleGUI as sg
from pathlib import Path

from layouts import layout
from convert import convert

def execute():

    window = sg.Window('会場JSON出力ツール', layout, icon="./venues_json.ico")

    while True:
        event, values = window.read()

        if event == None:
            break

        elif event == "実行":
            try:
                path_home = str(Path.home())
                result = convert(values["-file_csv-"], path_home)
            except:
                sg.popup("エラーです。担当者に連絡してください。", icon="./venues_json.ico")
            else:
                sg.popup(*result, icon="./venues_json.ico")

execute()
