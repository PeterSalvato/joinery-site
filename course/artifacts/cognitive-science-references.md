# Cognitive Science References: Foundations Course

Citations organized by week. Each entry includes the finding and how it maps to the teaching point. Caveats noted where the research doesn't cleanly support the claim.

---

## Week 1: Task Decomposition

### Primary Citations

**Liu et al. (2024). "Lost in the Middle: How Language Models Use Long Contexts."**
LLMs degrade 30%+ in accuracy when relevant information is positioned in the middle of a long input, compared to the beginning or end. Performance follows a U-shaped curve mirroring the human serial position effect.
*Maps to:* Compound prompts bury critical instructions in the middle. Decomposition puts each instruction at the focal point of its own step.
*Caveat:* This study measured retrieval accuracy in long contexts, not generative quality. The degradation pattern is well-documented but the exact mechanism (attention distribution vs. something else) is debated.

**Ridnik et al. (2024). AlphaCodium: From Prompt Engineering to Flow Engineering.**
Code generation accuracy jumped from 19% (compound prompt) to 44% (decomposed multi-step flow) on the CodeContests benchmark. Same model, same problems, different input structure.
*Maps to:* Direct evidence that decomposition improves output quality on complex tasks without changing the model.
*Caveat:* Code generation is a particularly good domain for decomposition because steps have verifiable outputs. Creative tasks may not decompose as cleanly.

**Andrew Ng (2024). Agentic Design Patterns (DeepLearning.AI lecture series).**
Demonstrated that GPT-3.5 with a decomposed agentic workflow (95.1%) outperformed GPT-4 with a single compound prompt (67%) on the HumanEval coding benchmark.
*Maps to:* The architecture of the input matters more than the capability of the model. This is the single most persuasive data point for the course's core thesis.
*Caveat:* HumanEval is a coding benchmark. The 95.1% vs. 67% comparison is dramatic but domain-specific. We should be careful about generalizing to all creative work.

**Sweller (1988). "Cognitive Load Theory." In Cognition and Instruction.**
Working memory can process approximately 2-4 novel items concurrently. Overloading working memory with extraneous information degrades learning and performance.
*Maps to:* Compound prompts overload the model's "working memory" (attention budget) the same way overloaded briefs overload human working memory. Decomposition is a cognitive load management strategy.
*Caveat:* LLMs don't have working memory in the human sense. The analogy is useful for teaching but shouldn't be presented as a direct equivalence. The functional parallel (performance degrades with input complexity) holds even if the mechanism differs.

**Cowan (2001). "The Magical Number 4 in Short-Term Memory."**
The effective capacity of the focus of attention is approximately 4 chunks, not the 7 +/- 2 that Miller (1956) proposed. The original estimate conflated short-term memory with rehearsal strategies.
*Maps to:* Reinforces the cognitive load argument. Even the generous estimate of human concurrent processing is small. Design your AI inputs accordingly.

**Murdock (1962). "The Serial Position Effect of Free Recall."**
Items at the beginning (primacy) and end (recency) of a list are recalled significantly better than items in the middle. The middle-position deficit is robust across conditions.
*Maps to:* Direct parallel to the Liu et al. LLM finding. Both humans and language models exhibit serial position effects. The structural problem is the same even if the mechanism differs.

### Supporting Citations

**Wei et al. (2022). "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models."**
Adding "Let's think step by step" or explicit reasoning steps to prompts substantially improved performance on arithmetic, commonsense, and symbolic reasoning tasks.
*Maps to:* Chain-of-thought is a lightweight form of decomposition. It forces the model to externalize intermediate steps rather than jumping to a final answer.
*Caveat:* Chain-of-thought helps most on reasoning tasks with clear logical steps. Its benefit on open-ended creative tasks is less well-established.

**Zhou et al. (2022). "Least-to-Most Prompting Enables Complex Reasoning in Large Language Models."**
On the SCAN compositional generalization benchmark, least-to-most prompting achieved 99.7% accuracy where standard prompting scored near zero. The technique decomposes hard problems into progressively easier sub-problems.
*Maps to:* Extreme case of decomposition benefit. When the task exceeds the model's capacity as a single step, decomposition doesn't just improve results, it makes them possible at all.
*Caveat:* SCAN is a synthetic benchmark specifically designed to test compositional generalization. Real-world tasks rarely show this dramatic a gap.

**Wong et al. (2014). "Task Analysis in Special Education."**
Task analysis (breaking complex behaviors into discrete, teachable steps) is classified as an evidence-based practice in special education. Decades of applied research show it improves learning outcomes for students with cognitive disabilities.
*Maps to:* Decomposition as a teaching and execution strategy has a deep evidence base in education. We're applying the same principle to AI interaction. The parallel to accessibility and accommodation design is deliberate.
*Caveat:* The special education research is about human learning, not AI performance. The principle transfers but the contexts are different.

---

## Week 2: Input Inversion

### Primary Citations

