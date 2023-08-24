# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['C:\\Users\\polla\\OneDrive\\Documentos\\orochi/run/main.py'],
    pathex=[],
    binaries=[],
    datas=[('C:\\Users\\polla\\OneDrive\\Documentos\\orochi/orochi', 'orochi'), ('C:\\Users\\polla\\OneDrive\\Documentos\\orochi/run/src', 'src'), ('C:\\Users\\polla\\OneDrive\\Documentos\\orochi/run/scripts', 'scripts')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='C:/Users/polla/OneDrive/Documentos/Audacity/installer/src/icon.ico',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
