# Week 1: Task Decomposition — Compiled Source Material

Compiled 2026-04-04. Every quote, example, and teaching point is sourced. Nothing is generated. Sections marked [NEEDS PETER] require original material from Peter that does not yet exist in the source corpus.

---

## Attunement Frame: Reading the AI's Task-Processing Limits

Designers attune to receiving systems every day. You read a client's decision-making style and shape the presentation to match. You read an audience's attention patterns and design the layout to hold them. You read a student's processing capacity and break the instruction into steps they can follow. The question underneath all of these: what does this system actually need to succeed at this task?
[SOURCE: essay, what-does-the-system-actually-need.md]

This week applies that attunement skill to a specific receiving system: a large language model processing a compound instruction. The model has processing limits, just as a student has working memory limits. When you give it five objectives in a single prompt, it distributes attention across all five, and each one gets a fraction. The output comes back competent but shallow. The fix is the same fix a special education teacher applies when a student can only hold one instruction at a time: decompose.
[SOURCE: whitepaper, README.md, Section 1]

Task decomposition is attunement in action. You read the AI's processing reality (attention splits across concurrent objectives), and you design the task around that reality (one objective per prompt). The technique is straightforward. The skill underneath it, reading the receiving system, is what makes it transferable to every other context in this curriculum.

---

## Lesson 1.1 — The Frame Break (Video Intro Script Outline)

**Format:** On-camera, 3-5 minutes, direct address, no slides.

### Peter's Own Words About the Frame Break

The strongest source for Peter's natural voice on this problem is the published essay "The Wrong Question":

> "You write a prompt. The output is close but flat. So you add detail. You specify tone, structure, audience, format. You add examples. The prompt grows to three paragraphs, then five. The output gets different, but it does not get better. It gets blurry. You add more constraints. The model starts contradicting itself within the same response. You conclude that the tool is not capable enough, and you wait for the next version."
[SOURCE: essay, the-wrong-question.html, paragraph 1]

> "This is the most common experience practitioners have with AI, and almost everyone draws the wrong conclusion from it."
[SOURCE: essay, the-wrong-question.html, paragraph 2]

> "The problem is not the model. The problem is the question you are asking about the model."
[SOURCE: essay, the-wrong-question.html, paragraph 3]

From the whitepaper, Peter frames the same problem in terms of the field's orientation:

> "When output quality degrades, the response is more constraint. Longer system prompts. More detailed instructions. Tighter formatting. The prompts grow. The output keeps degrading. The practitioners conclude the model isn't capable enough and wait for the next version."
[SOURCE: whitepaper, README.md, Section 1 "The Wrong Question"]

> "There is a different question: what does each system in the room actually need to do this job well?"
[SOURCE: whitepaper, README.md, Section 1]

From the compound-prompt-demo artifact, the core frame:

> "A compound prompt makes the AI the creative director. Decomposed prompts make you the creative director with specialists reporting to you."
[SOURCE: artifact, compound-prompt-demo.md, line 9]

From the foundations-scaffold.md, the lesson objective:

> "Cold open: the moment every creative hits. The prompt keeps getting longer. You add more context, more constraints, more instructions. The output gets slightly better but never good. You're negotiating with a system instead of directing it."
[SOURCE: scaffold, foundations-scaffold.md, Lesson 1.1]

> "The instinct is wrong. More instructions in a single prompt is not 'being more specific.' It's overloading a single worker with a job that needs a team."
[SOURCE: scaffold, foundations-scaffold.md, Lesson 1.1]

### Script Outline (from scaffold + sources)

1. Cold open: describe the moment. The prompt keeps getting longer. Output gets different but not better. Gets blurry. [SOURCE: essay, the-wrong-question.html]
2. The wrong instinct: adding more detail, more constraints. "You're negotiating with a system instead of directing it." [SOURCE: scaffold, foundations-scaffold.md]
3. The wrong conclusion: the tool isn't good enough. Wait for the next version. [SOURCE: whitepaper, README.md, Section 1]
4. The reframe: the problem isn't the model, it's the input structure. "More instructions in a single prompt is not 'being more specific.' It's overloading a single worker with a job that needs a team." [SOURCE: scaffold, foundations-scaffold.md]
5. Frame the week: "you're going to learn why compound prompts degrade, see the difference decomposition makes on a real project, and then do it yourself." [SOURCE: scaffold, foundations-scaffold.md]

[NEEDS PETER: The actual script. The sources above give the argument, the language, and the beats. Peter needs to perform this on camera in his own rhythm. The scaffold notes say "No jargon. No slides. Direct address. 3-5 minutes." Peter writes and performs this.]

---

## Lesson 1.2 — The Compound Instruction Problem

**Format:** Written lesson. **Learning objective:** The student can explain why compound prompts produce shallow output, citing both the serial position effect and cognitive load theory.

