// Beta access check — redirect to gate if not authenticated
(function() {
    var AUTH_KEY = 'joinery-beta-access';
    try {
        if (sessionStorage.getItem(AUTH_KEY) !== 'true') {
            window.location.replace('../index.html');
            return;
        }
    } catch(e) {
        window.location.replace('../index.html');
        return;
    }
})();

// Course protection and watermarking

(function() {
    const params = new URLSearchParams(window.location.search);
    const student = params.get('s') || 'Beta Reader';

    // Inject watermark
    const watermark = document.createElement('div');
    watermark.className = 'watermark';
    watermark.textContent = 'Beta review copy — ' + student;
    document.body.appendChild(watermark);

    const diag = document.createElement('div');
    diag.className = 'watermark-diagonal';
    diag.textContent = student;
    document.body.appendChild(diag);

    // Disable right-click on lesson content
    document.addEventListener('contextmenu', function(e) {
        if (e.target.closest('.lesson-content')) e.preventDefault();
    });

    // Disable copy on lesson content (allow on exercise blocks)
    document.addEventListener('copy', function(e) {
        if (e.target.closest('.lesson-content') && !e.target.closest('.exercise-block')) e.preventDefault();
    });

    // Disable keyboard shortcuts for copy on lesson content
    document.addEventListener('keydown', function(e) {
        if ((e.ctrlKey || e.metaKey) && e.key === 'c') {
            const sel = window.getSelection();
            if (sel.anchorNode && sel.anchorNode.parentElement) {
                const parent = sel.anchorNode.parentElement.closest('.lesson-content');
                const exercise = sel.anchorNode.parentElement.closest('.exercise-block');
                if (parent && !exercise) e.preventDefault();
            }
        }
    });

    // Course map — Module 1 only for beta
    var COURSE = [
        {
            label: 'Module 1 \u00b7 Task Decomposition',
            lessons: [
                { path: 'module-1/lesson-1.html', title: '1.1 The Frame Break' },
                { path: 'module-1/lesson-2.html', title: '1.2 The Compound Instruction Problem' },
                { path: 'module-1/lesson-3.html', title: '1.3 The Decomposition' },
                { path: 'module-1/lesson-4.html', title: '1.4 The Synthesis Step' },
                { path: 'module-1/lesson-5.html', title: '1.5 Decompose Your Own Work' },
                { path: 'module-1/lesson-6.html', title: '1.6 Week 1 Deliverable' }
            ]
        }
    ];

    // Build sidebar on lesson pages only
    var coursePage = document.querySelector('.course-page');
    var isLessonPage = window.location.pathname.match(/\/module-\d+\/lesson-\d+\.html/);

    if (coursePage && isLessonPage) {
        // Detect current lesson from URL
        var pathParts = window.location.pathname.split('/').filter(Boolean);
        var currentKey = pathParts.slice(-2).join('/');

        // Track visited lessons
        var VISITED_KEY = 'joinery-beta-visited';
        var visited = [];
        try {
            var raw = localStorage.getItem(VISITED_KEY);
            if (raw) visited = JSON.parse(raw);
            if (!Array.isArray(visited)) visited = [];
        } catch(e) { visited = []; }
        if (currentKey && visited.indexOf(currentKey) === -1) {
            visited.push(currentKey);
            try { localStorage.setItem(VISITED_KEY, JSON.stringify(visited)); } catch(e) {}
        }

        // Wrap course-page in layout container
        var layout = document.createElement('div');
        layout.className = 'course-layout';
        coursePage.parentNode.insertBefore(layout, coursePage);
        layout.appendChild(coursePage);

        // Build sidebar
        var sidebar = document.createElement('nav');
        sidebar.className = 'course-sidebar';
        sidebar.id = 'course-sidebar';
        sidebar.setAttribute('aria-label', 'Course contents');

        // Course index link
        var indexLink = document.createElement('a');
        indexLink.href = '../index.html';
        indexLink.className = 'sidebar-index';
        indexLink.textContent = 'Foundations Beta';
        sidebar.appendChild(indexLink);

        // Module sections
        COURSE.forEach(function(module) {
            var section = document.createElement('div');
            section.className = 'sidebar-module';

            var moduleLabel = document.createElement('div');
            moduleLabel.className = 'sidebar-module-label';
            moduleLabel.textContent = module.label;
            section.appendChild(moduleLabel);

            var ul = document.createElement('ul');
            ul.className = 'sidebar-lessons';

            module.lessons.forEach(function(lesson) {
                var li = document.createElement('li');
                var a = document.createElement('a');
                a.href = '../' + lesson.path;
                a.textContent = lesson.title;
                var classes = [];
                if (currentKey && lesson.path.endsWith(currentKey)) {
                    classes.push('current');
                    li.setAttribute('aria-current', 'page');
                }
                if (visited.indexOf(lesson.path) !== -1) {
                    classes.push('visited');
                }
                if (classes.length) li.className = classes.join(' ');
                li.appendChild(a);
                ul.appendChild(li);
            });

            section.appendChild(ul);
            sidebar.appendChild(section);
        });

        // Reset progress link
        var resetLink = document.createElement('button');
        resetLink.type = 'button';
        resetLink.className = 'sidebar-reset';
        resetLink.textContent = 'Reset progress';
        resetLink.addEventListener('click', function() {
            if (!confirm('Clear your visited lessons? Your persona selection stays.')) return;
            try { localStorage.removeItem(VISITED_KEY); } catch(e) {}
            sidebar.querySelectorAll('.sidebar-lessons li.visited').forEach(function(li) {
                li.classList.remove('visited');
            });
            var here = sidebar.querySelector('.sidebar-lessons li.current');
            if (here) here.classList.add('visited');
            try {
                localStorage.setItem(VISITED_KEY, JSON.stringify(currentKey ? [currentKey] : []));
            } catch(e) {}
        });
        sidebar.appendChild(resetLink);

        layout.insertBefore(sidebar, coursePage);

        // Mobile toggle button
        var toggle = document.createElement('button');
        toggle.className = 'sidebar-toggle';
        toggle.setAttribute('aria-label', 'Open course contents');
        toggle.innerHTML = '<span>Contents</span>';
        coursePage.insertBefore(toggle, coursePage.firstChild);

        // Overlay
        var overlay = document.createElement('div');
        overlay.className = 'sidebar-overlay';
        overlay.setAttribute('aria-hidden', 'true');
        document.body.appendChild(overlay);

        function openSidebar() {
            sidebar.classList.add('open');
            overlay.classList.add('open');
            toggle.setAttribute('aria-label', 'Close course contents');
        }
        function closeSidebar() {
            sidebar.classList.remove('open');
            overlay.classList.remove('open');
            toggle.setAttribute('aria-label', 'Open course contents');
        }

        toggle.addEventListener('click', function() {
            sidebar.classList.contains('open') ? closeSidebar() : openSidebar();
        });
        overlay.addEventListener('click', closeSidebar);
    }

    // Propagate student parameter to all internal links
    document.querySelectorAll('a[href]').forEach(function(link) {
        const href = link.getAttribute('href');
        if (href && !href.startsWith('http') && !href.startsWith('#')) {
            const url = new URL(href, window.location.href);
            if (student !== 'Beta Reader') {
                url.searchParams.set('s', student);
            }
            link.setAttribute('href', url.pathname + url.search);
        }
    });

    // Nav scroll behavior
    const nav = document.getElementById('nav');
    if (nav) {
        window.addEventListener('scroll', function() {
            nav.classList.toggle('scrolled', window.scrollY > 20);
        });
    }

    // Persona selector on index page
    var personaSelector = document.getElementById('persona-selector');
    if (personaSelector) {
        var savedPersona;
        try { savedPersona = localStorage.getItem('joinery-persona'); } catch(e) {}
        personaSelector.querySelectorAll('.persona-btn').forEach(function(btn) {
            if (savedPersona && btn.dataset.domain === savedPersona) btn.classList.add('selected');
            btn.addEventListener('click', function() {
                personaSelector.querySelectorAll('.persona-btn').forEach(function(b) {
                    b.classList.remove('selected');
                });
                btn.classList.add('selected');
                try { localStorage.setItem('joinery-persona', btn.dataset.domain); } catch(e) {}
            });
        });
    }
})();