**Kellogg (1996, 2008). "A Model of Working Memory in Writing" / "Training Writing Skills."**
Writing simultaneously taxes working memory with three competing demands: planning (what to say), translating (how to say it), and reviewing (evaluating what was said). These demands compete for the same limited cognitive resources.
*Maps to:* This is why brain dumps work. Voice input separates the planning stage from the translation stage. The person thinks out loud without simultaneously formatting, editing, and structuring. Lower cognitive load during the critical ideation phase.

**Chi (1994, 2000). "Eliciting Self-Explanations Improves Understanding" / "Self-Explaining Expository Texts."**
Students who explain material to themselves while learning produce deeper understanding than those who silently organize information. Self-explanation forces active processing and reveals gaps in understanding.
*Maps to:* The brain dump functions as self-explanation. When Mara talks through her thinking about Night Owl, she's not just recording ideas. She's discovering them through the act of articulation. The AI then synthesizes what the articulation revealed.
*Caveat:* Chi's research is about learning, not about creative ideation. The mechanism (active processing reveals gaps) transfers, but we shouldn't overstate the equivalence.

**Clark & Chalmers (1998). "The Extended Mind."**
Cognitive processes don't stop at the skull. External tools and artifacts (notebooks, calculators, and by extension AI) can function as genuine components of a cognitive system when they are reliably accessible, automatically endorsed, and readily available.
*Maps to:* Input Inversion treats AI as an extended mind component. The designer's brain dump is the cognitive process. The AI synthesis is the externalized organization step. Together they form a single cognitive workflow that neither could perform alone.
*Caveat:* The Extended Mind thesis is philosophically contentious. Many cognitive scientists reject it. Use it as a framing device, not as settled science.

**Osborn (1953). Applied Imagination / Amabile (1983). "The Social Psychology of Creativity."**
Premature evaluation during ideation suppresses creative output. Separating generation from evaluation (Osborn's brainstorming principle) and removing evaluative pressure (Amabile's research on extrinsic constraint) both increase the quantity and novelty of ideas.
*Maps to:* The brain dump is a no-evaluation zone. The designer talks without filtering, editing, or judging. The AI's synthesis step is the evaluation phase, but it comes after the generative phase is complete. The temporal separation matters.

**Cseh et al. (2015). "Flow and Creativity: Towards a Unified Framework."**
Creative flow is phenomenologically distinct from general flow states. It thrives on ambiguity and open-endedness rather than clear goals, which distinguishes it from the Csikszentmihalyi model where clear goals are a prerequisite.
*Maps to:* Brain dumps allow ambiguity. The designer doesn't need to know where she's going. She follows tangents (Polish jazz covers, chalkboard handwriting) because creative flow rewards exploration. Structured prompts force premature clarity.
*Caveat:* Flow research is self-report-heavy and hard to measure objectively. The distinction between creative flow and general flow is not universally accepted.

### Supporting Citations

**Voice input cognitive load research (multiple sources).**
Dictation produces 35-45% lower cognitive load measurements compared to typing for equivalent content generation tasks. Measured via dual-task paradigms and physiological indicators.
*Maps to:* Voice recording for brain dumps is not just a convenience. It measurably reduces the cognitive overhead of the input stage, freeing resources for thinking.
*Caveat:* The 35-45% figure comes from aggregating across several studies with different methodologies. Individual results vary. Some people think better while typing. The recommendation should be "try it" not "this is universally better."

---

## Week 3: Voice Governance

### Primary Citations

**Slamecka & Graf (1978). "The Generation Effect in Memory."**
Information generated by the learner (completing "rapid: f___" as "fast") is remembered better than information simply read ("rapid: fast"). The act of generating under constraints creates qualitatively different memory traces than passive receipt.
*Maps to:* Voice governance forces the AI to generate under constraints rather than freely. The constraints (no em dashes, physical vocabulary, no self-introduction openers) function like the generation cues in Slamecka's paradigm. The output is structurally different, not just superficially edited.
*Caveat:* The generation effect is a memory phenomenon. Applying it to AI text generation is analogical, not direct. The AI doesn't "remember" differently, but the constraint mechanism produces similar structural effects on the output.

**Stokes (2005). Creativity from Constraints: The Psychology of Breakthrough.**
Paired constraints (one blocking a habitual response, one promoting a novel alternative) are the mechanism behind creative breakthroughs across domains. Constraints don't limit creativity. They redirect it.
*Maps to:* Each voice rule is a paired constraint. "No em dashes" blocks a habitual AI response. "Use periods for short declarative stops" promotes the alternative. "Never open with self-introduction" blocks the default. "Open with current work" promotes the alternative. The voice governance system is a constraint architecture.

