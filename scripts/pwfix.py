# Fixes the "side" key in all .toml so that all mods are included in the packfiles
# To be ran from the project directory:  python ./scripts/pwfix.py
import os

import tomlkit

dir: str = './mods/'
files: list[str] = os.listdir(dir)

for filename in files:
    with open(dir+filename, 'r+', encoding="utf-8") as file:
        contents: tomlkit.TOMLDocument = tomlkit.parse(file.read())
        if contents['side'] == 'server':
            contents['side'] = 'both'
            file.seek(0)
            tomlkit.dump(contents, file)
            file.truncate()
            print(f'{filename} overwritten successfully.')
        else:
            print(f'{filename} is OK. Skipping file.')