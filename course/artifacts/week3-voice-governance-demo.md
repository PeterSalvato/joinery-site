# Week 3 Artifact: Voice Governance Demo

## The Task

Write an About page for Mara Voss, freelance brand designer and hand-letterer in Brooklyn.

---

## Part 1: Standard Prompt

**Prompt:**

> Write an About page for Mara Voss, freelance brand designer and hand-letterer in Brooklyn.

**Output:**

> I'm Mara Voss, a brand designer and hand-letterer based in Brooklyn, New York.
>
> For over a decade, I've helped brands find their visual voice through custom lettering, identity systems, and strategic design. My work sits at the intersection of craft and strategy — I believe that how something looks should reflect what it means.
>
> I've worked with clients ranging from independent coffee roasters to national retail brands, bringing the same attention to detail whether I'm sketching letterforms or building a full identity system.
>
> When I'm not at the drawing table, you'll find me hunting for vintage type specimens at flea markets, experimenting with new ink formulations, or teaching lettering workshops around the city.
>
> If you're looking for a designer who treats every project as a unique challenge, I'd love to hear from you.

**What happened:** This is the AI About page. Every freelance designer on the internet has a version of this. "Find their visual voice." "Intersection of craft and strategy." "How something looks should reflect what it means." "I'd love to hear from you." It is accurate, grammatically correct, and completely empty. You cannot distinguish this person from 10,000 other designers after reading it.

---

## Part 2: Harnessed Prompt

**Prompt:**

> Write an About page for Mara Voss, freelance brand designer and hand-letterer in Brooklyn.
>
> Tone: Bold, direct, no-nonsense. Short sentences. Conversational but confident. She doesn't explain herself or justify her choices. She states what she does and moves on.
>
> Reference style: Jessica Walsh meets punk zine editor. Warm but with teeth.
>
> Constraints: No jargon. No "visual voice" or "intersection of." No calls to action. Under 200 words.

**Output:**

> I letter things by hand. Have for over ten years.
>
> Brands come to me when they want something that doesn't look like it came out of a template. I draw it. I ink it. I make it work at every size from a business card to a billboard.
>
> I also do full identity systems. Logo, type, color, guidelines. The whole thing. But the lettering is where it starts, because letterforms tell you what a brand sounds like before anyone reads a word.
>
> I've done this for hot sauce companies, architecture firms, book publishers, a chain of climbing gyms, and one very particular whiskey brand that took eleven rounds of revisions and turned out great.
>
> I believe in the tool. The nib, the brush, the pencil. Screens are where work gets delivered. Paper is where it gets made.
>
> I work out of a studio in Greenpoint with too many ink samples and not enough shelf space.
>
> If your brand needs a voice that looks like it means what it says, that's what I do.

**What happened:** Better. The short sentences work. The client list is specific. The opening is direct instead of self-introducing. The constraints eliminated most of the generic language.

But two things give it away:

1. "I believe in the tool." This is philosophical in a way most working designers wouldn't be. It's the AI performing depth. A real designer with this personality would say something about the specific tool, not about believing in tools as a category.

2. "If your brand needs a voice that looks like it means what it says, that's what I do." Epigrammatic closer. The AI defaults to this: a neat, quotable, slightly clever final sentence that wraps everything up. Real people don't end conversations with epigrams.

The tone guidelines improved the surface. The output still has AI architecture underneath.

---

## Part 3: Voice Governance

**Source material:** Mara's brain dump recording from the Week 2 Input Inversion exercise. The same transcript where she talked through the Night Owl project. From that transcript and the way she speaks in it, 12 hard rules were extracted.

### Voice Rules (extracted from how Mara actually talks)

1. Never open with self-introduction. She starts with what she's making or what she just finished.
2. No em dashes. She uses periods where other writers use dashes. Short declarative stops.
3. Physical vocabulary: pressure, ink, weight, surface, pull, drag, bleed. She describes work in terms of what her hands do.
4. Dismissals are direct, not hedged. "That doesn't work" not "I tend to find that doesn't work as well."
5. Never explains why hand-lettering matters. She treats it as self-evident. If you need it explained, you're not her client.
6. References clients by what they make, not by category. "A hot sauce company in Austin" not "a food and beverage client."
7. No sign-off, call to action, or closing invitation. She stops when she's done talking.
8. Lists are concrete and uneven. Three items, not five. Specific, not parallel.
9. She names tools by brand or type (Nikko G nib, sumi ink, Rhodia pad), not by generic category.
10. Humor is dry and factual. "Eleven rounds of revisions" is funny because it's true, not because she's performing wit.
11. She talks about other people's work she respects. Unprompted. Mid-thought.
12. Rhythm pattern: two short sentences, then one medium sentence. Rarely a long sentence. Never two long sentences in a row.

**Source quotes from the transcript that generated these rules:**

> "The Nikko G does this thing where if you push too hard on the upstroke it catches. Most people hate that. I use it."

