#!/usr/bin/env python3
"""Process compiled course markdown into student-facing HTML lesson pages."""

import re
import markdown
import os

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} — Joinery Foundations</title>
    <meta name="robots" content="noindex, nofollow">
    <link rel="icon" href="../../../favicon.ico" sizes="32x32">
    <link rel="icon" href="../../../assets/favicon.svg" type="image/svg+xml">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Archivo:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400&family=Figtree:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../../../assets/style.css">
    <link rel="stylesheet" href="../assets/course.css">
</head>
<body>
    <div class="page">

        <nav class="nav" id="nav">
            <div class="nav-inner">
                <a class="nav-mark" href="../../../index.html">
                    <img src="../../../assets/logo.svg" alt="Joinery">
                    <span>Joinery</span>
                </a>
                <ul class="nav-links">
                    <li><a href="../../../index.html">Home</a></li>
                    <li><a href="../../../courses.html" class="active">Courses</a></li>
                    <li><a href="../../../research.html">Research</a></li>
                    <li><a href="../../../about.html">About</a></li>
                </ul>
            </div>
        </nav>

        <div class="course-page">
            <div class="course-header">
                <div class="module-label">{module_label}</div>
                <h1>{lesson_title}</h1>
                <p class="lesson-meta">{meta}</p>
            </div>

            <div class="lesson-content">
                {content}
            </div>

            <div class="lesson-nav">
                {nav_prev}
                {nav_next}
            </div>
        </div>

        <footer class="footer">
            <p>Founded by <a href="https://petersalvato.com">Peter Salvato</a></p>
        </footer>

    </div>
    <script src="../assets/course.js"></script>
