from agents import project_planner
from agents import test_case_generator
from agents import user_story_generator
from memory.memory import save_vectorstore

def main():
    project_description = "Build a web-based platform for managing freelance projects with milestone tracking and payment integration."

    print("\n--- Generating Project Plan ---")
    plan = project_planner.run_project_planner(project_description)
    print(plan)

    print("\n--- Generating User Stories ---")
    stories = user_story_generator.run_user_story_generator(plan)
    print(stories)

    print("\n--- Generating Test Cases for First User Story ---")
    first_story = stories.split("As a")[1]  # crude extraction
    first_story = "As a" + first_story.split("\n")[0]
    tests = test_case_generator.run_test_case_generator(first_story)
    print(tests)

    # Persist FAISS index to disk
    save_vectorstore()
    print("\n Long-term memory saved successfully.\n")

if __name__ == "__main__":
    main()
