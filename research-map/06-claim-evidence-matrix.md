# Research Map 06 — Claim-Evidence Matrix

Labels per Appendix M: [Established] [Math-verified] [Finite-check] [SGP-commitment] [SGP-interpretation] [SGP-hypothesis] [Author-inference] [Negative] [Unresolved]. "Book use" = where the claim may appear and with what label.

## Physics claims (Part III)

| # | Claim | Label | Evidence | Book use |
|---|---|---|---|---|
| P1 | Bell correlations violate local-hidden-variable inequalities; loophole-free violations observed (Hensen 2015: S=2.42±0.20) | [Established] | Bell 1964; CHSH 1969; Aspect 1982; Hensen 2015 (bibliography) | Ch. 15 as background |
| P2 | No controllable superluminal signaling via entanglement (no-signaling) | [Established] | Standard QM (textbooks, bibliography) | Ch. 15 as background |
| P3 | "Nonlocality" means different things in different QM interpretations | [Established] | Literature controls (bibliography) | Ch. 15 as background |
| P4 | SGP relational reading of entanglement adds no constraint (beyond_standard_adds=[]) | [Negative] | Exp25 :139–141; Bridge Q1 :134 | Ch. 15 as SGP-interpretation verdict |
| P5 | BEC: macroscopic occupation of one quantum state (Rb-87, ~170 nK, Anderson 1995; Na, Davis 1995) | [Established] | Anderson 1995; Davis 1995; Bose 1924; Einstein 1925 (bibliography) | Ch. 16 as background |
| P6 | BEC ≠ loss of all distinctions; condensate is symmetric, not Bell-like; RELATED but DISTINCT from entanglement | [Established] + [Negative] | Textbooks; `sgp_physics_cases_01.py:271–276` (Institute's own distinction) | Ch. 16 |
| P7 | BEC never graduated to bridge audit; Type 1 / ANALOGY only | [Negative] | cases :391–397; sections09_10 :75–95; Exp25 domain list | Ch. 16 |
| P8 | All electrons identical species properties; all protons identical species properties; electron ≠ proton (mass, charge, spin class, structure) | [Established] | PDG; Griffiths Ch. 5; Pauli 1940 (bibliography) | Ch. 17 as background |
| P9 | "ONE Fock state → N particles" is standard symmetrization, not an SGP discovery | [Established] + [Negative] | Textbooks; `sgp_physics_cases_01.py:43,226` | Ch. 17 |
| P10 | NO record of an electron=proton identity claim or "same particle" doctrine; "equation-idea" searches return only the ONE-EQUATION formalism hypothesis | [Negative] (search result) | Repo-wide searches (map 07 notes) | Ch. 17 — report the negative search honestly |
| P11 | Road-D pools (Λ, DM, strong CP, ν-ordering) all fail gates; I(T;S)=0 | [Negative] | ROAD_D §§4–5; INFORMATION_ANCESTRY_REAUDIT :113 | Ch. 18 (table only for documented ones) |

## Mathematics claims (Part II)

| # | Claim | Label | Evidence | Book use |
|---|---|---|---|---|
| M1 | response(R)⟺R≠∅ over 66,067; 0/15 required; kill 8/8 | [Finite-check] + [Negative] | Exp24 (verified lines) | Ch. 7 |
| M2 | Orientation forced; reciprocity/asymmetry optional | [Math-verified] (audit reasoning) | Minimal-response audit | Ch. 8 |
| M3 | R31 collapse; R40 universality (contravariant) | [Math-verified] | Notebooks; foundation ledger | Ch. 9 |
| M4 | R35 reconstruction FALSE (witness pairs) | [Negative] (counterexample) | phase033_r35 :27–34 | Ch. 9 |
| M5 | R_C unique maximum (R45 correction); fibers finite posets (R51) | [Math-verified] + [Finite-check] | foundation ledger; Paper 3 | Ch. 9 |
| M6 | Paper 3 theorems (3.1/4.1/5.1/6.1/8.1–8.2) as manuscript claims | [Math-verified]-as-manuscript + [Finite-check] | submission text; R64/R65 internal | Ch. 9 with peer-review caveat |
| M7 | Paper 4 bijection + count 2^\|S\|+\|E\|; checked \|S\|≤5 | [Math-verified]-as-manuscript + [Finite-check] | paper_v3 (verified) | Ch. 10 with peer-review caveat |
| M8 | T0 essential; non-T0 fiber = loops × SC-digraphs | [Math-verified] + [Finite-check] | R88/R89 | Ch. 11 |
| M9 | C3 boundary: joint determines composition; separate does not (\|S\|≥2) | [Math-verified] | Boundary files | Ch. 11 (standard math; no novelty) |
| M10 | No qualifying interaction question; selector UNRESOLVED; viability NOT VALIDATED | [Negative] + [Unresolved] | Compass I; selector :83; viability :40–52 | Ch. 12 |
| M11 | Stage-1: C1–C4 exclude nothing; Exp25 boxes FAIL; Road D 0/6 | [Negative] | Stage1; Exp25 (verified); Road D | Ch. 13 |

## Framework claims (Parts I, IV)

| # | Claim | Label | Evidence | Book use |
|---|---|---|---|---|
| F1 | C1–C5 package (RD-001 wording) | [SGP-commitment] | RD-001:345–349 (verified) | Ch. 1–6 |
| F2 | Sentience wording discrepancy (feel vs respond) | [SGP-commitment] + provenance fact | GOVERNANCE:19 vs RD-001:345 (verified) | Ch. 2; App. B |
| F3 | Package coherent but not distinctive | RD-002 decision (report as decision, not theorem) | RD-002:28 | Ch. 20 |
| F4 | Generality chain broken 4/6; concepts familiar | RD-003 decision (report as decision) | RD-003 | Ch. 12/20 |
| F5 | Framework retained; explanatory claims suspended; program closed | RD-004 decision (report as decision) | RD-004:28–30,375 | Ch. 20–21 |
| F6 | Informational equivalence I(T;S)=0 | Frozen audit result (report scope) | INFORMATIONAL_STATUS :201,207–211 | Ch. 20 |
| F7 | Resume conditions (new primitive / empirical prediction / combination solution) | RD-004 §10 (report as stated conditions) | RD-004 | Ch. 21; App. L |

## Author inferences (flagged in text as such)

- I1: 66,067 = 66,066 + empty carrier (arithmetic reconciliation; Ch. 7). [Author-inference], checkable.
- I2: Poset paper is "a genuine new rung" (specialization filling cardinality gap) vs "within preceding rung" — book judges: new rung in ladder narrative because it answers a question the general theory left open (count). [Author-inference].
- I3: Chapter transitions ("why this question next") are narrative reconstructions from record order, not claims the Institute planned the ladder in advance. [Author-inference], stated in Ch. 7 intro and App. C.
