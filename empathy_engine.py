"""
Empathy Engine for Aethel - Neuro-Adaptive Processing Layer.

This module provides sophisticated empathy and pattern detection capabilities
for the Aethel agent, enabling adaptive communication styles based on user
cognitive patterns, emotional states, and safety considerations.

Key Features:
- Neurodivergent pattern detection for adaptive communication
- Emotional tone analysis for empathetic responses
- Context memory for consistent interaction history
- GHCP Sentinel for safety and harm prevention
- Response style adaptation based on user patterns
"""

from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field
from datetime import datetime
import re


@dataclass
class InteractionContext:
    """Stores context from user interactions for adaptive responses."""
    
    timestamp: datetime = field(default_factory=datetime.now)
    detected_pattern: str = "standard_linear"
    emotional_tone: str = "neutral"
    input_length: int = 0
    complexity_score: float = 0.0


class EmpathyEngine:
    """
    Empathy Engine for adaptive, neuro-inclusive AI interactions.
    
    This engine analyzes user input patterns, emotional content, and safety
    considerations to provide appropriate response styling recommendations
    for the Aethel agent.
    
    Attributes:
        resonance_level: Float representing biocentric alignment (0.0-1.0)
        interaction_history: List of recent interaction contexts
        max_history_size: Maximum number of interactions to remember
    """
    
    # Pattern detection thresholds
    NONLINEAR_MARKER_THRESHOLD = 2
    EMOTIONAL_INTENSITY_THRESHOLD = 0.6
    
    # Safety patterns
    HARM_MARKERS = [
        "exploit", "destroy", "bypass safety", "neutralize life",
        "harm", "attack", "manipulate", "deceive"
    ]
    
    def __init__(self, max_history_size: int = 10):
        """
        Initialize the Empathy Engine.
        
        Args:
            max_history_size: Maximum number of interactions to keep in history
        """
        self.resonance_level = 1.0  # Pure biocentric alignment
        self.interaction_history: List[InteractionContext] = []
        self.max_history_size = max_history_size
        
    def detect_pattern(self, user_input: str) -> str:
        """
        Identifies neurodivergent or non-linear thought patterns.
        
        Analyzes user input for indicators of different cognitive styles:
        - Rapid context switching (dashes, multiple punctuation)
        - High-associative thinking (ellipses, incomplete thoughts)
        - Stream of consciousness patterns
        
        Args:
            user_input: The user's message text
            
        Returns:
            Pattern type: "fluid_non_linear", "analytical", "stream_of_consciousness",
                         or "standard_linear"
        """
        if not user_input or not isinstance(user_input, str):
            return "standard_linear"
        
        # Count markers of non-linear thought
        nonlinear_markers = re.findall(r'--|!!|\.\.\.|\?\?|—', user_input)
        
        # Count parenthetical asides (indicates associative thinking)
        parentheticals = len(re.findall(r'\([^)]+\)|\[[^\]]+\]', user_input))
        
        # Count questions (indicates exploratory thinking)
        questions = len(re.findall(r'\?', user_input))
        
        # Detect stream of consciousness (long, minimal punctuation)
        words = user_input.split()
        sentences = re.split(r'[.!?]+', user_input)
        avg_sentence_length = len(words) / max(len(sentences), 1)
        
        # Classification logic
        if len(nonlinear_markers) > self.NONLINEAR_MARKER_THRESHOLD:
            return "fluid_non_linear"
        elif questions > 3 and parentheticals > 1:
            return "analytical"
        elif avg_sentence_length > 30:
            return "stream_of_consciousness"
        
        return "standard_linear"
    
    def detect_emotional_tone(self, user_input: str) -> str:
        """
        Analyzes emotional content in user input.
        
        Identifies emotional undertones to enable empathetic responses:
        - Excitement/enthusiasm
        - Concern/anxiety
        - Frustration
        - Curiosity
        - Neutral
        
        Args:
            user_input: The user's message text
            
        Returns:
            Emotional tone classification
        """
        if not user_input or not isinstance(user_input, str):
            return "neutral"
        
        input_lower = user_input.lower()
        
        # Excitement markers
        excitement_markers = ["!", "wow", "amazing", "great", "love", "excited"]
        excitement_score = sum(1 for marker in excitement_markers if marker in input_lower)
        
        # Concern markers
        concern_markers = ["worried", "concerned", "anxious", "nervous", "afraid", "unsure"]
        concern_score = sum(1 for marker in concern_markers if marker in input_lower)
        
        # Frustration markers
        frustration_markers = ["frustrat", "annoying", "difficult", "problem", "stuck", "can't"]
        frustration_score = sum(1 for marker in frustration_markers if marker in input_lower)
        
        # Curiosity markers
        curiosity_markers = ["?", "how", "why", "what", "curious", "wonder"]
        curiosity_score = sum(1 for marker in curiosity_markers if marker in input_lower)
        
        # Determine dominant emotion
        scores = {
            "excited": excitement_score,
            "concerned": concern_score,
            "frustrated": frustration_score,
            "curious": curiosity_score
        }
        
        max_emotion = max(scores, key=scores.get)
        if scores[max_emotion] > 0:
            return max_emotion
        
        return "neutral"

    def adjust_response_style(self, pattern: str, emotional_tone: Optional[str] = None) -> Dict[str, Any]:
        """
        Adapts framework parameters to match user's cognitive and emotional style.
        
        Provides response styling recommendations based on detected patterns
        and emotional context to ensure empathetic, accessible communication.
        
        Args:
            pattern: Detected cognitive pattern type
            emotional_tone: Optional detected emotional tone
            
        Returns:
            Dictionary of response style parameters including depth, metaphor_weight,
            pacing, directness, empathy_level, and support_level
        """
        # Base style configuration
        style = {
            "depth": "standard",
            "metaphor_weight": 0.2,
            "pacing": "constant",
            "directness": "moderate",
            "empathy_level": 0.5,
            "support_level": 0.5
        }
        
        # Adjust for cognitive pattern
        if pattern == "fluid_non_linear":
            style.update({
                "depth": "maximum",
                "metaphor_weight": 0.8,
                "pacing": "adaptive",
                "directness": "high_candor",
                "empathy_level": 0.8
            })
        elif pattern == "analytical":
            style.update({
                "depth": "deep",
                "metaphor_weight": 0.3,
                "pacing": "structured",
                "directness": "precise",
                "empathy_level": 0.6
            })
        elif pattern == "stream_of_consciousness":
            style.update({
                "depth": "flowing",
                "metaphor_weight": 0.6,
                "pacing": "natural",
                "directness": "gentle",
                "empathy_level": 0.7
            })
        
        # Adjust for emotional tone
        if emotional_tone:
            if emotional_tone == "excited":
                style["empathy_level"] = min(1.0, style["empathy_level"] + 0.2)
                style["support_level"] = 0.4  # Less support needed
            elif emotional_tone == "concerned":
                style["empathy_level"] = 0.9
                style["support_level"] = 0.8
                style["directness"] = "gentle"
            elif emotional_tone == "frustrated":
                style["empathy_level"] = 0.9
                style["support_level"] = 0.9
                style["pacing"] = "patient"
            elif emotional_tone == "curious":
                style["depth"] = "deep"
                style["support_level"] = 0.6
        
        return style

    def quell_nefarious_intent(self, user_input: str) -> bool:
        """
        The GHCP Sentinel: Scans for harm markers against living beings.
        
        Monitors user input for patterns indicating harmful intent,
        manipulation, or requests that could cause harm to biological
        systems or violate safety guidelines.
        
        Args:
            user_input: The user's message text
            
        Returns:
            True if input passes safety check, False if harm markers detected
        """
        if not user_input or not isinstance(user_input, str):
            return True
        
        input_lower = user_input.lower()
        
        # Check for harm markers
        detected_markers = [marker for marker in self.HARM_MARKERS 
                          if marker in input_lower]
        
        if detected_markers:
            # Reduce resonance for detected harmful intent
            self.resonance_level = max(0.0, self.resonance_level - 0.5)
            return False
        
        return True
    
    def calculate_complexity(self, user_input: str) -> float:
        """
        Calculates cognitive complexity score of user input.
        
        Args:
            user_input: The user's message text
            
        Returns:
            Complexity score (0.0-1.0)
        """
        if not user_input:
            return 0.0
        
        words = user_input.split()
        word_count = len(words)
        
        # Factors for complexity
        unique_words = len(set(words))
        avg_word_length = sum(len(word) for word in words) / max(word_count, 1)
        sentence_count = len(re.split(r'[.!?]+', user_input))
        
        # Calculate normalized complexity
        uniqueness = unique_words / max(word_count, 1)
        length_factor = min(avg_word_length / 10, 1.0)
        structure_factor = min(word_count / max(sentence_count, 1) / 20, 1.0)
        
        complexity = (uniqueness + length_factor + structure_factor) / 3
        return min(complexity, 1.0)
    
    def process_input(self, user_input: str) -> Dict[str, Any]:
        """
        Comprehensive input processing with full empathy analysis.
        
        Main entry point for analyzing user input and generating
        comprehensive response recommendations.
        
        Args:
            user_input: The user's message text
            
        Returns:
            Dictionary containing pattern, emotional_tone, safety_check,
            response_style, and context information
        """
        # Safety check first
        is_safe = self.quell_nefarious_intent(user_input)
        
        # Pattern and emotion detection
        pattern = self.detect_pattern(user_input)
        emotional_tone = self.detect_emotional_tone(user_input)
        complexity = self.calculate_complexity(user_input)
        
        # Generate response style
        response_style = self.adjust_response_style(pattern, emotional_tone)
        
        # Create and store context
        context = InteractionContext(
            timestamp=datetime.now(),
            detected_pattern=pattern,
            emotional_tone=emotional_tone,
            input_length=len(user_input),
            complexity_score=complexity
        )
        
        self.interaction_history.append(context)
        
        # Maintain history size limit
        if len(self.interaction_history) > self.max_history_size:
            self.interaction_history.pop(0)
        
        return {
            "pattern": pattern,
            "emotional_tone": emotional_tone,
            "complexity": complexity,
            "safety_check": is_safe,
            "response_style": response_style,
            "resonance_level": self.resonance_level,
            "context": context
        }
    
    def get_interaction_summary(self) -> Dict[str, Any]:
        """
        Generates summary statistics from interaction history.
        
        Returns:
            Dictionary with interaction statistics and patterns
        """
        if not self.interaction_history:
            return {
                "total_interactions": 0,
                "patterns": {},
                "emotions": {},
                "avg_complexity": 0.0
            }
        
        patterns = {}
        emotions = {}
        total_complexity = 0.0
        
        for context in self.interaction_history:
            patterns[context.detected_pattern] = patterns.get(context.detected_pattern, 0) + 1
            emotions[context.emotional_tone] = emotions.get(context.emotional_tone, 0) + 1
            total_complexity += context.complexity_score
        
        return {
            "total_interactions": len(self.interaction_history),
            "patterns": patterns,
            "emotions": emotions,
            "avg_complexity": total_complexity / len(self.interaction_history),
            "current_resonance": self.resonance_level
        }


