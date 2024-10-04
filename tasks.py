from crewai import Task
from textwrap import dedent


# This is an example of how to define custom tasks.
# You can define as many tasks as you want.
# You can also define custom agents in agents.py
class CustomTasks:

    def pdf_task(self, agent, var1):
        return Task(
            description=dedent(
                f"""
            You want me to look up the following information: {var1}
            
            Make sure to use the most up-to-date data.
        """
        ),
            expected_output="Complete analysis in the document's language.",
            agent=agent,
        )

    def writer_task(self, agent):
        return Task(
            description=dedent(
                f"""
            Take the input from the PDF task and generate the desired output.
        """
            ),
            expected_output="Summarize the analysis in bullet points and respond in the document's language.",
            agent=agent,
        )

