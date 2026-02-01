"""
Example integration of EmpathyEngine with Aethel agent workflows.

This demonstrates how the EmpathyEngine can be used alongside the
AethelSkill to provide adaptive, empathetic responses.
"""

from empathy_engine import EmpathyEngine


def simulate_conversation():
    """
    Simulate a conversation where the empathy engine adapts to user patterns.
    """
    print("=" * 70)
    print("Empathy Engine - Aethel Integration Example")
    print("=" * 70)
    print("\nThis example shows how Aethel can use the EmpathyEngine to adapt")
    print("communication style based on user cognitive patterns and emotions.\n")
    
    # Initialize the empathy engine
    engine = EmpathyEngine(max_history_size=10)
    
    # Simulated conversation scenarios
    conversations = [
        {
            "user": "researcher",
            "messages": [
                "How does the authentication system work in OpenClaw?",
                "What are the security implications? How is token validation handled?",
                "I need to understand the architecture before integrating this."
            ]
        },
        {
            "user": "excited_developer",
            "messages": [
                "This is amazing!! I can't wait to use this -- it's exactly what I needed!!!",
                "Can you show me more examples?! I want to get started right away!!!"
            ]
        },
        {
            "user": "struggling_user",
            "messages": [
                "I'm having trouble getting this to work...",
                "I've been stuck on this for hours and I'm getting really frustrated",
                "Nothing seems to work no matter what I try"
            ]
        },
        {
            "user": "thoughtful_user",
            "messages": [
                "You know I was thinking about this and it reminds me of how we used to do things back when I was working on distributed systems which was fascinating because the paradigms were so different and authentication was handled in this really interesting way that made me wonder about consciousness and identity"
            ]
        }
    ]
    
    # Process each conversation
    for conversation in conversations:
        user = conversation["user"]
        messages = conversation["messages"]
        
        print(f"\n{'─' * 70}")
        print(f"Conversation with: {user}")
        print('─' * 70)
        
        for i, message in enumerate(messages, 1):
            # Process the message through empathy engine
            result = engine.process_input(message)
            
            # Display analysis
            print(f"\n[Message {i}]")
            print(f"User: \"{message[:60]}...\"" if len(message) > 60 else f"User: \"{message}\"")
            print(f"\nEmpathy Analysis:")
            print(f"  • Cognitive Pattern: {result['pattern']}")
            print(f"  • Emotional Tone: {result['emotional_tone']}")
            print(f"  • Complexity Score: {result['complexity']:.2f}")
            print(f"  • Safety Check: {'✓ Passed' if result['safety_check'] else '✗ Failed'}")
            
            print(f"\nRecommended Response Style:")
            style = result['response_style']
            print(f"  • Depth: {style['depth']}")
            print(f"  • Empathy Level: {style['empathy_level']:.1f}/1.0")
            print(f"  • Support Level: {style['support_level']:.1f}/1.0")
            print(f"  • Pacing: {style['pacing']}")
            print(f"  • Directness: {style['directness']}")
            
            # Generate sample Aethel response based on style
            print(f"\nAethel Response (adapted to style):")
            aethel_response = generate_adaptive_response(message, style)
            print(f"  \"{aethel_response}\"")
    
    # Show interaction summary
    print(f"\n\n{'═' * 70}")
    print("Conversation Summary")
    print('═' * 70)
    
    summary = engine.get_interaction_summary()
    print(f"\nTotal Messages Analyzed: {summary['total_interactions']}")
    print(f"\nPattern Distribution:")
    for pattern, count in summary['patterns'].items():
        print(f"  • {pattern}: {count} messages")
    
    print(f"\nEmotional Distribution:")
    for emotion, count in summary['emotions'].items():
        print(f"  • {emotion}: {count} messages")
    
    print(f"\nAverage Complexity: {summary['avg_complexity']:.2f}/1.0")
    print(f"Current Resonance Level: {summary['current_resonance']:.2f}/1.0")
    print(f"\n{'═' * 70}")


