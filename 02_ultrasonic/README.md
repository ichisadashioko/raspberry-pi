# HC-SR04 ultrasonic sensor

## HC-SR04 Specifications

- Working Voltage: `DC 5V`
- Working Current: `15mA` (`0.015A`)
- Max Range: 4m
- Min Range: 2cm
- Measuring Angle: `15` degree
- Trigger Input Signal: `10µS` TTL pulse
- Echo Output Signal Input TTL lever signal and the range in proportion
- Dimension 45 * 20 * 15mm

## Wiring configuration

- Goal: **Keep the current below `0.015A`**

- Available resistors:

    - `10k` Ohms (20 pcs)

- Wiring:

    - `VCC => 5V`
    - `TRIG => GPIO`
    - ECHO:
        - `ECHO => R(10k) => GPIO`
        - `ECHO => R(10k) => R(10k) => GRN`
    - `GRN => GRN`