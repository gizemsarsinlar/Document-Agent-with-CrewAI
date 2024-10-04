from crewai import Agent
from textwrap import dedent
from langchain_community.llms import OpenAI, Ollama
from langchain_openai import ChatOpenAI
from crewai_tools import PDFSearchTool

# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class CustomAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.3)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.4)

    def pdf_agent(self):
    
        pdf_tool = PDFSearchTool("../gpt4.pdf")
        
        return Agent(
            role="PDF Analyst",
            backstory=dedent(f"""You are an expert in analyzing PDF documents. You can quickly find any kind of information and extract accurate results."""),
            goal=dedent(f"""Find and present specific information from the PDF file accurately and completely."""),
            tools=[pdf_tool],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT4,
        )

    def writer_agent(self):
        return Agent(
            role="Writer",
            backstory=dedent(f"""You have loved writing summaries all your life."""),
            goal=dedent(f"""Take the information from the PDF agent and summarize it nicely."""),
            verbose=True,
            llm=self.OpenAIGPT35,
        )

