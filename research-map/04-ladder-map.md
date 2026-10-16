# Research Map 04 — Mathematical Ladder Map

One row per rung. "Book chapter" gives the destination. Full citations live in Appendix D.

## Rung 1 — Response vs relation → Chapter 7

- Question: does "response" carry formal content beyond an oriented relation?
- Method: exhaustive enumeration of all relations on sets of size ≤ 4: counts 2^(n²) give 1 + 2 + 16 + 512 + 65536 = **66,067** records (n = 0..4; 66,066 excluding the empty carrier), plus 8 formalisms, 10 killers, 15 candidate properties, 7 literature controls.
- Result: response(R) ⟺ R≠∅, **0 violations in 66,067**; required count **0/15**; four-way A=1/B=15/C=0/D=0; kill fires **8/8**; engine 29/29 green.
- Establishes: boundary result — the word is load-bearing for interpretation, zero formal payload above arbitrary oriented relation.
- Does not: refute the stipulation; claim SGP false.
- Status: established / negative. Source: `SGP_RESPONSE_VS_RELATION_AUDIT_001.md:59–63,69,96,272,319,363,390,408,412` (directly verified).

## Rung 2 — Orientation and relational structure → Chapter 8

- Question: does SGP force asymmetry/reciprocity/selfhood, or only orientation?
- Result: orientation FORCED (ordered pairs); reciprocity OPTIONAL; asymmetry OPTIONAL; readings B/C/D all COMPATIBLE; SGP does not distinguish them.
- Establishes: source/target roles as first unavoidable content; direction ≠ asymmetry; roles are tuple slots, not objects.
- Does not: establish influence, causation, information.
- Status: established. Source: `relational_information_geometry_audit/SGP_MINIMAL_RESPONSE_MATHEMATICS_09.md:20–22,39–46,51–56,93–98,104`.

## Rung 3 — Relations and closure (R19–R47) → Chapter 9

- R29: F_f least closure system consistent with f. R30: minimality proof corrected (closure-system hypothesis required). R31: I_f = C_f = cl_f collapse (special case of known order theorem).
- R35: reconstruction claim (I_f ⇒ f up to conjugacy) FALSE at |S|=3 (2 counterexamples; e.g. f1={0↦1,1↦0,2↦1} vs f2={0↦1,1↦0,2↦0} sharing I_f={∅,{0,1},S}) and |S|=4 (26). Root cause: minimal invariant sets are cycles, not singletons.
- R40: Inv(R) universal — left adjoint to inclusion; functor contravariant (corrected).
- R44–R46 / R45: R_C formula gives unique MAXIMUM (not minimum) of {R : Inv(R)=C}; at |S|=3, 13/29 non-minimal, 7 with two minima.
- R50: R46.1 ("fibers are convex sublattices") FALSE — 7 counterexamples at |S|=3; Inv(R1∩R2) ⊇ Inv(R1)∩Inv(R2), reverse fails.
- R51: repair — fiber is a finite poset with unique maximum; not closed under ∩/∪, not convex, not a lattice.
- Status: established / conditional / negative / frozen. Sources: `interphase_a_notebook.md`, `interphase_b_notebook.md`, `phase033_r35_reconstruction_falsification.md:27–34,42–56,69–84`, `foundation_v1.0.md`, `foundation_consolidation_001.md`, `phase035_r50_foundation_freeze.md`, `phase035_r51_repair_campaign.md`.

## Rung 4 — Paper 3, Fibers of the Relation-to-Closure Correspondence → Chapter 9

- Manuscript: `papers/paper3_kernel_geometry/final/paper3_submission.tex` (top-level `paper.tex` does not exist in this tree). Author: Mark Rowe Traver, SFI Research Association.
- Abstract (verified): Φ: Rel(S) → ClSys(S); image = Alexandrov topologies containing ∅; every fiber has unique maximum R_C; edges essential/conditionally-removable; fiber = finite poset with unique max; convex-sublattice conjecture false; holds for arbitrary sets/relations.
- Theorems (per R64/R65 records; statements as in submission text): Thm 3.1 canonical maximal representative; Thm 4.1 fiber geometry; Thm 5.1 edge classification (+ Lemma 5.1); Thm 6.1 falsification; Thm 8.1/8.2 generalization.
- Verification scope: exhaustive at |S|≤4 (29 closure systems at n=3, 355 at n=4 — later corrected to T0 counts 19/219/4231, R88).
- Audits: R64 adversarial verification; R65 literature attack; novelty wording: "The internal order structure of the fibers … has not previously been investigated" (with elementary/folklore caveat).
- RC1: all checklist items complete; PDF compiled (11 pp.).
- Book stance: report as manuscript claims with stated scope + internal audits; independent (peer-review) verification remains. Do NOT declare correct/novel/publishable.
- Status: proof + finite computational check; publication logistics (not research) remaining.

