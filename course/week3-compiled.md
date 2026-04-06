# Week 3: Voice Governance — Compiled Course Content

**Compiled:** 2026-04-04
**Status:** Source-attributed compilation. Every quote, example, and teaching point traced to origin.
**Sources read:**
- `course/artifacts/week3-voice-governance-demo.md` (Mara Voss demo)
- `petersalvato.com/_research/voice-governance.md` (whitepaper)
- `petersalvato.com/_essays/voice-governance.md` (published essay)
- `joinery/voice/voice-protocol.md` (40-rule protocol)
- `joinery/voice/voice-fingerprint.md` (generative voice constraints)
- `joinery/voice/profiles/` (all 5 output profiles)
- `joinery/skills/copy-verify/SKILL.md` (13-item checklist)
- `course/artifacts/cognitive-science-references.md` (Week 3 section)
- `petersalvato-dev/_drafts/` (voice-drift, build-a-voice-governance-checklist, compilation-not-generation, constraint-as-creative-fuel, fidelity-in-ai-output, the-anti-slop-thesis, the-overcorrection-when-governance-catches-false-positives, maintaining-fidelity-across-200-posts, everyones-talking-about-what-ai-can-do, what-registration-actually-means)
- `memory/voice-sample.md` (159-session voice extraction)
- Session logs (morning execution page prompt with register rules)

---

## Attunement Frame: Reading the AI's Generation Defaults

Weeks 1 and 2 taught you to attune to how the AI processes tasks and receives input. This week, you attune to how it generates output.

Left unconstrained, the AI generates in its training distribution's default voice. Published writing, marketing copy, blog posts, documentation: all the polished, performed text it learned from. That default is why all AI copy sounds the same. The person disappears because the model's generation defaults occupy the space where the person's voice should be.
[SOURCE: essay, voice-governance.md, paragraphs 1-3]

Voice governance is attunement to generation defaults. You read what the AI's output system does when unconstrained (converges toward generic published register), and you design constraints that occupy that space before the defaults can. Constraints applied during generation produce structurally different work than constraints applied after. That structural difference is the subject of this week.

---

## Lesson 3.1 — Why AI Copy Sounds the Same (Video Close Script Outline)

**Lesson type:** Demo (instructor presents)
**Deliverable:** Video close script outline. Peter explains the problem, shows the three-output demo, names the generation vs. post-hoc distinction.

---

### The Problem Statement (Peter's Own Words)

**Source: Whitepaper, Section 1 (voice-governance.md, lines 40-47)**

> "LLMs generate text from training data dominated by published writing: polished, performative, audience-aware. The statistical center of that data produces a specific voice: hedged, parallel, abstract-leading, em-dash-heavy, fortune-cookie-closing prose. Ask the model to write in a specific person's voice and it produces competent content marketing that sounds like everyone and no one."

> "I tried the standard fixes. Longer style descriptions. More examples of the target voice. 'Write like a practitioner, not a marketer.' 'Be direct and specific.' 'Sound like a real person.' The model followed the instruction for a sentence, sometimes two, and then the defaults came back. Abstract openings. Mechanical parallelism. Three consecutive sections with identical skeleton structures. The pull of the training distribution was stronger than any style prompt I could write."

**Source: Published essay (_essays/voice-governance.md, lines 17-28)**

> "Read ten AI-assisted 'About' pages and you'll notice they sound identical. The same cadence, the same transitions, the same way of building to a point. Different words, same voice. The person disappears and what's left is the tool's default register."

> "You can fix this partially with style guides, voice examples, tone specifications. The output gets better than the default, but it still won't sound like the person. It sounds like an AI doing an impression of a style guide."

**Source: Published essay (_essays/voice-governance.md, lines 22-28)**

> "The way someone writes a LinkedIn post is not how they think. The way someone writes a case study is not how they explain the same project to a friend over dinner. The rough edges, the false starts, the way someone actually arrives at an idea: gone before publication."

> "So when you ask an AI to write 'in your voice' and give it your published work as examples, you're handing it the performance. The AI learns to imitate that, and since most people's published performances converge toward the same conventions (clean transitions, parallel structure, building to a thesis), the output converges too. Different people, same register."

### The Generation vs. Post-Hoc Distinction

**Source: Whitepaper, Section 3.1 (voice-governance.md, lines 78-84)**

> "By the time the model has generated a paragraph, the voice is embedded in the structure, not just the word choice. A paragraph that opens with 'This project explores the intersection of...' has that shape baked in. The abstract concept leads. The specific situation follows (if it appears at all). The closing resolves neatly."

> "Post-hoc editing can change the words. It cannot easily change the shape. Rewriting 'This project explores the intersection of' to 'I walked into a company and found a Windows Forms application' requires restructuring the entire paragraph, because the second opening demands a different sequence: situation first, then implication."

**Source: Whitepaper, Section 4.3 (voice-governance.md, lines 140-147)**

> "When constraints are applied during generation, the model builds the paragraph around the constraints. The structure supports the voice from the first sentence."

> "When constraints are applied after generation, the model builds the paragraph around its defaults and then tries to edit it. The bones are wrong. The structure was built to support abstraction-first, parallel, neatly-resolved prose. Changing the words does not change the bones."

### The Accommodation Frame

**Source: Whitepaper, Section 3.3 (voice-governance.md, lines 93-98)**

> "Generate-then-filter is the equivalent of giving a student a compound task, letting them attempt it without scaffolding, and then correcting their work after they fail."

> "A teacher working with a student who has processing limitations does not say: 'Write an essay. I will tell you what is wrong after you are done.' The teacher scaffolds the production: provide the structure, constrain the approach, define success criteria before the work begins. The accommodation happens at the point of production, not at the point of review."

### The Site Failure Story (Peter's Origin)

**Source: Whitepaper, opening (voice-governance.md, lines 20-21)**

> "The first complete draft of this site was produced through conventional AI-assisted writing. Twenty-one project pages. Every one of them opened with an abstract concept before any real situation was established. 'This project explores the intersection of...' on a page that should have said what broke and what I built to fix it. The pages were competent. Not one of them sounded like a person had written it."

**Source: Blog draft, fidelity-in-ai-output.md (lines 18-26)**

> "AI tools produce competent output. The grammar is correct. The structure is logical. The tone is professional. If you asked for a bio, you get a bio. If you asked for a project description, you get a project description. The output passes every quality check you can think of."
>
> "And it doesn't sound like you."
>
> "This is the fidelity problem. Quality asks whether the output is good. Fidelity asks whether the output is yours. Those are different questions and AI tools are very good at the first one and very bad at the second."

**Source: Blog draft, fidelity-in-ai-output.md (lines 23-27)**

