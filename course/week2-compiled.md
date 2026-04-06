# Week 2: Input Inversion -- Compiled Content

Compiled from Peter Salvato's published writing, whitepapers, drafts, narrative architecture, cognitive science references, and conversation history. Every quote and teaching point is sourced. Sections marked [NEEDS PETER] require Peter's direct input (interview, voice recording, or confirmation).

---

## Attunement Frame: Reading the AI's Input Capacity

Week 1 taught you to attune to how the AI processes tasks: one objective at a time, not five at once. This week, you attune to how it receives input.

The conventional approach assumes the AI needs structure from you: clear instructions, defined formats, specific constraints. The attunement approach asks a different question. What kind of input actually carries the most information to this receiving system? The answer, grounded in cognitive science research, is that unstructured human thinking (brain dumps, voice memos, working notes) carries richer raw material than polished prompts. The structuring step compresses your thinking before the AI sees it.
[SOURCE: whitepaper, input-inversion, Section 1]

Input inversion is attunement to input capacity. You read what the AI actually needs from you (your raw thinking, not your pre-organized conclusions), and you design the input pipeline around that reading. The technique is counter-intuitive. The skill underneath it is the same one you use when you listen to a client talk through their problem instead of reading their brief: the unstructured version carries more.

---

## Lesson 2.1: Video Intro Script Outline
**Why Better Prompts Still Produce Generic Output**

### Bridge from Week 1

Week 1 taught task decomposition: break compound prompts into single-objective steps, and the output improves because the model processes each step with full attention. That was about how the model processes. Week 2 is about what goes into the model in the first place.

Decomposition fixes the structure of the task. Input inversion fixes the quality of the raw material.

### Peter's Own Framing of the Problem

**Source: Input Inversion whitepaper, Section 1 (petersalvato.com/_research/input-inversion.md)**

> "The AI industry operates on a foundational assumption: the quality of AI output is a function of the quality of AI input, where 'quality' means structure, specificity, and format."

> "Best-practice guidance is consistent. 'Write clear, specific instructions.' 'Define the output format.' 'Use few-shot examples.' 'Apply chain-of-thought reasoning.' 'Avoid dumping unstructured data at an LLM.' The prompt engineering field has produced taxonomies of 58 distinct prompting techniques and a cottage industry of courses, certifications, and role definitions organized around the same claim: better-structured input produces better output."

> "The assumption feels obviously true. And the evidence is starting to contradict it."

**Source: "Talk to It, Don't Type at It" essay (petersalvato.com/_essays/talk-to-it.md)**

> "When you type a prompt, you're already editing. You feel the friction of the keyboard or the smallness of the phone screen. You compress a thought to fit the effort of the input. By the time you hit enter, you've lost something. The raw version. The version where you changed direction mid-sentence, contradicted yourself, stumbled into the thing you actually meant."

**Source: "The Unstructured Corpus" essay (petersalvato.com/_essays/the-unstructured-corpus.md)**

> "Most prompt advice treats unstructured input as a problem to solve. Pre-organize, use few-shot examples, define output formats. The assumption is that messy input produces messy output."

> "I went the other way. And the unstructured corpus turned out to be the most valuable thing I've built."

### The Transition Point

**Source: Input Inversion whitepaper, Section 5**

> "The conventional model: Human (structures thinking) -> Structured prompt -> Model -> Output"

> "The inverted model: Human (thinks out loud) -> Dump -> Accommodation tools (structure for model) -> Model -> Output"

> "The difference is where the structuring happens. In the conventional model, the human does it before the input reaches any system. In the inverted model, purpose-built tools do it after the human has finished thinking."

### Script Outline Notes

The intro video should walk through this arc:
1. You learned to decompose your tasks (Week 1). But even a well-decomposed task can produce generic output. Why?
2. Because the input itself is thin. Structured prompts are clean, but they have already edited out the raw material the model needs.
3. This week: what happens when you change the input instead of the prompt structure.
4. Preview the Night Owl demo (the same task, three levels of input quality, dramatically different results).

