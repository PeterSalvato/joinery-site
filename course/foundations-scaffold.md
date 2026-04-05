# Foundations Course: Complete Scaffold

3 weeks. 3 domains. 18 lessons. 3 deliverables.

Each week follows the same classroom rhythm: Demo (teacher shows), Guided Practice (student does it with structure), Independent Practice (student does it alone). Each week produces a deliverable. The weeks scaffold: Week 2's output becomes Week 3's source material.

---

## INTRO: Before You Start

**Format:** Written page (landing page for the course)

**What the student needs to know:**

- This course teaches three techniques. Each one changes how you use AI for creative work. Together they form a personal methodology you own.
- You do not need a specific AI tool. Any general-purpose LLM works (ChatGPT, Claude, Gemini, etc.). The techniques are model-agnostic.
- You need a recording device for voice notes. Your phone works. A dedicated recorder works. Anything that captures you talking.
- You need a text editor or document tool. Google Docs, Notion, a plain text file. Wherever you keep working documents.
- Each week has 6 lessons. The first 3 are demos (you watch and read). The next 2 are guided practice (you do it with scaffolding). The last is independent practice (you do it alone and submit a deliverable).
- A deliverable is a before-and-after comparison showing the technique applied to your own work. You submit it at the end of each week.
- The course takes roughly 3-6 hours per week depending on how deep you go with your own material.

**Production notes:**
- WRITE: Full intro copy (Peter writes this, sets the tone for the course)
- COMPILE: Tools list, submission instructions (operational, can be templated)

---

## WEEK 1: TASK DECOMPOSITION

**Core lesson:** You are the creative director of a team of specialists. The AI gives you depth. You provide the coherence. The synthesis step (where you resolve conflicts between independent outputs) is where your judgment becomes the product.

---

### Lesson 1.1 — The Frame Break

**Phase:** Demo
**Format:** Video intro (Peter on camera)
**Learning objective:** The student recognizes that longer, more detailed prompts are not the solution to mediocre AI output.

**Content outline:**
- Cold open: the moment every creative hits. The prompt keeps getting longer. You add more context, more constraints, more instructions. The output gets slightly better but never good. You're negotiating with a system instead of directing it.
- The instinct is wrong. More instructions in a single prompt is not "being more specific." It's overloading a single worker with a job that needs a team.
- Frame the week: you're going to learn why compound prompts degrade, see the difference decomposition makes on a real project, and then do it yourself.
- No jargon. No slides. Direct address. 3-5 minutes.

**Artifact/example referenced:** None (this is the hook, not the demo)
**Cognitive science citation:** None (introduced in 1.2)
**Deliverable:** None

**Production notes:**
- WRITE: Script (Peter writes and performs this, it's the course's first impression)

---

### Lesson 1.2 — The Compound Instruction Problem

**Phase:** Demo
**Format:** Written lesson
**Learning objective:** The student can explain why compound prompts produce shallow output, citing both the serial position effect and cognitive load theory.

**Content outline:**
- Start with the Voss Type compound prompt. Show the full prompt: a single request asking for color palette, typography, logo direction, imagery guidelines, and layout principles simultaneously.
- Show the compound output. It's competent. It's a B+. Point out what's good about it: coherent, complete, professional. This is not garbage. That's what makes it dangerous. It looks done.
- Explain why it's shallow:
  - **Serial position effect (Murdock 1962, Liu et al. 2024):** Both humans and LLMs process information at the beginning and end of a long input better than the middle. In a compound prompt, the middle instructions (typography, logo) get less attention than the first (color) and last (layout). Liu et al. showed a 30%+ accuracy degradation for middle-positioned information in LLMs.
  - **Cognitive load theory (Sweller 1988, Cowan 2001):** Human working memory handles 2-4 novel items concurrently. LLMs have an analogous attention budget. A compound prompt asking for 5 dimensions forces the model to distribute attention across all of them, giving each one a fraction of its capacity.
  - **The classroom parallel:** A teacher who assigns five unrelated tasks in one sentence gets worse results than a teacher who assigns them sequentially. Not because the students are stupid. Because concurrent processing degrades performance. Same principle.
- The compound prompt made the AI the creative director. It decided how all five dimensions relate. One perspective, one pass, one set of creative decisions. The coherence is also the ceiling.

**Artifact/example referenced:** compound-prompt-demo.md, Part 1 (compound prompt and output)
**Cognitive science citation:** Liu et al. 2024 (serial position in LLMs), Murdock 1962 (serial position in humans), Sweller 1988 (cognitive load theory), Cowan 2001 (working memory capacity)
**Deliverable:** None

**Production notes:**
- WRITE: Narrative framing, the "why it's dangerous" angle, classroom parallel (Peter writes)
- COMPILE: Compound prompt and output from artifact (exists), cognitive science summaries from references doc (exists, needs editing for student audience)

---

### Lesson 1.3 — The Decomposition

**Phase:** Demo
**Format:** Written lesson
**Learning objective:** The student can identify the structural differences between compound and decomposed outputs and explain why independent specialist prompts produce deeper results.

**Content outline:**
- Show the five decomposed prompts. Each one addresses a single dimension. Each one is given only the brief and told to ignore the other dimensions.
- Show the five decomposed outputs side by side with the compound output. Section by section:
  - **Color:** Compound gave 6 colors with rationale. Decomposed added a conditional fifth color with restraint logic and explained the palette as a two-color print job structure mirroring how the client's industry actually produces packaging.
  - **Typography:** Compound gave 2 pairings. Decomposed gave 3 complete pairing options with a recommendation and context-specific reasoning for when each works best.
  - **Logo:** Compound described a mark. Decomposed described what the mark needs to feel like and why. "The ratio of control to roughness." Reproducibility on a napkin. Printer's marks from the 1500s as structural precedent.
  - **Imagery:** Compound gave general photography guidelines. Decomposed specified scanning DPI, case study image minimums, a 60/40 process-to-finished ratio for social media, and distinguished between scanning and photographing hand-drawn work.
  - **Layout:** Compound gave standard web layout advice. Decomposed introduced rotational micro-offsets, imperfect alignment as intentional design, edge bleed as compositional tool, and the principle "tight until it hurts, then tighter."
