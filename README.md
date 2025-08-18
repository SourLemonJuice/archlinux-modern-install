# Arch Linux Modern Install

Contain some example `/etc` system-wide configurations and some common utils and drivers.

To install a list of packages, run something like:

```bash
sudo ./install-pkgs.py pkgs-system.x86_64.txt
```

## pkgs-system

Follow the [Installation guide - ArchWiki](https://wiki.archlinux.org/title/Installation_guide)\
Provide:

- kernel & firmware
- Microcode for AMD and Intel CPU
- bootloader(dracut and ukify)
- common filesystems support and utils
- common hardware, networking, and disk utils
- common file archive utils
- power management tools

The time sync service does not include, I recommend use `chrony` with NTS but not `systemd-timesyncd` to synchronize time.\
My config: [chrony.conf](https://gist.github.com/SourLemonJuice/dde88d0cffc20d5f1119f8a10e5b51e9)

## pkgs-gpu-*

- OpenGL, Vulkan, and video hardware acceleration drivers for AMD and Intel GPU.\
  See NVIDIA's driver at: [NVIDIA - ArchWiki](https://wiki.archlinux.org/title/NVIDIA)\
  The Accelerated Computing/GPGPU drivers such as OpenCL, CUDA and RCOm are not included.

## pkgs-media

- video, image, and video codecs
- basic fonts

## pkgs-cjk

- Noto Sans CJK
- fcitx5 input method