[NEEDS PETER: Record this intro in Peter's voice. The script outline above is compiled from his published framing. He should talk through it naturally, not read a script. The video intro should demonstrate the principle it teaches: raw spoken thinking, not performed polish.]

---

## Lesson 2.2: Three Levels of Input Quality
**The Night Owl Brewing Demo**

### Core Example: The Night Owl Brewing Rebrand

**Source: week2-input-inversion-demo.md (course artifact)**

The full demo is the backbone of this lesson. Three levels, same task (creative concept ideation for a brewery rebrand), same model:

#### Level 1: Standard Prompt

Prompt: "Give me 10 creative concept directions for a craft brewery rebrand."

Output: The Observatory, Old Growth, Ash and Ember, Undertow, Iron Bell, Black Lantern, The Roost, Deep Root, Nocturne, Stone Circle.

**Peter's analysis (source: demo artifact):**

> "These are generic concepts any AI would produce for any brewery in any city. They reference Portland only through cliches (forests, Pacific Northwest). They reference 'dark' only through literal darkness metaphors. None of them connect to anything specific about this brewery, this founder, or this taproom. A competing brewery in Denver would get 7 of the same 10."

#### Level 2: Harnessed Prompt

Prompt includes role assignment, client specifics (Tomas Kowalski, former music venue promoter, homebrewing since 2016), competitive context (70+ Portland breweries), constraints (no nature cliches, no industrial-rustic).

Output: The Green Room, Setlist, The Backline, Headliner/Opener, Soundcheck, Low End, B-Side, House Left, The Encore, 11PM.

**Peter's analysis (source: demo artifact):**

> "Significantly better. The role assignment and constraints eliminated the generic Portland/nature concepts. The competitive context forced differentiation. The founder's background gave the AI a real thread to pull."

> "But these are still the AI's ideas. The AI identified 'music venue + brewery = music-themed brewery branding' and executed that logic competently. The concepts are clever. They're also exactly what a strategist would produce in a brainstorm: tidy, parallel, self-consciously branded. They came from prompt logic, not from a person's actual thinking about this project."

#### Level 3: Inverted Input (Brain Dump)

The designer (Mara Voss) recorded a 12-minute brain dump. Unstructured, full of tangents.

Key excerpt from transcript:

> "...the thing that keeps bugging me is that Tomas doesn't think of it as a brewery with music. He thinks of it as a venue that happens to brew. Like the beer is the hospitality, the show is the reason you're there. And when I was in the taproom last week, there's this wall of records behind the bar, and half of them are these Polish jazz covers from the 70s that his dad collected. And nobody knows what they are. They're not decoration. He actually plays them."

> "I keep coming back to 'dark.' Not just the beer. The venue is dark. He books dark music. The aesthetic is dark. His whole sensibility is dark. But not goth-dark, not heavy-metal-dark. More like... a jazz club at midnight dark. Intimate dark. The kind of dark where you lean in."

> "The Polish jazz thing. It's not a style reference. It's an attitude. Obscure taste presented without explanation. You either get it or you ask about it, and both of those are fine. That's the whole brand right there actually..."

Prompt: "Do NOT generate concept ideas. Instead, identify what the designer has already figured out. Synthesize her thinking. Tell her what she said."

Output identified: "Dark" as entire positioning (not just beer descriptor). The origin story inversion (venue that brews, not brewery with music). The Polish jazz covers as brand attitude. The owl as printer's mark, not mascot. Tomas's handwriting as typographic voice. The designer's job as translation, not invention.

### The Comparison Table

**Source: demo artifact**

| Dimension | Standard | Harnessed | Inverted |
|-----------|----------|-----------|----------|
| Source of ideas | AI pattern matching | AI reasoning with constraints | Designer's own thinking |
| Specificity | Generic (any brewery) | Targeted (this brewery type) | Singular (this brewery, this person) |
| Could another designer use this? | Yes, anyone | Yes, a good strategist | No. These came from Mara's brain. |
| Role of AI | Generator | Constrained generator | Synthesizer and mirror |
| Quality of output | Disposable | Presentable | Foundational |

### Peter's Summary of What Changed

**Source: demo artifact**

> "Standard produced garbage everyone gets. The concepts are interchangeable with any dark-themed business in any city."

> "Harnessed produced passable, AI-shaped ideas. A competent strategist might present these in a deck. They're smart. They're also the AI's ideas, organized by AI logic, and another AI with the same constraints would produce similar results."

> "Inverted produced the designer's own ideas, excavated from her thinking, that could not have come from any prompt because they came from a specific person's observations in a specific taproom on a specific Tuesday. The AI didn't generate. It listened, organized, and reflected back what was already there."

> "The input changed. Not the model. Not the prompt engineering. The input."

### The Whitepaper's Argument for Why Structured Input Compresses

**Source: Input Inversion whitepaper, Section 5**

> "Richer source material. Unfiltered thinking contains information that structured prompts discard: false starts that reveal what the person considered and rejected, contradictions that map the boundaries of their understanding, language patterns that reveal how they actually communicate rather than how they perform."

> "Preserved cognitive state. The act of pre-structuring disrupts the thinking it's trying to capture. You have an insight, you stop to format it into a clean prompt, and by the time you're done formatting, you've lost the thread that produced the insight in the first place."

**Source: "Compilation, Not Generation" essay**

> "That's the codebase. It's raw, unpolished, and entirely mine. It exists because the system was designed to accept it raw. In FormWork, the first accommodation is aimed at the human: get the thinking out of your head with as little friction as possible. Talk, dictate, answer questions. Don't organize, don't outline, don't perform. The rawness is the point. Structured input has already lost the thing the tools need most, which is how I actually think."

### Teaching Point

The lesson ends with this framing: the student has now seen the same task produce three different quality levels. The variable that changed was the input, not the model, not the prompt technique. The rest of this week teaches the student to produce Level 3 input.

### Real Brain Dump Transcript (replaces simulated placeholder)

The following is an edited excerpt from a real working session. The process, decisions, and outcomes are real. Names and language edited for professional context. See `course/artifacts/real-session-excerpts.md` (Excerpt 1) for the full annotated version.

This excerpt shows a five-minute brain dump that pivoted from building a job-search tool to launching an education platform. The direction changes, contradictions, and mid-sentence discoveries are the point. This is what unstructured input looks like when it works.

[EXCERPT 1 FROM: course/artifacts/real-session-excerpts.md — embed full Excerpt 1 content here when rendering student-facing pages. The compiled source references the artifact file rather than duplicating the full text.]

---

## Lesson 2.3: Why Unstructured Input Is Richer
**The Cognitive Science Argument**

### The Writing Cognition Problem

**Source: Cognitive science references, Week 2 section**

**Kellogg (1996, 2008). "A Model of Working Memory in Writing" / "Training Writing Skills."**
Writing simultaneously taxes working memory with three competing demands: planning (what to say), translating (how to say it), and reviewing (evaluating what was said). These demands compete for the same limited cognitive resources.

*Teaching point:* This is why brain dumps work. Voice input separates the planning stage from the translation stage. The person thinks out loud without simultaneously formatting, editing, and structuring. Lower cognitive load during the critical ideation phase.

### The Self-Explanation Effect

**Source: Cognitive science references, Week 2 section**

**Chi (1994, 2000). "Eliciting Self-Explanations Improves Understanding" / "Self-Explaining Expository Texts."**
Students who explain material to themselves while learning produce deeper understanding than those who silently organize information. Self-explanation forces active processing and reveals gaps in understanding.

*Teaching point:* The brain dump functions as self-explanation. When Mara talks through her thinking about Night Owl, she is not just recording ideas. She is discovering them through the act of articulation. The AI then synthesizes what the articulation revealed.

*Caveat from references:* "Chi's research is about learning, not about creative ideation. The mechanism (active processing reveals gaps) transfers, but we shouldn't overstate the equivalence."

### Knowledge-Transforming vs Knowledge-Telling

**Source: Cognitive science references, Week 2/3 section; foundations-scaffold.md, Lesson 2.3 citation**

**Flower & Hayes (1981). "A Cognitive Process Theory of Writing." / Bereiter & Scardamalia (1987). *The Psychology of Written Composition.***

Writers operate in two modes. Knowledge-telling is retrieval: the writer accesses what they already know and puts it on the page. The result is organized but static. Knowledge-transforming is generative: the act of writing itself changes what the writer knows. New connections form during production. The result contains ideas the writer did not have before starting.

*Teaching point:* Standard prompting is knowledge-telling. The designer retrieves what they think the AI needs to hear, organizes it into a prompt, and hits enter. The prompt contains retrieved knowledge. The AI processes a fixed input.

A brain dump is knowledge-transforming. The designer thinks out loud without pre-organizing. Talking produces connections that silent retrieval misses. Ideas arrive mid-sentence. Contradictions surface. The designer changes direction when a new thought displaces an old one. The dump contains thinking-in-progress, and when the AI processes it, the raw material is richer because it includes the discovery, not just the conclusion.

This is the conceptual spine of Week 2. Input inversion works because it forces the human into knowledge-transforming mode before the AI touches the material. Structured prompts force the human into knowledge-telling mode. The difference in input quality is not about word count or specificity. It is about whether the human was discovering or retrieving when they produced the input.
[SOURCE: cognitive-science-references.md, Flower & Hayes citation; foundations-scaffold.md, line 377]

*Caveat:* Flower & Hayes studied expert human writers. Applying the knowledge-telling/knowledge-transforming framework to AI input is analogical. The mechanism (generative articulation produces richer raw material than organized retrieval) is supported by the evidence, but the exact transfer to AI processing contexts is Peter's inference, not the original researchers' claim.

### The Extended Mind Thesis

**Source: Cognitive science references, Week 2 section**

**Clark & Chalmers (1998). "The Extended Mind."**
Cognitive processes do not stop at the skull. External tools and artifacts (notebooks, calculators, and by extension AI) can function as genuine components of a cognitive system when they are reliably accessible, automatically endorsed, and readily available.

**Peter's framing of this (source: Input Inversion whitepaper, Section 6):**

> "The human's processing reality: ideas lose fidelity when forced into structure at the point of capture. The act of organizing, outlining, or formatting disrupts the thinking it's trying to capture. When the burden of structure is removed, the human can talk, dictate, answer questions. What comes out carries the maker's actual voice, actual thinking, actual structure."

*Teaching point:* Input inversion treats AI as an extended mind component. The designer's brain dump is the cognitive process. The AI synthesis is the externalized organization step. Together they form a single cognitive workflow that neither could perform alone.

*Caveat from references:* "The Extended Mind thesis is philosophically contentious. Many cognitive scientists reject it. Use it as a framing device, not as settled science."

### Creative Flow and Premature Evaluation

**Source: Cognitive science references, Week 2 section**

**Osborn (1953) / Amabile (1983).** Premature evaluation during ideation suppresses creative output. Separating generation from evaluation increases the quantity and novelty of ideas.

**Cseh et al. (2015). "Flow and Creativity."** Creative flow thrives on ambiguity and open-endedness rather than clear goals.

*Teaching point:* Brain dumps allow ambiguity. The designer does not need to know where she is going. She follows tangents (Polish jazz covers, chalkboard handwriting) because creative flow rewards exploration. Structured prompts force premature clarity.

### The Voice Input Advantage

**Source: Input Inversion whitepaper, Section 2.3**

> "Humans speak at 125-150 words per minute and type at 40. The friction of the keyboard compresses thought. By the time a typed prompt reaches the model, the human has already edited, compressed, and filtered the raw thinking. The unfiltered version, the one that contains false starts, mid-sentence corrections, and the moment where the idea actually crystallized, never makes it into the prompt."

> "Voice input bypasses that filter. The human thinks out loud. The full texture of the thinking reaches the system."

**Source: Cognitive science references, Week 2 section**

Voice input reduces cognitive load because it separates the planning stage from the translation stage (Kellogg, 1996, cited in Lesson 2.3 above). When you speak, you are not simultaneously formatting, punctuating, and structuring. The translation burden is deferred. Multiple studies have found measurable load reduction during dictation compared to typing, though the size of the effect varies with the person and the task. Some people think better while typing. The recommendation is to try voice input on your next brain dump and notice whether your thinking goes further before you hit a wall.

*Note:* A previous version of this section cited a "35-45% lower cognitive load" figure without specific attribution. That figure has been removed pending source verification. The principle (voice input reduces translation-stage cognitive load) is well-grounded in Kellogg's working memory model. The specific percentage should not be cited without a traceable source.

### Andrew Ng's Benchmark (Systems vs. Prompts)

**Source: Input Inversion whitepaper, Section 2.2 / Cognitive science references, Week 1 section**

> "Andrew Ng's team demonstrated the point empirically. On the HumanEval coding benchmark, GPT-3.5 with a single optimized prompt achieved 48.1% accuracy. GPT-4 with a single optimized prompt reached 67%. GPT-3.5 wrapped in an agentic workflow (multiple steps, decomposed tasks, iterative evaluation) hit 95.1%. A weaker, cheaper model nearly doubled the advanced model's performance by changing how the system worked, not what the input said."

> "The implication is direct: prompt optimization hits diminishing returns quickly. The gains from system design are larger and they compound."

*Teaching point for this lesson:* The Ng benchmark was introduced in Week 1 for decomposition. Now extend it: the same principle applies to input quality. The system design matters more than the prompt craft, and the richest system design starts with richer raw material.

### The Pedagogical Parallel

**Source: Input Inversion whitepaper, Section 3**

> "A teacher does not require a student to organize their thoughts before speaking. The student speaks. The teacher listens, captures what was expressed, identifies the structure in it, and designs the next instructional step to fit. The accommodation runs from the teacher to the student's processing reality, not from the student to the teacher's preferred format."

> "A student with processing delays who is required to pre-structure their thoughts before communicating will produce less, not more. The filtering suppresses the raw material the teacher needs: how the student actually thinks, where they get stuck, what language they reach for, where their understanding breaks down."

> "The parallel to AI interaction is direct. A practitioner required to pre-structure their input before communicating with a model will produce less raw material for the system to work with. The prompts are cleaner. They're also thinner."

### The Sculpting Loop

**Source: Narrative architecture (petersalvato-dev/narrative-architecture.md), "The Sculpting Loop" section**

Discovery from 2026-03-15: interactive re-traversal of the maker's own ideation corpus through a context-loaded system produces emergent connections between existing ideas. Not drafting/revising. Sculpting.

The metaphor: Clay, not marble.

> **The full loop:**
> 1. **Dump** -- raw ideation in any medium. Voice memos, notes, conversations. The first blob of clay.
> 2. **Shape** -- re-traversal through a context-loaded system. The system holds the full architecture. The maker talks through it. Connections form between pieces too far apart for any single mind to hold simultaneously.
> 3. **Add** -- interviews bring new clay. Richer because the questions come from the existing shape and the new material is informed by what is already there.
> 4. **Shape again** -- new material integrates, produces more connections, changes the overall form.
> 5. **Repeat** -- each cycle produces a more refined shape with richer additions.

> "The tool exists -- everyone is chatting with AI. The gap is the method. The corpus doesn't need years. A week of brainstorming, voice memos, a napkin sketch. Any externalized thinking. The contribution is showing people how to use the tool they already have."

*Teaching point:* The sculpting loop is the long-term workflow. The brain dump (Lesson 2.4) is step 1. This week teaches step 1. The rest of the course teaches the student to shape, add, and shape again.

### Honest Limitations

**Source: Cognitive science references, "Honest Limitations" section**

> "Moderate support: Cognitive load reduction through voice input and brain dumps (Week 2). The underlying cognitive science is solid, but the specific application to AI-mediated creative workflows hasn't been directly studied. We're applying established principles to a new context."

---

## Lesson 2.4: Guided Brain Dump Exercise
**How Peter Actually Does Brain Dumps**

### Peter's Own Process

**Source: "The Unstructured Corpus" essay**

> "For three years I've been thinking out loud into AI tools the way I used to think into sketchbooks and production shops. Brainstorming, arguing with myself, changing direction mid-sentence, working through problems at 2 AM when the idea won't let go. 1,643 ChatGPT sessions. 700+ Claude sessions. Gemini exports. Voice notes dictated while driving. Unfinished thoughts. Arguments with no resolution."

**Source: "Talk to It, Don't Type at It" essay**

> "Dictate into your phone on the drive home. Brainstorm out loud into a voice note at 2 AM when the idea won't let go. Open a conversation and just speak. It doesn't need to be clean. Say 'no wait, that's not what I mean' and keep going."

> "Talking instead of typing removes the friction between thinking and input. You don't compress, don't edit, don't organize before the thought is finished. The keyboard forces you to compose. Your voice lets you dump."

> "That dumping is the first half of what I call bidirectional accommodation. The human side. Get the thinking out with as little resistance as possible."

**Source: "Knowledge Traversal" draft (petersalvato-dev/_drafts/knowledge-traversal.md)**

> "I was looking for something I'd said six months ago. A specific formulation of an idea about governance that I remembered being good, better than anything I'd written since. I knew I'd said it in a conversation with Claude. I knew roughly when. But finding it meant scrolling through exports, scanning hundreds of exchanges, trying to locate five sentences I'd written in the middle of a longer thread about something else entirely."

> "That search took over an hour. And when I found it, it was better than I remembered. It was a crystallization that had happened in the flow of conversation, the way ideas sometimes land when you're talking through a problem instead of writing for an audience. Casual. Precise. Unrepeatable in those exact terms."

**Source: Input Inversion whitepaper, Section 4.1**

> "Between 2023 and 2026, I accumulated three years of unstructured thinking across ChatGPT, Claude, and Gemini: brainstorming, arguing with myself, changing direction mid-sentence, working through problems at 2 AM, dictated voice notes while driving. No performance. No formatting. No pre-organization."

> "This corpus was not designed as a dataset. It accumulated naturally from thinking out loud with AI rather than assigning it tasks. The material includes unfinished thoughts, abandoned arguments, contradictions, and false starts alongside the moments where something actually clicked."

### The Practical Protocol

**Source: Input Inversion whitepaper, Section 8 / "The Unstructured Corpus" essay / "Talk to It" essay**

**Minimum viable entry:**

> "Input inversion does not require three years and thousands of sessions. The principle scales down."

> "A single dictated session. Even one conversation where someone speaks freely about their work produces richer material than a carefully structured brief."

**Scaling up:**

> "One month of voice notes. Dictated observations on the commute, spoken reactions to the day's work, brainstormed solutions while walking. Enough for an initial voice sample and a body of raw thinking the tools can process."

> "A few dozen conversations. Open-ended sessions where the practitioner thinks out loud about their work. 'Tell me about what you're building.' The interview skill processes these into stories, language patterns, and concept maps."

**Source: "The Unstructured Corpus" essay**

> "The scale matters less than the rawness. A month of voice notes contains real voice, real thinking patterns, real concerns. Enough for the tools to begin extracting."

> "For someone starting fresh, an interview works. 'Tell me about what you're building.' Open-ended questions that produce stories, language, instincts. That becomes the initial corpus."

> "What the corpus can't be is retroactively assembled from polished writing. Published work has already been edited for an audience. The properties that make the corpus valuable (unfinished thoughts, contradictions, the moment an idea first shows up under the wrong name) only exist in material that was never edited for an audience."

### The Habit Barrier

**Source: Input Inversion whitepaper, Section 8**

> "I think the barrier to entry is less about technical infrastructure and more about habit. The industry has trained practitioners to perform for the model: clean prompts, specific instructions, defined formats. Unlearning that performance is harder than building the tools. Input inversion asks you to stop organizing your input and start organizing the system that processes it, and most people find the first part harder than the second."

### Tools and Timing

**Compiled from Peter's process documentation across multiple sources:**

- **Voice memo app** on phone (any app that records). The tool does not matter. The friction does.
- **AI conversation window** (ChatGPT, Claude, Gemini). Open it and talk, do not type a structured prompt.
- **Timing:** No set time. Peter's corpus includes "2 AM when the idea won't let go" and "dictated voice notes while driving." The point is to capture thinking when it is happening, not to schedule a session.
- **Duration:** Peter's individual conversation sessions range from ten minutes to multi-hour architecture sessions. There is no minimum. Even one recording is enough to start. The brain dump excerpt in Lesson 2.2 (Excerpt 1) took five minutes and produced a complete strategic direction.

### What the Real Brain Dump Looks Like

You already saw it in Lesson 2.2. The Excerpt 1 brain dump demonstrates: a direction change in under sixty seconds ("no. stop this."), a market identified mid-conversation, a vehicle named with a question mark, competitive positioning discovered from personal knowledge, and conviction strong enough to start building the same day. That is what unstructured input produces. The student's brain dump will be different in content and smaller in scope, but the PROCESS (talk without structure, discover through articulation, arrive at something actionable) is the same.

### Guided Scenario for Student Practice

The student practices on a provided scenario before doing their own (Lesson 2.5).

**Scenario:** You are a freelance designer. You have a new client: a small bakery in your neighborhood that is expanding to a second location. The owner asked for "a new logo and maybe a website." You visited the bakery yesterday. Now do a brain dump about it.

**Guided prompts (delivered one at a time, pacing the student through the exercise):**

1. Talk about what you noticed in the bakery. Not what you think the brand needs. What you saw, smelled, heard.
2. What stuck with you after you left? What keeps coming back?
3. What does the owner care about that they did not say directly? What did you pick up from the visit that was not in the brief?
4. What is the gap between how the bakery feels in person and how it looks online (or in its current materials)?
5. What is the one thing you would protect if you could only protect one thing about this place?

**Instructions to student:** Record yourself talking through these prompts. Do not write. Do not organize. Do not stop to fix what you said. Say "actually, that's not what I mean" and keep going. The tangents are the material.

**After recording:** Paste the transcript into a conversation with an AI tool. Use this prompt:

> "Below is a raw transcript from a designer thinking through a bakery rebrand project. Read it carefully. Do NOT generate concept ideas. Instead, identify what the designer has already figured out. Synthesize their thinking. Tell them what they said."

**Debrief questions:**
- What did the AI find that you did not consciously know you had figured out?
- How does the synthesis compare to what you would have gotten from a standard prompt like "give me 10 logo directions for a bakery"?
- What specific details from your visit showed up in the synthesis that would never have appeared in a structured brief?

---

## Lesson 2.5: Student's Own Brain Dump
**Independent Practice**

### Exercise Structure

The student applies the brain dump method to their own real project. This is the critical transfer: from guided scenario to actual work.

**What the student does:**

1. **Choose a real project.** Current client work, personal project, or a project they are about to start. Not a hypothetical. The exercise only works with material the student actually knows and cares about.

2. **Record a brain dump.** 8-15 minutes. Voice preferred. Typing acceptable if voice is genuinely not available. Talk through what they are thinking about the project: what they have noticed, what is bugging them, what they keep coming back to, what the client said that did not sit right, what they saw during research that stuck.

**Source: "Talk to It" essay, for the student's instruction framing:**

> "Open your phone's voice memo app or start a conversation with any AI tool. Talk about what you're building, what's frustrating you, what you figured out yesterday. Don't organize it. Just talk."

> "Brainstorm into a voice note at midnight. Answer your own questions out loud and let yourself change direction halfway through."

3. **Transcribe.** Use the voice memo app's built-in transcription, or paste the audio into an AI tool for transcription. The transcript does not need to be perfect. Errors and artifacts are fine.

4. **Submit to AI for synthesis.** Use the same prompt pattern from Lesson 2.4:

> "Below is a raw transcript from a [designer/writer/strategist] thinking through [brief description of the project]. Read it carefully. Do NOT generate ideas. Identify what I have already figured out. Synthesize my thinking. Tell me what I said."

### How They Process the Output

The student reviews the AI synthesis and answers these questions:

1. **What did the AI surface that I did not realize I had figured out?** The synthesis should contain at least one insight the student recognizes as their own but had not articulated as a decision. If it does not, the brain dump was too thin (too short, too organized, or too guarded).

2. **What specific details from my own experience appear in the synthesis?** Names, places, observations from site visits, things the client said. If the synthesis is generic, the input was generic.

3. **Where did the AI connect two things I mentioned separately?** The best syntheses link observations the student made at different points in the dump. "You mentioned X in the first minute and Y near the end. Together they suggest Z." This is the extended mind at work.

4. **What is missing?** The AI can only synthesize what was in the transcript. If an important dimension of the project is absent from the synthesis, the student did not talk about it. That absence is information about where their thinking has not yet gone.

### What to Look For

**Source: Night Owl demo comparison table (course artifact)**

The student should be able to assess their own output against the three-level framework from Lesson 2.2:

- **Level 1 output:** Generic. Could apply to any similar project. No specific details from the student's experience. (This means the brain dump was too guarded or too brief.)
- **Level 2 output:** Targeted. References the specific project and constraints. Shows competent strategic thinking. But the ideas feel like they came from the AI. (This means the brain dump included facts but not the student's actual thinking about those facts.)
- **Level 3 output:** Singular. Contains the student's own observations, connections, and instincts, organized and reflected back. Could not have come from anyone else's brain dump about the same project. (This is the target.)

### Troubleshooting

If the output is Level 1 or 2:
- The dump was probably too short. Try again, longer. 12+ minutes.
- The student may have been organizing instead of dumping. The instruction "do not organize" is harder to follow than it sounds.
- The student may have been performing for the recording. The dump should sound like talking to yourself, not presenting to a client.

**Source: Input Inversion whitepaper, Section 8:**

> "The industry has trained practitioners to perform for the model: clean prompts, specific instructions, defined formats. Unlearning that performance is harder than building the tools."

---

## Lesson 2.6: Independent Exercise + Deliverable
**The Input Practice Document**

### What the Student Submits

The student creates an **Input Practice Document** containing:

1. **The raw transcript.** Unedited. The original brain dump as transcribed. (This is the evidence that the student actually did unstructured input, not a cleaned-up version.)

2. **The AI synthesis.** The full output from the synthesis prompt.

3. **The student's reflection (200-400 words).** Answering:
   - What did the synthesis surface that I had not articulated as a decision?
   - What specific observations from my own experience appeared in the synthesis?
   - How does this compare to what I would have gotten from a structured prompt about the same project?
   - What did I learn about how I think by seeing my own thinking synthesized?

4. **One key insight extracted from the synthesis.** A single sentence naming the most important thing the brain dump produced. This is the seed the student carries into Week 3.

### The Connection to Week 3

**This is critical for the course arc.** The brain dump transcript from this exercise becomes the source material for Week 3's voice extraction work.

In Week 3 (Voice Governance), the student will:
- Analyze their own transcript for voice patterns (sentence rhythm, vocabulary, opening moves, qualifiers, absent words)
- Extract voice rules from their own speech
- Use those rules to constrain AI output so it sounds like them

The transcript they produce this week is the raw material for that extraction. This is why the transcript must be unedited and the brain dump must be genuine. Cleaned-up transcripts will not contain the voice patterns Week 3 needs.

**Source: Input Inversion whitepaper, Section 4.2 (voice sampling tool):**

> "Voice sampling extracts how I actually talk from conversation transcripts. Published writing is performance. Conversation is the source register. The tool identifies sentence rhythm, vocabulary patterns, opening moves, qualifiers, and absent words, then encodes them as generation constraints."

**Source: "The Unstructured Corpus" essay:**

> "Every tool in the accommodation design framework depends on this corpus. Voice sampling needs unstructured speech to sample from, because published writing is already cleaned up and conversation is where someone's actual patterns live."

### The Compounding Corpus

The student should understand that this single brain dump is the beginning of a practice, not a one-time exercise.

**Source: Input Inversion whitepaper, Section 9:**

> "The corpus compounds. A structured prompt gets used once. You write it, the model processes it, the output arrives, the prompt is spent. An unstructured corpus works differently. The same conversations can be traversed from completely different angles, and each traversal produces a genuinely different compiled document."

> "Two practitioners with the same tools and the same model, one who accumulated three years of unstructured thinking and one who wrote three years of structured prompts, are not in the same position. The first can run a new traversal tomorrow and get a document that surfaces connections they hadn't considered. The second would need to start writing new prompts from scratch."

**Source: Narrative architecture, Sculpting Loop section:**

> "The corpus doesn't need years. A week of brainstorming, voice memos, a napkin sketch. Any externalized thinking."

### Assessment Criteria

The deliverable is assessed on:

1. **Authenticity of the transcript.** Does it contain false starts, tangents, corrections, moments of "actually that's not what I mean"? If the transcript reads like clean prose, the student organized instead of dumped.

2. **Quality of the synthesis prompt.** Did the student use the "tell me what I said" pattern, or did they revert to asking the AI to generate ideas?

3. **Depth of reflection.** Does the student identify specific moments where the synthesis surfaced thinking they had not consciously articulated? Generic reflections ("this was useful") indicate the student did not engage with the output.

4. **Extracted insight.** Is the key insight specific to this student and this project? Could it have come from someone else's brain dump? If yes, the brain dump did not reach deep enough.

---

## Source Index

All content in this document was compiled from the following sources:

### Published Writing (petersalvato.com)
- `_research/input-inversion.md` -- Input Inversion whitepaper (Sections 1-9)
- `_essays/the-unstructured-corpus.md` -- "The Unstructured Corpus"
- `_essays/talk-to-it.md` -- "Talk to It, Don't Type at It"
- `_essays/compilation-not-generation.md` -- "I'm Compilative, Not Generative"
- `_essays/what-does-the-system-actually-need.md` -- "What Does the System Actually Need?"
- `_essays/why-does-chatgpt-get-worse.md` -- "Why Does ChatGPT Get Worse the More You Type?"

### Course Artifacts
- `course/artifacts/week2-input-inversion-demo.md` -- Night Owl Brewing demo (three levels)
- `course/artifacts/cognitive-science-references.md` -- Week 2 cognitive science citations

### Unpublished Drafts (petersalvato-dev/_drafts/)
- `knowledge-traversal.md` -- "Knowledge Traversal: Mining Conversation History"
- `the-colophon-as-proof.md` -- "The Colophon as Proof"
- `the-human-in-the-loop-is-not-a-checkbox.md` -- "The Human in the Loop Is Not a Checkbox"
- `classroom-to-ai.md` -- "Classroom to AI"
- `everyones-talking-about-what-ai-can-do.md` -- "Everyone's Talking About What AI Can Do"

### Narrative Architecture and Memory
- `petersalvato-dev/narrative-architecture.md` -- Sculpting Loop section, Maker's Domains, Core Operation
- `memory/core-insight-2026-03-08.md` -- The Selector, attunement unified, DJ as pacing origin
- `memory/practice-pillars.md` -- Five practice pillars (Input-First Design)

### Cognitive Science References (full citations in cognitive-science-references.md)
- Kellogg (1996, 2008) -- Working memory in writing
- Chi (1994, 2000) -- Self-explanation effect
- Clark & Chalmers (1998) -- Extended mind thesis
- Osborn (1953) / Amabile (1983) -- Premature evaluation suppresses creativity
- Cseh et al. (2015) -- Creative flow and ambiguity
- Ng (2024) -- Agentic workflow benchmarks (GPT-3.5 at 95.1% vs GPT-4 at 67%)
- Voice input cognitive load research (Kellogg 1996, planning-translation separation; specific percentage removed pending source verification)

---

## Items Requiring Peter

| Item | Lesson | What Is Needed |
|------|--------|----------------|
| Video intro recording | 2.1 | Peter talks through the "better prompts still produce generic output" arc naturally, not from script |
| Real Night Owl transcript | 2.2 | Replace simulated Mara Voss brain dump with a real recorded transcript |
| Brain dump demo recording | 2.4 | Peter records a real brain dump (tangents, corrections, false starts visible) |
| Bakery scenario validation | 2.4 | Confirm the guided scenario works or replace with a better one |
| Assessment rubric review | 2.6 | Confirm the four assessment criteria and their weighting |
| Week 3 handoff confirmation | 2.6 | Confirm the transcript-to-voice-extraction pipeline is how Week 3 opens |
