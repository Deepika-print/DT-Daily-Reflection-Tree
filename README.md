# Daily Reflection Tree - Fellowship Assignment

## Project Overview
This project is a deterministic decision tree designed to guide users through a daily reflection process. It follows a structured logic path to help users identify blockers, celebrate wins, and plan for continuous growth.

Developed for the **DeepThought CultureTech Fellowship**.

## 🛠 Tech Stack
- **Language:** Python 3.x
- **Architecture:** Data-Driven Deterministic Logic (JSON + Python Engine)

## 🧠 Thought Process & Methodology
I approached this assignment by separating the **Logic (Data)** from the **Execution (Code)**.

### 1. Deterministic Guardrails
To prevent AI hallucination or "logical drift," I used a JSON schema to define the decision nodes. This ensures:
- The path is 100% predictable.
- The user cannot reach an undefined state.
- The reflection follows a specific pedagogical flow designed for self-improvement.

### 2. Guarding Against Hallucination
During the design phase, I used AI to brainstorm reflection prompts. However, I manually audited every prompt to ensure they followed the **Socratic Method**. I implemented a "Strict Input" policy in the code—rejecting non-numerical or out-of-range inputs—to maintain the integrity of the data collection.

### 3. Disagreements with AI
The AI initially suggested a recursive function for the tree. I disagreed and chose a **While Loop with State Tracking** instead. 
*Reasoning:* Recursion in a long reflection could lead to stack overflow issues and make it harder to "save state" if this were to be expanded into a web app later.

## 📁 Project Structure
```text
DailyReflectionTree/
├── main.py              # Entry point for the application
├── tree_engine.py       # Core logic for navigating nodes
├── data/
│   └── reflection_nodes.json  # The decision tree structure
└── README.md            # Documentation
## 🚀 How to Run

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Deepika-print/DT-Daily-Reflection-Tree.git]
2. **Navigate to the folder:**
   ```Bash
   cd DT-Daily-Reflection-Tree
3. **Run the script:**

   ```Bash
   python main.py
