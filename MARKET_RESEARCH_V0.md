# CatVTON Business Market Research v0

Date: 2026-03-16

## Scope

This memo evaluates a business built on this repository's CatVTON-style training outputs.

Working product hypothesis:

- Korea-first B2B SaaS/API for fashion sellers and platforms
- Primary use cases:
  - virtual try-on on product pages
  - on-model image generation from garment images
  - styling/merchandising content generation for catalogs and campaigns

Installed skills used as framing:

- `apify-market-research`
- `apify-competitor-intelligence`
- `startup-financial-modeling`
- `pricing-strategy`

Operational note:

- The Apify skills were installed successfully, but not executed in this repo because `mcpc` is not installed and no usable `APIFY_TOKEN` was found locally.
- Research below is therefore based on direct web/source review, using the installed skills as the analysis structure.

## Executive Summary

The most viable near-term business is not a consumer try-on app.
It is a B2B tool for Korean fashion merchants, agencies, and fashion platforms that need:

- higher PDP conversion
- faster image production
- lower return friction from fit uncertainty
- more model diversity without repeated shoots

Why this wedge is attractive:

- Korea is already a very large, mobile-first online commerce market.
- Fashion discovery and purchase are concentrated in digital-native platforms and apps.
- Return pressure remains meaningful in online retail, especially for categories where fit matters.
- The market is splitting into two tiers:
  - low-end Shopify-style apps priced roughly `$8-$100/month`
  - enterprise vendors selling via demo/contact-sales motions
- That leaves a practical middle wedge for a localized, category-optimized, service-assisted B2B offering.

Recommended initial target:

- independent and growth-stage women's fashion brands in Korea
- agencies or studios producing catalog/PDP content for multiple brands
- Korean fashion platforms that want an internal seller enablement tool

Recommended launch wedge:

- "AI on-model image generation + light try-on" for tops and dresses first
- not "full body exact fit simulation" as the lead promise

## What This Repo Suggests About Product Readiness

From the local repo README:

- the project reconstructs CatVTON-style self-attention-only training on DressCode
- it supports warm-start from public CatVTON checkpoints
- it prepares category-aware agnostic masks from `label_maps`
- it exports attention checkpoints in a CatVTON-compatible layout

Implication:

- the current asset is strongest as a controllable image-generation core
- it is not yet enough, by itself, to promise highly accurate size/fit guarantees
- the business pitch should emphasize:
  - visual confidence
  - content production speed
  - merchandising productivity
- not:
  - exact body-measurement-grade fit prediction

## Market Demand

### 1. Korea is already a large digital shopping market

Statistics Korea reported that online shopping transaction value reached `21.6858 trillion won` in April 2025, with mobile shopping at `16.7943 trillion won`.

This matters because:

- the addressable commerce base is already large
- mobile-first purchase flows favor lightweight try-on and visual merchandising tools

### 2. Fashion demand in Korea is increasingly platform-driven and AI-assisted

ABLY passed `10.05 million` MAU in mid-2025 according to WiseApp data cited by ChosunBiz, and attributes engagement partly to its AI recommendation system.

MUSINSA's global store also reported strong Japan growth, with Japan MAU up `82% YoY` as of March 2025.

This matters because:

- Korean fashion consumers are already used to algorithmic discovery
- sellers are competing inside visually dense, high-frequency platforms
- merchants have incentive to improve imagery and confidence signals quickly

### 3. Returns remain a real business pain

NRF said retailers expected `15.8%` of annual sales to be returned in 2025, and `19.3%` of online sales to be returned.

Narvar notes that, among information that would prevent returns:

- `77%` of shoppers wanted sizing charts or measurements
- `66%` wanted to see models of different shapes and sizes

Interpretation:

- visual certainty and model diversity are not cosmetic extras
- they directly support return reduction and purchase confidence

### 4. Big platforms are validating the category

Google announced at I/O 2025 that users could virtually try on `billions of apparel listings` by uploading a photo.
Google also launched Doppl in the U.S. in 2025 as a dedicated try-on app experiment.

Interpretation:

- virtual try-on demand is real enough for top platform investment
- but this also means direct-to-consumer app competition is structurally harder

## Recommended Target Customers

### Tier 1: Korean SMB and mid-market fashion brands

Profile:

- D2C brands with frequent new arrivals
- brands using Shopify, Cafe24, Makeshop, or custom storefronts
- especially women's apparel sellers with high SKU turnover

Pain:

- expensive and slow shoot cycles
- limited model diversity
- too many SKUs to shoot every styling variation
- weak conversion on new drops

Why they buy:

- lower content production cost
- faster launch cadence
- better visual merchandising

Best offer:

- managed SaaS with white-glove onboarding
- batch garment upload
- approved model templates
- PDP embed or export workflow

### Tier 2: Agencies / content studios

Profile:

- agencies producing catalog, PDP, or social creative for multiple brands

Pain:

- low-margin manual workflows
- scheduling complexity for shoots
- repeated requests for minor variant content

Why they buy:

