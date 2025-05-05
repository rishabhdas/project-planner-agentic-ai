from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from models.ollama_models import llama3
from memory.memory import stm_memory, ltm_memory

# Prompt definition
project_prompt = PromptTemplate(
    input_variables=["project_description"],
    template="""
    You are a project planning expert.
    Given the project description: "{project_description}", perform the following:
    - Generate detailed project documentation
    - Identify key deliverables
    - Break the delivery plan over the next 2 quarters (6 months)
    Format clearly.
    """
)

# New Runnable chain
project_chain = project_prompt | llama3 | StrOutputParser()

def run_project_planner(description: str):
    response = project_chain.invoke({"project_description": description})
    ltm_memory.save_context({"input": description}, {"output": response})
    return response
