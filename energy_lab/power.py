import math

MAX_CP = 16 / 27  # Model assumption: an idealised, unblocked rotor.


def electrical_power_w(
    *,
    radius_m: float,
    speed_m_s: float,
    cp: float,
    efficiency: float,
    rho_kg_m3: float = 1025.0,
    cut_in_m_s: float = 0.5,
    cut_out_m_s: float = 4.0,
    rated_power_w: float = 250_000.0,
) -> float:
    """Return electrical power in watts for a nonnegative speed magnitude."""
    parameters = {
        "radius_m": radius_m,
        "speed_m_s": speed_m_s,
        "cp": cp,
        "efficiency": efficiency,
        "rho_kg_m3": rho_kg_m3,
        "cut_in_m_s": cut_in_m_s,
        "cut_out_m_s": cut_out_m_s,
        "rated_power_w": rated_power_w,
    }
    for name, value in parameters.items():
        if not isinstance(value, (int, float)) or not math.isfinite(value):
            raise ValueError(f"{name} must be a finite number.")

    if radius_m <= 0 or rho_kg_m3 <= 0:
        raise ValueError("Radius and water density must be positive.")
    if speed_m_s < 0:
        raise ValueError("Use a nonnegative current-speed magnitude.")
    if not 0 <= cp <= MAX_CP:
        raise ValueError("cp must be between 0 and 16/27 for this model.")
    if not 0 <= efficiency <= 1:
        raise ValueError("efficiency must be between 0 and 1.")
    if cut_in_m_s < 0 or cut_out_m_s <= cut_in_m_s:
        raise ValueError("Require 0 <= cut-in < cut-out.")
    if rated_power_w <= 0:
        raise ValueError("Generator rated power must be positive.")

    if speed_m_s < cut_in_m_s or speed_m_s >= cut_out_m_s:
        return 0.0

    area_m2 = math.pi * radius_m**2
    mechanical_power_w = 0.5 * rho_kg_m3 * area_m2 * speed_m_s**3 * cp
    unconstrained_electrical_w = mechanical_power_w * efficiency
    return float(min(unconstrained_electrical_w, rated_power_w))