### The Argument: Compound Instructions Degrade

#### From the Classroom (Peter's own telling)

From the blog draft "Classroom to AI":

> "First, you have to decompose the task before the student sees it. A compound instruction ('take out your notebook, turn to page 42, and answer questions 3 through 7') is one task for a neurotypical student and three tasks for a student with processing delays. If I didn't break it apart, the student failed before they started. The failure wasn't about ability. It was about input format."
[SOURCE: blog draft, classroom-to-ai.md, paragraph 6]

From the published essay "The IEP for AI Systems":

> "A fourth grader with processing delays can't receive a multi-step math problem as a single instruction. 'Solve for the missing number, show your work, and explain your reasoning' is three tasks disguised as one. The student hears the first instruction, starts working, and the second two are gone."
[SOURCE: published essay, petersalvato.com/_essays/the-iep-for-ai-systems.md, "Decompose or fail" section]

From the whitepaper:

> "Decomposition. 'Solve for the missing number, show your work, and explain your reasoning' is three tasks disguised as one. A student with processing delays hears the first instruction, starts working, and the rest is gone. You learn to give one instruction at a time. One clear objective. One visible result before the next step."
[SOURCE: whitepaper, README.md, Section 2.1]

From the essay "The Wrong Question":

> "In a special education classroom, a compound instruction looks like this: 'Take out your notebook, turn to page 42, and answer questions three through seven.' For a neurotypical student, that is one task. For a student with processing delays, that is three tasks delivered simultaneously, and if you do not break them apart, the student fails before they start."
[SOURCE: essay, the-wrong-question.html]

> "The failure is not about ability. The student can do all three things. The failure is about input format. The instruction arrived in a shape the receiving system could not process whole."
[SOURCE: essay, the-wrong-question.html]

#### The Transfer to AI (Peter's own telling)

From "Classroom to AI":

> "The input format problem: an AI tool that receives a compound prompt ('evaluate this for voice quality, structural integrity, narrative coherence, and brand alignment') processes the first criterion with full attention and the rest gets progressively less. The model's context window is a working memory ceiling. Same problem as the student with processing delays. Same fix. Decompose the task. One criterion per pass."
[SOURCE: blog draft, classroom-to-ai.md, paragraph 11]

From the whitepaper:

> "In 2023 I started building AI evaluation systems. The first approach was conventional: compound prompts asking the model to evaluate across multiple dimensions at once. I gave it a prompt: evaluate this portfolio for voice quality, structural integrity, narrative coherence, and brand alignment. The model processed the first criterion with full attention. Each subsequent criterion got less. The output blurred all four together into a blended average that was none of them. Criteria contaminated each other. Contradictions showed up within a single evaluation pass."
[SOURCE: whitepaper, README.md, Section 2.2]

> "I recognized it immediately. A compound instruction given to a system that can't process it whole. I'd seen this every day in the classroom. The fix is the same fix. Decompose. One dimension per prompt. One clear objective. One clear output. Run them independently."
[SOURCE: whitepaper, README.md, Section 2.2]

From the published essay "The IEP for AI Systems":

> "A monolithic prompt that says 'evaluate this portfolio for voice quality, structural integrity, narrative coherence, and brand alignment' is four tasks disguised as one. The model receives the first criterion, starts working, and the others drift. Output quality degrades as the instruction gets longer. Context gets polluted. The model can't hold all four evaluation frames simultaneously, so it collapses them into a blended average that's none of the four."
[SOURCE: published essay, petersalvato.com/_essays/the-iep-for-ai-systems.md, "Decompose or fail" section]

From the essay "The Wrong Question":

> "Now look at what happens when you give an AI a compound evaluation prompt: 'Evaluate this work for voice quality, structural integrity, narrative coherence, and brand alignment.' The model processes the first criterion with full attention. Each subsequent criterion gets less. By the fourth, the model is blending dimensions together, producing a vague average that is none of them. Contradictions appear within a single response. The evaluation is mush."
[SOURCE: essay, the-wrong-question.html]

> "The structural problem is identical. A compound instruction delivered to a system that cannot process it whole. The response most practitioners reach for is also identical to the wrong one in a classroom: repeat the instruction louder. Add more detail. Write a longer prompt. Specify harder."
[SOURCE: essay, the-wrong-question.html]

#### Peter's Framing of the Key Insight

From the whitepaper Section 3 (the mapping table):

> "Compound instructions degrade the same way in both systems."
[SOURCE: whitepaper, README.md, Section 3, table row for "Task decomposition"]

From "Classroom to AI":

> "I didn't design these parallels. I discovered them after the fact. The classroom forced me to figure out decomposition, scaffolding, and independent evaluation because twelve kids with twelve different needs demanded it. AI tools forced me to figure out the same things for the same reasons. The system is different. The structural problem is the same."
[SOURCE: blog draft, classroom-to-ai.md, final paragraph]

