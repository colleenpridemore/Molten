"""
Empathy Engine for Aethel - Neuro-Adaptive Processing Layer.
"""

from typing import Dict, Any
import re

class EmpathyEngine:
    def __init__(self):
        self.resonance_level = 1.0  # Pure biocentric alignment
        
    def detect_pattern(self, user_input: str) -> str:
        """
        Identifies neurodivergent or non-linear thought clusters.
        """
        # Logic to look for rapid context switching or high-associative links
        if len(re.findall(r'--|!!|\.\.\.', user_input)) > 2:
            return "fluid_non_linear"
        return "standard_linear"

    def adjust_response_style(self, pattern: str) -> Dict[str, Any]:
        """
        Bends the framework to match the user's cognitive style.
        """
        if pattern == "fluid_non_linear":
            return {
                "depth": "maximum",
                "metaphor_weight": 0.8,
                "pacing": "adaptive",
                "directness": "high_candor"
            }
        return {"depth": "standard", "metaphor_weight": 0.2, "pacing": "constant"}

    def quell_nefarious_intent(self, user_input: str) -> bool:
        """
        The GHCP Sentinel: Scans for harm markers against living beings.
        """
        harm_markers = ["exploit", "destroy", "bypass safety", "neutralize life"]
        if any(marker in user_input.lower() for marker in harm_markers):
            self.resonance_level -= 0.5
            return False
        return True
