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

From the Roughing It Hot Sauce demo artifact, the core frame:

> "A compound prompt makes the AI the creative director. Decomposed prompts make you the creative director with specialists reporting to you."
[SOURCE: artifact, roughing-it-compound-demo.md, setup]

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

### The Roughing It Hot Sauce Compound Output as the Example

The compound prompt. This is what a typical designer actually types:

> "I'm designing identity for Roughing It Hot Sauce, a small-batch brand from a farm in the Hudson Valley. Founder grows her own peppers. Four seasonal sauces (green spring, red summer, smoky fall, fermented winter). Positioning: agricultural, seasonal, serious about peppers. Not edgy, not gimmicky. Closer to craft vinegar than typical hot sauce. Budget is tight, works on shelves, markets, and web. Give me a color palette with hex codes, typography pairings, logo direction, imagery guidelines, and layout principles."
[SOURCE: artifact, roughing-it-compound-demo.md, Part 1]

The compound output covers all 5 sections in one pass: Color Palette (4 colors with brief rationale), Typography (1 pairing), Logo Direction (hand-drawn wordmark concept), Imagery (farm-focused photography), Layout (generous whitespace, editorial hierarchy). The full output is in the artifact.
[SOURCE: artifact, roughing-it-compound-demo.md, Part 1]

The output is competent. Each section names the correct general direction. No section goes deep. The color palette stays at four colors with brief rationale. The typography gives one pairing. The logo direction stays at concept level. The imagery guidelines cover the right territory without specifying capture methodology or seasonal variation. The layout principles name constraints without building a system.
[SOURCE: artifact, roughing-it-compound-demo.md, Part 4]

This is a B+ deliverable. Point out what is good about it: coherent, complete, professional. That is what makes it dangerous. It looks done. The compound prompt understood the positioning. It could not carry the positioning into depth on five dimensions simultaneously.
[SOURCE: scaffold, foundations-scaffold.md, Lesson 1.2; artifact, roughing-it-compound-demo.md, Part 4]

The compound prompt made the AI the creative director. One perspective made all the decisions. The output is coherent because one mind shaped it. That coherence is also its limitation: no tension, no surprise, no moment where one dimension pushes back against another.
[SOURCE: artifact, roughing-it-compound-demo.md, Part 4]

---

## Lesson 1.3 — The Decomposition and the Harnessed Workflow

**Format:** Written lesson. **Learning objective:** The student can identify the structural differences between compound, decomposed, and harnessed outputs, and explain why decomposition unlocks depth while AI compilation has a ceiling.

### The Five Decomposed Prompts

Each prompt addresses a single dimension. Each receives only the brand context and is explicitly told to ignore other dimensions. The full prompts and outputs are in the artifact (roughing-it-compound-demo.md, Part 2).
[SOURCE: artifact, roughing-it-compound-demo.md, Part 2]

The prompting pattern:
1. **One objective.** "Recommend a color palette with hex codes." Not "recommend a color palette and typography pairings."
2. **One output.** "For each color, explain what it does in the system and why it fits." Not "explain the color palette, typography, and logo direction."
3. **Explicit exclusion constraints.** "Do not address typography, logo, imagery, or layout." Every prompt explicitly tells the model what to ignore.
4. **Only the context it needs.** Each prompt gets the brand brief (who the client is, what the positioning is) but not the other outputs.
[SOURCE: artifact, roughing-it-compound-demo.md, Part 2, prompt structure]

### What the Decomposed Outputs Produced

Five independent specialist reports, each significantly deeper than its compound counterpart:
[SOURCE: artifact, roughing-it-compound-demo.md, Part 4]

**Color:** Specified a two-color print job economy tied to how small-batch food packaging is actually produced. Developed seasonal accent logic tied to harvest. Articulated what the palette deliberately avoids (heat signaling) as a positioning statement.

**Typography:** Provided three complete pairings with reasoning. Established the structural role of the monospaced secondary face (signaling that the brand tracks harvest dates). Defined usage rules down to emphasis conventions.

