# -*- mode: python -*-

block_cipher = None


a = Analysis(['exe.py'],
             pathex=['C:\\Users\\s-nakai\\venues_json_generator'],
             binaries=[],
             datas=[
                ('constant.py','.'),
                ('convert.py','.'),
                ('layouts.py','.'),
                ('util.py','.'),
                ('venues_json.ico', '.')
             ],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='app',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False,
          icon="venues_json.ico")