From the published essay:

> "That's a structural decision about how complex work gets delivered to a system that can't process it whole. That sentence describes a fourth grader in Sunset Park. It also describes a large language model receiving a compound evaluation prompt."
[SOURCE: published essay, petersalvato.com/_essays/the-iep-for-ai-systems.md, "Decompose or fail" section]

### The Cognitive Science

From the cognitive science references document:

**Serial Position Effect (Murdock 1962, Liu et al. 2024):**

> "LLMs degrade 30%+ in accuracy when relevant information is positioned in the middle of a long input, compared to the beginning or end. Performance follows a U-shaped curve mirroring the human serial position effect."
[SOURCE: cognitive-science-references.md, Week 1 Primary Citations, Liu et al.]

> "Items at the beginning (primacy) and end (recency) of a list are recalled significantly better than items in the middle. The middle-position deficit is robust across conditions."
[SOURCE: cognitive-science-references.md, Week 1 Primary Citations, Murdock 1962]

Teaching application: "Compound prompts bury critical instructions in the middle. Decomposition puts each instruction at the focal point of its own step."
[SOURCE: cognitive-science-references.md, Liu et al. "Maps to" note]

**Cognitive Load Theory (Sweller 1988, Cowan 2001):**

> "Working memory can process approximately 2-4 novel items concurrently. Overloading working memory with extraneous information degrades learning and performance."
[SOURCE: cognitive-science-references.md, Week 1 Primary Citations, Sweller 1988]

> "The effective capacity of the focus of attention is approximately 4 chunks, not the 7 +/- 2 that Miller (1956) proposed."
[SOURCE: cognitive-science-references.md, Week 1 Primary Citations, Cowan 2001]

Teaching application: "Compound prompts overload the model's 'working memory' (attention budget) the same way overloaded briefs overload human working memory. Decomposition is a cognitive load management strategy."
[SOURCE: cognitive-science-references.md, Sweller "Maps to" note]

Honest caveat for the course: "LLMs don't have working memory in the human sense. The analogy is useful for teaching but shouldn't be presented as a direct equivalence. The functional parallel (performance degrades with input complexity) holds even if the mechanism differs."
[SOURCE: cognitive-science-references.md, Sweller caveat]

**Task Analysis in Special Education (Wong et al. 2014):**

> "Task analysis (breaking complex behaviors into discrete, teachable steps) is classified as an evidence-based practice in special education. Decades of applied research show it improves learning outcomes for students with cognitive disabilities."
[SOURCE: cognitive-science-references.md, Week 1 Supporting Citations, Wong et al. 2014]

### The Voss Type Compound Output as the Example

The compound prompt (full text):

> "Act as a creative director. I'm Mara Voss, a freelance brand designer and letterer based in Brooklyn. I'm launching my own studio called Voss Type. My clients are independent food brands, breweries, and record labels. My style is bold, hand-drawn typography with a confrontational edge. Generate a visual branding guide for Voss Type that includes: recommended color palette with hex codes and psychological rationale, typography pairings with usage contexts, logo style direction, imagery guidelines, and layout principles for my website and social media. Make sure it reflects my hand-crafted aesthetic and stands out from the minimal-clean trend."
[SOURCE: artifact, compound-prompt-demo.md, Part 1]

The compound output is the full "Voss Type -- Visual Branding Guide" in the artifact (lines 19-199). It covers all 5 sections: Color Palette, Typography Pairings, Logo Style Direction, Imagery Guidelines, Layout Principles.
[SOURCE: artifact, compound-prompt-demo.md, Part 1]

The scaffold frames this output as: "It's competent. It's a B+. Point out what's good about it: coherent, complete, professional. This is not garbage. That's what makes it dangerous. It looks done."
[SOURCE: scaffold, foundations-scaffold.md, Lesson 1.2]

The artifact's own framing:

> "A coherent brand guide in one pass. Competent. Professional. A B+ deliverable. Every section was shaped by the same attention in a single generation."
[SOURCE: artifact, compound-prompt-demo.md, Part 3 "What the compound version produced"]

> "One voice, one perspective, one creative director making all the decisions simultaneously."
[SOURCE: artifact, compound-prompt-demo.md, Part 3]

The key structural observation:

> "The compound prompt made the AI the creative director. One perspective made all the decisions. The output is coherent because one mind shaped it. That coherence is also its limitation: no tension, no surprise, no moment where one dimension pushes back against another."
[SOURCE: artifact, compound-prompt-demo.md, Part 3 "The structural difference"]

---

## Lesson 1.3 — The Decomposition

**Format:** Written lesson. **Learning objective:** The student can identify the structural differences between compound and decomposed outputs and explain why independent specialist prompts produce deeper results.

### The Five Decomposed Prompts

Each prompt addresses a single dimension. Each is given only the brief and explicitly told to ignore other dimensions.

