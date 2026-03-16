# Brainstorm Output

## Executive Summary

The current CatVTON asset is strong enough to support a first shortlist of business ideas, but the shortlist should bias toward merchant-side workflow tools rather than mass consumer promises. The repo demonstrates reusable try-on style preview generation with stable paired results and usable unpaired previews on simpler garments, which is enough to justify visual decision-support products. It does not yet justify a broad "perfect virtual fitting" claim.

The first-pass shortlist below keeps one B2C option for exploration, but the recommended direction is a B2B workflow product where qualitative preview quality already creates practical value.

## Candidate Shortlist

| Candidate ID | Idea | Buyer / ICP | Why it fits current repo | Main risk |
| --- | --- | --- | --- | --- |
| C1 | SMB fashion seller try-on preview copilot | Small apparel brands, Instagram shops, Shopify sellers | Lets merchants generate on-model garment previews for product page testing, ad concepting, and manual merchandising review without needing perfect fit simulation | Commercial buyers may still need cleaner visual quality than the current checkpoint delivers |
| C2 | Internal merchandising and catalog planning tool | Fashion brand e-commerce teams, merchandising managers, catalog studios | Current qualitative paired/unpaired previews are already useful for comparing garment-category alignment and visual consistency during planning | Harder to justify budget if workflow ROI is not quantified |
| C3 | Creative studio concept generator for campaign mockups | D2C brand creative teams, boutique agencies, performance marketing teams | The repo can already produce "demo-like" variant previews that are good enough for concept testing before a real shoot | Might be seen as adjacent to image generation tools unless workflow differentiation is clear |
| C4 | Consumer outfit preview app | Style-conscious online shoppers | Conceptually intuitive and large market, and the unpaired preview behavior points in this direction | Highest risk because current repo does not prove consumer-grade reliability, fit trust, or production serving quality |

## ICP Table

| Candidate ID | Core ICP | JTBD | Current alternative | Buying motion | Why now |
| --- | --- | --- | --- | --- | --- |
| C1 | Founder-led or lean e-commerce apparel seller with limited creative budget | "Help me preview garments on models quickly so I can test listings and creatives faster." | Manual Photoshop edits, costly model shoots, external design freelancers | Founder or small team self-serve with light sales assist | AI-assisted catalog creation is becoming normal, but lean sellers still lack affordable workflow tools |
| C2 | Mid-size fashion brand merchandising or e-commerce manager | "Help me review assortments and preview garment presentation before committing studio resources." | Spreadsheet planning, sample reviews, manual design mockups, reshoots | Sales-assisted or team pilot | Brands want to reduce sampling and visual iteration cost |
| C3 | Creative strategist or boutique agency serving apparel brands | "Help me mock campaign visuals before committing to a shoot or edit pipeline." | Moodboards, generic generative image tools, manual comps | Project-based, agency-led | Faster ad iteration is valuable even if outputs are still pre-production quality |
| C4 | Online fashion shopper buying tops, pants, or dresses | "Help me imagine how this garment could look on a person like me before I buy." | Product photos, size charts, reviews, existing VTO apps | Pure B2C self-serve | Very large opportunity, but trust threshold is high |

## Selection Criteria

| Criterion | Weight | Why it matters now |
| --- | --- | --- |
| Fit with verified repo capability | 30% | The first business item must not depend on capabilities the repo does not prove |
| Speed to validate with a pilot | 25% | A narrow pilot matters more than a broad story |
| Buyer willingness to pay | 20% | The selected direction should support a credible paid workflow |
| Differentiation from generic image tools | 15% | The offer needs a CatVTON-specific wedge |
| Operational simplicity for v1 | 10% | Lower integration and support burden improves execution odds |

## Scored Recommendation

| Candidate ID | Capability Fit | Pilot Speed | Willingness To Pay | Differentiation | Operational Simplicity | Weighted View |
| --- | --- | --- | --- | --- | --- | --- |
| C1 | High | High | Medium | Medium | High | Best initial wedge |
| C2 | High | Medium | Medium-High | Medium | Medium | Strong second option |
| C3 | Medium | High | Medium | Medium | High | Good adjacent experiment |
| C4 | Low-Medium | Medium | Unknown | Low-Medium | Low | Do not prioritize first |

## Recommendation

Recommend promoting `C1` as the primary candidate and `C2` as the backup candidate for downstream validation.

Recommended working concept:

`CatVTON-powered merchant preview copilot for small-to-mid-size apparel sellers`

Working value proposition:

- Who: lean apparel sellers and merchandising teams
- Why: they need faster, lower-cost visual preview workflows before investing in shoots or manual edits
- What before: spreadsheets, manual mockups, freelancers, and expensive content iteration
- How: CatVTON-based garment-on-model preview generation focused on tops, pants, and dresses, with human review in the loop
- What after: faster merchandising decisions, cheaper content testing, and better creative throughput
- Alternatives: manual design work, product shoots, generic image tools, and high-end virtual try-on platforms

This recommendation is intentionally narrower than a consumer shopping app because the repo currently proves qualitative usefulness, not consumer-grade trust.

## Evidence References

- `../../README.md`
- `../../RESULTS_AND_HANDOFF.md`
- `../brainstorm-pmf/evidence/repo-grounding.md`

## Open Risks

- No direct market evidence yet that SMB apparel sellers will pay for this workflow.
- The current model quality may be enough for internal review but not enough for customer-facing storefront output.
- No latency, serving cost, or upload workflow assumptions have been validated.
- The strongest categories appear to be simpler tops, pants, and structured dresses, which may constrain the first ICP.

## Confidence

medium
