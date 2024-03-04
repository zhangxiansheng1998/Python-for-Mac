from setuptools import setup

APP = ['upload_load_test_generator.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['tkinter'],
    'plist': {
        'CFBundleShortVersionString': '0.1.0',
        'CFBundleName': 'upload_load_test_generator',
    },
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)