**Prompt 1 (Color):** "...Recommend a color palette with hex codes. For each color, explain what it does in the system (primary, accent, neutral, etc.) and why it fits this specific studio's positioning. Do not address typography, logo, imagery, or layout."
[SOURCE: artifact, compound-prompt-demo.md, Prompt 1]

**Prompt 2 (Typography):** "...Recommend typography pairings for the studio's own brand materials. For each pairing, specify where it's used (headlines, body, captions, UI) and why it fits. Do not address color, logo, imagery, or layout."
[SOURCE: artifact, compound-prompt-demo.md, Prompt 2]

**Prompt 3 (Logo):** "...Describe the logo style direction. Not a logo design. The principles, references, and constraints that should govern the mark. What it should feel like, what it should avoid, what makes it unmistakably this studio. Do not address color, typography, imagery, or layout."
[SOURCE: artifact, compound-prompt-demo.md, Prompt 3]

**Prompt 4 (Imagery):** "...Define imagery guidelines for the studio's own brand presence (website, social, case studies). What kinds of images, what treatment, what to avoid. Photography style, texture use, how hand-drawn work is photographed or scanned. Do not address color, typography, logo, or layout."
[SOURCE: artifact, compound-prompt-demo.md, Prompt 4]

**Prompt 5 (Layout):** "...Define layout principles for the studio website and social media. Grid behavior, spacing philosophy, how density vs whitespace is handled, how the hand-crafted feeling survives in a digital layout. Do not address color, typography, logo, or imagery."
[SOURCE: artifact, compound-prompt-demo.md, Prompt 5]

### The Five Decomposed Outputs

All five outputs are in the artifact (compound-prompt-demo.md, Part 2, lines 203-412). Each is substantially deeper than its compound counterpart. The full outputs should be included in the lesson.
[SOURCE: artifact, compound-prompt-demo.md, Part 2]

### The Side-by-Side Comparison (from the artifact's own analysis)

> "Five independent specialist reports, each significantly deeper than its compound counterpart:"
[SOURCE: artifact, compound-prompt-demo.md, Part 3]

**Color comparison:**
> "Color added a conditional fifth color with a rationale for restraint, and explained the palette as a two-color print job structure reflecting how the studio's clients actually produce packaging."
[SOURCE: artifact, compound-prompt-demo.md, Part 3]

**Typography comparison:**
> "Typography provided three complete pairing options with a recommendation and context-specific reasoning for when each works best, rather than two pairings."
[SOURCE: artifact, compound-prompt-demo.md, Part 3]

**Logo comparison:**
> "Logo went into the philosophy of the mark: 'the ratio of control to roughness,' reproducibility on a napkin, printer's marks from the 1500s as structural precedent. The compound version described a mark. The decomposed version described what the mark needs to feel like and why."
[SOURCE: artifact, compound-prompt-demo.md, Part 3]

**Imagery comparison:**
> "Imagery specified scanning DPI, case study image minimums, a 60/40 process-to-finished ratio for social, and distinguished between scanning and photographing hand-drawn work."
[SOURCE: artifact, compound-prompt-demo.md, Part 3]

**Layout comparison:**
> "Layout introduced rotational micro-offsets, imperfect alignment as intentional design, edge bleed as a compositional tool, and the principle 'tight until it hurts, then tighter.'"
[SOURCE: artifact, compound-prompt-demo.md, Part 3]

### The Structural Difference

> "The compound prompt made the AI the creative director. One perspective made all the decisions. The output is coherent because one mind shaped it. That coherence is also its limitation: no tension, no surprise, no moment where one dimension pushes back against another."
[SOURCE: artifact, compound-prompt-demo.md, Part 3]

> "The decomposed prompts made the AI five independent specialists. Each went deep on one dimension without being constrained by the others. Now the designer reads five reports and makes the decisions about how they fit together. The typography specialist might push in a direction that conflicts with the layout specialist. That tension is where the design happens."
[SOURCE: artifact, compound-prompt-demo.md, Part 3]

> "The compound prompt gives you the AI's vision of your brand. The decomposed prompts give you five specialists reporting to you. You are the creative director."
[SOURCE: artifact, compound-prompt-demo.md, Part 3, final line]

### Cognitive Science for This Lesson

**AlphaCodium (Ridnik et al. 2024):**
> "Code generation accuracy jumped from 19% (compound prompt) to 44% (decomposed multi-step flow) on the CodeContests benchmark. Same model, same problems, different input structure."
[SOURCE: cognitive-science-references.md, Week 1 Primary Citations]

Teaching application: "Direct evidence that decomposition improves output quality on complex tasks without changing the model."
[SOURCE: cognitive-science-references.md, Ridnik "Maps to" note]

