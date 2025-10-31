![banner](./assets/banner.png)

![release](https://img.shields.io/github/v/release/rabbit-time/rascal-modpack?logo=github&color=22272E)
![issues](https://img.shields.io/github/issues-raw/rabbit-time/rascal-modpack?style=flat&label=issues&color=22272E&logo=github)
![license](https://img.shields.io/github/license/rabbit-time/rascal-modpack?style=flat)
![mods](https://img.shields.io/github/directory-file-count/rabbit-time/rascal-modpack/mods?type=file&style=flat&label=mods)
![fabric-loader](https://img.shields.io/badge/fabric--loader-0.17.3-blue?style=flat)

Rascal modpack is a vanilla-plus pack aiming to enhance the Minecraft experience. It was designed with gameplay, balance, quality of life, and performance in mind. It was crafted with passion and I hope that you enjoy it.

## Features
Here are some of the major features included in this modpack:
- A new immersive experience in a world that feels alive
- Greatly enhanced visuals - even without the shaders
- Overhauled sound system
- Terralith world generation
- Overhauled existing structures
- Plenty of new structures, wildlife, and biomes
- Backpacks
- Waystones
- Vanilla-friendly world maps
- Interactive item physics
- Expanded farming and cooking
- Wide selection of new furniture and building blocks
- Numerous quality of life features

An in-game guidebook is provided to help players learn about all the features.

A full list of mods are credited [here](./docs/mod_list.md) and [here](./docs/resourcepack_list.md) for resource packs.

## Installation
[![modrinth](https://img.shields.io/modrinth/game-versions/F9jhv9Km?color=00AF5C&label=latest&logo=modrinth&style=flat&last=true)](https://modrinth.com/modpack/rascal-modpack)

### Modrinth App
*If you don't know what you're doing, use this method.*
1. Install the latest version of the [Modrinth App](https://modrinth.com/app).
2. Navigate to "Discover content" on the left-hand bar and search for "Rascal Modpack" and install it.
3. In your instance settings, manually set your memory allocation to at least 8 GiB. You can also set a default for all instances in your general Modrinth settings, if you don't want to do this every time.
4. Launch the game. Shaders will be disabled by default but can be accessed with `CTRL+O` while in a world.

### Other launchers
1. Using another launcher that supports Modrinth packfiles (`.mrpack`). If you're using a launcher doesn't support `.mrpack` files, you must manually [build](./README.md#build-guide) the packfiles.
2. Download the latest release of the packfiles from [Modrinth](https://modrinth.com/modpack/rascal-modpack). Then, create a new Minecraft instance in your launcher by importing the packfiles.
3. In your instance settings, manually set your memory allocation to at least 8 GiB.
4. Launch the game. Shaders will be disabled by default but can be accessed with `CTRL+O` while in a world.

### Build guide
A platform independent build guide for those looking to run a server instance.

1. Clone Rascal Modpack on your system and swap to the stable branch: `git checkout stable`.
2. Install [packwiz](https://github.com/packwiz/packwiz) following their installation guide.
3. Run `packwiz mr export` to generate Modrinth packfiles (`.mrpack`).
4. Alternatively, run `packwiz cf export` to generate packfiles with `.jar` files.
5. Drop the contents of the `overrides` folder into your instance.

## Support
Please refer to the [FAQ](./docs/faq.md) for help. For suggestions and bug reports, please submit an [issue](https://github.com/rabbit-time/rascal-modpack/issues).