// Persona tabs
(function() {
    var STORAGE_KEY = 'joinery-persona';
    var DEFAULT_DOMAIN = 'brand-designer';

    function getPersona() {
        try {
            return localStorage.getItem(STORAGE_KEY) || DEFAULT_DOMAIN;
        } catch (e) {
            return DEFAULT_DOMAIN;
        }
    }

    function setPersona(domain) {
        try {
            localStorage.setItem(STORAGE_KEY, domain);
        } catch (e) {}
        applyPersona(domain);
    }

    function applyPersona(domain) {
        document.querySelectorAll('.domain-tabs').forEach(function(block) {
            block.querySelectorAll('.tab-btn').forEach(function(btn) {
                btn.classList.toggle('active', btn.dataset.domain === domain);
                btn.setAttribute('aria-selected', btn.dataset.domain === domain ? 'true' : 'false');
            });
            block.querySelectorAll('.tab-panel').forEach(function(panel) {
                panel.classList.toggle('active', panel.dataset.domain === domain);
                if (panel.dataset.domain === domain) {
                    panel.removeAttribute('hidden');
                } else {
                    panel.setAttribute('hidden', '');
                }
            });
        });
        document.querySelectorAll('.sidebar-persona-btn').forEach(function(btn) {
            btn.classList.toggle('active', btn.dataset.domain === domain);
        });
    }

    window.joinerySetPersona = setPersona;

    function initTabs() {
        applyPersona(getPersona());
        var tabBlocks = document.querySelectorAll('.domain-tabs');
        tabBlocks.forEach(function(block) {
            block.querySelectorAll('.tab-btn').forEach(function(btn) {
                btn.addEventListener('click', function() {
                    if (btn.dataset.domain) setPersona(btn.dataset.domain);
                });
            });
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initTabs);
    } else {
        initTabs();
    }
})();

// Sidebar persona indicator
(function() {
    var PERSONAS = [
        { key: 'brand-designer', label: 'Brand Designer' },
        { key: 'copywriter', label: 'Copywriter' },
        { key: 'fiction-writer', label: 'Fiction Writer' },
        { key: 'nonfiction-writer', label: 'Nonfiction Writer' }
    ];

    function build() {
        var sidebar = document.getElementById('course-sidebar');
        if (!sidebar) return;
        if (sidebar.querySelector('.sidebar-persona')) return;

        var indicator = document.createElement('div');
        indicator.className = 'sidebar-persona';

        var label = document.createElement('div');
        label.className = 'sidebar-persona-label';
        label.textContent = 'Viewing as';
        indicator.appendChild(label);

        var options = document.createElement('div');
        options.className = 'sidebar-persona-options';

        PERSONAS.forEach(function(p) {
            var btn = document.createElement('button');
            btn.className = 'sidebar-persona-btn';
            btn.dataset.domain = p.key;
            btn.textContent = p.label;
            btn.addEventListener('click', function() {
                if (window.joinerySetPersona) {
                    window.joinerySetPersona(p.key);
                } else {
                    try { localStorage.setItem('joinery-persona', p.key); } catch(e) {}
                    options.querySelectorAll('.sidebar-persona-btn').forEach(function(b) {
                        b.classList.toggle('active', b.dataset.domain === p.key);
                    });
                }
            });
            options.appendChild(btn);
        });

        indicator.appendChild(options);

        var indexLink = sidebar.querySelector('.sidebar-index');
        if (indexLink && indexLink.nextSibling) {
            sidebar.insertBefore(indicator, indexLink.nextSibling);
        } else {
            sidebar.appendChild(indicator);
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', build);
    } else {
        build();
    }
})();