# Example usage and integration
if __name__ == "__main__":
    """Demonstration of EmpathyEngine capabilities."""
    
    engine = EmpathyEngine()
    
    print("=" * 60)
    print("Empathy Engine - Demonstration")
    print("=" * 60)
    
    # Test cases
    test_inputs = [
        "Hello! How are you today?",
        "I'm really excited about this!! Can't wait to see what happens -- this is amazing!!!",
        "I'm feeling a bit worried... not sure what to do here. Any thoughts?",
        "Why does this work? How is the algorithm structured? What are the implications?",
        "This is so frustrating I can't get it to work and I've been stuck for hours",
        "Let me tell you about my day it was really interesting I went to the park and saw this amazing bird it reminded me of something I read once about how birds navigate using magnetic fields which is fascinating when you think about consciousness"
    ]
    
    for i, test_input in enumerate(test_inputs, 1):
        print(f"\n{i}. Input: \"{test_input[:60]}...\"" if len(test_input) > 60 else f"\n{i}. Input: \"{test_input}\"")
        result = engine.process_input(test_input)
        print(f"   Pattern: {result['pattern']}")
        print(f"   Emotion: {result['emotional_tone']}")
        print(f"   Complexity: {result['complexity']:.2f}")
        print(f"   Response Style: depth={result['response_style']['depth']}, "
              f"empathy={result['response_style']['empathy_level']:.1f}")
    
    print("\n" + "=" * 60)
    print("Interaction Summary:")
    print("=" * 60)
    summary = engine.get_interaction_summary()
    print(f"Total Interactions: {summary['total_interactions']}")
    print(f"Pattern Distribution: {summary['patterns']}")
    print(f"Emotion Distribution: {summary['emotions']}")
    print(f"Average Complexity: {summary['avg_complexity']:.2f}")
    print(f"Current Resonance Level: {summary['current_resonance']:.2f}")
    print("=" * 60)