- one tool can be resold across several clients
- service margin expands if generation is fast and controllable

Best offer:

- seat + usage pricing
- team workflow
- export packs
- client-facing preview links

### Tier 3: Fashion marketplaces / large platforms

Profile:

- vertical fashion platforms
- marketplaces with many small sellers

Pain:

- uneven image quality across sellers
- low conversion on long-tail catalog
- pressure to improve seller tooling

Why they buy:

- seller enablement and standardization
- platform-wide engagement lift
- potential returns reduction

Best offer:

- API / enterprise contract
- private deployment or priority inference
- governance and moderation controls

## Customer Segments to Avoid First

- direct consumer mobile app
  - high CAC
  - immediate competition with Google and social shopping flows
- luxury enterprise first
  - long sales cycles
  - high expectations around exact realism, compliance, and account support
- menswear as first wedge
  - Korea opportunity exists, but women's fashion is a more proven visual-commerce category

## Product Positioning

Recommended first positioning:

`Create on-model fashion imagery and lightweight virtual try-on for Korean fashion commerce.`

Do not lead with:

- "perfect sizing"
- "body-accurate fit guarantee"
- "return elimination"

Lead with:

- faster than photoshoots
- localized for Korean fashion catalogs
- better model diversity
- better launch speed for new arrivals
- optional shopper-facing try-on, but merchant workflow first

## Pricing and Packaging

### Observed market anchors

Low-end Shopify-style entrants are already offering consumer-facing try-on widgets:

- Aura advertises:
  - `$19.99/month` for `125 try-ons`
  - `$49.99/month` for `400 try-ons`
  - `$99.99/month` for `1,000 try-ons`
  - extra credits around `$0.08-$0.17`
- Revery exposes a free starter with `100 try-on images` and then custom enterprise pricing
- Lalaland.ai publicly lists:
  - `€600/month` business
  - `€900/month` enterprise

Interpretation:

- self-serve SMB pricing exists and is conditioning the market
- enterprise apparel pricing is still mostly quote-based
- there is room for a mid-market localized managed offer above Shopify apps but below classic enterprise software

### Recommended initial pricing model

Do not start with a pure per-image commodity API.

Start with:

- platform fee + included credits + overage

Suggested v0 packaging:

1. Starter
   - KRW `390,000/month`
   - 2,000 generations
   - 3 model presets
   - basic export and product-page assets

2. Growth
   - KRW `990,000/month`
   - 8,000 generations
   - team workflow
   - batch processing
   - custom brand presets

3. Enterprise
   - KRW `2.9M+/month`
   - API / platform integration
   - SLA / priority queue
   - dedicated onboarding

Overage:

- KRW `60-120` per generation depending on quality and latency tier

Setup / onboarding fee:

- KRW `500,000-3,000,000` depending on integration and brand template work

Why this is defensible:

- aligns with visible SMB app price anchors
- leaves room for service margin
- avoids racing to commodity per-image pricing too early

## Financial Model v0

This is a planning model, not a forecast of record.
It should be treated as an assumption set to validate.

### Variable cost assumptions

Public GPU pricing snapshots:

- Modal lists L40S at `$0.000542/sec`
- Runpod lists 4090 PRO at `$0.00031/sec` flex and `$0.00021/sec` active

If one generation effectively consumes:

- 10-15 sec on a 4090-class GPU, GPU cost is roughly `$0.0021-$0.0047/image`
- 20-30 sec on an L40S-class GPU, GPU cost is roughly `$0.0108-$0.0163/image`

Practical planning assumption after retries, storage, preprocessing, support overhead:

- target COGS per delivered generation: `$0.01-$0.03`

That means:

- SMB overage pricing at roughly `$0.04-$0.09` equivalent still leaves workable gross margin
- the bigger risk is not raw inference cost
- the bigger risk is support, QA, and implementation drag

### 12-month base case

Assumptions:

- 15 paying customers by month 12
- mix:
  - 8 Starter
  - 5 Growth
  - 2 Enterprise
- average realization:
  - Starter KRW 390k
  - Growth KRW 990k
  - Enterprise KRW 2.9m
- average customer ramp reaches roughly 55% of exit MRR over the year

Exit MRR:

- Starter: 8 x 390k = KRW 3.12m
- Growth: 5 x 990k = KRW 4.95m
- Enterprise: 2 x 2.9m = KRW 5.8m
- Total exit MRR = KRW `13.87m`

Approximate year-1 revenue:

- KRW `90m-105m`

Base operating cost sketch:

- GPU / inference / storage / tools: KRW `12m-20m`
- founder/operator labor not fully loaded here
- sales and onboarding cost likely dominates if motion is service-heavy

Implication:

- the business is viable at small scale only if onboarding and QA do not become agency work
- the first financial milestone is not profitability
- it is proving repeatable deployment and gross margin discipline

### What to measure immediately

- time from garment upload to acceptable output
- acceptance rate of first-pass outputs
- manual QA minutes per 100 generations
- try-on usage per SKU
- conversion delta on enabled PDPs
- change in returns or exchange rate where measurable

