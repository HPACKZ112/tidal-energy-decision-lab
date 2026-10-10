from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from energy_lab import electrical_power_w

speeds = [0.0, 0.49, 0.5, 2.0, 3.0, 3.99, 4.0, 4.5]

for speed in speeds:
    power_w = electrical_power_w(
        radius_m=5.0,
        speed_m_s=speed,
        cp=0.40,
        efficiency=0.90,
    )
    print(f"{speed:.2f} m/s -> {power_w / 1000:.2f} kW")