// Course protection and watermarking

(function() {
    // Read student identifier from URL parameter
    const params = new URLSearchParams(window.location.search);
    const student = params.get('s') || 'Preview Mode';

    // Inject watermark
    const watermark = document.createElement('div');
    watermark.className = 'watermark';
    watermark.textContent = 'Licensed to: ' + student;
    document.body.appendChild(watermark);

    // Inject diagonal watermark
    const diag = document.createElement('div');
    diag.className = 'watermark-diagonal';
    diag.textContent = student;
    document.body.appendChild(diag);

    // Disable right-click on lesson content
    document.addEventListener('contextmenu', function(e) {
        if (e.target.closest('.lesson-content')) {
            e.preventDefault();
        }
    });

    // Disable copy on lesson content (allow on exercise blocks)
    document.addEventListener('copy', function(e) {
        if (e.target.closest('.lesson-content') && !e.target.closest('.exercise-block')) {
            e.preventDefault();
        }
    });

    // Disable keyboard shortcuts for copy on lesson content
    document.addEventListener('keydown', function(e) {
        if ((e.ctrlKey || e.metaKey) && e.key === 'c') {
            const sel = window.getSelection();
            if (sel.anchorNode && sel.anchorNode.parentElement) {
                const parent = sel.anchorNode.parentElement.closest('.lesson-content');
                const exercise = sel.anchorNode.parentElement.closest('.exercise-block');
                if (parent && !exercise) {
                    e.preventDefault();
                }
            }
        }
    });

    // Propagate student parameter to all internal links
    document.querySelectorAll('a[href]').forEach(function(link) {
        const href = link.getAttribute('href');
        if (href && !href.startsWith('http') && !href.startsWith('#')) {
            const url = new URL(href, window.location.href);
            if (student !== 'Preview Mode') {
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
})();
