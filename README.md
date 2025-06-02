# 📚 StudyBuddy – Smart Learning Assistant with MCP

 An interactive learning assistant that uses open-source LLMs and modular tools via MCP to help students study smarter, not harder.

## 🎯 Project Goal
Build an intelligent agent that students can chat with to:  
- Summarize lessons
- Quiz themselves
- Create flashcards
- Explain difficult concepts
- Generate study schedules

All tools are dynamically exposed using Model Context Protocol (MCP), making the system modular and extensible.  

## 🧠 Core Tech Stack  
- LLM Agent: TODO

- MCP Server: Streamlit + tools implemented as callable Python functions

- MCP Client: Some kind of agentic framework with an agent capable of tool invocation

- Frontend: Streamlit demo for student interaction


## 🔧 MCP Tools
1. `summarize(text)`  
Converts a lecture or textbook excerpt into bullet points or key takeaways.  


Could optionally support modes like simple, technical, exam-ready.


2. `generate_flashcards(topic)`  
Returns Q&A pairs on the given topic.  


Could be formatted as {"question": "...", "answer": "..."} for easy integration into flashcard apps like Anki.


3. `quiz_me_on(topic)`  
Dynamically creates a short quiz (multiple choice or short answer).  


Supports difficulty levels: easy, medium, hard.


4. `explain(term)`  
Provides a simplified explanation, optionally tailored to high school, college, or beginner.


5. `study_plan(topics, days)`
Builds a study schedule over the specified number of days.


Returns a breakdown like:

```json
{
  "Day 1": ["Intro to Calculus", "Basic Derivatives"],
  "Day 2": ["Chain Rule", "Product Rule"]
}
```



## 💬 Example Conversation
User: I have an exam on biology next week. Can you help me plan my study?  
 Agent: Sure! How many days do you have to prepare and which topics are you covering?  
 User: 5 days. Topics: cell structure, mitosis, photosynthesis, DNA replication.  
 Agent: Great! Here's your custom 5-day study plan...   

🏗️ Architecture
```text
+----------------+          +--------------------+         +----------------------+
|   Chat UI       | --->         |  Agent  |       --->       |  MCP Tools |
+----------------+          +--------------------+         +----------------------+
                                      ^                             |
                                      |    dynamic tool discovery   |
                                      +-----------------------------+
```

## 🧪 Bonus Features (Stretch Goals)
Memory & Progress Tracking: Store what users have already reviewed

Voice Input: voice-based queries


Teacher Mode: Suggest activities and materials for teachers to share



## 🚀 Use Cases
- Self-learners prepping for exams


- High school and college students


- Homeschooling setups


## 📁 Suggested Folder Layout
```text
studybuddy/
├── client.py               # The agent interface 
├── server.py               # MCP server with all study tools
├── tools/
│   ├── flashcards.py
│   ├── quiz.py
│   ├── explain.py
│   └── summarize.py
├── mcp.json
├── .env
├── requirements.txt
└── README.md
```

## More on tools:

### 🧠 Learning & Study Tools
`concept_mapper(text)`


 Extracts key concepts and maps relationships between them (e.g. concept graph as JSON).



`compare_terms(term1, term2)`  Side-by-side comparison (e.g. mitosis vs meiosis, socialism vs capitalism).



`generate_mnemonic(term)`


 Creates a simple memory aid for remembering definitions or lists.



`define_acronym(acronym)`


 Decodes and explains common academic acronyms (e.g. GDP, DNA, AI).



`term_translator(term, level)`


 Translates complex terms into different difficulty levels (beginner, advanced, etc.).



`visual_explainer(concept)`


 Returns a simple diagram or link to a visual for the concept (e.g., cell structure, math formula).



`study_timer(duration, break_time)`


 Starts a Pomodoro timer and sends reminders (requires Gradio+JS or browser extension).




### 📝 Writing & Reading Tools
`thesis_statement_helper(topic)`


 Generates a sample thesis statement based on a research topic.



`rewrite_for_clarity(text)`


 Rewrites dense or confusing writing into clearer, simpler prose.



`highlight_key_sentences(text)`


Outputs the most important sentences from a paragraph or page.
`tone_analyzer(text)`


Analyzes tone of writing (academic, casual, persuasive, etc.).
`citation_generator(text, style)`


Extracts sources and formats them in MLA/APA/Chicago/etc.

### 🧪 STEM Tools
`math_solver(equation)`


Solves algebra, calculus, or linear equations step-by-step.
`unit_converter(value, from_unit, to_unit)`


Converts units (kg to lbs, cm to inches, etc.).
`physics_formula_explainer(formula)`


Explains what a physics formula does and where it's used.
`periodic_table_lookup(element)`


Returns info about an element (symbol, atomic number, group, uses).
`graph_equation(equation)`


Returns a plot of a math function (could use matplotlib + Gradio image output).

### 🌍 Language & Translation Tools
`translate_phrase(phrase, language)`


Translate a phrase into another language (French, Spanish, German...).
`conjugate_verb(verb, tense, language)`


Returns verb conjugation tables.
`grammar_corrector(text)`


Detects and fixes grammar issues in a sentence.
`reading_level_estimator(text)`


Classifies the reading level (Flesch-Kincaid or grade level).

### 🧘 Study Wellness / Meta-Learning

`suggest_break_activity()`


Suggests a 5-minute physical or mental refresh activity.

`track_focus(daily_minutes)`


Logs time spent studying and gives weekly summaries (with basic state handling).

`motivate_me(topic)`


Returns quotes or success stories about mastering difficult subjects.

`study_tips(subject)`


Provides topic-specific study strategies (e.g., “how to study chemistry”).