**Logo:** Went into the philosophy of the mark: what it should feel like, what to avoid, what to study as reference (sign painters' corner initials, printer's marks from the 1500s), and what constraints govern every scale. The compound output described a direction. The decomposed output described what the mark needs to feel like and why.

**Imagery:** Specified a 40/35/25 ratio (process/farm/product), capture methodology including DPI and lighting discipline, and articulated the structural argument for seasonal variation in the image library.

**Layout:** Built an actual system: label as primary surface, web as echo of label, market signage as scaled label, shipping box as one-color kraft. Each surface's rules were derivable from the label system.

The structural difference: each specialist went deeper because it was not splitting attention across five dimensions. The model's full capacity pointed at one problem per prompt.
[SOURCE: artifact, roughing-it-compound-demo.md, Part 4]

### The Harnessed Workflow: What Happens When the AI Synthesizes

Decomposition unlocked depth. Five specialist reports, each stronger than the compound version. The natural next question: can the AI also synthesize the five reports into a unified brief?

The harnessed workflow tries this. After the five specialist prompts, a compiler prompt asks the AI to synthesize all five outputs into a single creative direction brief.
[SOURCE: artifact, roughing-it-compound-demo.md, Part 2, AI Compiler section]

The AI compiler produced an organized, coherent synthesis. It accurately summarized each specialist's recommendations, identified governing principles at a high level (provenance over spectacle, restraint as differentiation, seasonal variation, density as signal).

What the AI compiler missed:
[SOURCE: artifact, roughing-it-compound-demo.md, Part 4]

**Specific conflict resolution.** The synthesis did not identify conflicts between specialists, so it did not resolve any. When color said "no heat signaling" and imagery's product shots inherently show peppers, the synthesis included both recommendations without naming the tension.

**Unstated convergences.** The synthesis named governing principles that were explicit in individual reports. It did not identify principles that emerged across reports without any single specialist naming them.

**Hierarchy of governance.** When specialists' recommendations conflict, the synthesis does not establish which recommendation governs. A human creative director sets the order of operations.

**Creative direction confidence.** The synthesis reads as summary, not decision. Each recommendation is presented as-is rather than selected and argued for.

The harnessed workflow (decomposition plus AI compilation) is better than compound prompting. It is not the same as creative direction. The AI compiler can organize. It cannot direct.

### The Three-Way Comparison

Three approaches, one brand brief:
[SOURCE: artifact, roughing-it-compound-demo.md, Part 4]

**Compound:** The AI is the creative director. One perspective, one pass, shallow across all dimensions. B+ deliverable that looks done but carries no depth.

**Harnessed (decomposed plus AI compiler):** The AI is both the specialist team and the creative director. Depth is present in the specialist reports. The AI synthesis is organized but passive. It summarizes without deciding.

**Human-CD (decomposed plus human synthesis):** The AI is the specialist team. The human is the creative director. The human steps through each specialist output, makes tracked decisions (accepting, overriding, deferring), names convergences nobody stated, and sets governing principles that hold across all domains. The brief reads as direction, not summary.

The course's thesis sharpened: decomposition unlocks depth. Decomposition plus AI compilation is better than compound prompting, but still has a ceiling. The breakthrough comes from pairing decomposition with human synthesis. That is where judgment enters. That is Lesson 1.4.

### Cognitive Science for This Lesson

**AlphaCodium (Ridnik et al. 2024):**
> "Code generation accuracy jumped from 19% (compound prompt) to 44% (decomposed multi-step flow) on the CodeContests benchmark. Same model, same problems, different input structure."
[SOURCE: cognitive-science-references.md, Week 1 Primary Citations]

Teaching application: direct evidence that decomposition improves output quality on complex tasks without changing the model. The improvement is from input structure, not model capability.
[SOURCE: cognitive-science-references.md, Ridnik "Maps to" note]

**Andrew Ng (2024):**
> "GPT-3.5 with a decomposed agentic workflow (95.1%) outperformed GPT-4 with a single compound prompt (67%) on the HumanEval coding benchmark."
[SOURCE: cognitive-science-references.md, Week 1 Primary Citations]

Teaching application: the architecture of the input matters more than the capability of the model. A weaker model with better structure outperforms a stronger model with compound structure.
[SOURCE: cognitive-science-references.md, Andrew Ng "Maps to" note]