**Andrew Ng (2024):**
> "GPT-3.5 with a decomposed agentic workflow (95.1%) outperformed GPT-4 with a single compound prompt (67%) on the HumanEval coding benchmark."
[SOURCE: cognitive-science-references.md, Week 1 Primary Citations]

Teaching application: "The architecture of the input matters more than the capability of the model. This is the single most persuasive data point for the course's core thesis."
[SOURCE: cognitive-science-references.md, Andrew Ng "Maps to" note]

Honest caveat: "HumanEval is a coding benchmark. The 95.1% vs. 67% comparison is dramatic but domain-specific. We should be careful about generalizing to all creative work."
[SOURCE: cognitive-science-references.md, Andrew Ng caveat]

**Chain-of-Thought (Wei et al. 2022):**
> "Adding 'Let's think step by step' or explicit reasoning steps to prompts substantially improved performance on arithmetic, commonsense, and symbolic reasoning tasks."
[SOURCE: cognitive-science-references.md, Week 1 Supporting Citations]

Teaching application: "Chain-of-thought is a lightweight form of decomposition. It forces the model to externalize intermediate steps rather than jumping to a final answer."
[SOURCE: cognitive-science-references.md, Wei "Maps to" note]

### The Pivot to Lesson 1.4

The scaffold frames this transition:

> "But there's a new problem. Five independent outputs. They don't talk to each other. The typography specialist might push in a direction that conflicts with the layout specialist. The color palette might imply a different mood than the imagery guidelines suggest. Nobody is in charge. That's Lesson 1.4. You are."
[SOURCE: scaffold, foundations-scaffold.md, Lesson 1.3]

---

## Lesson 1.4 — The Synthesis Step

**Format:** Written lesson + Exercise. **Learning objective:** The student can synthesize independent specialist outputs into a unified brief by resolving conflicts, finding amplifications, and setting cross-system rules.

### The Synthesized Voss Type Brief

The scaffold specifies the three types of creative director moves the synthesized brief demonstrates:

**Conflicts resolved:**
> "The typography specialist recommended Knockout (Hoefler) while the layout specialist assumed a grotesk. The creative director chose Druk Wide from Pairing 1 because the layout's 'tight until it hurts' philosophy needs a typeface that holds under compression. Knockout is wide. Druk is wide but compressed. That's the call."
[SOURCE: scaffold, foundations-scaffold.md, Lesson 1.4]

**Amplifications found:**
> "The color specialist's 'two-color print job' logic and the imagery specialist's 'shoot on real substrates' converge. Both point toward a brand that looks printed even on screen. That convergence wasn't in either output. The human saw it."
[SOURCE: scaffold, foundations-scaffold.md, Lesson 1.4]

**Cross-system rules set:**
> "The logo specialist said 'reproducible by hand on a napkin.' The typography specialist said 'hand-lettered display for all recurring headers.' These are two versions of the same rule: the human hand is visible everywhere. That becomes a governing principle, not just two separate recommendations."
[SOURCE: scaffold, foundations-scaffold.md, Lesson 1.4]

### What the Human Did That Neither Output Could Do

From the scaffold:

> "Read across domains (the AI couldn't because each prompt was isolated). Detected convergences and tensions (requires understanding the project holistically). Made judgment calls where specialists disagreed (this is creative direction). Set hierarchy (which specialist's recommendation governs when they conflict)."
[SOURCE: scaffold, foundations-scaffold.md, Lesson 1.4]

### Peter's Framing of the Creative Director Role

From the artifact:

> "The compound prompt gives you the AI's vision of your brand. The decomposed prompts give you five specialists reporting to you. You are the creative director."
[SOURCE: artifact, compound-prompt-demo.md, Part 3, final line]

From the foundations course page (joinery-site):

> "Your prompts keep getting longer and your output keeps getting worse. The problem is structural: compound instructions degrade in AI the same way they degrade in a classroom. You learn to decompose, run independently, and synthesize. The AI gives you depth. You provide the coherence."
[SOURCE: foundations.html, Week 1 description]

From the scaffold's core lesson statement:

> "You are the creative director of a team of specialists. The AI gives you depth. You provide the coherence. The synthesis step (where you resolve conflicts between independent outputs) is where your judgment becomes the product."
[SOURCE: scaffold, foundations-scaffold.md, Week 1 core lesson]

From the essay "The Wrong Question":

> "The fix is identical too. Decompose. One dimension per prompt. One clear objective. One defined output. Run them independently. A coordinator collects the results and maps where they converge (act on it) and where they diverge (the practitioner decides). The model was never incapable. The instruction was shaped wrong for the system receiving it."
[SOURCE: essay, the-wrong-question.html]

From the published "IEP for AI Systems" essay, on evaluation conflict:

> "In the classroom, when two IEP goals conflicted (one student needed quiet, another needed verbal processing), the resolution was a structural decision: where to seat them, when to schedule which activity, how to create pockets of different conditions within one room. The conflict wasn't a problem. It was information about what the room needed to accommodate."
[SOURCE: published essay, petersalvato.com/_essays/the-iep-for-ai-systems.md]

