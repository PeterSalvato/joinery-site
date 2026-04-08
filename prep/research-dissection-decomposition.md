# Research Dissection: Prompt Decomposition vs. Harness Engineering

**Status:** STAGED / PREP
**Objective:** A rigorous comparison of Joinery's methodology against Anthropic's "Harness Engineering," grounded in cognitive science and LLM research.

---

## 1. The Cognitive Load Problem (Sweller's Law)
Both frameworks address **Cognitive Load Theory (Sweller, 1988)**. In humans, "extraneous load" occurs when a task's structure forces the brain to process information that doesn't contribute to the learning goal.

- **The Anthropic "Harness" View:** Treats load as a **Technical Bottleneck**. If the model's context window is full, or the "Planner" is also the "Coder," the system crashes or "hallucinates." The fix is **State Externalization** (Feature Lists) to clear the model's "working memory."
- **The Joinery "Decomposition" View:** Treats load as a **Processing Reality**. Drawing from **special education pedagogy**, we see the AI as having a specific **Processing Profile**. A compound prompt (Strategy + Visuals + Voice) is a "Compound Instruction." 
- **The Research:** *Zhou et al. (2022)* demonstrated "Least-to-Most Prompting," proving that LLMs can solve complex problems only when they are decomposed into sub-problems. Joinery applies this to **Open-Ended Creative Problems**, where the sub-problems are "Dimensions of Identity."

---

## 2. The Evaluator Paradox (The "Consensus" Trap)
Anthropic relies on a **Generator-Evaluator Split** (where Agent B judges Agent A). 

- **The Technical Risk:** In coding (Anthropic’s primary use case), there is an "Inviolable Test" (Does it compile?). The Evaluator has a ground truth.
- **The Creative Risk:** In design, there is no ground truth. When Agent B (AI) evaluates Agent A (AI), they suffer from **Regression to the Mean**. 
- **The Research:** *Huang et al. (2023)* found that LLMs struggle with "Self-Correction" in the absence of external feedback. They often "correct" a unique, divergent idea back into a safe, probable consensus.
- **Joinery’s Better Way:** We decompose to **Isolate for Human Judgment**. We don't want the AI to "Harness" itself into a consensus. We want the Specialist to provide a "Deep Raw Material" (Divergent Thinking) so the **Human Creative Director** can provide the "Synthesis" (Convergent Judgment).

---

## 3. Structural Priming and Voice (The Identity Gap)
Anthropic's harness is "Voice-Agnostic." It wants the code to be "Correct." Joinery’s decomposition is "Voice-Critical."

- **The Research:** *Bock (1986)* on **Structural Priming** shows that the *form* of an input heavily influences the *form* of the output. 
- **The Harness Problem:** A technical harness usually provides a "Structured Template" (JSON, Markdown). This structure "primes" the AI to sound like a technical manual.
- **The Joinery Solution (Week 3: Voice Governance):** We treat voice as a **Structural Dimension**, not a stylistic layer. By decomposing "Content" from "Voice," we prevent the "Content" from priming the "Voice" into a generic default.

---

## 4. The Synthesis Ceiling (Directorial vs. Agentic)
Anthropic’s goal is an **Agent** (Autonomous). Joinery’s goal is a **Synthesis** (Directed).

- **Dreyfus Model of Skill Acquisition:** AI currently sits at the "Competent" level—it can follow rules and harnesses. "Expertise" requires the ability to see the "Whole" and make intuitive, non-rule-based leaps.
- **Why Joinery is Better:** A "Harness" attempts to automate the synthesis through a "Coordinator Agent." This results in a "Unified Brief" that is a **Logical Average**.
- **The Peter-Level Synthesis:** Joinery acknowledges that **Synthesis IS the Creative Act**. We decompose specifically to provide the CD with high-resolution "blocks." The human's job is to see the "Whole" that the "Specialists" cannot see.

---

## Summary for Launch Narrative:
"Anthropic built a harness to keep their AI from failing at code. We built a decomposition methodology to keep our AI from failing at identity. 

A harness is a cage built for reliability. Decomposition is a room built for depth. When you isolate the dimensions of a task, you don't just get better results; you get the raw material needed for real creative direction. 

**Don't build a harness. Build a squad of specialists, and learn how to direct them.**"
