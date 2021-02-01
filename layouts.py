# coding:utf-8

import PySimpleGUI as sg
from pathlib import Path

sg.theme('DarkBlue2')

path_home = str(Path.home())

layout = [
        [sg.Text('会場JSON出力ツール', font=('Any', 17))],
        [sg.Text('会場CSV'),
        sg.InputText('', key='-file_csv-',enable_events=True),
        sg.FileBrowse('読み込み', target='-file_csv-',file_types=[('CSV ファイル', '*.csv')],
                            initial_folder=rf"{path_home}\Desktop")],
        [sg.Submit("実行")]
    ]