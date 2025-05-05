from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from models.ollama_models import falcon3, llama3
from memory.memory import stm_memory, ltm_memory

# Prompt definition
story_prompt = PromptTemplate(
    input_variables=["project_plan"],
    template="""
    You are an Agile product manager.
    Given the project plan: "{project_plan}", generate user stories for implementation.
    - Use the format: As a [type of user], I want [some goal] so that [some reason].
    - Group stories by features or deliverables.
    - Include bullet-pointed **Acceptance Criteria** under each story.
    """
)

# Runnable chain
story_chain = story_prompt | llama3 | StrOutputParser()

def run_user_story_generator(project_plan: str):
    response = story_chain.invoke({"project_plan": project_plan})
    ltm_memory.save_context({"input": project_plan}, {"output": response})
    return response
