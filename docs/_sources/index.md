# Graupel-2

Graupel-2 is a High Altitude Balloon launch designed with the goal of sending a balloon to 100,000' or more,
capturing a high definition video of the flight, and recovering the payload.  It is a follow-up to the mostly successful
[Graupel-1](https://sea7aero.space/graupel-1) mission with improvements to the payload and tracker software designed to fix the problem of our camera battery getting too cold and dying half way through the mission.

In addition, it is serving as a test bed for the [PyHAB](https://sea7aero.space/pyhab) python library for HAB flight
simulations.

Graupel-2 was launched on September 25th, 2021 and successfully recovered - all mission goals were achieved.


## Mission Parameters

As the mission requirements were to use a rather high-end camera - a [GoPro Hero 9 Black](https://gopro.com/en/us/shop/cameras/hero9-black/CHDHX-901-master.html) - and recovery of the payload was a priority, we used two redundant tracking solutions: a [SPOT Trace](https://www.findmespot.com/en-us/products-services/spot-trace) satellite tracker, and an [Arduino-based flight computer](https://github.com/sea7aero/horizon2).  In addition to tracking, the flight computer was used to log telemetry for later analysis and processing.

Attached to the payload was a [4' Rocketman Parachute](https://the-rocketman.com/recovery-html/) to safely return the payload to Earth.

And to get the whole thing up in the air, we decided on a [Kaymont HAB-1200](https://www.kaymont.com/habphotography) balloon, procured from [High Altitude Science](https://www.highaltitudescience.com/products/near-space-balloon-1200-g)

```python
payload_mass = 1460.0 * units.g
parachute_mass = 120.0 * units.g
balloon_mass = 1200.0 * units.g
```
