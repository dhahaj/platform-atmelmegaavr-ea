# Atmel megaAVR-EA: development platform for [PlatformIO](https://platformio.org)

Microchip AVR EA is a family of microcontrollers (MCUs) with high-speed integrated analog, hardware-based Core Independent Peripherals (CIPs) and low-power performance for efficient real-time control, sensor node and secondary safety monitoring applications.

# Usage

1. [Install PlatformIO](https://platformio.org)
2. Create PlatformIO project and configure a platform option in [platformio.ini](https://docs.platformio.org/page/projectconf.html) file:

## Development version

```ini
[env:development]
platform = https://github.com/TODO/platform-atmelmegaavr-ea.git
board = ...
...
```