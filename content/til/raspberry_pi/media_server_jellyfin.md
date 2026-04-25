---
title: Media Server Project
date: 2024-01-01
draft: false
categories:
  - TIL
tags:
  - jellyfin
  - raspberrypi
  - mediaserver
  - til
---

## Goals

- Raspberry Pi
- External drive
- Load my music
- make it shareable
- Add Sweetie's music

- [This looks cool https://jellyfin.org/](https://jellyfin.org/)


## Tasks

- configure my Raspberry Pi 400.
- put a small mount of music on it.
- get/find an external drive, gather copy of music
- profit.


## Configuration

- follow instructions
   [This looks cool https://jellyfin.org/](https://jellyfin.org/)

- Jellyfin is now at http://192.168.1.34:8096/
(assuming my pi stays there. Not sure which dude.local doesn't resolve)

- copy a little bit of music for testing. Need an external drive, or USB drive. Or something.

- user jellyfin no password

Now it just works. Dang.

    scp -r Grateful\ Dead/* pi@192.168.1.34:Music


## The hard drive dance

- find drives
- look at them
- possibly reformat
- copy music
- put on the pi


## Ebooks and audiobooks

- https://github.com/jellyfin/jellyfin-plugin-bookshelf

- [installed dotnet](https://learn.microsoft.com/en-us/dotnet/iot/deployment)

But I get errors that I don't understand. No audio books for me yet.
