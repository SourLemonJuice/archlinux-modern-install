# Arch Linux Modern Install

This repo contains some example `/etc` system-wide configurations and some common utils and drivers.\
Only consider x86_64 architecture.

To install a list of packages, run something like:

```bash
pacman -Sy --needed $(./filter-pkgs.py pkgs-system.txt pkgs-media.txt)
```

You can parse multiple pkgs.txt at once like above.

It can also be used in archiso with [pacstrap](https://wiki.archlinux.org/title/Pacstrap):

```bash
pacstrap -K /path/to/chroot $(./filter-pkgs.py ...)
```

## System Structures

Arch Linux can be customized to any distro, this repo contains my opinions and may be look like a Red Hat branch(RHEL, Fedora).

It use **dracut** to generate initramfs, **systemd-ukify** to generate unified kernel image(UKI), and manage them with **systemd-boot**. The kernel is the standard one(package name `linux`).\
It won't setup or install secure boot stuff.

The network manager is pure **NetworkManager**, no systemd-networkd or other middleware will be used.\
The randomized mac address will be enabled, and won't send hostname via DHCP by default. When disconnected, will send a DHCP release signal.\
The DNS client is **systemd-resolved**.

The time synchronized service is **chrony** rather then **systemd-timesyncd**.

It use [**tuned**](https://wiki.archlinux.org/title/TuneD) to implement power management, and also will install **tuned-ppd** to compatible with power-profiles-daemon's interface used for GUI desktop.

No desktop will be installed or configured.

You can follow the instructions at the last part of page.

## pkgs-system.txt

Follow the [Installation guide - ArchWiki](https://wiki.archlinux.org/title/Installation_guide)\
Provide:

- kernel & firmware
- microcode for AMD and Intel CPU
- bootloader(dracut, ukify, and kernel-install)
- common filesystems support and utils
- common hardware, networking, and disk utils
- common file archive utils
- power management tools

## pkgs-gpu-*.txt

- OpenGL, Vulkan, and video hardware acceleration drivers for AMD and Intel GPU.\
  See NVIDIA's driver at: [NVIDIA - ArchWiki](https://wiki.archlinux.org/title/NVIDIA)\
  The Accelerated Computing/GPGPU drivers such as OpenCL, CUDA and RCOm are not included.

## pkgs-media.txt

- video, image, and video codecs
- basic fonts

## pkgs-cjk.txt

- Noto Sans CJK
- fcitx5 input method

## Installation Guide

Boot the archiso and partitioning your disk layout at first.

After that mount them to `/mnt` and install system packages with pacstrap:

```bash
pacstrap -K /mnt $(./filter-pkgs.py pkgs-system.txt pkgs-...)
```

I recommend to install these for desktop system:

- pkgs-system.txt
- pkgs-gpu-*.txt
- pkgs-media.txt

Many PC are all have an Intel GPU inside their CPU chip, don't forget this. :)\
And you can also install NVIDIA GPU drivers yourself at this time.

Edit the /etc/fstab file of the new system. I preferred to add a `lazytime` option to all the main drives, and a `umask=0077` to the boot partition.

And install my config files:

```bash
./install-config.sh /path_to_repo/etc /mnt/etc
```

Now arch-chroot into your new system via `arch-chroot /mnt` and follow the [official guide](https://wiki.archlinux.org/title/Installation_guide) to setup keyboard layout, timezone.

After the that, edit the `/etc/kernel/cmdline` file and fill your real root filesystem UUID, like:

```text
root=UUID:6ab9c8fc-5b7d-42fc-97a3-82feec3f5d7d
```

Edit the `/etc/dracut.conf.d/local.conf` to make sure you have all the kernel modules that you need in the initramfs state.\
For example, btrfs need `btrfs` module, LUKS2 encrypted root need `crypto`, TPM2 need `tpm2-tss`:

```ini
add_dracutmodules+=" systemd resume btrfs crypt tpm2-tss "
```

Setup [systemd-resolved](https://wiki.archlinux.org/title/Systemd-resolved) stub mode:

```bash
# note: this step require outside chroot
ln -sf ../run/systemd/resolve/stub-resolv.conf /mnt/etc/resolv.conf
```

Then setup systemd services:

```bash
# run resolved before NetworkManager
systemctl enable --now systemd-resolved
systemctl disable --now systemd-networkd
systemctl enable --now NetworkManager

systemctl disable --now systemd-timesyncd
systemctl enable --now chronyd
```

And finally, if you think you've done everything, run this(still inside chroot):

```bash
kernel-install add-all
bootctl install
```

Hope everything works fine...

Oh right, if bootctl didn't tell you they created an EFI boot entry. You can exit the chroot and create entry under a real environment.\
But in this way, you will be using the old version of systemd-boot when archiso was created:

```bash
# outside chroot
bootctl install --esp-path=/mnt/boot
```