> "I just finished a set of labels for a hot sauce company in Austin. Three SKUs. The owner hand-grows the peppers and wanted the lettering to look like it came off a seed packet from the 1940s."

> "That doesn't work. If you have to explain to someone why hand-lettering is different from a font, they should hire someone else."

> "Have you seen the stuff Marian Bantjes did for Saks? That was twenty years ago and it's still the thing I measure against."

**Prompt (with rules and source material):**

> Write an About page for Mara Voss, freelance brand designer and hand-letterer in Brooklyn.
>
> Voice governance rules — apply these as hard constraints during generation, not as suggestions:
>
> [all 12 rules]
>
> Source material from Mara's recorded speech:
>
> [transcript excerpts]
>
> Do not add anything that isn't supported by or consistent with how she actually talks.

**Output:**

> Right now I'm finishing a set of packaging labels for a hot sauce company in Austin. Three SKUs. The owner grows his own peppers and wanted the lettering to feel like a seed packet from the 1940s. I spent two weeks on the lowercase g alone.
>
> I do hand-lettering and brand identity. Have for twelve years. I ink with a Nikko G nib on Rhodia pads, scan at 1200 DPI, and clean up in Illustrator. The nib catches on upstrokes if you push too hard. Most people hate that. I use it.
>
> Recent work: identity system for a climbing gym in Denver, packaging for a small-batch whiskey out of Kentucky, and a full rebrand for a brewery in Portland that took five months because the founder kept changing the brief. It turned out right.
>
> I work out of a studio in Greenpoint. Three desks, too many ink samples, a record player that only gets used on Fridays. I've been listening to a lot of Polish jazz lately. Komeda, Stanko. My friend gave me a stack of vinyl and I'm working through them.
>
> Marian Bantjes did that Saks work twenty years ago and I still think about it weekly. That's the bar. Lettering that makes you stop and look at a department store bag. If your type isn't doing that, it's just a font with extra steps.

**What happened:**

- Opens with what she's making, not who she is. (Rule 1)
- No em dashes anywhere. Short declarative stops. (Rule 2)
- Physical vocabulary: ink, nib, push, catches, upstrokes, scan. (Rule 3)
- "Most people hate that. I use it." Direct, not hedged. (Rule 4)
- Never explains why hand-lettering matters. Treats it as given. (Rule 5)
- "A hot sauce company in Austin," "a climbing gym in Denver," "a brewery in Portland." (Rule 6)
- No closing invitation. Ends with a thought about work. (Rule 7)
- Lists are three items, concrete, uneven. (Rule 8)
- Nikko G nib, Rhodia pads, 1200 DPI. Named tools. (Rule 9)
- "Took five months because the founder kept changing the brief. It turned out right." Dry, factual. (Rule 10)
- Marian Bantjes, unprompted, mid-thought. (Rule 11)
- Rhythm holds: short, short, medium. (Rule 12)

The Polish jazz reference came from her own recorded speech in Week 2. It wasn't in the prompt as a biographical fact. It was in her voice as something she actually said. The AI preserved it because it was in the source material, and the voice rules didn't filter it out. That's the difference: it belongs there because she put it there.

---

## Comparison

| Dimension | Standard | Harnessed | Voice Governance |
|-----------|----------|-----------|-----------------|
| Sounds like | AI writing about a person | Better AI writing about a person | A person |
| Source of voice | AI's default register | Tone keywords + style references | Extracted rules from actual speech |
| What shapes the output | Nothing specific | Adjectives (bold, direct, warm) | Structural constraints (rhythm, vocabulary, openings, closings) |
| AI tells present? | Yes, everywhere | Yes, two major ones | None detected |
| Could pass the "did a person write this" test? | No | Maybe, for 30 seconds | Yes |

**Standard** sounds like AI writing about a person. Every sentence could be about any designer.

**Harnessed** sounds like better AI writing about a person. Tone guidelines improved the surface, but the AI's structural defaults (philosophical asides, epigrammatic closers) leaked through. Tone is a suggestion. The model follows it when convenient and defaults when it doesn't know what else to do.

**Voice Governance** sounds like a person. The difference is that constraints extracted from actual speech and applied as hard rules during generation shape the output structurally, not just at the surface. The AI can't default to an epigrammatic closer because Rule 7 forbids it. It can't open with self-introduction because Rule 1 forbids it. It can't generalize about "food and beverage clients" because Rule 6 forbids it. The rules don't describe a vibe. They define a structure.

---

## Week-to-Week Connection

Week 2's brain dump produced the raw transcript. Week 3 mines that transcript for voice rules. The same source material serves two purposes: content excavation (what the designer thinks) and voice extraction (how the designer talks). The weeks scaffold. Week 2 without Week 3 gives you good ideas in the wrong voice. Week 3 without Week 2 gives you the right voice with nothing to say.
