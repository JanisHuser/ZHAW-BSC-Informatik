# Embedded Linux

- Smallest possible linux
- Some open source addons


## Key Advantages

- Ability to re-use componentes
- Many components exist already
- No-one should re-develop yet another operation system kernel, TCP/IP stack, USB stack or another graphical tooklit value

-> Focus on the added value of the product


## Build system

- Adds dependencies to a minimal kernel
- Automatic creation of linux systems
- Repeatability

# Yocto

- Build system
- Allows creation custom linux embedded distributions

## Layers

### bblayers.conf

```bblayers.conf
BBLAYERS ?= " \
	/home/mc2/poky-mickledore/meta \
	/home/mc2/poky-mickledore/meta-poky \
	/home/mc2/poky-mickledore/meta-yocto-bsp \
	/home/mc2/rpi64/meta-openembedded/meta-oe \
	/home/mc2/rpi64/meta-raspberrypi \
	/home/mc2/rpi64/meta-mc2 \
	/home/mc2/rpi64/meta-student \
"
```

| Symbol | Description |
|--------|-------------|
| =  |when using the variable, value is expand |
| := | immediately expand the value |
| ?= | assign if no other value was previously assigned |
| ??= | same as previous, with a lower precedence |