> "I found this out the hard way. I was building my site using Claude as a compiler for three years of my own raw thinking. Conversations, notes, rough drafts. The AI processed my material. The output read well. It read clearly. Every page made its point. And then I read the whole site top to bottom as a stranger and found a fabricated claim. A sentence about work I never did, written in my voice, that sounded specific and grounded. It had survived every quality check I had. Five independent evaluation tools had looked at the page. All five passed it. The sentence was still wrong."

### Script Outline Structure

1. Open with the problem: read ten AI about pages, they sound identical
2. Show the Mara Voss standard output (artifact Part 1) as evidence
3. Name what happened: the AI learned from published writing, published writing is performance
4. The generation vs. post-hoc distinction: by the time the paragraph exists, the structure is set
5. Peter's site story: twenty-one pages of competent copy, none of it sounding like a person
6. The accommodation frame: constrain during production, not filter after
7. Close: this week teaches you how to constrain the generation so the output sounds like you

[NEEDS PETER: Record this as a video close. The script outline is compiled from his own words, but the actual delivery and transitions need to be his. Specific emphasis points, pauses, which sentences he leads with vs. saves for the turn.]

---

## Lesson 3.2 — Three Levels of Voice Control (Demo)

**Lesson type:** Demo (instructor presents)
**Deliverable:** The Mara Voss three-output comparison. Students see the same brief at three levels of control.

---

### The Task

**Source: week3-voice-governance-demo.md (line 5)**

Write an About page for Mara Voss, freelance brand designer and hand-letterer in Brooklyn.

### Level 1: Standard Prompt (No Control)

**Source: week3-voice-governance-demo.md (lines 16-26)**

> "I'm Mara Voss, a brand designer and hand-letterer based in Brooklyn, New York.
>
> For over a decade, I've helped brands find their visual voice through custom lettering, identity systems, and strategic design. My work sits at the intersection of craft and strategy -- I believe that how something looks should reflect what it means.
>
> I've worked with clients ranging from independent coffee roasters to national retail brands, bringing the same attention to detail whether I'm sketching letterforms or building a full identity system.
>
> When I'm not at the drawing table, you'll find me hunting for vintage type specimens at flea markets, experimenting with new ink formulations, or teaching lettering workshops around the city.
>
> If you're looking for a designer who treats every project as a unique challenge, I'd love to hear from you."

**Peter's analysis (source: demo artifact, lines 27-28):**

> "This is the AI About page. Every freelance designer on the internet has a version of this. 'Find their visual voice.' 'Intersection of craft and strategy.' 'How something looks should reflect what it means.' 'I'd love to hear from you.' It is accurate, grammatically correct, and completely empty. You cannot distinguish this person from 10,000 other designers after reading it."

### Level 2: Harnessed Prompt (Tone + Constraints)

**Source: week3-voice-governance-demo.md (lines 35-43, prompt)**

Prompt included: Bold, direct, no-nonsense tone. Jessica Walsh meets punk zine editor reference. Constraints: no jargon, no "visual voice" or "intersection of," no calls to action, under 200 words.

**Source: week3-voice-governance-demo.md (lines 45-57, output)**

The full harnessed output is in the artifact. Key passage:

> "I letter things by hand. Have for over ten years. Brands come to me when they want something that doesn't look like it came out of a template."

**Peter's analysis (source: demo artifact, lines 59-68):**

> "Better. The short sentences work. The client list is specific. The opening is direct instead of self-introducing. The constraints eliminated most of the generic language."
>
> "But two things give it away:"
>
> "1. 'I believe in the tool.' This is philosophical in a way most working designers wouldn't be. It's the AI performing depth. A real designer with this personality would say something about the specific tool, not about believing in tools as a category."
>
> "2. 'If your brand needs a voice that looks like it means what it says, that's what I do.' Epigrammatic closer. The AI defaults to this: a neat, quotable, slightly clever final sentence that wraps everything up. Real people don't end conversations with epigrams."
>
> "The tone guidelines improved the surface. The output still has AI architecture underneath."

### Level 3: Voice Governance (Extracted Rules + Source Material)

**Source: week3-voice-governance-demo.md (lines 76-89, the 12 rules)**

Rules extracted from Mara's brain dump recording (Week 2 exercise):

1. Never open with self-introduction. She starts with what she's making or what she just finished.
2. No em dashes. She uses periods where other writers use dashes. Short declarative stops.
3. Physical vocabulary: pressure, ink, weight, surface, pull, drag, bleed. She describes work in terms of what her hands do.
4. Dismissals are direct, not hedged. "That doesn't work" not "I tend to find that doesn't work as well."
5. Never explains why hand-lettering matters. She treats it as self-evident.
6. References clients by what they make, not by category. "A hot sauce company in Austin" not "a food and beverage client."
7. No sign-off, call to action, or closing invitation. She stops when she's done talking.
8. Lists are concrete and uneven. Three items, not five. Specific, not parallel.
9. She names tools by brand or type (Nikko G nib, sumi ink, Rhodia pad), not by generic category.
10. Humor is dry and factual. "Eleven rounds of revisions" is funny because it's true, not because she's performing wit.
11. She talks about other people's work she respects. Unprompted. Mid-thought.
12. Rhythm pattern: two short sentences, then one medium sentence. Rarely a long sentence. Never two long sentences in a row.

**Source quotes that generated the rules (demo artifact, lines 92-99):**

> "The Nikko G does this thing where if you push too hard on the upstroke it catches. Most people hate that. I use it."

> "I just finished a set of labels for a hot sauce company in Austin. Three SKUs. The owner hand-grows the peppers and wanted the lettering to look like it came off a seed packet from the 1940s."

> "That doesn't work. If you have to explain to someone why hand-lettering is different from a font, they should hire someone else."

> "Have you seen the stuff Marian Bantjes did for Saks? That was twenty years ago and it's still the thing I measure against."

**The voice-governed output (demo artifact, lines 116-125):**

> "Right now I'm finishing a set of packaging labels for a hot sauce company in Austin. Three SKUs. The owner grows his own peppers and wanted the lettering to feel like a seed packet from the 1940s. I spent two weeks on the lowercase g alone.
>
> I do hand-lettering and brand identity. Have for twelve years. I ink with a Nikko G nib on Rhodia pads, scan at 1200 DPI, and clean up in Illustrator. The nib catches on upstrokes if you push too hard. Most people hate that. I use it.
>
> Recent work: identity system for a climbing gym in Denver, packaging for a small-batch whiskey out of Kentucky, and a full rebrand for a brewery in Portland that took five months because the founder kept changing the brief. It turned out right.
>
> I work out of a studio in Greenpoint. Three desks, too many ink samples, a record player that only gets used on Fridays. I've been listening to a lot of Polish jazz lately. Komeda, Stanko. My friend gave me a stack of vinyl and I'm working through them.
>
> Marian Bantjes did that Saks work twenty years ago and I still think about it weekly. That's the bar. Lettering that makes you stop and look at a department store bag. If your type isn't doing that, it's just a font with extra steps."

