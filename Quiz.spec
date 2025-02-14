# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['hello_app.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['webview.platforms.cocoa'],
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
    [],
    exclude_binaries=True,
    name='Quiz Kiosk',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Quiz Kiosk',
)

app = BUNDLE(
    coll,
    name='Quiz Kiosk.app',
    icon='QuizIcon.icns',
    bundle_identifier='com.quizkiosk.app',
    info_plist={
        'NSHighResolutionCapable': 'True',
        'LSUIElement': 'False',
        'CFBundleShortVersionString': '1.1.0',  # Updated version
        'CFBundleVersion': '1.1.0',  # Updated version
    },
)