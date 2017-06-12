# Sensor data request

This is sent from Teensy to Pi whenever Pi requests data:

| Byte  | Content               |
|:-----:| --------------------- |
| 1     | Speed (km/h)          |
| 2     | Steering value (0-255)|
| 3     | Throttle value (0-255)|