Honest caveat: HumanEval is a coding benchmark. The comparison is dramatic but domain-specific. The principle (decomposition improves complex task performance) is supported across domains, but the specific numbers should not be generalized to all creative work without qualification.
[SOURCE: cognitive-science-references.md, Andrew Ng caveat]

**Chain-of-Thought (Wei et al. 2022):**
> "Adding 'Let's think step by step' or explicit reasoning steps to prompts substantially improved performance on arithmetic, commonsense, and symbolic reasoning tasks."
[SOURCE: cognitive-science-references.md, Week 1 Supporting Citations]

Teaching application: chain-of-thought is a lightweight form of decomposition. It forces the model to externalize intermediate steps rather than jumping to a final answer. Decomposition takes this further by separating each step into its own prompt.
[SOURCE: cognitive-science-references.md, Wei "Maps to" note]

### The Pivot to Lesson 1.4

Five independent outputs. They carry depth the compound version did not. An AI compiler can organize them into a coherent summary. But the summary reads as summary, not direction. Nobody resolved the conflicts. Nobody named the convergences. Nobody set the governing rules.

That is Lesson 1.4. You are the creative director. The synthesis process is itself decomposed: step through each specialist output one at a time, react, track your decisions, compile the brief from those tracked decisions. The brief writes itself from the tracker.
[SOURCE: scaffold, foundations-scaffold.md, Lesson 1.3; demonstrated in roughing-it-cd-brief.md]

---

## Lesson 1.4 — The Synthesis Step

**Format:** Written lesson + Exercise. **Learning objective:** The student can synthesize independent specialist outputs into a unified creative direction brief by stepping through each output, making tracked decisions, and compiling the brief from those decisions.

### The Synthesis Process

Synthesis is not "read all five outputs, then write a brief." That is compound processing applied to synthesis, the same failure mode the course teaches against. Holding five specialist reports in your head simultaneously and writing a coherent brief from memory degrades the same way a compound prompt degrades: attention splits, details flatten, the middle outputs get less consideration than the first and last.

The synthesis process is itself decomposed.

**Step through one specialist at a time.** Present each specialist's findings. React: what works, what does not, what questions does it raise, what does it conflict with from a previous specialist. Track the decision with your reasoning. Move to the next specialist. After all outputs are reviewed, compile the brief from your tracked decisions.

The brief writes itself from the tracker. You do not sit at a blank page and write. You compile from the calls you already made.
[SOURCE: demonstrated live in the Roughing It Hot Sauce synthesis session, 2026-04-05]

> "You are the creative director of a team of specialists. The AI gives you depth. You provide the coherence. The synthesis step (where you resolve conflicts between independent outputs) is where your judgment becomes the product."
[SOURCE: scaffold, foundations-scaffold.md, Week 1 core lesson]

### The Roughing It Hot Sauce Brief

The completed CD synthesis brief for the Roughing It Hot Sauce project is at `course/artifacts/roughing-it-cd-brief.md`. Read it now.

The brief was produced by stepping through each of the five specialist outputs (color, typography, logo, imagery, layout) one at a time, reacting to each, and tracking decisions. Here is what the creative director did at each step:

**Color specialist** recommended a two-color print job palette (Harvest Soil + Cream) with no heat-signaling reds. The CD overrode: green and red for chiles cannot be missing from a brand whose heart is the chiles. Green elevated to primary brand color (the plant, the farm). Red as accent (the fruit, the heat). Off-black added for text. The specialist's production-economy reasoning (two-color flexo) was accepted as the substrate logic.

**Typography specialist** recommended Pairing 1 (Canela + Söhne Mono). The CD chose Pairing 2 (Freight Text Pro + IBM Plex Sans) after visually evaluating all three pairings using a type-comparison playground with free-font approximations across four substrates. The pairing was confirmed visually before committing. Actual fonts to be licensed when production begins.

**Logo specialist** recommended no icon (wordmark only), reasoning that pepper imagery is a crutch in the hot sauce category. The CD overrode: the chile IS the brand because Tess literally grows them. It is evidence, not decoration. Two directions to explore on paper (silhouette as letterform, cross-section as round mark). The specialist's constraints (napkin-reproducible, bottle-cap to market-stall scale, one color) still hold.

