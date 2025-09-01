![banner](./assets/banner.png)

![release](https://img.shields.io/github/v/release/rabbit-time/rascal-modpack?logo=github&color=22272E)
![issues](https://img.shields.io/github/issues-raw/rabbit-time/rascal-modpack?style=flat&label=issues&color=22272E&logo=github)
![license](https://img.shields.io/github/license/rabbit-time/rascal-modpack?style=flat)
![mods](https://img.shields.io/github/directory-file-count/rabbit-time/rascal-modpack/mods?type=file&style=flat&label=mods)
![fabric-loader](https://img.shields.io/badge/fabric--loader-0.17.2-blue?style=flat)

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
- Vanity armor slots
- Vanilla-friendly minimaps
- Interactive item physics
- Expanded farming and cooking
- Wide selection of new furniture and building blocks
- Experience storage (at a cost)
- Numerous quality of life features

A full list of mods are credited [here](./docs/mod_list.md) and [here](./docs/resourcepack_list.md) for resource packs.

## Guide
A written [guide](./docs/guide.md) is available to help players orient themselves with basic gameplay mechanics and explore the best features in this modpack. It is **highly recommended** to utilize the guide.

## Installation
[![modrinth](https://img.shields.io/modrinth/game-versions/F9jhv9Km?color=00AF5C&label=latest&logo=modrinth&style=flat&last=true)](https://modrinth.com/modpack/rascal-modpack)

1. Install any Minecraft launcher that supports Modrinth packfiles (`.mrpack`). If you're using a launcher doesn't support `.mrpack` files, you must manually [build](./README.md#build-guide) the packfiles. If you don't know what you're doing, use the [Modrinth App](https://modrinth.com/app).
2. Download the latest release of the packfiles. Then, create a new Minecraft instance in your launcher by importing the packfiles.
3. Set the Java installation to Java 21. For the Modrinth App, navigate through `Settings > Java Installations > Java 21 Location` and copy the path there. If there's no installation, click *Install recommended* and a path will be generated when it's done. Navigate to your instance settings and find *Java installation* and paste the path there.
4. In your instance settings, manually set your Memory allocation to at least 8 GiB.
5. Launch the game.
6. It is highly recommended to disable shaders and Distant Horizons if you're using less powerful hardware.

## Build guide
A platform independent build guide for those looking to run a server instance.

1. Clone Rascal Modpack on your system and swap to the stable branch: `git checkout stable`.
2. Install [packwiz](https://github.com/packwiz/packwiz) following their installation guide.
3. Run `packwiz mr export` to generate Modrinth packfiles (`.mrpack`).
4. Alternatively, run `packwiz cf export` to generate packfiles with `.jar` files.
5. Drop the override files into your instance.

## Support
Please refer to the [FAQ](./docs/faq.md) for help. For suggestions and bug reports, please submit an [issue](https://github.com/rabbit-time/rascal-modpack/issues).
