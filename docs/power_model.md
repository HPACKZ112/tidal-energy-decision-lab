# Power Model Rules
## Units
Inputs will use units of meters, meters per second, kilograms per cubic meter and watts
## Assumptions
| Parameter | Value|
|---|---|
| Water density | 1025kg/m^3|
|Radius|5m|
|Cp|0.40|
|Mechanical to electrical efficiency|0.90|
|Cut in speed| 0.5m/s|
|Cut out speed| 4.0m/s|
|Rated electrical power|250,000W = 250kW|

- Output is zero when V > Cut out speed
- Output is zero when V < Cut in speed
- Swept area (A) = πr²
- Mechanical power = 0.5 × ρ × A × v³ × Cp
- Electrical power = Mechanical power * Conversion efficiency


Cp is constant in this screening model. For an idealised unblocked rotor we restrict Cp to 0–16/27, following the classical actuator-disc assumption. This is a model boundary, not a universal restriction for every tidal installation: channel blockage and free-surface effects require a different treatment.

The start/stop transitions are deliberately idealised. Rated-power clipping is a simplified control assumption, rather than a model of blade pitching or generator control. These values are illustrative and have not been validated for a particular turbine or site.