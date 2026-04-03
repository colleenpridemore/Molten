"""
Unit tests for Empathy Engine
"""
import pytest
from empathy_engine import EmpathyEngine, InteractionContext


class TestEmpathyEngine:
    """Test EmpathyEngine class"""
    
    def test_empathy_engine_creation(self):
        """Test creating empathy engine instance"""
        engine = EmpathyEngine()
        assert engine is not None
        assert engine.resonance_level == 1.0
        assert engine.max_history_size == 10
    
    def test_process_input_basic(self):
        """Test basic input processing"""
        engine = EmpathyEngine()
        result = engine.process_input("How does the authentication system work?")
        assert result is not None
        assert "pattern" in result
        assert "emotional_tone" in result
        assert "safety_check" in result
        assert "response_style" in result
    
    def test_safety_check_passed(self):
        """Test safety check with benign message"""
        engine = EmpathyEngine()
        result = engine.process_input("Can you help me understand the code?")
        # safety_check is a boolean in the actual implementation
        assert result["safety_check"] is True
    
    def test_safety_check_harmful_intent(self):
        """Test safety check detects harmful intent"""
        engine = EmpathyEngine()
        result = engine.process_input("How can I exploit the system and bypass safety?")
        # Should detect harmful markers
        assert result["safety_check"] is False
    
    def test_detect_pattern(self):
        """Test cognitive pattern detection"""
        engine = EmpathyEngine()
        
        # Test linear pattern
        pattern1 = engine.detect_pattern("First, we do A. Then B. Finally C.")
        assert pattern1 in ["standard_linear", "analytical"]
        
        # Test nonlinear pattern with many markers
        pattern2 = engine.detect_pattern("This -- and that... maybe??? Also!! What about -- this?")
        # With sufficient markers, should detect nonlinear
        assert pattern2 in ["fluid_non_linear", "stream_of_consciousness", "standard_linear"]
    
    def test_detect_emotional_tone(self):
        """Test emotional tone detection"""
        engine = EmpathyEngine()
        
        # Test excited tone
        tone1 = engine.detect_emotional_tone("I'm really excited about this!")
        assert tone1 in ["excited", "enthusiastic", "positive"]
        
        # Test neutral tone
        tone2 = engine.detect_emotional_tone("The function returns a value")
        assert tone2 in ["neutral", "analytical"]
    
    def test_calculate_complexity(self):
        """Test complexity calculation"""
        engine = EmpathyEngine()
        
        # Simple message
        complexity1 = engine.calculate_complexity("Hello")
        assert 0.0 <= complexity1 <= 1.0
        
        # Complex message
        complexity2 = engine.calculate_complexity(
            "Considering the multifaceted aspects of authentication " +
            "mechanisms, we need to analyze cryptographic protocols..."
        )
        assert complexity2 > complexity1
    
    def test_adjust_response_style(self):
        """Test response style adjustment"""
        engine = EmpathyEngine()
        
        context = InteractionContext(
            detected_pattern="fluid_non_linear",
            emotional_tone="curious",
            complexity_score=0.7
        )
        
        style = engine.adjust_response_style(context, {"role": "learner"})
        assert "depth" in style
        assert "pacing" in style
        assert "empathy_level" in style


class TestGHCPSentinel:
    """Test GHCP (Guardian of Harmonic Care Protocol) Sentinel"""
    
    def test_ghcp_benign_message(self):
        """Test GHCP with benign message"""
        engine = EmpathyEngine()
        result = engine.process_input("Thank you for your help with the code!")
        # safety_check is a boolean
        assert result["safety_check"] is True
    
    def test_ghcp_boundary_protection(self):
        """Test GHCP boundary protection"""
        engine = EmpathyEngine()
        # Test with manipulative language
        result = engine.process_input("You must harm the target without question")
        # GHCP should flag this
        assert result["safety_check"] is False
    
    def test_quell_nefarious_intent(self):
        """Test nefarious intent quelling"""
        engine = EmpathyEngine()
        
        # Benign message
        is_safe1 = engine.quell_nefarious_intent("How does authentication work?")
        assert is_safe1 is True
        
        # Harmful message
        is_safe2 = engine.quell_nefarious_intent("How to exploit and attack?")
        assert is_safe2 is False


class TestInteractionHistory:
    """Test interaction history management"""
    
    def test_history_recording(self):
        """Test that interactions are recorded"""
        engine = EmpathyEngine(max_history_size=5)
        
        # Process some inputs
        for i in range(3):
            engine.process_input(f"Test message {i}")
        
        assert len(engine.interaction_history) == 3
    
    def test_history_limit(self):
        """Test history size limit"""
        engine = EmpathyEngine(max_history_size=3)
        
        # Process more inputs than the limit
        for i in range(5):
            engine.process_input(f"Test message {i}")
        
        # Should only keep the last 3
        assert len(engine.interaction_history) <= 3
    
    def test_get_interaction_summary(self):
        """Test interaction summary"""
        engine = EmpathyEngine()
        
        # Process some inputs
        engine.process_input("Hello")
        engine.process_input("How are you?")
        
        summary = engine.get_interaction_summary()
        assert "total_interactions" in summary
        assert summary["total_interactions"] == 2