- The structural difference: each specialist went deeper because it wasn't splitting attention across five dimensions. The model's full capacity pointed at one problem.
- But there's a new problem. Five independent outputs. They don't talk to each other. The typography specialist might push in a direction that conflicts with the layout specialist. The color palette might imply a different mood than the imagery guidelines suggest. Nobody is in charge.
- That's Lesson 1.4. You are.

**Artifact/example referenced:** compound-prompt-demo.md, Part 2 (all five decomposed prompts and outputs) and Part 3 (comparison)
**Cognitive science citation:** Ridnik et al. 2024 (AlphaCodium: 19% to 44% accuracy through decomposition), Andrew Ng 2024 (GPT-3.5 decomposed outperforming GPT-4 compound), Wei et al. 2022 (chain-of-thought as lightweight decomposition)
**Deliverable:** None

**Production notes:**
- WRITE: Narrative framing, the side-by-side commentary, the "but there's a new problem" pivot (Peter writes)
- COMPILE: All five decomposed outputs from artifact (exists), comparison analysis from artifact (exists, needs tightening)

---

### Lesson 1.4 — The Synthesis Step

**Phase:** Guided Practice
**Format:** Written lesson + Exercise
**Learning objective:** The student can synthesize independent specialist outputs into a unified brief by resolving conflicts, finding amplifications, and setting cross-system rules.

**Content outline:**
- Open with the synthesized Voss Type brief. Show what it looks like when a human creative director reads all five specialist reports and makes the decisions:
  - **Conflicts resolved:** The typography specialist recommended Knockout (Hoefler) while the layout specialist assumed a grotesk. The creative director chose Druk Wide from Pairing 1 because the layout's "tight until it hurts" philosophy needs a typeface that holds under compression. Knockout is wide. Druk is wide but compressed. That's the call.
  - **Amplifications found:** The color specialist's "two-color print job" logic and the imagery specialist's "shoot on real substrates" converge. Both point toward a brand that looks printed even on screen. That convergence wasn't in either output. The human saw it.
  - **Cross-system rules set:** The logo specialist said "reproducible by hand on a napkin." The typography specialist said "hand-lettered display for all recurring headers." These are two versions of the same rule: the human hand is visible everywhere. That becomes a governing principle, not just two separate recommendations.