## Competitor Landscape

### 1. Platform incumbents

Google

- Google Shopping rolled out user-photo try-on for billions of apparel listings in 2025
- Doppl extends this into a consumer app experience

Threat:

- direct consumer try-on is becoming platform infrastructure

Response:

- do not compete as a generic consumer app
- focus on merchant workflow, localization, and controllability

### 2. Enterprise fashion AI vendors

Veesual

- positions around conversion and engagement
- Adore Me case study cites `+20%` conversion and `+18%` AOV

Revery

- offers free starter and enterprise tier
- emphasizes retailer/developer tooling and virtual dressing room workflows

Vue.ai

- broader fashion AI suite, not only try-on
- pushes conversion/AOV/engagement outcomes

Lalaland.ai

- closer to AI model studio / digital model content production
- public pricing suggests willingness to pay for content generation workflows, not just shopper try-on

Perfect Corp.

- very strong in beauty and accessories
- shows how this category often grows from one vertical into adjacent try-on workflows

### 3. Shopify and long-tail plugin entrants

Examples include Aura, Wearbly, PixelDrapeAI, and similar new apps.

Threat:

- low-end SMB merchants will compare against app-store pricing, not enterprise decks

Response:

- avoid selling a bare widget alone
- bundle merchant workflow, presets, Korean support, batch operations, and measurable service

## Entry Barriers

Real barriers you can build:

- category-specific output quality on Korean fashion imagery
- merchant workflow integration, not just inference
- brand presets and reusable model libraries
- QA tooling and approval flows
- customer data accumulation on what outputs convert
- relationships with agencies / platforms / seller ecosystems

Weak barriers you should not overestimate:

- the model weights alone
- "we fine-tuned CatVTON"
- generic API access

Open-source and cloud compute reduce moat on core generation over time.
Your moat must migrate upward into workflow, distribution, and customer-specific data loops.

## Likely Fast-Follower Risks

### Risk 1: Shopify apps race downward on price

Response:

- sell managed outcomes, not only widgets
- win where localization and catalog workflow matter

### Risk 2: Large platforms add native try-on

Response:

- own merchant-side asset creation and seller tooling
- integrate into seller operations before platforms absorb the use case

### Risk 3: Enterprise competitors move downmarket

Response:

- move faster in onboarding
- specialize on Korea-first apparel catalogs
- keep implementation light

### Risk 4: Quality complaints around realism or fit

Response:

- narrow category scope first
- disclose limitations clearly
- frame outputs as confidence aids and content tools, not exact fit guarantees

## Recommended Go-To-Market Sequence

1. Start with 3-5 pilot brands or agencies
2. Focus on one or two categories:
   - tops
   - dresses
3. Sell a managed beta, not self-serve first
4. Measure:
   - output acceptance
   - content production time saved
   - PDP engagement / conversion lift
5. Only then decide whether to productize:
   - merchant workflow
   - shopper try-on widget
   - API

## Bottom-Line Recommendation

Best business model to test first:

- Korea-first B2B SaaS + service hybrid for fashion merchants and agencies

Best initial promise:

- faster on-model imagery and confidence-enhancing try-on

Best customer:

- women's fashion brands and agencies with frequent SKU updates

Best monetization:

- monthly subscription plus credits plus onboarding fee

Biggest mistake to avoid:

- launching as a generic consumer app or promising exact-fit accuracy too early

## Sources

- Statistics Korea, Online Shopping in April 2025:
  - https://www.kostat.go.kr/board.es?act=view&bid=11722&list_no=436903&mid=a20101000000&ref_bid=&tag=
- NRF, Consumers Expected to Return Nearly $850 Billion in Merchandise in 2025:
  - https://nrf.com/media-center/press-releases/consumers-expected-to-return-nearly-850-billion-in-merchandise-in-2025
- Narvar, The 6 Critical Touchpoints of the Return Process:
  - https://corp.narvar.com/blog/returns-experience-that-customers-love
- Google I/O 2025 announcements:
  - https://blog.google/innovation-and-ai/products/google-io-2025-all-our-announcements/
- Google Labs Doppl announcement:
  - https://blog.google/innovation-and-ai/models-and-research/google-labs/doppl/
- MUSINSA newsroom, Japan growth / MAU:
  - https://about.musinsa.com/newsroom/musinsa-global-store
- ChosunBiz, ABLY reaches 10 million monthly users:
  - https://biz.chosun.com/en/en-retail/2025/06/18/CA4FTPQ5UJD6XJFUKDBHAFUOLU/
- Veesual Adore Me case:
  - https://www.veesual.ai/case-study-adore-me
- Revery pricing:
  - https://www.revery.ai/pricing
- Lalaland.ai pricing:
  - https://lalaland.ai/pricing/
- Aura pricing:
  - https://tryonaura.com/
- Modal pricing:
  - https://modal.com/pricing
- Runpod serverless pricing:
  - https://docs.runpod.io/serverless/pricing