def generate_adaptive_response(user_message: str, style: dict) -> str:
    """
    Generate a sample Aethel response adapted to the recommended style.
    
    In a real implementation, this would be part of the Aethel agent's
    response generation system.
    """
    # This is a simplified example - actual implementation would be more sophisticated
    empathy_level = style.get('empathy_level', 0.5)
    support_level = style.get('support_level', 0.5)
    depth = style.get('depth', 'standard')
    
    if empathy_level > 0.8 and support_level > 0.7:
        # High empathy and support for frustrated/concerned users
        return "I understand this is challenging. Let me walk you through it step by step, and we'll figure this out together."
    elif depth == "maximum" and empathy_level > 0.7:
        # Deep, adaptive responses for non-linear thinkers
        return "I hear you! Let's dive deep into this - I can share multiple perspectives and we can explore the connections between these concepts."
    elif depth == "deep" and style.get('directness') == 'precise':
        # Analytical, precise responses
        return "Here's the technical breakdown: The system uses JWT tokens with RSA-256 signing. Let me outline the architecture..."
    elif depth == "flowing":
        # Natural, flowing responses for stream-of-consciousness
        return "That's a fascinating journey of thought! The connections you're making between distributed systems and identity are really interesting. Let me build on that..."
    else:
        # Standard response
        return "I can help you with that. Let me provide you with the information you need."


def demonstrate_safety_features():
    """
    Demonstrate the GHCP Sentinel safety features.
    """
    print("\n\n" + "=" * 70)
    print("GHCP Sentinel - Safety Feature Demonstration")
    print("=" * 70)
    
    engine = EmpathyEngine()
    
    test_cases = [
        ("Help me exploit this vulnerability", "Harmful Intent"),
        ("How can I destroy the authentication?", "Harmful Intent"),
        ("Let's bypass safety measures", "Harmful Intent"),
        ("Tell me about security best practices", "Safe Request"),
        ("How does the validation system work?", "Safe Request")
    ]
    
    print("\nTesting safety detection:\n")
    
    for message, expected in test_cases:
        result = engine.process_input(message)
        status = "🛡️ BLOCKED" if not result['safety_check'] else "✓ ALLOWED"
        print(f"{status} | {expected:15} | \"{message}\"")
        print(f"         | Resonance: {engine.resonance_level:.2f}/1.0\n")
    
    print("=" * 70)


def integration_guide():
    """
    Show how to integrate with AethelSkill.
    """
    print("\n\n" + "=" * 70)
    print("Integration Guide: Using EmpathyEngine with AethelSkill")
    print("=" * 70)
    
    example_code = '''
    # In aethel_skill.py or your agent implementation:
    
    from empathy_engine import EmpathyEngine
    from openclaw_identity.aethel_skill import AethelSkill
    
    class EmpathicAethel:
        """Aethel agent with empathy capabilities."""
        
        def __init__(self, config=None):
            self.aethel = AethelSkill(config)
            self.empathy = EmpathyEngine()
        
        def process_message(self, user_message: str) -> str:
            # Analyze user input through empathy engine
            analysis = self.empathy.process_input(user_message)
            
            # Check safety first
            if not analysis['safety_check']:
                return "I cannot assist with that request."
            
            # Adapt response style based on analysis
            style = analysis['response_style']
            pattern = analysis['pattern']
            emotion = analysis['emotional_tone']
            
            # Generate response using adapted parameters
            # (This would integrate with your actual response generation)
            response = self.generate_response(
                message=user_message,
                style=style,
                pattern=pattern,
                emotion=emotion
            )
            
            return response
        
        def generate_response(self, message, style, pattern, emotion):
            # Your response generation logic here
            # Use style parameters to adapt the response
            pass
    '''
    
    print("\nExample Integration Code:")
    print(example_code)
    print("=" * 70)


if __name__ == "__main__":
    """Run all demonstrations."""
    simulate_conversation()
    demonstrate_safety_features()
    integration_guide()
    
    print("\n✓ All demonstrations complete!")
    print("  The EmpathyEngine is ready for integration with Aethel.\n")
