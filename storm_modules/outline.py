from config import call_gemini

def generate_academic_outline(hypothesis: str, literature: list) -> str:
    """
    Generates a hypothesis-driven academic outline based on retrieved PubMed data.
    """
    system_prompt = "You are a senior principal investigator writing a review paper."
    
    lit_context = "\n".join(literature)
    prompt = f"""
    Hypothesis: {hypothesis}
    
    Retrieved Literature Context:
    {lit_context[:3000]} # Truncated for prototype safety
    
    Generate a rigorous academic outline for a scientific literature review. 
    Structure it with standard sections (Abstract, Introduction, Mechanisms, Contradictions, Conclusion).
    Ensure the focus is on testing the hypothesis, not just summarizing consensus.
    """
    
    return call_gemini(prompt, system_prompt)