## Rung 5 — Paper 4, Finite Poset Lower-Set Closure → Chapter 10

- Manuscript: `papers/paper4_fiber_complexity/paper_v3.tex` (FOUND; identical copy in `submission_package/`).
- Claim (verified abstract :24 + Thm :46–52): for finite poset (S,≤), fiber F = {R : cl_R = cl} is in canonical bijection φ: P(S)×P(E) → F, φ(A,E′) = self-loops on A ∪ T ∪ E′, where T = transitive reduction (covering pairs), E = R_≤ ∖ T (non-covering comparable pairs). Cardinality 2^|S|+|E|.
- Proof (verified :62–79): four paragraphs (self-loop independence; inducing ⊆ R_≤; subsets of E preserve closure via covering chains; inducing ⊇ T since covering edges admit no intermediate vertex).
- Examples (verified :83–93): chain n=3 → |F|=16; n=4 → 128; antichain → 2^n; V-poset {a<c,b<c} → 8.
- Computational scope (verified remark :95–97): all finite partial orders on |S|≤5 (1, 3, 19, 219, 4231 — labeled-poset counts), zero violations.
- Note: v3 abstract corrects v2 ("covering" → non-covering comparable pairs). Posets are antisymmetric ⇒ T0 implicit. Genuine specialization of rung 4 (fills the cardinality gap the general theory left open).
- Status: proof + finite computational check.

## Rung 6 — T0, representation, C3 boundary → Chapter 11

- R88: Counterexamples to F_C ≅ P(S)×P(E) at n=3 are ALL non-T0 (10 violations); 0 violations among 219 T0 at n=4; T0 added to abstract + theorems.
- R89: T0 minimal — first failure at Lemma 3.3 (Path Lemma); non-T0 fiber = self-loops × strongly-connected digraphs (verified 10/10); no natural generalization.
- C3 boundary: joint classification determines composition; separate isomorphism classes do not (for |S|≥2; boundary at |S|=1); lost information = shared-carrier alignment. Standard equivariance mathematics; no SGP-specific structure; does not move I%.
- Status: established (T0 case proved; non-T0 falsified). Sources: `phase057_r88_adversarial_validation.md`, `phase058_r89_t0_boundary.md`, `COMPASS_I_BOUNDARY_RESULT.md:47–54,70–74`, `INTERACTION_MATHEMATICS_C3_GENERALITY_TEST.md:40–84`, `INTERACTION_MATHEMATICS_C3_RECONSTRUCTION.md:140–168`.

## Rung 7 — Interaction, composition, selection → Chapter 12

- Compass I audit: NO QUALIFYING MATHEMATICAL QUESTION FOUND; P1–P10 all negative/standard; stop conditions S1/S2/S5 fire; 19/19 SPLIT is ordinary composition corollary.
- Exp20: amplification WITHOUT selection (x0=0 stays 0; :122, :510).
- Exp21: actualization WITHOUT selection is generic mathematics (differentiator + instability; :174, :439–445). Actualization = ∃, not ∃!.
- Exp19: plurality is generic mathematics; zero SGP residue (:327, :544).
- Selector: UNRESOLVED (selector audit :83). Viability (C+S+F): NOT VALIDATED, 7/7 kill tests UNRESOLVED (:40–52). DSC-1 composition generic (SAO-1).
- Status: negative / unresolved. Sources: `COMPASS_I_INTERACTION_MATHEMATICS_BOUNDARY_AUDIT.md:32–38,260–269,318–326,460` (+ Compass I boundary files).

## Rung 8 — Physical bridges → Chapter 13

- Stage 1: C1–C4 define no admissibility predicate beyond ordinary relational algebra; "PRIOR RESULTS ALREADY SETTLE THE QUESTION" (:59–69, :193–200).
- Exp25: 7 domains × Level A only; B=0, C=0; 0 selections among 7 forks; both success boxes FAIL (:440–456); kill 8/8 → "SGP HAS NOT YET ACQUIRED EMPIRICAL CONTENT" (:458–475, directly verified).
- Road D: 0/6 pools advance; all fail D6 (arbitrary encoding / target-specific info required) (:21–23, :114–210, :223).
- Exp16: "NO PREDICTIVE BRIDGE FOUND" (`SGP_PHYSICS_BRIDGE_AUDIT_001.md:397`).
- Establishes: interpretive correspondence without selection (N2 reached; N3/N4 empty).
- Status: negative.

## Ladder synthesis (Chapter 14)

Genuine mathematical content: closure universality (R40), three-object collapse (R31), fiber poset geometry + R_C maximum (Paper 3), poset product decomposition + count (Paper 4), T0 boundary (R88/R89), C3 composition boundary. All belong to standard mathematics (order theory, Alexandrov topology, relation algebra); none is SGP-specific. The gap between philosophical ambition and derived consequence is the finding — not a failure to report, but the report.