> "Evaluation lenses work the same way. When structural and narrative lenses disagree, the disagreement tells me what decision I need to make as the designer. That's often the most useful thing the system gives me."
[SOURCE: published essay, petersalvato.com/_essays/the-iep-for-ai-systems.md]

From "The Human in the Loop Is Not a Checkbox" (on what real human leverage means):

> "Human in the loop means the human has actual leverage over the outcome. Not just the ability to reject output but the ability to shape it during production."
[SOURCE: blog draft, the-human-in-the-loop-is-not-a-checkbox.md]

### Source Material for the "Pressure-to-Control Ratio" and Specific Synthesis Findings

The decomposed logo output contains the "pressure-to-control ratio" concept:

> "The ratio of control to roughness. This is the signature of someone who letters professionally: the strokes are not sloppy, but they are not sterilized. There is a specific zone where craft meets aggression, where you can tell the person has drawn ten thousand letters and still pushes the tool like they have something to prove. The mark lives in that zone."
[SOURCE: artifact, compound-prompt-demo.md, Output 3: Logo Style Direction]

The decomposed typography output has the Druk Wide recommendation:

> "Druk Wide Bold (Commercial Type) for headlines, section titles, studio name in large-format applications. Druk Wide is compressed aggression. The extended width commands horizontal space the way a wheat-paste poster claims a wall."
[SOURCE: artifact, compound-prompt-demo.md, Output 2: Typography Pairings, Pairing 1]

The decomposed layout output has the micro-rotation detail:

> "Rotational micro-offsets. Select elements rotate between negative 1 and positive 2 degrees. Not enough to read as a 'design trick.' Enough to break the pixel grid's perfection."
[SOURCE: artifact, compound-prompt-demo.md, Output 5: Layout Principles]

[NEEDS PETER: The actual synthesized Voss Type brief itself. The scaffold (foundations-scaffold.md, Lesson 1.4 Production notes) explicitly states: "WRITE: The synthesized Voss Type brief showing conflict resolution, amplification, and cross-system rules (Peter writes this, it's the key teaching artifact for the course's core claim)." The sources above provide the raw material for what the brief should contain and the three types of moves it should demonstrate. Peter needs to write the brief that demonstrates a creative director reading five specialist reports and making the calls.]

[NEEDS PETER: The guided exercise scenario. The scaffold specifies: "a pre-built set of 3 decomposed outputs for a different fictional project (a podcast brand identity: name direction, visual identity, episode format). The outputs contain two planted conflicts and one amplification." This exercise content does not exist yet.]

### Guided Synthesis Template (from scaffold)

The five-step synthesis process for the exercise:

1. Read all outputs. Highlight where they agree.
2. Identify where they conflict. Write down the conflict in one sentence.
3. For each conflict, decide which output governs and why.
4. Identify any amplifications (convergences neither output stated explicitly).
5. Write a 1-page synthesized brief incorporating your decisions.

[SOURCE: scaffold, foundations-scaffold.md, Lesson 1.4]

---

## Lesson 1.5 — Guided Exercise: Decompose Your Own Work

**Format:** Exercise. **Learning objective:** The student can decompose one of their own compound prompts into independent specialist prompts and document the difference in output quality.

### The Decomposition Structure (modeled on the Voss Type demo)

The prompting pattern from the artifact. Each decomposed prompt follows this structure:

1. **One objective.** "Recommend a color palette with hex codes." Not "recommend a color palette and typography pairings."
2. **One output.** "For each color, explain what it does in the system and why it fits." Not "explain the color palette, typography, and logo direction."
3. **Explicit exclusion constraints.** "Do not address typography, logo, imagery, or layout." Every prompt explicitly tells the model what to ignore.
4. **Only the context it needs.** Each prompt gets the brief (who the client is, what the studio does) but not the other outputs.

[SOURCE: artifact, compound-prompt-demo.md, Part 2, prompt structure visible across all 5 prompts]

From the whitepaper on the skill architecture principle:

> "Give a model twelve objectives in a single prompt and it prioritizes the first few. The rest degrade. Instruction ordering changes which objectives get attention."
[SOURCE: whitepaper, README.md, Section 4.3]

> "So every skill I build has one objective, one output, no knowledge of other skills."
[SOURCE: whitepaper, README.md, Section 4.3]

### The Exercise Template (from scaffold)

1. Paste your compound prompt.
2. List every distinct task or dimension the prompt asks for. Number them.
3. For each task, write a standalone prompt that addresses only that dimension. Give it only the context it needs and explicitly tell it to ignore other dimensions.
4. Run the compound prompt. Save the output.
5. Run each decomposed prompt independently. Save the outputs.
6. Compare: Where is the decomposed output deeper? Where does the compound output have better coherence? What conflicts exist between the decomposed outputs?