### The Comparison Table

**Source: demo artifact, lines 147-153**

| Dimension | Standard | Harnessed | Voice Governance |
|-----------|----------|-----------|-----------------|
| Sounds like | AI writing about a person | Better AI writing about a person | A person |
| Source of voice | AI's default register | Tone keywords + style references | Extracted rules from actual speech |
| What shapes the output | Nothing specific | Adjectives (bold, direct, warm) | Structural constraints (rhythm, vocabulary, openings, closings) |
| AI tells present? | Yes, everywhere | Yes, two major ones | None detected |
| Could pass the "did a person write this" test? | No | Maybe, for 30 seconds | Yes |

### The Polish Jazz Detail

**Source: demo artifact, lines 141-142**

> "The Polish jazz reference came from her own recorded speech in Week 2. It wasn't in the prompt as a biographical fact. It was in her voice as something she actually said. The AI preserved it because it was in the source material, and the voice rules didn't filter it out. That's the difference: it belongs there because she put it there."

### Week Scaffolding Connection

**Source: demo artifact, lines 164-166**

> "Week 2's brain dump produced the raw transcript. Week 3 mines that transcript for voice rules. The same source material serves two purposes: content excavation (what the designer thinks) and voice extraction (how the designer talks). The weeks scaffold. Week 2 without Week 3 gives you good ideas in the wrong voice. Week 3 without Week 2 gives you the right voice with nothing to say."

---

## Lesson 3.3 — Voice Is Structural, Not Stylistic

**Lesson type:** Guided (instructor explains concept, student follows along)
**Deliverable:** Student understands why voice governance works and what voice actually consists of.

---

### The Core Argument: Voice Lives in Structure, Not Word Choice

**Source: Whitepaper, Section 8 (voice-governance.md, lines 203-208)**

> "Voice is not style. Style is surface: word choice, sentence length, formality level. Voice is structural: what does this person lead with, what do they never tolerate, what's the relationship between the specific and the abstract, how do they use evidence. Style can be adjusted after the fact. Voice lives in the paragraph structure, and that structure is set during generation."

**Source: Whitepaper, Section 3.1 (voice-governance.md, lines 80-84)**

> "Post-hoc editing can change the words. It cannot easily change the shape. Rewriting 'This project explores the intersection of' to 'I walked into a company and found a Windows Forms application' requires restructuring the entire paragraph, because the second opening demands a different sequence: situation first, then implication. The paragraph was generated around the abstract opening. The structure supports the abstraction. Swapping the opening without rebuilding the structure produces incoherence."

### What Voice Actually Consists Of (The Components)

**Source: Voice fingerprint (voice-fingerprint.md) — operational categories Peter uses**

Peter's voice protocol identifies these structural dimensions of voice:

1. **Sentence Architecture** — How sentences are built and connected. Two modes alternating: long exploratory runs when building a thought, short conclusive punches when the thought lands. (voice-fingerprint.md, Section 1)

2. **Opening Moves** — How paragraphs and sections begin. "Lead with the thing itself, not setup." Never opens with a thesis statement. (voice-fingerprint.md, Section 2)

3. **Imagery Source** — Where metaphors come from. Peter's are physical: construction, print, cooking, spatial. Never corporate. (voice-fingerprint.md, Section 3)

4. **Transitions** — How ideas connect. "And" is the primary connector. Some transitions are abrupt on purpose. Never "however," "furthermore," "additionally." (voice-fingerprint.md, Section 4)

5. **Emotional Register** — How feeling enters text. "Name the feeling before the thought when something matters." Vulnerability stated, not performed. (voice-fingerprint.md, Section 5)

6. **Evidence Pattern** — How claims are supported. Lead with the specific incident, then extract the principle. (voice-fingerprint.md, Section 6)

7. **Qualification Style** — How certainty and uncertainty are expressed. State opinions directly. "I think" is thinking out loud, not a hedge. (voice-fingerprint.md, Section 7)

8. **Vocabulary** — Actual word choices vs. AI defaults. Peter says "figure out," AI defaults to "determine." Peter says "sucks," AI defaults to "suboptimal." (voice-fingerprint.md, Section 8)

9. **Compositional Roughness** — The core differentiator. "AI-smooth copy sounds like every paragraph knew where it was going before it started. Peter's copy should sound like a person who thinks clearly sat down and wrote something, and you can feel the thinking in it." (voice-fingerprint.md, Section 9)

### Function Words Carry Identity (Cognitive Science)

**Source: cognitive-science-references.md, Week 3 section**

**Pennebaker & King (1999). "Linguistic Styles: Language Use as an Individual Difference."**

> "Individual voice is carried primarily by function words (pronouns, articles, prepositions, conjunctions), which are processed below conscious awareness. Content words carry meaning. Function words carry identity."

Teaching point: "Voice governance rules target structural and functional elements (sentence length, opening patterns, use of periods vs. dashes, vocabulary domains) rather than content. This aligns with how voice actually works. Telling the AI to 'sound bold and direct' targets content-level mimicry. Constraining structural patterns targets the layer where voice actually lives."

### Structural Priming (Why Early Constraints Shape Everything After)

**Source: cognitive-science-references.md, Week 3 section**

**Bock & Loebell (1990). "Framing Sentences" (Structural Priming).**

> "Syntactic structures activated during language production prime all subsequent output. If a speaker produces a passive construction, their next sentence is more likely to be passive. Structure begets structure."

Teaching point: "Voice rules function as structural primes. When the AI generates 'Most people hate that. I use it.' (short, declarative, period-stopped), that syntactic structure primes subsequent sentences toward the same pattern. The rules don't just constrain individual sentences. They set the structural momentum for the entire output."

Caveat: "Structural priming is documented in human language production. Whether transformer architectures exhibit analogous priming during autoregressive generation is an open question. The functional parallel (early output structure shapes later output) holds observationally."

### The Generation Effect (Constrained Generation Produces Different Output)

**Source: cognitive-science-references.md, Week 3 section**

**Slamecka & Graf (1978). "The Generation Effect in Memory."**

> "Information generated by the learner (completing 'rapid: f___' as 'fast') is remembered better than information simply read ('rapid: fast'). The act of generating under constraints creates qualitatively different memory traces than passive receipt."

Teaching point: "Voice governance forces the AI to generate under constraints rather than freely. The constraints (no em dashes, physical vocabulary, no self-introduction openers) function like the generation cues in Slamecka's paradigm. The output is structurally different, not just superficially edited."

