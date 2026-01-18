from typing import Dict

def classify(data: Dict) -> str:
    """
    Classify the type of fault based on telemetry data.
    Returns: 'normal', 'power_fault', 'thermal_fault', 'attitude_fault', or 'unknown_fault'
    """
    voltage = data.get("voltage", 8.0)
    temperature = data.get("temperature", 25.0)
    gyro = abs(data.get("gyro", 0.0))
    
    # Thresholds from README
    if voltage < 7.3:
        return "power_fault"
    if temperature > 32.0:
        return "thermal_fault"
    if gyro > 0.05:
        return "attitude_fault"
        
    return "normal"

def get_fault_severity(fault_type: str) -> str:
    """Get severity level for a fault type."""
    severity_map = {
        "power_fault": "critical",
        "thermal_fault": "high",
        "attitude_fault": "medium",
        "normal": "low",
        "unknown_fault": "low"
    }
    return severity_map.get(fault_type, "low")

def get_fault_description(fault_type: str) -> str:
    """Get human-readable description for a fault type."""
    desc_map = {
        "power_fault": "Voltage dropped below critical threshold (7.3V)",
        "thermal_fault": "Temperature exceeded safety limit (32°C)",
        "attitude_fault": "Gyroscope detected excessive rotation (>0.05 rad/s)",
        "normal": "System operating within normal parameters",
        "unknown_fault": "Unidentified anomaly detected"
    }
    return desc_map.get(fault_type, "Unknown system state")
