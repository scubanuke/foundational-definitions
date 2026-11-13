# The Foundational Definitions

A walk through the Foundational Definitions of *Design Basis for AI Governance in Critical Infrastructure* (Eclectic Technologies): what each instrument says, why it matters, and its formal statement, term by term. Sibling of the [Design Basis for AI Governance](https://scubanuke.github.io/ai-governance-course/) course.

**Built on:** *FD — Foundational Definitions, November 2026 Edition*, version DOI [10.5281/zenodo.23401272](https://doi.org/10.5281/zenodo.23401272), concept DOI [10.5281/zenodo.22181028](https://doi.org/10.5281/zenodo.22181028). Where this site and an instrument differ, the instrument governs.

**Owner:** Project 0 (Cross-Project Alignment), which holds the Foundational Definitions. The definitions are Project 0's, except *Local Sovereignty*, which is Project 5's construct mastered in Project 0.

**Posted for Comment.** Every formal statement on the site is a reading under review, until a mathematician has checked it. It comes from the working paper *The Mathematics Under the Foundational Definitions* v0.2, with drafts marked NEW for changes the November 2026 Edition made after that paper.

## Structure

`index.html` is the shell. It loads Markdown pages from `pages/`, typesets math with KaTeX 0.16.11 and renders Markdown with marked 12.0.2, both pinned on jsDelivr. Math is lifted out before Markdown runs, so `$…$` and `$$…$$` reach KaTeX intact.

The pages are: `pages/home.md` (the One Principle and the stack diagram); `pages/how-to-read.md`; `pages/instruments/` (one page for each of the eight instruments); `pages/sectors.md` (one worked example for each of the sixteen sectors); and `pages/cite.md`.

The pages must be served over http. Opening `index.html` from disk will not load them. To preview locally, run `python -m http.server` in this folder and open `http://localhost:8000`.

## Versions

- **v0.1, 16 October 2026.** First build. Not published until the November 2026 Edition is deposited on 19 October 2026.