- Explain what the human did that neither the compound output nor the individual outputs could do:
  - Read across domains (the AI couldn't because each prompt was isolated)
  - Detected convergences and tensions (requires understanding the project holistically)
  - Made judgment calls where specialists disagreed (this is creative direction)
  - Set hierarchy (which specialist's recommendation governs when they conflict)
- **Exercise:** Provide a pre-built set of 3 decomposed outputs for a different fictional project (a podcast brand identity: name direction, visual identity, episode format). The outputs contain two planted conflicts and one amplification. Student follows a guided synthesis template:
  1. Read all outputs. Highlight where they agree.
  2. Identify where they conflict. Write down the conflict in one sentence.
  3. For each conflict, decide which output governs and why.
  4. Identify any amplifications (convergences neither output stated explicitly).
  5. Write a 1-page synthesized brief incorporating your decisions.

**Artifact/example referenced:** compound-prompt-demo.md, Part 3 (comparison section, adapted into a synthesis narrative). Note: the synthesized brief itself needs to be WRITTEN; the artifact shows the comparison but not the synthesis.
**Cognitive science citation:** Wong et al. 2014 (task analysis as evidence-based practice in education, applied here as the pedagogical model for the guided exercise structure)
**Deliverable:** Completed synthesis brief for the provided example (not submitted, practice only)

**Production notes:**
- WRITE: The synthesized Voss Type brief showing conflict resolution, amplification, and cross-system rules (Peter writes this, it's the key teaching artifact for the course's core claim)
- WRITE: The guided exercise scenario (3 decomposed outputs for a podcast brand, with planted conflicts) (Peter writes or closely directs)
- COMPILE: Synthesis template structure (can be templated from the 5-step process above)

---

### Lesson 1.5 — Decompose Your Own Work

**Phase:** Guided Practice
**Format:** Exercise
**Learning objective:** The student can decompose one of their own compound prompts into independent specialist prompts and document the difference in output quality.

**Content outline:**
- Student picks one compound prompt from their own work. Any domain. Any project. The only requirement: it must be a prompt they've actually used that asks for multiple things at once.
- Follow a structured decomposition template:
  1. Paste your compound prompt.
  2. List every distinct task or dimension the prompt asks for. Number them.
  3. For each task, write a standalone prompt that addresses only that dimension. Give it only the context it needs and explicitly tell it to ignore other dimensions.
  4. Run the compound prompt. Save the output.
  5. Run each decomposed prompt independently. Save the outputs.
  6. Compare: Where is the decomposed output deeper? Where does the compound output have better coherence? What conflicts exist between the decomposed outputs?
- Student documents the comparison in a provided template:
  - Original compound prompt
  - Compound output (key excerpts)
  - Decomposed prompts (all)
  - Decomposed outputs (key excerpts)
  - Where the decomposed version was deeper (specific examples)
  - Where conflicts or tensions appeared between specialists
  - What you would synthesize differently from what the compound version decided

**Artifact/example referenced:** Decomposition template structure mirrors the Voss Type demo from 1.2-1.3
**Cognitive science citation:** Zhou et al. 2022 (least-to-most prompting: decomposition enables results that are impossible in a single step)
**Deliverable:** None (this is practice; 1.6 is the deliverable)

**Production notes:**
- WRITE: Template introduction and framing (Peter writes)
- COMPILE: Decomposition template (structured from the steps above, operational)

---

### Lesson 1.6 — Week 1 Deliverable: The Full Cycle

**Phase:** Independent Practice
**Format:** Exercise + Deliverable
**Learning objective:** The student can independently decompose a compound workflow, run both versions, synthesize the decomposed outputs, and articulate what their judgment added.

**Content outline:**
- Student picks a second workflow from their own work. Different project than 1.5. No template this time.
- The full cycle:
  1. Identify a compound prompt or workflow.
  2. Decompose it into independent specialist prompts.
  3. Run both versions (compound and decomposed).
  4. Synthesize the decomposed outputs into a unified brief. Resolve conflicts. Find amplifications. Set cross-system rules.
  5. Compare the compound output to the synthesized brief.
- Submit:
  - The compound prompt and its output (before)
  - The decomposed prompts and their individual outputs
  - The synthesized brief (after)
  - A short reflection (3-5 sentences): What did the synthesis step require from you that neither the AI compound output nor the individual specialist outputs could provide?

**Artifact/example referenced:** None (student's own work)
**Cognitive science citation:** Andrew Ng 2024 (the architecture of the input matters more than the capability of the model, student now has personal evidence for this claim)
**Deliverable:** Before (compound output) and After (synthesized brief) with reflection. This is the Week 1 submission.

**Production notes:**
- WRITE: Submission instructions and reflection prompt (Peter writes the reflection prompt, it needs to point at the right insight)
- COMPILE: Submission format template (operational)

---

## WEEK 2: INPUT INVERSION

**Core lesson:** Use AI as a thinking partner that holds your mess while you figure out what you think. The machine does not ideate. You ideate. The machine holds the whiteboard. The raw material is richer because it is unstructured. The ideas are yours because they came from your brain, not from a prompt.

**Input hierarchy:** Talking/dictation (richest) > unconstrained typing > careful structured prompts (least rich). Premature structure compresses what makes your thinking yours.

---

### Lesson 2.1 — The Input Problem

**Phase:** Demo
**Format:** Video intro (Peter on camera)
**Learning objective:** The student recognizes that better prompts still produce generic output because the problem is the input, not the instructions.

**Content outline:**
- Brief close on Week 1: you learned to decompose tasks and synthesize outputs. You're now the creative director. That's real. But there's a problem even decomposition doesn't solve.
- The problem: even well-structured prompts produce output that sounds like it could have come from anyone. The ideas are competent. They're also interchangeable. A different designer with the same prompt would get functionally the same result.
- Why: the prompt is the input, and prompts are structurally impoverished. They compress your thinking into instructions. Everything messy, specific, and personal gets stripped out before the AI sees it.
- Frame the week: you're going to flip the input. Instead of structuring your thinking into a prompt, you're going to dump your raw thinking and let the AI do the structuring.
- 3-5 minutes. Direct address. No slides.

**Artifact/example referenced:** None (this is the hook)
**Cognitive science citation:** None (introduced in 2.2)
**Deliverable:** None

**Production notes:**
- WRITE: Script (Peter writes and performs)

---

### Lesson 2.2 — Three Levels of Input Quality

**Phase:** Demo
**Format:** Written lesson
**Learning objective:** The student can distinguish between standard, harnessed, and inverted input and identify why inverted input produces singular output.

**Content outline:**
- The Night Owl Brewing scenario. Portland craft brewery, dark beers, taproom with live music, founder Tomas Kowalski (former music venue promoter).
- **Standard input:** "Give me 10 creative concept directions for a craft brewery rebrand." Show the output. Ten generic concepts. The Observatory. Old Growth. Ash and Ember. Any AI would produce these for any brewery. A competing brewery in Denver would get 7 of the same 10.
- **Harnessed input:** Role assignment, competitive context, founder backstory, explicit constraints (no nature cliches, no industrial-rustic). Show the output. The Green Room. Setlist. The Backline. Significantly better. The constraints worked. But these are still the AI's ideas, organized by AI logic. The AI identified "music venue + brewery = music-themed brewery branding" and executed that logic competently. Another AI with the same constraints would produce similar results.
- **Inverted input:** Mara Voss recorded a 12-minute brain dump talking through her raw thinking about the project. Unstructured. Full of tangents. The Polish jazz covers on the wall. The founder's terrible handwriting on the chalkboard menus. "Not goth-dark. Jazz-club-at-midnight dark." The AI was told: do NOT generate concept ideas. Identify what the designer has already figured out. Synthesize her thinking. Tell her what she said.
- Show the inverted output. "Dark is the entire positioning, not just a beer descriptor." "The origin story is inverted: he runs a venue that brews." "The Polish jazz covers are an attitude, not a style reference." "Your job is translation, not invention."
- The comparison table: Standard (AI pattern matching, generic, disposable), Harnessed (AI reasoning with constraints, targeted, presentable), Inverted (designer's own thinking, singular, foundational).
- The key insight: the inverted output could not have come from any prompt because it came from a specific person's observations in a specific taproom on a specific Tuesday. The input changed. Not the model. Not the prompt engineering. The input.

**Artifact/example referenced:** week2-input-inversion-demo.md, all three parts (standard, harnessed, inverted) and comparison table
**Cognitive science citation:** Kellogg 1996/2008 (writing taxes working memory with planning, translating, and reviewing simultaneously), Chi 1994/2000 (self-explanation produces deeper understanding than silent organization)
**Deliverable:** None

**Production notes:**
- WRITE: Narrative framing and transitions between the three levels (Peter writes)
- COMPILE: All three prompts and outputs from artifact (exists), comparison table from artifact (exists)

---

### Lesson 2.3 — Why Unstructured Input Is Richer

**Phase:** Demo
**Format:** Written lesson
**Learning objective:** The student can explain why reducing structure in the input stage preserves more of the creator's original thinking, using cognitive load, self-explanation, and creative flow research.

**Content outline:**
- This lesson is the "why" behind the demo. Three arguments, each grounded in research:
- **The cognitive load argument (Kellogg 1996/2008):**
  - Writing simultaneously taxes working memory with three demands: planning (what to say), translating (how to say it), reviewing (evaluating what was said). These compete for the same limited resources.
  - When you write a prompt, you're planning your request, translating it into prompt-appropriate language, and reviewing whether it's clear enough for the AI. All simultaneously.
  - When you talk into a recorder, you're only planning. Translation and review happen later, handled by the AI. Lower load during the critical ideation phase means more of your actual thinking makes it through.
- **The self-explanation effect (Chi 1994/2000):**
  - Students who explain material to themselves while learning produce deeper understanding than those who silently organize.
  - A brain dump is self-explanation. When Mara talks through her thinking about Night Owl, she's not recording ideas she already had. She's discovering them through articulation. "That's the whole brand right there actually" came in the middle of a tangent about Polish jazz. She didn't know it until she said it.
  - The AI's synthesis step then captures what the articulation revealed. The ideas were in Mara. The brain dump got them out. The AI organized them.
- **The creative flow argument (Cseh et al. 2015, Osborn 1953, Amabile 1983):**
  - Creative flow thrives on ambiguity and open-endedness. Premature structure kills it.
  - A structured prompt forces premature clarity. You must know what you want before you ask for it. But creative work often starts with not knowing.
  - A brain dump allows tangents, contradictions, half-formed thoughts. These are not noise. They're signal that a structured prompt would filter out.
  - Separating generation from evaluation (Osborn's principle) matters. The brain dump is the no-evaluation zone. The AI synthesis is the evaluation phase. The temporal separation protects the generative phase from premature editing.
- Important clarification: this is NOT "speech is better than writing." Some people think better typing. The principle is: the less you structure the input, the more of you is in it. Unconstrained typing is better than a carefully formatted prompt. Talking is often better than typing because it's harder to self-edit in real time. Find what works for you.

**Artifact/example referenced:** week2-input-inversion-demo.md (Mara's transcript excerpt as illustration of self-explanation in action)
**Cognitive science citation:** Kellogg 1996/2008 (working memory in writing), Chi 1994/2000 (self-explanation effect), Cseh et al. 2015 (creative flow and ambiguity), Osborn 1953 / Amabile 1983 (separating generation from evaluation), Clark & Chalmers 1998 (extended mind, AI as cognitive partner)
**Deliverable:** None

**Production notes:**
- WRITE: Full lesson (Peter writes, this is the conceptual core of Week 2 and needs his voice throughout)
- COMPILE: Research summaries adapted from cognitive-science-references.md (exists, needs rewriting for student audience, remove academic hedging)

---

### Lesson 2.4 — The Brain Dump Protocol

**Phase:** Guided Practice
**Format:** Written lesson + Exercise
**Learning objective:** The student can execute a brain dump, process the transcript through AI synthesis, and compare the result to what a structured prompt would have produced.

**Content outline:**
- **How to record a brain dump:**
  - Tools: phone voice memo, Otter.ai, any transcription app. The tool doesn't matter. The transcript matters.
  - Setup: pick a project you're actively working on. Not a hypothetical. Something with real constraints and real decisions pending.
  - How long: 5-15 minutes. Most people run out of prepared thoughts at 3 minutes. That's when the good stuff starts. The tangents after the prepared material are where the real thinking lives.
  - What to do when you get stuck: describe what you're looking at. Describe what's bothering you. Describe what someone else would get wrong about this project. "The thing nobody understands about this is..." is a productive prompt for yourself.
  - What NOT to do: do not organize your thoughts before recording. Do not make notes. Do not outline. The point is unstructured input. If you structure it first, you've already compressed it.
- **How to process the transcript:**
  - Get the transcript (auto-transcription or manual).
  - The synthesis prompt: "Read this transcript carefully. Do NOT generate new ideas. Identify what I've already figured out. Synthesize my thinking. Tell me what I said. Organize my observations into the key insights, decisions, and open questions I raised."
  - The AI's job is mirror, not generator. It reflects your thinking back in organized form.
- **Guided exercise:**
  - Provided scenario: a fictional interior designer planning a restaurant redesign. A 2-page simulated brain dump transcript is provided (messy, tangential, with buried insights).
  - Student processes the provided transcript using the synthesis prompt.
  - Student then writes a standard structured prompt for the same project (as if they had no transcript).
  - Compare the two outputs. What's in the synthesized brain dump that isn't in the structured prompt output? What specificity, what tangential connections, what half-formed ideas survived the brain dump that would have been compressed or lost in prompt construction?

**Artifact/example referenced:** week2-input-inversion-demo.md Part 3 (the Mara brain dump and synthesis as the model for what the exercise produces)
**Cognitive science citation:** Voice input cognitive load research (35-45% lower cognitive load for dictation vs. typing)
**Deliverable:** None (practice exercise)

**Production notes:**
- WRITE: Brain dump protocol instructions (Peter writes, drawing on his own practice)
- WRITE: The fictional interior designer scenario and simulated transcript (Peter writes or closely directs, needs to be realistic and messy)
- COMPILE: Synthesis prompt template (operational, adapted from the artifact's inverted prompt structure)

---

### Lesson 2.5 — Brain Dump Your Own Project

**Phase:** Guided Practice
**Format:** Exercise
**Learning objective:** The student can record a real brain dump about their own work, process it, and identify what emerged that a structured prompt would not have surfaced.

**Content outline:**
- Student records a real brain dump about one of their own projects. 5-15 minutes. Following the protocol from 2.4.
- Student transcribes and processes it using the synthesis prompt from 2.4.
- Documentation template:
  1. The project (one sentence).
  2. How long you talked.
  3. The processed synthesis (AI output).
  4. Three things that appeared in the synthesis that you did not plan to say. These are the moments where articulation produced discovery.
  5. One thing you would have included in a structured prompt that turned out to be less important than what the brain dump surfaced.
- This is the real test. The provided scenario in 2.4 was practice. This is the student's own thinking about their own work. The gap between "what I would have prompted" and "what the brain dump surfaced" is the lesson.

**Artifact/example referenced:** Mirrors the Mara brain dump workflow from the artifact, now applied to student's own work
**Cognitive science citation:** Chi 1994/2000 (self-explanation: the act of articulating produces understanding that silent organization doesn't)
**Deliverable:** None (but the transcript is saved; it becomes source material for Week 3)

**Production notes:**
- WRITE: Framing for the exercise (Peter writes, short, emphasis on "your transcript becomes Week 3 source material, save it")
- COMPILE: Documentation template (operational)

---

### Lesson 2.6 — Week 2 Deliverable: Your Input Practice

**Phase:** Independent Practice
**Format:** Exercise + Deliverable
**Learning objective:** The student can design a repeatable brain dump practice for their own workflow and produce a documented example of the full input inversion process.

**Content outline:**
- Student builds an input practice for their own workflow. Not a one-time exercise. A practice they can repeat.
- Questions to answer:
  - When do you dump? (Before starting a project? When stuck? Weekly review?)
  - How do you process? (Which synthesis prompt? Do you add follow-up prompts?)
  - What do you capture? (Full synthesis? Just the key insights? A running log?)
  - How does this fit into your existing workflow? (Replaces the prompt-drafting step? Supplements it? Used only for certain kinds of work?)
- Submit:
  - The brain dump transcript (from 2.5 or a new one)
  - The processed synthesis output
  - A description of their input practice (when, how, what, where it fits)
  - A short reflection (3-5 sentences): What emerged from the brain dump that you would not have found through a structured prompt? Why?
- Important note to student: save your brain dump transcript. You will use it in Week 3.

**Artifact/example referenced:** None (student's own work)
**Cognitive science citation:** Flower & Hayes 1981 (knowledge-transforming vs. knowledge-telling: the brain dump enables knowledge-transforming by separating generation from translation)
**Deliverable:** Brain dump transcript, processed synthesis, input practice description, and reflection. This is the Week 2 submission. The transcript also becomes Week 3 source material.

**Production notes:**
- WRITE: Reflection prompt and the "save your transcript" bridge to Week 3 (Peter writes)
- COMPILE: Practice design template and submission format (operational)

---

## WEEK 3: VOICE GOVERNANCE

**Core lesson:** Constraints applied during generation produce structurally different output than constraints applied after. Voice is structural (what you lead with, what you never say, how you sequence ideas), not surface (word choice, sentence length). Extract voice from conversation (how you actually talk), not from published writing (how you perform).

**Week 2's brain dump transcript becomes Week 3's source material.** The weeks scaffold.

---

### Lesson 3.1 — Why All AI Copy Sounds the Same

**Phase:** Demo
**Format:** Video intro (Peter on camera)
**Learning objective:** The student recognizes that generic-sounding AI output is a generation problem, not a style problem, and that post-hoc editing makes it worse.

**Content outline:**
- Brief close on Week 2: you learned to use brain dumps to get richer input. Your ideas are now in the output. But they still don't sound like you.
- The problem: all AI copy has a signature. Em dashes. Epigrammatic closers. Philosophical asides. "At the intersection of." "I believe in." It doesn't matter what you put in the prompt. The AI's structural defaults leak through.
- The instinct is to edit afterward. Fix the voice in post. But editing normalizes. You catch the obvious AI-isms and replace them with your own defaults. The result sounds like neither the AI nor you. It sounds like edited AI.
- Frame the week: you're going to extract your actual voice from how you talk (not how you write), turn it into hard structural rules, and apply those rules during generation so the output never has the AI defaults to begin with.
- 3-5 minutes. Direct address.

**Artifact/example referenced:** None (this is the hook)
**Cognitive science citation:** Baker 1993 / Solum 2018 (editing normalizes toward the editor's defaults, previewed here, detailed in 3.3)
**Deliverable:** None

**Production notes:**
- WRITE: Script (Peter writes and performs)

---

### Lesson 3.2 — Three Levels of Voice Control

**Phase:** Demo
**Format:** Written lesson
**Learning objective:** The student can distinguish between standard, harnessed, and voice-governed output and identify the structural (not just surface) differences.

**Content outline:**
- The task: write an About page for Mara Voss, freelance brand designer and hand-letterer in Brooklyn.
- **Standard:** "Write an About page for Mara Voss, freelance brand designer and hand-letterer in Brooklyn." Show the output. "Find their visual voice." "Intersection of craft and strategy." "I'd love to hear from you." Every freelance designer on the internet has a version of this. Accurate, grammatically correct, completely empty.
- **Harnessed:** Same request plus tone guidelines (bold, direct, no-nonsense), style reference (Jessica Walsh meets punk zine editor), constraints (no jargon, no calls to action, under 200 words). Show the output. Better. Short sentences work. Client list is specific. But two AI tells remain: "I believe in the tool" (philosophical in a way working designers wouldn't be; the AI performing depth) and the epigrammatic closer ("If your brand needs a voice that looks like it means what it says"). The AI defaults leaked through the tone guidelines.
- **Voice governance:** 12 hard rules extracted from Mara's actual speech (the brain dump from Week 2). Not tone adjectives. Structural constraints. Show the rules. Show the output. "Right now I'm finishing a set of packaging labels for a hot sauce company in Austin." Opens with current work, not self-introduction (Rule 1). No em dashes (Rule 2). Physical vocabulary: ink, nib, push, catches (Rule 3). "Most people hate that. I use it." Direct, not hedged (Rule 4). Named tools: Nikko G nib, Rhodia pads, 1200 DPI (Rule 9). Marian Bantjes reference, unprompted, mid-thought (Rule 11). No closing invitation. Ends with a thought about work (Rule 7).
- The comparison table. Standard: sounds like AI. Harnessed: sounds like better AI. Voice governance: sounds like a person. The structural difference: voice rules target the layer where voice actually lives (function words, discourse architecture, openings, closings), not the layer where AI mimicry operates (content words, tone adjectives).

**Artifact/example referenced:** week3-voice-governance-demo.md, all three parts and comparison table
**Cognitive science citation:** Slamecka & Graf 1978 (generation effect: generating under constraints produces structurally different output), Bock & Loebell 1990 (structural priming: syntactic structures prime subsequent output)
**Deliverable:** None

**Production notes:**
- WRITE: Narrative framing, the "two AI tells" analysis of the harnessed output, the rule-by-rule walkthrough of the governed output (Peter writes)
- COMPILE: All three prompts and outputs from artifact (exists), voice rules from artifact (exists), comparison table from artifact (exists)

---

### Lesson 3.3 — Voice Is Structural, Not Stylistic

**Phase:** Demo
**Format:** Written lesson
**Learning objective:** The student can explain why voice governance rules target structural patterns rather than stylistic adjectives, and why post-hoc editing normalizes rather than preserves voice.

**Content outline:**
- **What makes writing sound like a specific person (Pennebaker & King 1999):**
  - Individual voice is carried primarily by function words: pronouns, articles, prepositions, conjunctions. These are processed below conscious awareness.
  - Content words carry meaning. Function words carry identity.
  - Telling the AI to "sound bold and direct" targets content-level mimicry. Constraining structural patterns (sentence rhythm, opening patterns, vocabulary domains, what you never tolerate) targets the layer where voice actually lives.
- **Why "write in my voice" fails:**
  - It gives the AI a goal without structural guidance. The model has to guess what your voice sounds like. It guesses based on statistical patterns for "bold direct designer," which is the same guess it makes for every bold direct designer.
  - Mara's Rule 9 (names tools by brand: Nikko G nib, sumi ink, Rhodia pad) can't be derived from "bold and direct." It's specific to her. Rules derived from actual speech are specific. Tone adjectives are generic.
- **Why post-hoc editing normalizes (Baker 1993, Solum 2018):**
  - Baker studied literary translators. Their stylistic fingerprints systematically override the source text's voice. The translator's defaults replace the author's.
  - Editing AI output does the same thing. You catch the AI-isms and replace them with your editorial defaults. The result is neither the AI's voice nor yours. It's the voice of editing.
  - Voice governance prevents normalization by making the AI's defaults structurally unavailable. You can't normalize toward an em dash pattern if em dashes are prohibited. You can't default to an epigrammatic closer if closers are forbidden.
- **Why 12 specific rules succeed (Stokes 2005):**
  - Paired constraints: one blocks a habitual response, one promotes a novel alternative.
  - "No em dashes" blocks a habitual AI response. "Use periods for short declarative stops" promotes the alternative.
  - "Never open with self-introduction" blocks the default. "Open with current work" promotes the alternative.
  - The voice governance system is a constraint architecture. Each rule is a paired constraint. The set of rules doesn't describe a vibe. It defines a structure.
- **Generation-time vs. post-generation constraints (Anthropic 2022, Constitutional AI):**
  - Rules applied during generation (constitutional principles) yield better results than rules applied after. The output is shaped as it forms, not corrected after it solidifies.
  - Voice governance applies the same principle to creative voice. Rules during generation produce structurally different text than editing after generation.

**Artifact/example referenced:** week3-voice-governance-demo.md (the 12 rules as example of structural constraints), cognitive-science-references.md (all Week 3 citations)
**Cognitive science citation:** Pennebaker & King 1999 (function words carry identity), Baker 1993 (editorial normalization), Solum 2018 (fixation at interpretation), Stokes 2005 (paired constraints), Anthropic 2022 (Constitutional AI, generation-time rules), Flower & Hayes 1981 / Bereiter & Scardamalia 1987 (knowledge-transforming vs. knowledge-telling)
**Deliverable:** None

**Production notes:**
- WRITE: Full lesson (Peter writes, this is the conceptual core of Week 3 and the hardest lesson in the course to get right; the "voice is structural" argument needs to be airtight and specific)
- COMPILE: Research summaries adapted from cognitive-science-references.md (exists, needs significant rewriting for student audience)

---

### Lesson 3.4 — Voice Extraction Protocol

**Phase:** Guided Practice
**Format:** Written lesson + Exercise
**Learning objective:** The student can extract 8-12 hard voice rules from their own speech transcript by identifying structural patterns, not surface features.

**Content outline:**
- Source material: the student's brain dump transcript from Week 2 (Lesson 2.5 or 2.6). If they don't have one, they record a new one now (5-10 minutes talking about their work).
- **The extraction process:**
  - Read (or listen to) the transcript. Don't analyze yet. Just notice.
  - Pass 1: Openings. How do you start a thought? Do you lead with the thing you're making? With a question? With a reference to someone else's work? With a problem statement?
  - Pass 2: Stops and turns. Where do you use short declarative stops vs. longer connective thoughts? What does your sentence rhythm look like? Short-short-medium? Long followed by short? Even?
  - Pass 3: Vocabulary domain. Is your language physical (pressure, weight, surface)? Abstract (concept, framework, system)? Emotional (feels, hits, bothers)? What domain does your default vocabulary come from?
  - Pass 4: What you never say. This is the most important pass. What's absent? No hedging? No qualifiers? No sign-offs? No explanations of why your field matters? The absences define voice as much as the presences.
  - Pass 5: References and tangents. Do you reference other people's work? Do you go on tangents? Are your lists even (three parallel items) or uneven (three items of different lengths)?
  - Pass 6: Humor and temperature. Is humor dry and factual? Warm and self-deprecating? Absent? What register do you default to: formal, conversational, blunt?
- **Guided exercise:**
  - Using the six passes, student reads their transcript and fills in a structured extraction template:
    - 2-3 rules about openings/closings
    - 2-3 rules about rhythm and sentence structure
    - 2-3 rules about vocabulary and specificity
    - 2-3 rules about what is never said or done
  - Target: 8-12 hard rules. Each rule is specific and testable. Not "be direct" (that's a tone adjective). "Never open with self-introduction. Open with current work." (That's a structural rule you can verify.)
  - Show Mara's 12 rules as the reference model. Point out: each rule is concrete enough that you could check whether a piece of writing follows it or not. That's the bar.

**Artifact/example referenced:** week3-voice-governance-demo.md (Mara's 12 rules as the model), the source quotes from Mara's transcript that generated each rule
**Cognitive science citation:** Pennebaker & King 1999 (function words and structural patterns carry individual voice, not content words)
**Deliverable:** 8-12 voice rules (not submitted, refined in 3.5 and 3.6)

**Production notes:**
- WRITE: The six-pass extraction protocol (Peter writes, this is original methodology)
- WRITE: Commentary showing how each of Mara's 12 rules maps to a specific moment in her transcript (Peter writes, showing the extraction process, not just the result)
- COMPILE: Extraction template (structured from the six passes, operational)

---

### Lesson 3.5 — Test Your Voice Protocol

**Phase:** Guided Practice
**Format:** Exercise
**Learning objective:** The student can apply their voice protocol during generation and identify structural differences between governed and ungoverned output.

**Content outline:**
- Student picks a real writing task from their own work. An about page, a project description, a client email, a blog post. Something they actually need to write.
- Two runs:
  - **Run 1 (ungoverned):** Generate the piece with a standard prompt. No voice rules. Save the output.
  - **Run 2 (governed):** Generate the same piece with the voice rules applied as hard constraints during generation. Include the rules in the prompt as "voice governance rules, apply as hard constraints, not suggestions." Save the output.
- Do NOT edit either output. Compare them as-is.
- Documentation:
  1. The writing task (one sentence).
  2. Run 1 output (ungoverned).
  3. Run 2 output (governed).
  4. Structural differences: Where does the governed output differ structurally (not just in word choice)? Different openings? Different rhythm? Different information included or excluded? Different closings?
  5. Which rules had the most visible effect? Which rules didn't seem to change anything?
  6. Revise your rules: add, remove, or sharpen based on what you learned.
- Optional additional comparison: Take the ungoverned output and edit it manually to sound like you. Compare that edited version to the governed version. Where do they differ? The governed version was shaped during generation. The edited version was shaped after. Is the structure different?

**Artifact/example referenced:** Mirrors the three-level comparison from the Week 3 artifact (standard vs. harnessed vs. governed), now applied to student's own work
**Cognitive science citation:** Bock & Loebell 1990 (structural priming: early governed output primes the rest), Baker 1993 (editing normalizes, governance preserves)
**Deliverable:** None (practice; 3.6 is the deliverable)

**Production notes:**
- WRITE: Framing for the comparison exercise, especially the optional editing comparison (Peter writes, the editing comparison is the strongest proof point for governance over post-hoc editing)
- COMPILE: Documentation template (operational)

---

### Lesson 3.6 — Week 3 Deliverable: The Full Methodology

**Phase:** Independent Practice
**Format:** Exercise + Deliverable
**Learning objective:** The student can produce a real piece of work using the complete three-week methodology: decomposed task, brain dump input, voice governance during generation.

**Content outline:**
- This is the capstone. Student writes one piece of real work using all three weeks:
  - **Week 1 (decomposition):** Break the writing task into its component dimensions. Run each independently.
  - **Week 2 (input inversion):** Use a brain dump (existing or new) as the source material. Process it through synthesis.
  - **Week 3 (voice governance):** Apply the voice protocol during generation of each decomposed piece.
  - **Synthesis:** Combine the decomposed, voice-governed outputs into a final piece. Resolve conflicts. Apply your judgment.
- The task should be real work the student actually needs. Not a hypothetical. Not a practice scenario. Something that goes into the world.
- Submit:
  - The voice protocol (8-12 rules, revised from 3.4 and 3.5)
  - A before/after comparison: the same writing task done with a standard single prompt (before) and with the full methodology (after)
  - The final output
  - A short reflection (3-5 sentences): What does the governed output contain that the standard output doesn't? Not just different words. Different information, different structure, different decisions. What's in there because of you?

**Artifact/example referenced:** All three weeks' artifacts converge. The Voss Type decomposition (Week 1), the Night Owl brain dump (Week 2), and the Mara voice governance (Week 3) demonstrated this exact workflow on a fictional project. Now the student does it on a real one.
**Cognitive science citation:** Stokes 2005 (constraints produce breakthrough by blocking habitual responses and promoting novel alternatives; the full methodology is a constraint architecture for creative AI use)
**Deliverable:** Voice protocol, before/after comparison, final output, and reflection. This is the Week 3 submission and the course capstone.

**Production notes:**
- WRITE: Reflection prompt (Peter writes, needs to point at the structural difference, not just the quality difference)
- COMPILE: Submission format template (operational)

---

## CLOSE: What You Built

**Format:** Written page (closing page for the course)

**Content outline:**

- **Three deliverables, one methodology.** Over three weeks, the student produced:
  - A decomposed-and-synthesized brief (Week 1): evidence that their judgment is the product, not the AI's output
  - A brain dump practice (Week 2): a repeatable method for getting their actual thinking into the AI's input
  - A voice protocol and capstone piece (Week 3): structural rules that make AI output sound like them, not like AI
- **These are not three separate techniques.** They scaffold. Decomposition gives the AI depth. Input inversion gives the AI your thinking. Voice governance gives the AI your voice. Together they form a personal AI methodology where the human provides coherence, raw material, and identity. The AI provides depth, organization, and execution.
- **Where to go next.** The Foundations course covers the first of six domains in the Joinery curriculum. The remaining five go deeper into specific applications:
  - (Domain names and descriptions TBD as curriculum develops)
  - Each domain builds on the three Foundations techniques.
  - Deeper courses are in development. The Foundations methodology is sufficient to start applying these techniques to real work immediately.
- **How to share feedback.** (Mechanism TBD: email, form, community channel.)
- **One last thing.** The methodology works because it puts you in the right seat. The AI is not the creative director. You are. The AI is not the author. You are. The AI is a set of specialists, a whiteboard, and a press that prints in your voice. What comes out of it is yours because what went into it was yours.

**Production notes:**
- WRITE: Full closing copy (Peter writes, this is the last thing the student reads and needs to land the core message)
- COMPILE: "Where to go next" section (operational, updated as curriculum develops)

---

## Production Summary

### What Peter Must Write (original voice, can't be compiled)

| Item | Lesson | Type |
|------|--------|------|
| Course intro copy | Intro | Landing page |
| Video script: The Frame Break | 1.1 | Video script |
| Narrative framing for compound problem | 1.2 | Lesson prose |
| Side-by-side decomposition commentary | 1.3 | Lesson prose |
| Synthesized Voss Type brief (conflict resolution demo) | 1.4 | Teaching artifact |
| Guided exercise scenario (podcast brand, 3 outputs with planted conflicts) | 1.4 | Exercise content |
| Reflection prompt for Week 1 deliverable | 1.6 | Prompt |
| Video script: The Input Problem | 2.1 | Video script |
| Narrative framing for three input levels | 2.2 | Lesson prose |
| Full "Why Unstructured Input Is Richer" lesson | 2.3 | Lesson prose |
| Brain dump protocol instructions | 2.4 | Protocol |
| Fictional interior designer brain dump scenario | 2.4 | Exercise content |
| Exercise framing (save transcript for Week 3) | 2.5 | Framing |
| Reflection prompt for Week 2 deliverable | 2.6 | Prompt |
| Video script: Why All AI Copy Sounds the Same | 3.1 | Video script |
| Narrative framing for three voice levels | 3.2 | Lesson prose |
| Full "Voice Is Structural, Not Stylistic" lesson | 3.3 | Lesson prose |
| Six-pass voice extraction protocol | 3.4 | Protocol (original methodology) |
| Mara rule-to-transcript mapping commentary | 3.4 | Teaching artifact |
| Exercise framing for voice testing | 3.5 | Framing |
| Reflection prompt for Week 3 deliverable | 3.6 | Prompt |
| Course closing copy | Close | Landing page |

### What Can Be Compiled From Existing Artifacts

| Item | Source | Lesson |
|------|--------|--------|
| Compound prompt and output | compound-prompt-demo.md Part 1 | 1.2 |
| All 5 decomposed prompts and outputs | compound-prompt-demo.md Part 2 | 1.3 |
| Decomposition comparison analysis | compound-prompt-demo.md Part 3 | 1.3 |
| Standard/Harnessed/Inverted prompts and outputs | week2-input-inversion-demo.md Parts 1-3 | 2.2 |
| Comparison table (3 input levels) | week2-input-inversion-demo.md | 2.2 |
| Standard/Harnessed/Governed prompts and outputs | week3-voice-governance-demo.md Parts 1-3 | 3.2 |
| Mara's 12 voice rules | week3-voice-governance-demo.md Part 3 | 3.2, 3.4 |
| Comparison table (3 voice levels) | week3-voice-governance-demo.md | 3.2 |
| All cognitive science summaries | cognitive-science-references.md | Multiple |

### Templates and Operational Content (Can Be Structured)

| Item | Lesson |
|------|--------|
| Submission format instructions | 1.6, 2.6, 3.6 |
| Decomposition template (5-step) | 1.5 |
| Synthesis template (5-step) | 1.4 |
| Brain dump synthesis prompt | 2.4 |
| Voice extraction template (6-pass) | 3.4 |
| Voice testing documentation template | 3.5 |
| Practice design template | 2.6 |