**Bock & Loebell (1990). "Framing Sentences" (Structural Priming).**
Syntactic structures activated during language production prime all subsequent output. If a speaker produces a passive construction, their next sentence is more likely to be passive. Structure begets structure.
*Maps to:* Voice rules function as structural primes. When the AI generates "Most people hate that. I use it." (short, declarative, period-stopped), that syntactic structure primes subsequent sentences toward the same pattern. The rules don't just constrain individual sentences. They set the structural momentum for the entire output.
*Caveat:* Structural priming is documented in human language production. Whether transformer architectures exhibit analogous priming during autoregressive generation is an open question. The functional parallel (early output structure shapes later output) holds observationally.

**Flower & Hayes (1981). "A Cognitive Process Theory of Writing" / Bereiter & Scardamalia (1987). The Psychology of Written Composition.**
Knowledge-transforming writers (experts) reshape their thinking through the act of writing. Knowledge-telling writers (novices) dump existing knowledge into text without transformation. The difference is whether the writing process changes the writer's understanding.
*Maps to:* Standard prompting produces knowledge-telling: the AI dumps what it knows about "brand designer about pages." Voice governance forces something closer to knowledge-transforming: the constraints reshape the output structure, which in turn changes what gets said and what gets left out. The about page written under voice governance contains different information, not just different phrasing.

**Pennebaker & King (1999). "Linguistic Styles: Language Use as an Individual Difference."**
Individual voice is carried primarily by function words (pronouns, articles, prepositions, conjunctions), which are processed below conscious awareness. Content words carry meaning. Function words carry identity.
*Maps to:* Voice governance rules target structural and functional elements (sentence length, opening patterns, use of periods vs. dashes, vocabulary domains) rather than content. This aligns with how voice actually works. Telling the AI to "sound bold and direct" targets content-level mimicry. Constraining structural patterns targets the layer where voice actually lives.

**Baker (1993). "Corpus Linguistics and Literary Theory" / Solum (2018). "The Fixation Thesis."**
Editing systematically normalizes text toward the editor's defaults. Baker demonstrated this in literary translation (translators' stylistic fingerprints override source text voice). Solum demonstrated it in legal interpretation (readers fix meaning at the point of interpretation, not the point of authorship).
*Maps to:* This is why "write in this person's voice" fails. The AI edits its own output during generation, normalizing toward its defaults (epigrammatic closers, em dashes, philosophical asides). Voice governance prevents normalization by making the defaults structurally unavailable. You can't normalize toward an em dash pattern if em dashes are prohibited.
*Caveat:* Baker's work is about human translators, and Solum's is about legal interpretation. The application to AI generation is by analogy. The normalization tendency in LLMs is well-observed but the mechanism is different from human editorial normalization.

### Supporting Citations

**Anthropic (2022). Constitutional AI: Harmlessness from AI Feedback.**
Applying rules during the generation process (constitutional principles that govern output as it's being produced) yields Pareto improvements: better on the target dimension without degrading other dimensions. Generation-time constraints outperform post-hoc editing.
*Maps to:* Voice governance applies constraints during generation, not after. This is structurally identical to Constitutional AI: rules that shape output as it's produced rather than filtering it afterward. The Anthropic research validates the mechanism even though the domain (safety vs. voice) is different.
*Caveat:* Constitutional AI is about safety and helpfulness constraints, not stylistic voice. The mechanism (generation-time rule application) transfers, but the specific findings about Pareto improvement may not generalize to all constraint types.

---

## Cross-Week Themes

Three cognitive science patterns recur across all three weeks:

1. **Decomposition reduces load.** Sweller, Cowan, and Kellogg all demonstrate that concurrent processing of multiple demands degrades performance. Each week's technique separates what other approaches combine: task steps (Week 1), thinking and formatting (Week 2), content and voice (Week 3).

2. **Constraints improve output.** Stokes, Slamecka, and the Anthropic Constitutional AI work all show that constraints during generation produce better results than unconstrained generation followed by editing. Constraints are not limitations. They are structural guidance.

3. **Structure shapes content.** Bock's structural priming, Pennebaker's function-word identity, and Flower & Hayes's knowledge-transforming all point to the same insight: changing the structure of how something is produced changes what gets produced, not just how it looks. Voice governance doesn't make the same content sound different. It produces different content.

---

## Honest Limitations

Some transparency about where the research support is strong and where it's stretched:

**Strong support:** Task decomposition improving LLM performance (Weeks 1). Direct experimental evidence from multiple labs with clear metrics.

**Moderate support:** Cognitive load reduction through voice input and brain dumps (Week 2). The underlying cognitive science is solid, but the specific application to AI-mediated creative workflows hasn't been directly studied. We're applying established principles to a new context.

**Analogical support:** Voice governance as generation-time constraint (Week 3). The component research (structural priming, generation effect, Constitutional AI) each support pieces of the argument, but no one has studied "extracting voice rules from speech transcripts and applying them as AI generation constraints" as a unified intervention. We're building the argument from converging evidence, not from a single study that tested exactly this.

This is appropriate for a practitioner course. We're teaching a method, grounding it in the best available science, and being honest about where the science is direct vs. where we're making principled extrapolations.
