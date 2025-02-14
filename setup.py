from setuptools import setup

APP = ['hello_app.py']
OPTIONS = {
    'argv_emulation': False,
    'packages': ['webview'],
    'includes': [
        'gc',
        'threading',
        'time',
        'os',
        'tkinter',
        'tkinter.filedialog',
        'tkinter.ttk',
        'webview.platforms.cocoa'
    ],
    'frameworks': [
        '/Library/Frameworks/Tk.framework',
        '/System/Library/Frameworks/WebKit.framework'
    ],
    'resources': [],
    'plist': {
        'CFBundleName': 'Quiz Kiosk',
        'CFBundleDisplayName': 'Quiz Kiosk',
        'CFBundleIdentifier': 'com.quizkiosk.app',
        'CFBundleVersion': '1.0.0',
        'CFBundleShortVersionString': '1.0.0',
        'LSMinimumSystemVersion': '10.10',
        'NSHighResolutionCapable': True,
        'LSUIElement': False,
        'NSRequiresAquaSystemAppearance': False,
    }
}

setup(
    app=APP,
    name='Quiz Kiosk',
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)