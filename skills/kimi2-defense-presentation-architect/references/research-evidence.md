# Research Evidence Baseline (As of February 7, 2026)

Use this file as the default evidence base. Refresh web verification when users ask for latest updates.

## 1) Kimi K2 Model Behavior

Source: [moonshotai/Kimi-K2-Thinking model card](https://huggingface.co/moonshotai/Kimi-K2-Thinking)

Observed evidence:
- Kimi K2 Thinking is described as a long-horizon thinking agent with tool orchestration.
- Model summary includes `Context Length 256K`, `Total Parameters 1T`, `Activated Parameters 32B`.
- Recommended temperature is explicitly `1.0` in usage examples.
- Tool calling flow requires passing tool schemas and iterative tool-call loop handling.

Design implications:
- Keep complete deck state in a single long context window.
- Use staged generation and explicit schemas to reduce drift on 30-slide outputs.
- Use structured tool loops for research retrieval when tools are available.

## 2) Multimedia Learning Evidence

Source: [Mayer research-based principles slides (2014)](https://www3.nd.edu/~twut/PDF/mayerslides.pdf)

Observed evidence:
- Coherence principle: excluding extraneous material improves learning (reported median effect size `0.86`, confirmed in `22/23` tests).
- Signaling principle: cues highlighting structure improve learning (reported median effect size `0.41`).
- Spatial contiguity: place text near related visuals (reported median effect size `1.10`).
- Temporal contiguity: align words/visuals in time (reported median effect size `1.22`).
- Segmenting: learner-paced chunks improve outcomes (reported median effect size `0.77`).

Design implications:
- Enforce concise on-slide text and remove decorative clutter.
- Use visible guidance cues (arrows, highlighted flow paths, numbered causal steps).
- Co-locate labels with visual components in prompt instructions.
- Break dense processes into progressive reveal segments.

Additional source: [A meta-analysis of how signaling affects learning with media (2018)](https://www.sciencedirect.com/science/article/pii/S1747938X17300581)

Observed evidence:
- 103 studies and 12,201 participants.
- Positive signaling effect on retention (`g+ = 0.53`) and transfer (`g+ = 0.33`).
- Reported reduction in cognitive load.

Design implications:
- Include explicit signaling in each concept slide (path markers, grouped labels, directional transitions).

Additional source: [Cromley & Chen 2025 meta-analysis](https://experts.illinois.edu/en/publications/a-meta-analysis-of-richard-mayers-multimedia-learning-research-se/)

Observed evidence:
- Overall effects remain positive (`g = 0.37`) with boundary conditions.
- Stronger effects for reducing seductive detail and for text+diagram combinations.

Design implications:
- Prefer text+diagram prompt composition over animation-heavy or ornament-heavy layouts.
- Treat novelty visuals as optional, not core.

## 3) Accessibility and Visual Legibility

Source: [W3C Understanding SC 1.4.3 Contrast (Minimum)](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum)

Observed evidence:
- Minimum text contrast: `4.5:1` for standard text.
- Large text may use `3:1`.

Design implications:
- Require dark text on light backgrounds for all instructional text.
- Validate palette pairs before finalizing color rules.
- Reserve low-contrast accents for decoration only, never body copy.

## 4) Defense AI Governance and Responsible Use

Source: [DoD adopts 5 AI ethics principles](https://www.defense.gov/News/Releases/Release/Article/2094085/dod-adopts-5-principles-of-artificial-intelligence-ethics/)

Observed evidence:
- Five principles: Responsible, Equitable, Traceable, Reliable, Governable.

Design implications:
- Add traceability, testing, bias mitigation, and deactivation/override context in major concept slides.
- Include defense application notes that emphasize oversight and bounded deployment.

Source: [NIST AI RMF 1.0 (2023)](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=936225)

Observed evidence:
- Voluntary practical framework with four core functions: `GOVERN`, `MAP`, `MEASURE`, `MANAGE`.
- Trustworthiness characteristics include valid/reliable, safe, secure/resilient, accountable/transparent, explainable/interpretable, privacy-enhanced, fairness with harmful bias managed.

Design implications:
- Map every major technical concept to a risk-management step.
- Require one explicit risk-control callout per concept slide.

Source: [NIST AI RMF Generative AI Profile (2024)](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=958388)

Observed evidence:
- Identifies risk areas including confabulation, CBRN-related misuse, information integrity, harmful bias, and content provenance.
- Recommends structured actions and measurement steps for these risks.

Design implications:
- Add dedicated "failure mode + mitigation" annotation in every concept slide.
- Include provenance, verification, and evaluation language in generative AI topics.

Source: [NATO revised AI strategy summary (2024)](https://www.nato.int/en/about-us/official-texts-and-resources/official-texts/2024/07/10/summary-of-natos-revised-artificial-intelligence-ai-strategy)

Observed evidence:
- Principles emphasize lawfulness, responsibility/accountability, explainability/traceability, reliability, governability, and bias mitigation.
- Strategy foregrounds interoperability, TEVV, and adversarial-risk awareness.

Design implications:
- Frame defense use cases with interoperability and TEVV cues.
- Avoid purely performance-centric narratives without governance context.

## 5) Consolidated Design Rules

Apply these non-negotiable rules:
- Prefer clarity over ornamental complexity.
- Use signaling and contiguity on all concept diagrams.
- Enforce accessibility contrast thresholds.
- Tie every major concept to defense governance and risk controls.
- Keep beginner comprehension explicit without diluting technical rigor.