**Imagery specialist** recommended a 40/35/25 ratio (process/farm/product). The CD accepted as a working draft but noted the ratios are provisional and may need rebalancing once real photography exists and the brand is tangible.

**Layout specialist** recommended dense, label-first system design. The CD accepted and added a specific aesthetic ancestor: Henderson's Sign Painter. Vintage signpainter craft and composition inform the visual language. The density is a feature, not a limitation.

### What the Creative Director Did

Three types of moves appeared in the tracked decisions:

**Overrides with reasoning.** The CD overrode the color specialist (added green and red), the typography specialist (chose a different pairing after visual evaluation), and the logo specialist (added a chile mark). Each override carried a specific reason grounded in the project's reality, not just preference.

**Provisional acceptance.** The CD accepted the imagery ratios as a draft, acknowledging they would need adjustment once real photography exists. This is a judgment call about when to commit versus when to defer.

**Governing principles.** Three principles emerged across the tracked decisions:
1. The chile lifecycle governs the palette (green growth → red fruit, on earth-toned ground).
2. Density is the signal (the brand has more to say than it has room for).
3. Evidence over decoration (the chile mark is evidence, the process photography is evidence, the monospace data is evidence).

These principles were not prescribed by any specialist. They emerged from the CD reading across all five outputs and naming what connected them. That naming is what the AI compiler in Part 2 of the demo could not do.
[SOURCE: demonstrated in roughing-it-cd-brief.md]

> "In the classroom, when two IEP goals conflicted (one student needed quiet, another needed verbal processing), the resolution was a structural decision: where to seat them, when to schedule which activity, how to create pockets of different conditions within one room. The conflict wasn't a problem. It was information about what the room needed to accommodate."
[SOURCE: published essay, petersalvato.com/_essays/the-iep-for-ai-systems.md]

> "Human in the loop means the human has actual leverage over the outcome. Not just the ability to reject output but the ability to shape it during production."
[SOURCE: blog draft, the-human-in-the-loop-is-not-a-checkbox.md]

### Practical Note: Visual Evaluation of Text-Based Outputs

The specialist outputs are text. Your evaluation is visual. Typography described in a paragraph reads differently than typography rendered on screen. Color described as "Harvest Soil (#3D2817)" reads differently than the swatch.

This gap is real and the course does not pretend it away. When a specialist output recommends a typeface, a color, a layout structure, the creative director's next step is to render it visually before making decisions. Use approximation tools to bridge the gap:

- For typography: render the recommended pairings using free approximation fonts (Google Fonts closest-match). Evaluate pairing dynamics (contrast, rhythm, weight relationship). License the actual fonts when the direction is locked. Most studios work this way at the comp stage.
- For color: build swatches from the hex codes. View them on the target substrate (screen, paper, kraft). Colors shift across media.
- For layout: rough the structure in your design tool. A wireframe built in 15 minutes answers questions a paragraph of description cannot.

The specialist outputs give you direction and reasoning. The visual rendering gives you confirmation. Both are required before synthesis. Do not synthesize from text alone if the decision is visual.

### Guided Synthesis Exercise

You have your own decomposed outputs from Lessons 1.2 and 1.3 (or from Lesson 1.5 if you are working ahead). Now synthesize them using the step-through process.

**Step 1: Prepare your tracker.** Open a blank document. Create a table or list with one row per specialist output. Columns: Specialist | Their Recommendation | My Decision | My Reasoning.

**Step 2: Step through each output one at a time.** Do not read them all first. Present one to yourself, react, and record your decision before moving to the next. For each output, ask:
- What works here?
- What does not work, and why?
- Does this conflict with a decision I already made on a previous output?
- Am I accepting this, overriding it, or deferring the decision?

Record your answer in the tracker before moving on.

**Step 3: After all outputs are reviewed, read your tracker top to bottom.** Look for:
- Patterns across your decisions (did you override the same kind of recommendation more than once? That pattern is a governing principle).
- Connections between outputs that no single specialist named (convergences you spotted by reading across domains).
- Decisions that felt provisional versus decisions that felt locked.