Caveat: "The generation effect is a memory phenomenon. Applying it to AI text generation is analogical, not direct."

### Editing Normalizes Toward the Editor's Defaults

**Source: cognitive-science-references.md, Week 3 section**

**Baker (1993). "Corpus Linguistics and Literary Theory" / Solum (2018). "The Fixation Thesis."**

> "Editing systematically normalizes text toward the editor's defaults. Baker demonstrated this in literary translation (translators' stylistic fingerprints override source text voice). Solum demonstrated it in legal interpretation."

Teaching point: "This is why 'write in this person's voice' fails. The AI edits its own output during generation, normalizing toward its defaults (epigrammatic closers, em dashes, philosophical asides). Voice governance prevents normalization by making the defaults structurally unavailable."

### Constraints Redirect Creativity

**Source: cognitive-science-references.md, Week 3 section**

**Stokes (2005). Creativity from Constraints: The Psychology of Breakthrough.**

> "Paired constraints (one blocking a habitual response, one promoting a novel alternative) are the mechanism behind creative breakthroughs across domains."

Teaching point: "Each voice rule is a paired constraint. 'No em dashes' blocks a habitual AI response. 'Use periods for short declarative stops' promotes the alternative. 'Never open with self-introduction' blocks the default. 'Open with current work' promotes the alternative."

### Constitutional AI Validates the Mechanism

**Source: cognitive-science-references.md, Week 3 section**

**Anthropic (2022). Constitutional AI: Harmlessness from AI Feedback.**

> "Applying rules during the generation process (constitutional principles that govern output as it's being produced) yields Pareto improvements: better on the target dimension without degrading other dimensions. Generation-time constraints outperform post-hoc editing."

Teaching point: "Voice governance applies constraints during generation, not after. This is structurally identical to Constitutional AI: rules that shape output as it's produced rather than filtering it afterward."

### Conversation vs. Published Writing as Source

**Source: Whitepaper, Section 4.2 (voice-governance.md, lines 127-137)**

> "The source material for the protocol is conversation, because published writing is performance. The practitioner has already edited, compressed, and shaped their thinking for an audience. Training on performance produces performed output."

> "Published writing says: 'The methodology was developed through iterative refinement of governance patterns.' Conversation says: 'I kept losing things between sessions. Not the notes. The exact moment something clicked.' The conversation version is the actual voice. The published version is what the voice sounds like after it has been cleaned up."

**Source: Published essay (_essays/voice-governance.md, lines 33-37)**

> "Most of that material is me talking. Explaining problems, working through decisions, arguing with myself about naming, reacting to what the tool produced, directing implementation. The way I start sentences, the vocabulary I reach for when I'm not performing, how I describe problems (feeling first or situation first), how I transition between ideas (connectors or hard breaks), what makes me funny and what makes me frustrated."

> "That conversational material is the actual voice. Published writing filters it out, which is why you can't use published writing as the source."

### Peter's Protocol as Living Example: What 40 Rules Look Like

**Source: voice-protocol.md (full file)**

The actual voice protocol has these categories:

**Hard Rules (zero tolerance, 8 rules):**
1. Zero em dashes. Periods, commas, colons, parentheses.
2. Zero banned words: paradigm, leverage, passionate, innovative, synergy, empower, journey, transformative.
3. Zero negation-affirmation ("Not X. Y."). Always rewrite as direct statement. "This pattern sounds douchy and is the #1 AI tell."
4. No epigrammatic closers. Includes "The [noun] is the [noun]" but also any short punchy sentence designed to be quotable: mirrored structures, symmetrical reversals, any sentence that sounds like it belongs on a poster.
5. No triple-beat negation ("Not the X. Not the Y. The Z.").
6. No personification of tools or methods.
7. No ungrounded metaphors.
8. No academic register where spoken English works.

