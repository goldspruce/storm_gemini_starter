from config import call_gemini

def generate_personas(hypothesis: str) -> list:
    """
    Dynamically generates specialized scientific personas based on the hypothesis.
    """
    system_prompt = "You are an AI architect designing a multi-agent peer-review panel."
    prompt = f"""
    Given the following biological hypothesis: '{hypothesis}'
    
    Generate 3 distinct academic personas needed to rigorously analyze and critique this hypothesis. 
    Format your response as a simple list of titles and their primary directive.
    Example:
    1. Biophysicist: Focuses on ion channel kinetics.
    2. Skeptical Neurologist: Looks for clinical contradictions.
    """
    
    raw_personas = call_gemini(prompt, system_prompt)
    
    # In production, use Pydantic/Instructor to parse this into strict JSON objects.
    return raw_personas.strip().split('\n')