from config import call_gemini

def synthesize_and_review(outline: str, hypothesis: str) -> dict:
    """
    Acts as the automated peer-review module, identifying weak links.
    """
    system_prompt = "You are Reviewer #2. You are highly skeptical, rigorous, and demand physiological proof."
    
    prompt = f"""
    Review the following outline for a paper proposing this hypothesis: {hypothesis}
    
    Outline:
    {outline}
    
    Perform an automated peer review. Provide:
    1. Confidence Level (1-100%)
    2. Weakest Links (Identify missing perspectives or biophysical leaps)
    3. Suggested revisions.
    """
    
    review_output = call_gemini(prompt, system_prompt)
    
    return {
        "status": "Review Completed",
        "feedback": review_output
    }