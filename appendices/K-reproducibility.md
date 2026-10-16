# Appendix K — Reproducibility and Computational Record

Only materials that can be safely and legally described. No datasets or engines are copied into this book; paths let a reader with repository access re-run them. Nothing here is claimed reproducible beyond what the records state.

| Computation | Engine → output (source repo) | Reported result | Reproducibility note |
|---|---|---|---|
| Exp24 census | `experiments/interaction_rule_space/exp24_response_vs_relation_engine.py` → `exp24_response_vs_relation_result.json` | 29/29; 0/66,067 | Deterministic (seed 24; reruns byte-identical modulo runtime) |
| Exp25 audits | parts 01–28 in `SGP_PHYSICAL_DISTINCTION_AUDIT_001.md` | 7×A; boxes FAIL; kill 8/8 | Finite declared inventories; exact counts |
| C2 hierarchy | `c2_hierarchy_engine.py` → `c2_hierarchy_engine_result.{txt,json}` | 66,066 relations; 9 classes; 54 strict; 29 incomparable; 10 covers | Authoritative run DONE in 131.0s |
| Paper 3 checks | `papers/paper3_kernel_geometry/computations/` | |S|≤4; 0 violations | Scope stated in submission text |
| Paper 4 checks | remark in `paper_v3.tex:95–97` | |S|≤5 (1,3,19,219,4231); 0 violations | Programs in `mtraver/sgp_core_v2` (per remark) |
| R88/R89 | brute force n=3,4 T0 vs non-T0 | 10 non-T0 violations; 0/219 T0 | Scope stated in phase records |
| Frozen controls | md5 baselines in Exp24 §1 (26 files) | Unchanged after write | Integrity mechanism, not science |

Software environments are not pinned in the records consulted; reruns may differ cosmetically (e.g. runtime fields). The book's mathematical claims rest on proofs and stated scopes, not on re-execution.
