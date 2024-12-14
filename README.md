# Multi-Agent Architecture for Market Research & AI Use Case Generation

## Overview
This project is a Multi-Agent System designed to conduct market research, understand an industry or company's operations, and generate actionable AI and Generative AI (GenAI) use cases. The system focuses on leveraging AI/ML and GenAI solutions to enhance operational efficiency and improve customer experience. The output includes actionable insights, proposed use cases, and resource assets (e.g., datasets and tools).

## Features
1. **Industry and Company Research**
   - Analyzes the company’s industry and identifies key offerings and strategic focus areas.
   - Provides a vision and detailed insights into the company’s operational goals.

2. **Market Standards & Use Case Generation**
   - Identifies trends and standards in the target industry.
   - Proposes relevant AI, ML, and GenAI use cases to improve processes, customer satisfaction, and operational efficiency.

3. **Resource Asset Collection**
   - Collects datasets and tools for the generated use cases from platforms like Kaggle, HuggingFace, and GitHub.
   - Saves resource links in a markdown or text file.

4. **Final Proposal**
   - Provides a list of actionable use cases aligned with the company’s operational goals.
   - Includes references for use case suggestions.
   - Offers clickable links to relevant datasets and resources.

5. **[Optional] GenAI Solutions**
   - Suggests additional GenAI solutions such as document search, automated report generation, and AI-powered chat systems.

---

## Architecture
The system leverages a Multi-Agent Architecture with the following key agents:

### 1. **Industry/Company Research Agent**
   - **Goal:** Research the industry and segment the company operates in.
   - **Responsibilities:**
     - Use web tools to gather insights on the industry.
     - Identify key offerings and strategic focus areas of the company.
     - Provide a detailed report on the industry and company.

### 2. **Market Standards & Use Case Generation Agent**
   - **Goal:** Analyze industry trends and generate relevant use cases.
   - **Responsibilities:**
     - Analyze AI/ML and automation trends in the industry.
     - Propose GenAI and ML use cases for enhancing operations and customer satisfaction.
     - Save generated use cases in a structured format.

### 3. **Resource Asset Collection Agent**
   - **Goal:** Collect datasets and tools for the proposed use cases.
   - **Responsibilities:**
     - Search for relevant datasets and tools on Kaggle, HuggingFace, and GitHub.
     - Save resource links in a markdown or text file with clickable links.

---

## Installation

### Prerequisites
- Python 3.10+
- Install dependencies using `pip`:

```bash
pip install -r requirements.txt
```

### Clone the Repository
```bash
git clone https://github.com/your-repo/multi-agent-ai-usecase
cd multi-agent-ai-usecase
```

---

## Usage

### 1. Run the Streamlit App
Launch the app to interact with the Multi-Agent System.

```bash
streamlit run app.py
```

### 2. Input Details
Provide the following inputs in the sidebar:
- Company Name
- Industry Type (e.g., Automotive, Manufacturing, Finance, Retail, Healthcare)

### 3. Generate Use Cases
- Click the **"Generate Use Cases"** button to start the process.
- The agents will:
  1. Research the company’s industry and key offerings.
  2. Generate AI/ML use cases based on industry trends.
  3. Collect resource links for the use cases.

---

## Output

### Final Proposal
The app will provide:
1. **Industry Research**: Detailed insights about the industry and company.
2. **Generated Use Cases**: Actionable AI/ML and GenAI use cases.
3. **Resource Assets**: Clickable links to relevant datasets and tools.
4. **Optional GenAI Solutions**: Proposals for GenAI solutions such as document search, automated reporting, and chat systems.

---

## Example Output

### Industry Research
```
Industry: Retail
Company: ABC Corp
Key Offerings: Supply Chain Management, Customer Analytics, eCommerce Solutions
Strategic Focus: Enhancing customer experience and optimizing logistics.
```

### Generated Use Cases
```
1. Predictive Analytics for Inventory Management
2. Personalized Customer Recommendations using GenAI
3. Automated Customer Support with AI-Powered Chatbots
```

### Resource Assets
```
1. [Kaggle Dataset: Retail Sales Analytics](https://www.kaggle.com/retail-sales-dataset)
2. [HuggingFace: Transformer Models for Customer Analytics](https://huggingface.co/transformers)
3. [GitHub: AI-Powered Chatbot Framework](https://github.com/ai-chatbot-framework)

