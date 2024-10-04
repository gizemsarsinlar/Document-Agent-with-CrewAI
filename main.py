import os
from textwrap import dedent

from crewai import Crew

from agents import CustomAgents
from tasks import CustomTasks

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# This is the main class that you will use to define your custom crew.
# You can define as many agents and tasks as you want in agents.py and tasks.py


class CustomCrew:
    def __init__(self, var1):
        self.var1 = var1

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = CustomAgents()
        tasks = CustomTasks()

        # Define your custom agents and tasks here
        pdf_agent = agents.pdf_agent()
        writer_agent = agents.writer_agent()

        # Custom tasks include agent name and variables as input
        task1 = tasks.pdf_task(
            pdf_agent,
            self.var1
        )

        task2 = tasks.writer_task(
            writer_agent,
        )

        # Define your custom crew here
        crew = Crew(
            agents=[pdf_agent, writer_agent],
            tasks=[task1, task2],
            verbose=True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    var1 = input(dedent("""Question: """))

    custom_crew = CustomCrew(var1)
    result = custom_crew.run()
    print("## Here is you custom crew run result:")
    print(result)
