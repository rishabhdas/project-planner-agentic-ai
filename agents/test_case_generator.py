from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from models.ollama_models import llama3
from memory.memory import stm_memory, ltm_memory

# Prompt definition
test_prompt = PromptTemplate(
    input_variables=["user_story"],
    template="""
    You are a QA engineer.
    Given the user story: "{user_story}", generate test cases.
    - Include both positive and negative test scenarios
    - Mention Preconditions, Test Steps, and Expected Results
    Format each test case clearly.
    """
)

# Runnable chain
test_case_chain = test_prompt | llama3 | StrOutputParser()

def run_test_case_generator(user_story: str):
    response = test_case_chain.invoke({"user_story": user_story})
    ltm_memory.save_context({"input": user_story}, {"output": response})
    return response