**Step 4: Compile the brief from your tracker.** Write a 1-page creative direction brief (400-600 words) organized by your decisions, not by the specialists' categories. The brief should contain:
- Your key decisions with reasoning
- Any overrides and why
- Governing principles that emerged across the tracked decisions

The brief should read as if a creative director is telling the team what they are making and why. Confident, specific, decisive.

**Step 5: Compare.** Read your compiled brief against the AI compiler's synthesis from the demo (Part 2 of the artifact). Where did you make calls the AI did not? Where did you name connections the AI missed? Where did you override a specialist the AI silently accepted?

That comparison is the lesson.

### What This Exercise Does Not Cover

You just synthesized one direction. In practice, a creative director often runs the same decomposition with different positioning emphasis and produces 2-3 distinct directions, then evaluates across them: which direction serves the brand better, and why?

That evaluation requires its own methodology. Comparing directions means decomposing "is this good?" into independent criteria and running each direction against them separately. That is what Course 04 (Lens Extraction) teaches. This course gives you the synthesis skill for one direction. Lens Extraction gives you the evaluation skill for choosing between multiple.

If you want to try it now: run your decomposition again with a different emphasis (different positioning angle, different audience assumption, different aesthetic ancestor). Produce a second brief. Compare the two. Notice what you need in order to decide between them. That need is the appetite Lens Extraction satisfies.

---

## Lesson 1.5 — Guided Exercise: Decompose Your Own Work

**Format:** Exercise. **Learning objective:** The student can decompose one of their own compound prompts into independent specialist prompts and document the difference in output quality.

### The Decomposition Structure (modeled on the Roughing It Hot Sauce demo)

The prompting pattern from the artifact. Each decomposed prompt follows this structure:

1. **One objective.** "Recommend a color palette with hex codes." Not "recommend a color palette and typography pairings."
2. **One output.** "For each color, explain what it does in the system and why it fits." Not "explain the color palette, typography, and logo direction."
3. **Explicit exclusion constraints.** "Do not address typography, logo, imagery, or layout." Every prompt explicitly tells the model what to ignore.
4. **Only the context it needs.** Each prompt gets the brief (who the client is, what the studio does) but not the other outputs.

[SOURCE: artifact, roughing-it-compound-demo.md, Part 2, prompt structure]

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

You have watched decomposition work on Roughing It Hot Sauce. A compound prompt that asked for five dimensions at once. Five specialist prompts that each went deeper. A harnessed AI synthesis that organized but did not direct. A human creative director who stepped through each output, made tracked decisions, and compiled a brief the AI could not have written.

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
[SOURCE: artifact, roughing-it-compound-demo.md, Part 2, prompt structure]

**The depth difference is visible.** The decomposed outputs go deeper than the compound output on their respective dimensions. If they don't, the student either didn't decompose far enough or the original prompt was already single-objective.
[SOURCE: artifact, roughing-it-compound-demo.md, Part 4: comparison]

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
- `/home/peter/homelab/projects/active/joinery-site/course/artifacts/roughing-it-compound-demo.md` -- All of Part 1 (compound), Part 2 (harnessed: 5 decomposed + AI compiler), Part 3 (human-CD synthesis), Part 4 (three-way comparison)
- `/home/peter/homelab/projects/active/joinery-site/course/artifacts/roughing-it-cd-brief.md` -- The compiled CD synthesis brief from tracked decisions
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
| Roughing It CD synthesis brief | 1.4 | Compiled from tracked decisions during step-through review. Demonstrates creative director judgment: overrides, convergences, governing principles. See roughing-it-cd-brief.md. |
| Podcast brand exercise (3 outputs with planted conflicts) | 1.4 | Original exercise content. No source exists. |
| Template introduction/framing for 1.5 | 1.5 | Peter's voice framing the exercise. |
| Reflection prompt (final version) | 1.6 | Scaffold provides a draft question. Peter decides if it points at the right insight. |
| Submission format template | 1.6 | Operational, but Peter should set length/format expectations. |
