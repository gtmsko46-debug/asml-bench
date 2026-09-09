# Corpus Index (curated bibliography)

Pointers and *why* — **not** pirated PDFs. Prefer DOI / publisher / arXiv / open datasets.

## §5-style curated set

| Ref | Link | Why it matters for litho-lab |
|-----|------|------------------------------|
| LithoBench | https://github.com/ScopeObject/LithoBench (search: LithoBench ICCAD) | Open ML lithography benchmark patterns; license-aware baselines for P1 twin work |
| LithoSim / open litho simulators | https://github.com (search LithoSim lithography) | Synthetic aerial-image / resist proxies without fab data |
| OpenLithoHub | community hub pointers (see `datasets/README.md`) | Aggregates open lithography datasets & licenses |
| Bakshi — EUV Source Technology | SPIE / books.spie.org (ISBN search: EUV Sources for Lithography) | LPP physics context for `lpp-source-v1` (cite, do not dump chapters) |
| Levinson — Principles of Lithography | SPIE Press | Imaging / overlay fundamentals for TH-04 thermal overlay toys |
| Mack — Fundamental Principles of Optical Lithography | Wiley | Coherence, pupil, partial coherence for FEL-02 |
| Naulleau et al. EUV stochastics literature | doi.org / Optics Express search "EUV stochastic" | Resist stochastics proxies (`stochastics-resist-v1`) |
| ASML public annual reports / Investor Day decks | asml.com/investors | **Public** TCO / throughput narratives only — never internal specs |
| SEMI standards (public abstracts) | semi.org | Overlay / metrology vocabulary |
| arXiv: computational lithography surveys | arxiv.org | Inverse lithography / ML OPC survey pointers |

## Usage rules

1. Store notes under `corpus/notes/` (markdown summaries you write).
2. `corpus/papers/` is for **open-access** PDFs or bibtex only — no paywalled dumps.
3. Always record license before copying any dataset into `corpus/datasets/`.