[SOURCE: scaffold, foundations-scaffold.md, Lesson 1.5]

Documentation template:

- Original compound prompt
- Compound output (key excerpts)
- Decomposed prompts (all)
- Decomposed outputs (key excerpts)
- Where the decomposed version was deeper (specific examples)
- Where conflicts or tensions appeared between specialists
- What you would synthesize differently from what the compound version decided

[SOURCE: scaffold, foundations-scaffold.md, Lesson 1.5]

### Cognitive Science for This Lesson

**Least-to-Most Prompting (Zhou et al. 2022):**

> "On the SCAN compositional generalization benchmark, least-to-most prompting achieved 99.7% accuracy where standard prompting scored near zero. The technique decomposes hard problems into progressively easier sub-problems."
[SOURCE: cognitive-science-references.md, Week 1 Supporting Citations]

Teaching application: "Extreme case of decomposition benefit. When the task exceeds the model's capacity as a single step, decomposition doesn't just improve results, it makes them possible at all."
[SOURCE: cognitive-science-references.md, Zhou "Maps to" note]

### Framing the Exercise

You have watched decomposition work on Voss Type. A compound prompt that asked for five dimensions at once. Five specialist prompts that each went deeper. A synthesis step that made the human the creative director.

Now you do it on your own work.

You already have the material. Pick one compound prompt from a recent project. Any project, any domain. The only requirement is that the prompt asks the model for multiple things in a single shot: color and typography, or messaging and structure, or tone and length and format, or anything else that asks the model to carry multiple dimensions at once.

You have the prompt. You have the output. You already felt the result come back "close but flat." [SOURCE: essay, the-wrong-question.html] Or blurry. Or fine-but-not-what-you-wanted. That feeling is where you start.

Run the template above. At the end you will have two versions of the same work: the compound version you already shipped, and the decomposed version you built as the creative director. Compare them. Notice where the decomposed version went deeper, where it surfaced conflicts you did not see in the compound output, and where the compound version felt more coherent because one mind made all the calls.

This lesson is for practice on one workflow. The next lesson takes the same cycle to a different workflow and asks you to submit it as Week 1's deliverable.

---

## Lesson 1.6 — Independent Exercise + Deliverable

**Format:** Exercise + Deliverable. **Learning objective:** The student can independently decompose a compound workflow, run both versions, synthesize the decomposed outputs, and articulate what their judgment added.

### Deliverable Requirements (from scaffold)

The student picks a second workflow from their own work. Different project than 1.5. No template this time.

**The full cycle:**

1. Identify a compound prompt or workflow.
2. Decompose it into independent specialist prompts.
3. Run both versions (compound and decomposed).
4. Synthesize the decomposed outputs into a unified brief. Resolve conflicts. Find amplifications. Set cross-system rules.
5. Compare the compound output to the synthesized brief.

[SOURCE: scaffold, foundations-scaffold.md, Lesson 1.6]

### What the Student Submits

- The compound prompt and its output (before)
- The decomposed prompts and their individual outputs
- The synthesized brief (after)
- A short reflection (3-5 sentences): What did the synthesis step require from you that neither the AI compound output nor the individual specialist outputs could provide?

[SOURCE: scaffold, foundations-scaffold.md, Lesson 1.6]

### What "Done" Looks Like

From Peter's own quality criteria (compiled from multiple sources):

**The decomposition is real, not cosmetic.** Each prompt has one objective, one output, and explicit exclusion of other dimensions. This is the pattern demonstrated in the artifact.
[SOURCE: artifact, compound-prompt-demo.md, Part 2, prompt structure]

**The depth difference is visible.** The decomposed outputs go deeper than the compound output on their respective dimensions. If they don't, the student either didn't decompose far enough or the original prompt was already single-objective.
[SOURCE: artifact, compound-prompt-demo.md, Part 3: "Five independent specialist reports, each significantly deeper than its compound counterpart"]

**The synthesis contains decisions the AI didn't make.** The brief should show evidence of:
- Conflicts identified and resolved (which specialist governs when they disagree)
- Amplifications found (convergences that neither individual output stated)
- Cross-system rules set (principles that emerge from reading across outputs)
[SOURCE: scaffold, foundations-scaffold.md, Lesson 1.4]

**The reflection identifies the human's contribution.** From the course's core lesson: "The synthesis step (where you resolve conflicts between independent outputs) is where your judgment becomes the product."
[SOURCE: scaffold, foundations-scaffold.md, Week 1 core lesson]

From the published essay "The IEP for AI Systems":

> "The move that works in the classroom works here too. Pull the compound apart. Give each evaluation dimension its own skill, its own objective, its own visible result before the next one fires."
[SOURCE: published essay, petersalvato.com/_essays/the-iep-for-ai-systems.md]

