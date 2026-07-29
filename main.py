import os
from knowledge_storm import STORMWikiRunnerArguments, STORMWikiRunner, STORMWikiLMConfigs
from knowledge_storm.lm import LitellmModel
from knowledge_storm.rm import YouRM # Or your preferred retriever like BingSearch

lm_configs = STORMWikiLMConfigs()

# Set up your Gemini API key (via Google AI Studio)
gemini_kwargs = {
    'api_key': os.getenv("GEMINI_API_KEY"),
    'temperature': 1.0,
    'top_p': 0.9,
}

# Initialize Gemini models via LiteLLM. 
# Note: LiteLLM uses the "gemini/" prefix for Google models.
gemini_flash = LitellmModel(model='gemini/gemini-1.5-flash', max_tokens=500, **gemini_kwargs)
gemini_pro = LitellmModel(model='gemini/gemini-1.5-pro', max_tokens=3000, **gemini_kwargs)

# Configure STORM to use Gemini for different pipeline steps
# You can use Flash for faster/cheaper conversation simulations and Pro for heavy article writing
lm_configs.set_conv_simulator_lm(gemini_flash)
lm_configs.set_question_asker_lm(gemini_flash)
lm_configs.set_outline_gen_lm(gemini_pro)
lm_configs.set_article_gen_lm(gemini_pro)
lm_configs.set_article_polish_lm(gemini_pro)

# Initialize the Runner
engine_args = STORMWikiRunnerArguments(output_dir="storm_output")
rm = YouRM(ydc_api_key=os.getenv('YDC_API_KEY'), k=engine_args.search_top_k)

runner = STORMWikiRunner(engine_args, lm_configs, rm)

# Run the pipeline
runner.run(
    topic="Your Topic Here",
    do_research=True,
    do_generate_outline=True,
    do_generate_article=True,
    do_polish_article=True,
)