</body>
</html>"""


def clean_compiled_markdown(text):
    """Strip production artifacts from compiled course markdown."""
    # Remove [SOURCE: ...] lines
    text = re.sub(r'\[SOURCE:.*?\]\n?', '', text)

    # Remove [NEEDS PETER: ...] blocks
    text = re.sub(r'\[NEEDS PETER:.*?\]', '', text, flags=re.DOTALL)

    # Remove "From the scaffold/whitepaper/artifact..." source intro lines
    text = re.sub(r'^From the (?:scaffold|whitepaper|artifact|published essay|blog draft|essay|foundations|cognitive|demo|Roughing).*?:\s*$', '', text, flags=re.MULTILINE)
    text = re.sub(r'^From ".*?".*?:\s*$', '', text, flags=re.MULTILINE)
    text = re.sub(r"^From Peter's.*?:\s*$", '', text, flags=re.MULTILINE)
    text = re.sub(r'^The (?:scaffold|artifact|whitepaper).*?:\s*$', '', text, flags=re.MULTILINE)

    # Remove **Source: ...** lines
    text = re.sub(r'^\*\*Source:.*?\*\*\s*$', '', text, flags=re.MULTILINE)

    # Remove "Teaching application:" and "Teaching point:" prefixes but keep content
    text = re.sub(r'^\*?Teaching (?:application|point)\*?:\s*', '', text, flags=re.MULTILINE)

    # Remove "Honest caveat:" prefix but keep content
    text = re.sub(r'^Honest caveat:\s*', 'Caveat: ', text, flags=re.MULTILINE)

    # Clean excessive blank lines
    text = re.sub(r'\n{4,}', '\n\n', text)

    return text.strip()


def process_cognitive_science(html):
    """Wrap cognitive science sections in callout boxes."""
    # Find patterns like **Citation (Year):** followed by blockquote
    pattern = r'<p><strong>([^<]+\(\d{4}[^)]*\))[^<]*</strong></p>\s*<blockquote>'

    def replace_science(match):
        citation = match.group(1)
        return f'<div class="callout-science"><div class="callout-label">Cognitive Science</div><p><strong>{citation}</strong></p><blockquote>'

    html = re.sub(pattern, replace_science, html)
    # Close the callout div after the blockquote
    # This is imperfect but handles basic cases
    return html


def process_exercises(html):
    """Wrap exercise sections in exercise blocks."""
    # Look for ### headers containing "Exercise" or "Your Turn" or "Template"
    html = re.sub(
        r'<h3>(.*?(?:Exercise|Your Turn|Template|Framing the Exercise).*?)</h3>',
        r'<div class="exercise-block"><div class="exercise-label">Exercise</div><h3>\1</h3>',
        html
    )
    return html


def split_lessons(content, module_num):
    """Split compiled markdown into individual lessons."""
    # Split by ## Lesson headers
    parts = re.split(r'\n## (Lesson \d+\.\d+[: —–-]+.+)\n', content)

    lessons = []
    for i in range(1, len(parts), 2):
        title_raw = parts[i].strip()
        body = parts[i+1] if i+1 < len(parts) else ""

        # Extract lesson number
        num_match = re.match(r'Lesson (\d+)\.(\d+)', title_raw)
        if num_match:
            lesson_num = int(num_match.group(2))
        else:
            lesson_num = len(lessons) + 1

        # Clean title (remove " — " formatting variations)
        title_clean = re.sub(r'\s*[—–-]\s*', ': ', title_raw)

        lessons.append({
            'num': lesson_num,
            'title_raw': title_raw,
            'title': title_clean,
            'body': body
        })

    return lessons


def build_lesson_page(lesson, module_num, total_lessons, module_title):
    """Build a complete HTML page for a single lesson."""
    # Clean the markdown
    cleaned = clean_compiled_markdown(lesson['body'])

    # Remove the **Format:** line from display (keep for reference)
    format_match = re.match(r'\*\*Format:\*\*.*?\n', cleaned)
    meta = ""
    if format_match:
        meta = format_match.group(0).replace('**Format:**', '').replace('**', '').strip()
        # Extract learning objective if present
        obj_match = re.search(r'\*\*Learning objective:\*\*\s*(.+?)(?:\n|$)', cleaned)
        if obj_match:
            meta = obj_match.group(1).strip()
        cleaned = cleaned[format_match.end():]

    # Remove standalone learning objective line
    cleaned = re.sub(r'^\*\*Learning objective:\*\*.*?\n', '', cleaned, flags=re.MULTILINE)

    # Convert markdown to HTML
    md = markdown.Markdown(extensions=['tables'])
    html_content = md.convert(cleaned)

    # Build navigation
    lesson_num = lesson['num']
    if lesson_num > 1:
        nav_prev = f'<a href="lesson-{lesson_num - 1}.html"><span class="nav-label">Previous</span>Lesson {lesson_num - 1}</a>'
    else:
        nav_prev = f'<a href="../index.html"><span class="nav-label">Back to</span>Course Overview</a>'

    if lesson_num < total_lessons:
        nav_next = f'<a href="lesson-{lesson_num + 1}.html"><span class="nav-label">Next</span>Lesson {lesson_num + 1}</a>'
    elif module_num < 3:
        nav_next = f'<a href="../module-{module_num + 1}/lesson-1.html"><span class="nav-label">Next Module</span>Module {module_num + 1}</a>'
    else:
        nav_next = f'<a href="../deliverables.html"><span class="nav-label">Next</span>Deliverables</a>'

    return TEMPLATE.format(
        title=lesson['title'],
        module_label=f'Module {module_num} &middot; {module_title}',
        lesson_title=lesson['title'],
        meta=meta if meta else f'Lesson {lesson_num} of {total_lessons}',
        content=html_content,
        nav_prev=nav_prev,
        nav_next=nav_next
    )


def process_module(compiled_file, module_num, module_title, output_dir):
    """Process a compiled markdown file into individual lesson HTML pages."""
    with open(compiled_file, 'r') as f:
        content = f.read()

    # Remove the attunement frame section (it goes in lesson 1 intro or module overview)
    # Keep it but note it

    lessons = split_lessons(content, module_num)

    os.makedirs(output_dir, exist_ok=True)

    for lesson in lessons:
        html = build_lesson_page(lesson, module_num, len(lessons), module_title)
        filename = f"lesson-{lesson['num']}.html"
        filepath = os.path.join(output_dir, filename)
        with open(filepath, 'w') as f:
            f.write(html)
        print(f"  Created {filepath} ({len(lesson['body'].split())} words)")

    return len(lessons)


if __name__ == '__main__':
    base = '/home/peter/homelab/projects/active/joinery-site'
    course_dir = os.path.join(base, 'course', 'foundations')

    modules = [
        {
            'file': os.path.join(base, 'course', 'week1-compiled.md'),
            'num': 1,
            'title': 'Task Decomposition',
            'output': os.path.join(course_dir, 'module-1')
        },
        {
            'file': os.path.join(base, 'course', 'week2-compiled.md'),
            'num': 2,
            'title': 'Input Inversion',
            'output': os.path.join(course_dir, 'module-2')
        },
        {
            'file': os.path.join(base, 'course', 'week3-compiled.md'),
            'num': 3,
            'title': 'Voice Governance',
            'output': os.path.join(course_dir, 'module-3')
        }
    ]

    for mod in modules:
        print(f"\nProcessing Module {mod['num']}: {mod['title']}")
        count = process_module(mod['file'], mod['num'], mod['title'], mod['output'])
        print(f"  {count} lessons created")

    print("\nDone. Review generated files and adjust as needed.")
