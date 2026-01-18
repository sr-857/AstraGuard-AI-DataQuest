from enum import Enum
from typing import Dict, Any

class SystemState(Enum):
    NORMAL = "NORMAL"
    ANOMALY_DETECTED = "ANOMALY_DETECTED"
    FAULT_DETECTED = "FAULT_DETECTED"
    RECOVERY_IN_PROGRESS = "RECOVERY_IN_PROGRESS"
    SAFE_MODE = "SAFE_MODE"

class StateMachine:
    def __init__(self):
        self.current_state = SystemState.NORMAL
        self.recovery_start_time = None
        self.recovery_duration = 5  # seconds (simulated)
        self.recovery_steps = 0

    def process_fault(self, fault_type: str, telemetry: Dict[str, Any]) -> Dict[str, str]:
        """Process a detected fault and transition state."""
        previous_state = self.current_state.value
        
        if fault_type == "normal":
            # If we were in anomaly/fault state but now normal, we might recover
            if self.current_state in [SystemState.ANOMALY_DETECTED, SystemState.FAULT_DETECTED]:
                # Auto-recover if transient
                self.current_state = SystemState.NORMAL
        else:
            # Escalation logic
            if self.current_state == SystemState.NORMAL:
                self.current_state = SystemState.ANOMALY_DETECTED
            elif self.current_state == SystemState.ANOMALY_DETECTED:
                self.current_state = SystemState.FAULT_DETECTED
            elif self.current_state == SystemState.FAULT_DETECTED:
                self.current_state = SystemState.RECOVERY_IN_PROGRESS
                self.recovery_steps = 0
                
        return {
            "previous_state": previous_state,
            "new_state": self.current_state.value,
            "action": "transition"
        }

    def check_recovery_complete(self) -> bool:
        """Check if recovery process is complete."""
        if self.current_state == SystemState.RECOVERY_IN_PROGRESS:
            self.recovery_steps += 1
            if self.recovery_steps >= self.recovery_duration:
                return True
        return False

    def resume_normal_operation(self) -> Dict[str, str]:
        """Force transition back to normal."""
        previous_state = self.current_state.value
        self.current_state = SystemState.NORMAL
        return {
            "previous_state": previous_state,
            "new_state": self.current_state.value,
            "action": "resume"
        }