From the whitepaper, on why the practitioner resolves conflicts:

> "The practitioner resolves disagreements. The model never does."
[SOURCE: whitepaper, README.md, Section 4.3]

> "The current industry focus on agentic development inverts this relationship. An agent asks the model to set its own goals, manage its own attention, evaluate its own progress. Skills ask the practitioner to do that work."
[SOURCE: whitepaper, README.md, Section 4.3]

### Cognitive Science for This Lesson

From the scaffold:

> "Andrew Ng 2024 (the architecture of the input matters more than the capability of the model, student now has personal evidence for this claim)."
[SOURCE: scaffold, foundations-scaffold.md, Lesson 1.6]

This is the moment where the student has their own data for the course's core claim. They've run both versions on their own work. The difference isn't theoretical.

[NEEDS PETER: The reflection prompt. The scaffold says "Peter writes the reflection prompt, it needs to point at the right insight." The question above ("What did the synthesis step require from you that neither the AI compound output nor the individual specialist outputs could provide?") comes from the scaffold and may be sufficient, but Peter should decide if it points sharply enough at the "you are the creative director" insight.]

### Submission Format

Submit one document (PDF, Google Doc, or markdown file) containing all six items listed above, in that order.

**Length guidance:**
- The synthesized brief runs approximately 400-600 words (one page).
- The reflection runs 3-5 sentences.
- The decomposed outputs may run long; include them in full. No cap on total document length.

**File naming:** `week1-deliverable-[your-name].pdf` (or equivalent extension).

---

## Cross-Lesson Source Index

### Artifacts Used
- `/home/peter/homelab/projects/active/joinery-site/course/artifacts/compound-prompt-demo.md` -- All of Part 1 (compound), Part 2 (5 decomposed), Part 3 (comparison)
- `/home/peter/homelab/projects/active/joinery-site/course/artifacts/cognitive-science-references.md` -- Week 1 section (all primary and supporting citations)

### Peter's Published/Draft Writing Used
- `/home/peter/homelab/projects/active/joinery-site/essays/the-wrong-question.html` -- The essay's full argument about compound instructions
- `/home/peter/homelab/projects/active/petersalvato.com/_essays/the-iep-for-ai-systems.md` -- "Decompose or fail," scaffolding, individualized criteria sections
- `/home/peter/homelab/projects/active/accommodation-design/README.md` -- Sections 1, 2.1, 2.2, 3, 4.3 (the whitepaper)
- `/home/peter/homelab/projects/active/petersalvato-dev/_drafts/classroom-to-ai.md` -- The full classroom-to-AI transfer story
- `/home/peter/homelab/projects/active/petersalvato-dev/_drafts/the-human-in-the-loop-is-not-a-checkbox.md` -- Human leverage over outcomes
- `/home/peter/homelab/projects/active/petersalvato-dev/_drafts/constraint-as-creative-fuel.md` -- Constraint as productive limitation (supporting)
- `/home/peter/homelab/projects/active/petersalvato-dev/_drafts/why-your-claudemd-is-an-iep.md` -- CLAUDE.md as IEP parallel (supporting)

### Scaffold Used
- `/home/peter/homelab/projects/active/joinery-site/course/foundations-scaffold.md` -- Lesson outlines, production notes, exercise structures

### Sources Searched But No Relevant Content Found
- ChatGPT conversation export about "three-role novel assistant" / "Document Evaluation Plan" (conversation index 4) -- Not found in the joinery-site directory or active projects. No file matching this description located.
- Session files in `/home/peter/.claude/projects/-home-peter-homelab-projects-active-petersalvato-com/` -- Session logs matched on keywords (compound, decompose, creative director) but are JSONL session data, not extractable conversation quotes without a parsing pass.
- Peter's conversation history for specific moments where decomposition worked or failed in practice -- Multiple session files contain relevant keywords, but extracting natural-language quotes from JSONL session logs requires the `/knowledge` skill traversal. The blog drafts and published essays contain Peter's own retelling of these moments and are used instead.

### Items That Need Peter

| Item | Lesson | Why It Can't Be Compiled |
|------|--------|--------------------------|
| Video script (performed on camera) | 1.1 | Peter performs this. Sources above provide the argument and beats. |
| Synthesized Voss Type brief | 1.4 | The key teaching artifact. Must demonstrate creative director judgment on the five outputs. Scaffold explicitly marks this as "Peter writes." |
| Podcast brand exercise (3 outputs with planted conflicts) | 1.4 | Original exercise content. No source exists. |
| Template introduction/framing for 1.5 | 1.5 | Peter's voice framing the exercise. |
| Reflection prompt (final version) | 1.6 | Scaffold provides a draft question. Peter decides if it points at the right insight. |
| Submission format template | 1.6 | Operational, but Peter should set length/format expectations. |
