# TinyBBS

A Meshtastic BBS (Bulletin Board System) module with games, mail, geocoding, and emergency survival guide — built as a [MeshForge](https://meshforge.org) project.

## Overview

TinyBBS adds a full-featured BBS to any Meshtastic node. Users interact via direct message using a menu-driven interface:

- **Bulletins** — multiple boards (General, Info, News, Urgent)
- **Private mail** — node-to-node messaging with subjects
- **QSL board** — radio contact logging with signal quality
- **Games** — Wordle, Vault-Tec word hacking, Chess by mail, Fallout Wasteland RPG
- **Survival guide** — emergency reference (water, fire, shelter, first aid, navigation…)
- **Reverse geocoding** — location lookups from GPS coordinates

## This is a MeshForge project

**Flash and data installation are handled automatically** by the [MeshForge web flasher](https://meshforge.org).

1. Open the MeshForge flasher
2. Select your device and the TinyBBS firmware build
3. Click **Flash** — the flasher writes the firmware and then automatically uploads the data files (Wordle dictionary, geocoding database, survival guide) to your device's external flash

No manual steps, no scripts to run, no serial terminal required.

## Supported devices

| Board | PlatformIO env | Platform |
|-------|---------------|----------|
| Lilygo T-Echo | `t-echo` | nRF52840 |
| Lilygo T-Echo Lite | `t-echo-lite` | nRF52840 |
| Lilygo T-Echo Plus | `t-echo-plus` | nRF52840 |
| RAK WisMesh Tap | `rak_wismeshtap` | nRF52840 |
| B&Q Nano G2 Ultra | `nano-g2-ultra` | nRF52840 |
| Heltec Mesh Node T114 | `heltec_mesh_node_t114` | nRF52840 |
| Lilygo T-Deck | `t-deck` | ESP32-S3 |

nRF52840 boards require an external QSPI flash chip to be present for the data files. ESP32 targets use the LittleFS partition.

## Building locally

```bash
pio run -e <target>   # e.g. pio run -e t-echo
```

PlatformIO will automatically:
1. Generate the data files (`data/fs/__ext__/bbs/kb/*.bin`) via `extra_scripts/gen_meshforge_data.py`
2. Compile firmware (post-flash uploads use Meshtastic XModem: Mesh Forge bundle `fs/`, or `meshtastic --upload` locally)

## Data files

Generated at build time under `data/fs/__ext__/bbs/kb/` (gitignored). GitHub Actions copies `data/fs/` into the firmware archive as top-level `fs/` for the Mesh Forge web flasher.

`meshforge.yaml` (if present) only carries Mesh Forge UI hints (`tags` / `targets`); it does not list data blobs.

CLI example (from this firmware directory, preserves paths under `data/fs/`):

```bash
meshtastic --port /dev/cu.usbmodem… --upload ./data/fs/ /
```

The in-browser Mesh Forge flasher uses the same XModem mechanism on the bundle’s `fs/` tree. On nRF52, `/__ext__/…` routes to external QSPI when present; on ESP32 it maps onto LittleFS.

| File | Description | Size |
|------|-------------|------|
| `wordle.bin` | 9,981-word validation dictionary | ~49 KB |
| `geo_us.bin` | US city geocoding index (GeoNames) | ~370 KB |
| `survival.bin` | Emergency survival guide | ~11 KB |

To regenerate manually:

```bash
python3 scripts/gen_wordle_packed.py
python3 scripts/gen_geo_packed.py
python3 scripts/gen_survival_packed.py
```

## Commands

Send any of these as a direct message to your TinyBBS node:

```
(empty or ?)    Main menu
B               Bulletin board menu
M               Mail menu
Q               QSL board
G               Games menu
S               System stats
H               Help
```

---

<!-- Meshtastic firmware README below -->

<div align="center" markdown="1">

<img src=".github/meshtastic_logo.png" alt="Meshtastic Logo" width="80"/>
<h1>Meshtastic Firmware</h1>

![GitHub release downloads](https://img.shields.io/github/downloads/meshtastic/firmware/total)
[![CI](https://img.shields.io/github/actions/workflow/status/meshtastic/firmware/main_matrix.yml?branch=master&label=actions&logo=github&color=yellow)](https://github.com/meshtastic/firmware/actions/workflows/ci.yml)
[![CLA assistant](https://cla-assistant.io/readme/badge/meshtastic/firmware)](https://cla-assistant.io/meshtastic/firmware)
[![Fiscal Contributors](https://opencollective.com/meshtastic/tiers/badge.svg?label=Fiscal%20Contributors&color=deeppink)](https://opencollective.com/meshtastic/)
[![Vercel](https://img.shields.io/static/v1?label=Powered%20by&message=Vercel&style=flat&logo=vercel&color=000000)](https://vercel.com?utm_source=meshtastic&utm_campaign=oss)

<a href="https://trendshift.io/repositories/5524" target="_blank"><img src="https://trendshift.io/api/badge/repositories/5524" alt="meshtastic%2Ffirmware | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

</div>

</div>

<div align="center">
	<a href="https://meshtastic.org">Website</a>
	-
	<a href="https://meshtastic.org/docs/">Documentation</a>
</div>

## Meshtastic Overview

This repository contains the official device firmware for Meshtastic, an open-source LoRa mesh networking project designed for long-range, low-power communication without relying on internet or cellular infrastructure. The firmware supports various hardware platforms, including ESP32, nRF52, RP2040/RP2350, and Linux-based devices.

Meshtastic enables text messaging, location sharing, and telemetry over a decentralized mesh network, making it ideal for outdoor adventures, emergency preparedness, and remote operations.

### Get Started

- 🔧 **[Building Instructions](https://meshtastic.org/docs/development/firmware/build)** – Learn how to compile the firmware from source.
- ⚡ **[Flashing Instructions](https://meshtastic.org/docs/getting-started/flashing-firmware/)** – Install or update the firmware on your device.

Join our community and help improve Meshtastic! 🚀

## Stats

![Alt](https://repobeats.axiom.co/api/embed/8025e56c482ec63541593cc5bd322c19d5c0bdcf.svg "Repobeats analytics image")