**AI Pattern Avoidance (9 patterns):**
- Negation-affirmation formula (the #1 AI tell)
- Em dashes
- Epigrammatic closers (broader than fortune-cookie)
- Triple-beat cadence
- Poetic metaphors without setup
- Academic register
- Constructed staccato
- Personification of abstractions
- Self-aware closers
- Uniform smoothness (the hardest AI tell to catch)
- Repeated mantra across pages

**Rhythm and Pacing:**
> "Direct but not clipped. Short declaratives build tension. Longer sentences land the weight. The pattern: Short. Shorter. Then a longer sentence that carries the consequence."

**Vocabulary:**
> "Reach for: holds, breaks, drifts, scaffold, fidelity, load, joints, structure, craft, strokes, terrain, anchor, navigate, coherence, lock."
>
> "Never use: solutions, innovation, transformation, paradigm, synergy, leverage, passionate, empower, journey, transformative, groundbreaking, revolutionary, game-changing, best-in-class."
>
> "The vocabulary is physical. It implies weight, load, durability."

**Specificity Over Generality:**
> "Not 'I had this problem' but the exact texture of the problem. Specific numbers, durations, moments. 'Twelve years' not 'over a decade.' 'Three rewrites' not 'multiple iterations.'"

**Action Over Description:**
> "Not: 'The methodology involves deep consultation to understand client needs.' But: 'You have a conversation. You listen to how they feel about what they're building.'"

**Output Profiles (5 registers):**
The protocol includes separate profiles for body-copy, pages, essays, whitepapers, and social. Each adjusts the base protocol for a specific output type. For example:
- Essays: "Closest to speech. Chains, run-ons, mid-sentence corrections all welcome." (essays.md)
- Whitepapers: "Conceptual precision matters. Still practitioner register, not academic." (whitepapers.md)
- Social: "Hook-first. The thing itself, no setup. The scene, not the speaker." (social.md)
- Body copy: "Shortest sentences in any register. Still not choppy." (body-copy.md)

### The Registration Metaphor (Why Slight Imperfection Reads as Human)

**Source: voice-fingerprint.md, "The Registration Principle" (lines 14-21)**

> "The target is slightly out of register. Not raw dictation (that's Peter talking to a tool). Not polished composition (that's AI writing about Peter). The target is Peter sitting down to write something he cares about, in his own rhythms, with the specific way his mind builds a thought."
>
> "Perfect registration = AI smoothness. Every paragraph resolves, every transition bridges, every closer lands. That reads as composed, not human."
>
> "Slightly out of register = tactile. A sentence that runs because the thought ran. A closer that moves forward instead of landing an epigram. A paragraph that changes direction because the idea changed direction. You can feel the hand in it."
>
> "This is not a flaw to tolerate. It is a design decision. The misregistration is intentional and controlled, the way a half-degree rotation in a print makes it feel handmade without looking broken."

**Source: Blog draft, what-registration-actually-means.md (lines 19-21)**

> "In screenprinting, registration is when the color layers land exactly where they're supposed to. Each color gets its own screen. Each screen prints one pass. If the screens are aligned, the colors stack and you get the image. If they're off by a fraction, you get mud."

### Honest Limitations of the Research

**Source: cognitive-science-references.md, "Honest Limitations" section**

> "Analogical support: Voice governance as generation-time constraint (Week 3). The component research (structural priming, generation effect, Constitutional AI) each support pieces of the argument, but no one has studied 'extracting voice rules from speech transcripts and applying them as AI generation constraints' as a unified intervention. We're building the argument from converging evidence, not from a single study that tested exactly this."

> "This is appropriate for a practitioner course. We're teaching a method, grounding it in the best available science, and being honest about where the science is direct vs. where we're making principled extrapolations."

---

## Lesson 3.4 — Guided Voice Extraction

**Lesson type:** Guided (student follows structured process)
**Deliverable:** Student produces their own voice protocol from their Week 2 brain dump.

---

### How Peter's Protocol Was Built

**Source: Published essay (_essays/voice-governance.md, lines 49-57)**

> "I had a draft of my This Site page that ended with 'The structure is the signal.' It scanned fine. The rhythm was satisfying. I read it twice before I noticed it meant nothing. That sentence could end any page about systems, infrastructure, design, governance. It belonged to no one in particular and said nothing specific about my work. That catch became a rule: no fortune-cookie closers. Sentences that feel like insight without containing any."

> "That's how most of these rules got built. I caught a pattern, named it, codified the prohibition."

**Source: Published essay (_essays/voice-governance.md, lines 57-58)**

> "Every rule is enforceable and has a specific origin. 'Zero em dashes' because they accumulate into a rhythm that belongs to no specific person."

**Source: Published essay (_essays/voice-governance.md, lines 58-62)**

> "'Every negation-affirmation pattern has to be earned' because that pattern ('Not X. Y.') is the single most common AI writing tell and most people don't notice it until you point it out. The test: does the negation correct a genuine misunderstanding the reader would actually have? If you're using it for emphasis or contrast, rewrite it. Every rule in the protocol got built the same way: I caught it in real output, named what was wrong, and wrote a prohibition specific enough that I couldn't rationalize my way past it later."

### The Two-Stage Extraction Pipeline

**Source: Whitepaper, Section 4.2 (voice-governance.md, lines 136-137)**

> "The extraction pipeline has two stages. The first samples how I talk in conversation: sentence rhythm, opening moves, vocabulary, transitions, emotional register. Raw observations, accumulated across sessions. The second converts those observations into operational generation rules organized by dimension: how sentences connect, how paragraphs open, where imagery comes from, how feeling enters the text. The protocol tells the model what it cannot do. The fingerprint tells it what I do. Both are loaded before generation begins."

### The Voice Sample Method

**Source: Published essay (_essays/voice-governance.md, lines 43-48)**

> "The voice-sample skill reads my conversation transcripts and captures observations about how I actually talk. The output isn't a style guide. It's a tuning fork. It tracks sentence rhythm (short bursts or long flowing thoughts?), opening moves ('so basically...', 'the thing is...', 'yeah let's...'), natural vocabulary, transitions, humor, qualifying phrases."

> "The key constraint: voice sampling reads conversations, not published pages. Published pages are the output. Conversations are the source. Conflating those is how you end up with AI voice that sounds polished but empty."

### The Categories Students Should Extract From Their Brain Dump

Based on Peter's actual protocol structure (voice-protocol.md + voice-fingerprint.md), students extract rules in these categories:

**Category 1: Hard Prohibitions (What You Never Do)**
Source template: voice-protocol.md "Hard Rules" section
- What punctuation patterns does the student never use?
- What words do they never reach for?
- What sentence structures feel wrong to them?
- What kinds of openings or closings feel fake?

**Category 2: AI Patterns to Block**
Source template: voice-protocol.md "AI Pattern Avoidance" section
- The student generates a standard prompt output about their work, then identifies what feels wrong about it
- Each "feels wrong" moment becomes a named pattern to prohibit

**Category 3: Sentence Architecture**
Source template: voice-fingerprint.md Section 1
- How does the student connect thoughts? ("And" chains? Hard breaks? "So" as consequence?)
- Short sentences or long ones? When do they switch?
- Do they use periods where others use commas?

**Category 4: Opening Moves**
Source template: voice-fingerprint.md Section 2
- How do they start explaining something? With the thing itself or with context?
- Do they lead with feeling or situation?
- What phrases signal they're about to make their real point?

**Category 5: Imagery and Vocabulary**
Source template: voice-fingerprint.md Sections 3 and 8
- Where do their metaphors come from? (Physical trade? Kitchen? Sports? Music?)
- What words do they reach for naturally vs. what the AI defaults to?
- Build a two-column table: "I say" / "AI defaults to"

**Category 6: Emotional Register**
Source template: voice-fingerprint.md Section 5
- How does excitement show up? (Velocity? Superlatives? Detail density?)
- How does frustration show up? (Bluntness? Silence? Humor?)
- How does vulnerability enter? (Stated directly? Hedged? Never?)

**Category 7: Evidence Pattern**
Source template: voice-fingerprint.md Section 6
- Does the student lead with the incident or the principle?
- Do they use hypotheticals or real examples?
- How do they handle uncertainty? ("I think" vs. hedging?)

**Category 8: Compositional Roughness**
Source template: voice-fingerprint.md Section 9
- Does every paragraph resolve neatly, or do some move forward instead of landing?
- Is there room for a thought to arrive partway through a paragraph?
- Does the student's writing have temperature variation (some paragraphs intense, some just factual)?

### The Guided Extraction Exercise

Step 1: Student re-reads their Week 2 brain dump transcript
Step 2: For each category above, student identifies 1-3 patterns from their own speech
Step 3: Student converts each pattern into an operational rule (following the format: what to do OR what not to do, with a specific enough description that the AI can follow it)
Step 4: Student assembles rules into a single protocol document

### Extraction Template

Use this table for each of the 8 categories. Fill in at least 4 categories with 1-3 patterns each. One row per pattern found.

| Category | Pattern Found | Quote from My Transcript | Operational Rule |
|----------|--------------|--------------------------|------------------|
| Hard Prohibitions | (what do you never do or say?) | (exact words from transcript) | (binary rule: "Zero [X]" or "Never [Y]") |
| AI Patterns to Block | (what AI defaults would sound wrong in your voice?) | (example from transcript showing the opposite) | (specific pattern to catch and prevent) |
| Sentence Architecture | (how do your sentences connect?) | (example) | (rule about connectors, length, rhythm) |
| Opening Moves | (how do you start a thought?) | (example) | (rule about what you lead with) |
| Imagery and Vocabulary | (what physical/concrete words do you reach for?) | (example) | (vocabulary list or reach-for guidance) |
| Emotional Register | (how does feeling enter your speech?) | (example) | (rule about when/how emotion surfaces) |
| Evidence Pattern | (how do you support claims?) | (example) | (rule about sourcing, specifics, proof) |
| Compositional Roughness | (where does your writing NOT resolve cleanly?) | (example) | (rule about allowing unresolved moments) |

**Example row (from Peter's own extraction, for reference):**

| Category | Pattern Found | Quote from Transcript | Operational Rule |
|----------|--------------|----------------------|------------------|
| Opening Moves | Leads with the situation or the feeling, not with context or credentials | "So basically what happened was the output came back flat and I knew immediately it was the prompt structure" | "Open with the thing itself. The situation, the feeling, or the object. Context comes after, if at all." |

**Minimum viable protocol:** 8-12 rules covering at least 4 of the 8 categories above.

**Source model for rule format (voice-protocol.md, hard rules):**
Each rule should be: binary (yes/no, zero tolerance, or specific threshold), testable (you can check whether the output follows it), and originated from real speech (traced to something the student actually said or did in their transcript).

### Real Extraction Walkthrough

The following excerpt shows the extraction process in practice. See `course/artifacts/real-session-excerpts.md` (Excerpt 2) for the full annotated version.

Peter was reviewing 8 book chapters against his voice protocol. The system found negation-affirmation patterns exceeding the allowed limit. His reaction: "I think they sound performed. Like the AI is landing a point instead of making one." That visceral response became an operational rule (zero tolerance), which propagated across 6 governance files in under three minutes.

The excerpt demonstrates: reading output, noticing a pattern, naming it with a concrete reason, converting the observation into a binary rule, and propagating the rule system-wide. The AI also distinguished between real negation-affirmation patterns and natural comparisons that look similar but serve a different function. That distinction (pattern vs false positive) is the nuance students must learn.

[EXCERPT 2 FROM: course/artifacts/real-session-excerpts.md — embed full Excerpt 2 content here when rendering student-facing pages.]

---

## Lesson 3.5 — Guided Application (Before/After Test)

**Lesson type:** Guided (student applies their protocol)
**Deliverable:** Student generates copy under their voice protocol and verifies the output.

---

### The Application Process

Step 1: Student takes a real writing task from their own work (about page, project description, bio, or similar)
Step 2: Student generates the output WITHOUT their voice protocol (standard prompt, to create the "before")
Step 3: Student generates the same output WITH their voice protocol loaded as generation constraints
Step 4: Student compares the two outputs side by side

### What Changed (Teaching the Analysis)

**Source: demo artifact, lines 126-142 (Mara Voss rule-by-rule analysis)**

The demo artifact shows Peter's analysis of what changed with voice governance. Each rule is checked against the output:

- "Opens with what she's making, not who she is. (Rule 1)"
- "No em dashes anywhere. Short declarative stops. (Rule 2)"
- "Physical vocabulary: ink, nib, push, catches, upstrokes, scan. (Rule 3)"
- "'Most people hate that. I use it.' Direct, not hedged. (Rule 4)"

Students do the same analysis with their own output: for each rule in their protocol, check whether the constrained output follows it, and whether the unconstrained output violates it.

### The Verification Checklist (Peter's Copy-Verify as Model)

**Source: copy-verify/SKILL.md, lines 73-85 (the 13-item checklist)**

Peter's verification checklist for published copy:

1. Does the opener make a stranger feel the problem (not just know about it)?
2. Does it pass the Grip Test at Grip or Lock level?
3. Is every specific detail traceable to a verified source?
4. Zero em dashes?
5. Zero banned words?
6. No fortune-cookie closer?
7. Zero negation-affirmation ("Not X. Y.")?
8. No ungrounded metaphors?
9. No personification of tools/methods?
10. Shaw check: does the copy feel like a room, not a pitch?
11. Practitioner authority: does this read like a practitioner telling a respected peer what happened?
12. Does the frontmatter match the body?
13. Does the index entry need updating?

**For student use:** Items 1-11 are adaptable to any voice protocol. Items 12-13 are Peter-specific (site infrastructure). Use this 8-item student verification checklist after generating constrained output:

### Student Verification Checklist

1. **Hard rules pass?** Read through your hard prohibitions one by one. Does the output follow each? Binary per rule: pass or fail.
2. **AI patterns caught?** Check for the AI defaults you listed (negation-affirmation, epigrammatic closers, performed enthusiasm, etc.). Did any slip through?
3. **Opening move matches?** Does the output open the way you actually open? Compare the first sentence to how you started thoughts in your transcript.
4. **Vocabulary right?** Does the output reach for YOUR physical/concrete words, or did it substitute generic alternatives?
5. **Sentence rhythm matches?** Read the output aloud. Does the pacing feel like you talking, or like AI performing smooth cadence?
6. **Feeling enters where it should?** Does emotion surface where you surface it (in your transcript), or where the AI defaults to surfacing it (typically at endings and transitions)?
7. **Roughness preserved?** Is there at least one moment where the thought moves forward instead of landing cleanly? Or does everything resolve with equal smoothness?
8. **The room test:** Could this only have come from you? If you stripped the byline, would a colleague recognize the voice?

Score: 8/8 means the protocol is working. 5-7/8 means specific rules need tightening. Below 5 means the protocol is too loose or the rules are surface-level (go back to extraction, look for structural patterns you missed).

### The Overcorrection Warning

**Source: Blog draft, the-overcorrection-when-governance-catches-false-positives.md (lines 18-33)**

> "The voice protocol has 40 rules. Zero em dashes. Zero negation-affirmation. No epigrammatic closers. No personification of tools. Each rule exists because it catches a specific AI pattern that makes copy sound machine-generated."

> "The rules work. They catch a lot. But a system tuned to catch every AI pattern will also catch human writing that happens to share the same pattern."

> "I write short declarative sentences followed by other short declarative sentences. Sometimes those sentences land in a rhythm that the protocol flags as 'constructed staccato.' The protocol says: 'Short. Sentence. After. Short. Sentence. Vary paragraph lengths.' But that's how I actually talk. The protocol can't tell the difference between an AI producing staccato because it defaults to staccato and a human producing staccato because that's their rhythm."

> "The negation-affirmation rule catches the most AI tells. 'Not X. Y.' is the pattern. Every LLM does it. Zero tolerance. But I've caught myself writing negation-affirmation naturally in conversation. 'Not the whole system. Just the front end.' That's a real thing I said to a real person. The protocol would flag it."

> "The fix isn't loosening the rules. Loosening the rules lets the real violations through. The fix is a human override that acknowledges the false positive and proceeds."

> "Governance that enforces without judgment strips the human out of the loop. Governance that informs while the human decides keeps the human where they need to be: making the calls that only a person can make."

Teaching point: Your voice protocol will sometimes flag your own writing. That means the rules are working. The human override is part of the system, not a failure of it.

### How to Tell If the Output Sounds Like You

**Source: voice-fingerprint.md, Section 10 "The Test" (lines 153-158)**

Three questions to ask:

> "1. Would [you] say this to a peer [you] respect? Not to a stranger at a bar (too casual). Not to an academic panel (too formal). To someone who does serious work in an adjacent field."

> "2. Can you feel the hand in it? Is there one moment where the thought turns, runs long, or doesn't resolve cleanly? If every sentence lands perfectly, it's too smooth."

> "3. Does it sound like a person or a writer? A person has rhythms that repeat, words they reach for, ways they build toward a point that are specific to them. A writer has technique. [You are] a person first."

### The Fidelity Chain

**Source: Blog draft, fidelity-in-ai-output.md (lines 34-36)**

> "The fidelity chain is: source material, constrained generation, independent evaluation, human verification. Skip any link and the output drifts. It'll still be competent. It just won't be yours."

### Real Verification Walkthrough

The following excerpt shows the verification and override process in practice. See `course/artifacts/real-session-excerpts.md` (Excerpt 3) for the full annotated version.

Peter drafted a LinkedIn comment responding to a well-known design educator's post about learning stages. Before posting, he ran copy-verify. The system caught three violations: an em dash (mechanical), a fortune-cookie closer (structural), and a negation-affirmation pattern (rhetorical). Each got a specific fix. The comment went from 9/12 to 12/12.

Then Peter overrode in the other direction: he ADDED substance the system did not flag ("I have to add that its the human in the loop making the CHOICE between those perspectives"). The protocol passed, but Peter's judgment said the content was incomplete. He also made a social judgment call the protocol has no rule for (whether to tag another practitioner in the comment). Fourteen minutes from seeing the post to "posted."

The excerpt demonstrates: system catches what eyes miss (3 categories of violation), human adds what the system cannot see (incomplete content, social positioning), and governance that informs while the human decides keeps the human where they need to be.

[EXCERPT 3 FROM: course/artifacts/real-session-excerpts.md — embed full Excerpt 3 content here when rendering student-facing pages.]

---

## Lesson 3.6 — Independent Exercise + Capstone Deliverable

**Lesson type:** Independent (student works alone)
**Deliverable:** A real piece of work produced with the full three-week methodology.

---

### The Full Stack (All Three Weeks Combined)

The student produces a single real deliverable using all three weeks:

1. **Week 1 (Task Decomposition):** The task is broken into discrete steps. Each step has a clear input and output. The AI handles one step at a time.

2. **Week 2 (Input Inversion):** The source material is the student's own brain dump. Unstructured thinking, recorded or typed, that captures how they actually think about the work. This is the substrate.

3. **Week 3 (Voice Governance):** The voice protocol constrains generation so the output sounds like the student. Rules extracted from their own speech patterns, applied during production.

### What "Done" Looks Like

The capstone deliverable must meet these criteria:

**Content criteria (from Weeks 1-2):**
- The task was decomposed before generation began
- The source material came from the student's own thinking (brain dump, not a prompt)
- Every specific detail in the output is traceable to the student's source material
- No hallucinated specifics (facts the student didn't provide)

**Voice criteria (from Week 3):**
- The student's voice protocol was loaded during generation, not applied after
- The output passes the student's own verification checklist
- The before/after comparison shows structural differences (not just word swaps)
- The output passes the three-question test: peer register, hand in it, person not writer

**Quality criteria (the "room test"):**
- A stranger reading this would feel a specific person behind it
- The output could not be swapped onto a competitor's site without feeling wrong
- The opening makes the stranger feel the problem, not just know about it

### Suggested Deliverable Options

Any of these, chosen by the student based on their actual work:

- An About page for their own practice/business
- A project description or case study for a completed project
- A bio for a specific context (conference, client proposal, portfolio)
- A pitch or proposal for a specific opportunity
- A blog post or essay about something they care about

The deliverable must be real. It should be something the student actually needs for their practice. The course produces working output, not exercises.

### The Constraint-as-Fuel Frame

**Source: Blog draft, constraint-as-creative-fuel.md (lines 28-29)**

> "The voice protocol I use for all my writing works this way too. Zero em dashes. Zero uses of words like 'innovative' or 'transformative.' Three locked fonts across the entire site. Every rule removes an option. And removing options is what makes the output distinctive. Freedom produces mush. A locked set of constraints produces a voice you can recognize across pages."

**Source: Blog draft, constraint-as-creative-fuel.md (lines 37-39)**

> "I keep finding this. The best work I've done came from the tightest constraints. The 9K gold. The closed glyph set. Twelve different learners in one room. Four people who can't eat the same thing. The terminal that only gives you six operations."

> "When you remove options, the remaining options have to work harder. And the work is better for it."

### What the Protocol Catches That You Cannot

**Source: Whitepaper, Section 5.3 (voice-governance.md, lines 163-168)**

> "The protocol catches patterns that the writer cannot hear in their own copy. After reading twenty drafts, the em-dash frequency becomes invisible. The fortune-cookie closers sound fine. The mechanical parallelism feels like 'good structure.' The protocol makes the patterns visible by prohibiting them. When the model cannot use them, the writer can see what remains, and what remains is either specific and grounded or it is empty."

> "The voice protocol is a diagnostic and a generation constraint simultaneously. It tells you what is wrong with the draft by preventing it from being wrong in those specific ways. If the constrained output is still flat, the voice was never the issue. The content itself needs work."

### What the Protocol Does NOT Do

**Source: Blog draft, fidelity-in-ai-output.md (lines 31-33)**

> "The protocol doesn't make the AI sound like me. It stops the AI from sounding like itself. That's a different operation. Fidelity in AI output isn't about adding personality. It's about preventing the tool from overwriting the personality that's already in the source material."

> "This is why I use AI as a compiler, not a generator. The source material is mine. The conversations, the rough thinking, the specific moments and vocabulary and structural instincts. The AI transforms it. Compiles it into publishable form. But it doesn't originate any of it."

### Cross-Week Cognitive Science Summary

**Source: cognitive-science-references.md, "Cross-Week Themes" section**

> "Three cognitive science patterns recur across all three weeks:"
>
> "1. Decomposition reduces load. Sweller, Cowan, and Kellogg all demonstrate that concurrent processing of multiple demands degrades performance. Each week's technique separates what other approaches combine: task steps (Week 1), thinking and formatting (Week 2), content and voice (Week 3)."
>
> "2. Constraints improve output. Stokes, Slamecka, and the Anthropic Constitutional AI work all show that constraints during generation produce better results than unconstrained generation followed by editing. Constraints are not limitations. They are structural guidance."
>
> "3. Structure shapes content. Bock's structural priming, Pennebaker's function-word identity, and Flower & Hayes's knowledge-transforming all point to the same insight: changing the structure of how something is produced changes what gets produced, not just how it looks. Voice governance doesn't make the same content sound different. It produces different content."

### Knowledge-Transforming vs. Knowledge-Telling

**Source: cognitive-science-references.md, Week 3 section**

**Flower & Hayes (1981) / Bereiter & Scardamalia (1987).**

> "Knowledge-transforming writers (experts) reshape their thinking through the act of writing. Knowledge-telling writers (novices) dump existing knowledge into text without transformation."

Teaching point: "Standard prompting produces knowledge-telling: the AI dumps what it knows about 'brand designer about pages.' Voice governance forces something closer to knowledge-transforming: the constraints reshape the output structure, which in turn changes what gets said and what gets left out. The about page written under voice governance contains different information, not just different phrasing."

### Real Capstone: Full-Stack Methodology in One Session

The following excerpt shows all three modules' skills demonstrated in a single real working session. See `course/artifacts/real-session-excerpts.md` (Excerpt 4) for the full annotated version.

Peter spent a full day building and executing a LinkedIn content strategy. The session contains the entire methodology:

- **Module 1 (Decomposition):** Planning the content calendar, breaking multi-post strategy into individual components, mapping the content landscape before writing anything.
- **Module 2 (Input Inversion):** Pasting raw source material (another educator's post, analytics data, existing content inventory) as unstructured input. The raw material became the basis for original content.
- **Module 3 (Voice Governance):** Copy-verify caught three violations in a drafted comment (Excerpt 3 is from inside this session). Peter overrode on specific terminology ("drift and fidelity are really accurate for what's happening") where his judgment said the voice protocol was wrong about those specific terms.
- **Shipping:** "Posts scheduled daily through thursday." Real deliverables shipped from the methodology.

The annotations in the full excerpt mark where each module's skill appears: "This is Module 1 (decomposition)" / "This is Module 2 (unstructured input)" / "This is Module 3 (voice governance and override)." The student should finish reading this and see how the three modules connect into one workflow.

[EXCERPT 4 FROM: course/artifacts/real-session-excerpts.md — embed full Excerpt 4 content here when rendering student-facing pages.]

---

## Course Summary

Three weeks. One complete cycle.

In Week 1 you watched compound prompts degrade. You saw why a single instruction with five objectives splits the model's attention across all of them, why the output comes back competent-but-shallow, and what decomposition does to fix it. You ran five specialist prompts, saw each go deeper than the compound version, and synthesized the outputs into a brief that only a human creative director could have written.

In Week 2 you saw why structured prompts cap the output at the level of the prompt itself, and why unstructured human thinking, captured as raw voice, produces richer results when it becomes the input. You ran a brain dump. You built structured inputs from it. You compared what the model returned against the compound baseline.

In Week 3 you wrote a voice protocol by listening to how you actually talk. You extracted operational rules. You loaded them as governance constraints during generation. You tested the output, caught where the model found loopholes, sharpened the rules, and ran the cycle again.

Across all three weeks one idea holds: **you are the creative director, and the AI is your department.** [SOURCE: roughing-it-compound-demo.md, setup; NORTHSTAR.md, line 31] You decide what to decompose. You decide what the inputs should contain. You decide what voice rules govern the work. The model is a capable specialist whose work you scope, shape, and constrain, exactly like any specialist reporting to you.

The methodology is portable. The specific tools will change. The underlying move stays the same: ask what the system receiving the work actually needs to succeed, then structure your instructions around that reality. That question came from a self-contained classroom in Sunset Park, Brooklyn, with twelve students on twelve IEPs, where designing around the processing reality of the receiving system is federal law. The fix was identical when the system receiving the work was a language model instead of a nine-year-old. [SOURCE: essay, what-does-the-system-actually-need.md] That transfer is why the framework has a name: Accommodation Design.

From here, the practitioner-track courses go deeper into each domain. Input Inversion, Prosthetic Cognition, Semantic Hierarchy, Voice Governance, and Lens Extraction each take a single domain, examine it as a standing practice, and expand what you've done in Foundations into sustained working methodology.

You've done the Foundations. The work from here is yours to shape.

---

## Source Inventory

All content in this document is compiled from the following files:

| Source | Location | Used In |
|--------|----------|---------|
| Mara Voss demo | `course/artifacts/week3-voice-governance-demo.md` | 3.1, 3.2, 3.5 |
| Voice governance whitepaper | `petersalvato.com/_research/voice-governance.md` | 3.1, 3.3, 3.6 |
| Voice governance essay | `petersalvato.com/_essays/voice-governance.md` | 3.1, 3.3, 3.4 |
| Voice protocol | `joinery/voice/voice-protocol.md` | 3.3, 3.4 |
| Voice fingerprint | `joinery/voice/voice-fingerprint.md` | 3.3, 3.4, 3.5 |
| Output profiles | `joinery/voice/profiles/*.md` | 3.3 |
| Copy-verify skill | `joinery/skills/copy-verify/SKILL.md` | 3.5 |
| Cognitive science refs | `course/artifacts/cognitive-science-references.md` | 3.3, 3.6 |
| Fidelity in AI Output (draft) | `petersalvato-dev/_drafts/fidelity-in-ai-output.md` | 3.1, 3.5, 3.6 |
| Constraint as Creative Fuel (draft) | `petersalvato-dev/_drafts/constraint-as-creative-fuel.md` | 3.6 |
| The Overcorrection (draft) | `petersalvato-dev/_drafts/the-overcorrection-when-governance-catches-false-positives.md` | 3.5 |
| Voice sample | `memory/voice-sample.md` | 3.3, 3.4 |

## Production Status (updated 2026-04-05)

**Resolved (replaced with real session excerpts from conversation history):**
- ~~Lesson 3.4: extraction walkthrough~~ → Excerpt 2 (negation-affirmation kill, March 18, 2026)
- ~~Lesson 3.5: verification walkthrough~~ → Excerpt 3 (LinkedIn copy-verify, March 7, 2026)
- ~~Lesson 3.6: capstone walkthrough~~ → Excerpt 4 (full-stack LinkedIn workflow, March 7, 2026)

**Remaining (optional, course ships without):**
1. **Lesson 3.1:** Video close recording. Script outline compiled. Nice-to-have for production polish. Not blocking.
