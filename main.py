from storm_modules.retrieval import fetch_pubmed_literature
from storm_modules.personas import generate_personas
from storm_modules.outline import generate_academic_outline
from storm_modules.synthesis import synthesize_and_review

def run_pipeline(hypothesis: str):
    print(f"--- Starting Pipeline for: {hypothesis} ---\n")
    
    print("1. Generating Multi-Agent Personas...")
    personas = generate_personas(hypothesis)
    print(f"Generated Personas:\n{personas}\n")
    
    print("2. Re-engineered Retrieval (Querying PubMed)...")
    # Using keywords from the hypothesis
    literature = fetch_pubmed_literature("Fast-Spiking Neurons AND Aging", max_results=3)
    print(f"Retrieved {len(literature)} blocks of literature data.\n")
    
    print("3. Generating Academic Outline...")
    outline = generate_academic_outline(hypothesis, literature)
    print("Outline generated.\n")
    
    print("4. Automated Peer-Review & Synthesis...")
    review = synthesize_and_review(outline, hypothesis)
    
    print("\n--- Final Review Output ---")
    print(review['feedback'])

if __name__ == "__main__":
    test_hypothesis = (
        "Fast-Spike Neuron Decline (FSND) bridges the physiological gap "
        "between neuromuscular dynapenia and cognitive bradyphrenia."
    )
    run_pipeline(test_hypothesis)
