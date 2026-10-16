# Appendix D — Theorem and Proof Index

Every theorem/lemma/equation discussed, with original location. "Cited via" marks items located through secondary audit tables rather than direct re-reading; the primary file:line is still given as reported.

## Closure program (R-series)

- R29 (least closure system) — `interphase_a_notebook.md:733` (cited via); ledger `foundation_v1.0.md:96,101`.
- R30 correction (closure-system hypothesis required) — `interphase_a_notebook.md:785` (cited via); `foundation_consolidation_001.md:55,136`.
- R31 collapse (I_f = C_f = cl_f) — `interphase_a_notebook.md:831,925–929` (cited via); `foundation_v1.0.md:102`.
- R35 falsification (witnesses f1={0↦1,1↦0,2↦1} vs f2={0↦1,1↦0,2↦0}, shared I_f={∅,{0,1},S}; second pair sharing {∅,{0,2},S}) — `phase033_r35_reconstruction_falsification.md:27–34,42–56,69–84,209–210`.
- R40 universality (Inv ⊣ inclusion; contravariant) — `interphase_a_notebook.md:1139–1155` (cited via); `phase033_r41_functor_audit.md:7,15`.
- R45 (R_C unique maximum; 13/29 non-minimal, 7 double minima at |S|=3) — `foundation_consolidation_001.md:223–235`; `foundation_v1.0.md:62`.
- R50 (R46.1 falsified; 7 cex; ∩-inclusion one-way) — `phase035_r50_foundation_freeze.md` (cited via); corroborated `paper3_submission.tex:482–488`.
- R51 (finite poset + unique max; not ∩/∪-closed, not convex, not lattice) — `foundation_v1.0.md:108–109`; `phase035_r51_repair_campaign.md` (cited via).

## Paper 3 (submission text `papers/paper3_kernel_geometry/final/paper3_submission.tex`)

- Abstract (verified :36–48): Φ: Rel(S)→ClSys(S); image = Alexandrov + ∅; unique max R_C; edge classes; finite poset; conjecture false; arbitrary sets/relations.
- Thm 3.1 canonical maximal representative; Thm 4.1 fiber geometry; Thm 5.1 edge classification (+ Lemma 5.1); Thm 6.1 falsification; Thm 8.1/8.2 generalization (statements per R64/R65 records; proofs in submission text §§3–8).
- Verification scope: |S|≤4 (29 @3, 355 @4; T0-refined 19/219 — R88).
- Internal audits: R64 (adversarial verification), R65 (literature attack; novelty sentence + folklore caveat).

## Paper 4 (`papers/paper4_fiber_complexity/paper_v3.tex` — verified)

- Abstract (:24): bijection P(S)×P(E); count 2^|S|+|E|.
- Thm (:46–52): φ(A,E′) = loops(A) ∪ T ∪ E′.
- Proof (:62–79): four paragraphs (verbatim structure in Ch. 10).
- Examples (:83–93): chain-3 → 16; chain-4 → 128; antichain → 2^n; V → 8.
- Remark (:95–97): exhaustive check |S|≤5 (1,3,19,219,4231), zero violations.

## Boundary results

- Path Lemma 3.3 (T0 boundary; holds T0, fails non-T0) — `phase058_r89_t0_boundary.md:21–24,40–44` (cited via).
- Non-T0 fiber = loops × SC-digraphs (10/10) — `:92–105` (cited via).
- C3 composition boundary (|S|=1 vs ≥2; alignment loss) — `COMPASS_I_BOUNDARY_RESULT.md:47–54,70–74` (cited via).

## Finite enumerations (equations reproduced in Ch. 7)

- Relation census: Σ_{n=0..4} 2^(n²) = 1+2+16+512+65536 = 66,067 (author-checked arithmetic; reconciles 66,066-nonempty convention).
- Exp24 tallies: 0/66,067 violations; 0/15 required; A=1/B=15/C=0/D=0; 8/8 formalisms; 10/10 killers; 29/29 engine (`SGP_RESPONSE_VS_RELATION_AUDIT_001.md:69,96,272,319,363,390,408,412` — verified).
- Exp25 tallies: 7×A; B=0; C=0; 0/7 selections; 8/8 kills (`SGP_PHYSICAL_DISTINCTION_AUDIT_001.md:440–475` — verified).
