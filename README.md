# PDF Analysis and Summary Agent Project

## Project Overview

This project is designed to utilize two custom agents: one for analyzing PDF documents and another for summarizing the results. The agents are implemented using the `crewai` library and work together to extract relevant information from a PDF file and generate a concise summary based on that information.

### Agents

There are two primary agents in this project:
1. **PDF Analyst Agent**: Analyzes PDF documents and retrieves specific information.
2. **Writer Agent**: Takes the information gathered by the PDF Analyst and generates a structured summary.

### Agent Roles and Responsibilities

#### PDF Analyst Agent

- **Role**: PDF Analyst
- **Backstory**: This agent is an expert in analyzing PDF documents and can quickly find relevant information.
- **Goal**: Its primary goal is to search the PDF for specific information and return accurate results. The PDF file to analyze is provided via the `PDFSearchTool`.
- **Tools**: The agent uses a tool called `PDFSearchTool` to access and search the PDF document.
  
Here’s how the PDF Analyst is defined in the code:

```python
def pdf_agent(self):
    
    pdf_tool = PDFSearchTool("../file.pdf")
    
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
