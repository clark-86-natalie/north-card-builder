# Product Requirements Document

**North Card Builder**

- **Version:** 2.0 (updated to match the built prototype)
- **Status:** Hackathon MVP, built
- **Product:** Interactive credit card builder website
- **Brand:** North
- **Primary deliverable:** Working, responsive web prototype (`index.html`)
- **Deadline:** End of hackathon day

> Version 1.0 described a design-first "NORTH Card Studio". The prototype moved on from that during the build. It now starts with a short eligibility questionnaire, recommends perks, and ends in a simulated application. This version describes what is built. Section 15 lists the changes from 1.0 and the 1.0 items that aren't built yet.

---

## 1. Executive summary

### 1.1 Product vision

North is a fictional, app-first bank exploring a more personal approach to credit cards.

North Card Builder is an interactive website where customers answer a few questions, get a simulated eligibility result, pick three perks that suit how they spend, design how their card looks, and finish with a card ready in their phone wallet.

Customers build their own card from perks and design choices, rather than picking one fixed product from a range.

The experience should feel engaging, quick and visually distinctive, combining the creativity of a design tool with the clarity of a modern fintech app.

### 1.2 Headline

A credit card built around how you live.

Supporting copy: "Pick the perks you'll actually use, design how it looks, and check your eligibility in about two minutes. Checking won't affect your credit score."

### 1.3 Problem statement

Traditional credit cards come as fixed packages. Customers have little control over the features or how the card looks, and often don't know whether they'll be accepted until they apply.

This concept explores whether three things together make a card feel more personal and relevant: an upfront eligibility check, a choice of perks with their value shown in pounds, and a card designed by the customer.

This is a product hypothesis to demonstrate, not a validated customer research finding.

### 1.4 Proposed solution

North Card Builder gives customers five connected capabilities:

1. Tell North what matters to them and check their eligibility with a simulated soft search.
2. Choose exactly three perks, with an estimate of what those perks are worth each year after fees.
3. Design the card's colour, pattern, material, finish, orientation and name.
4. Review the card, credit limit, fees and representative APR, then apply.
5. See the finished card drop into a phone wallet.

A "Surprise me" button on the design step generates a random new look.

---

## 2. Goals and success criteria

### 2.1 Product goals

- Demonstrate a customer-led credit card building experience.
- Show eligibility before the customer commits, without a credit score impact (simulated).
- Make the value of each perk concrete in pounds per year.
- Give immediate visual feedback on every design choice.
- Create a cohesive, premium, app-first fintech brand experience.
- Demonstrate how AI-assisted development can bring a product concept to life quickly.
- Deliver an end-to-end journey that can be presented in three minutes.

### 2.2 Hackathon success criteria

The prototype is successful when:

- A user can complete the main journey without assistance.
- Each question needs an answer before the user can continue.
- The perk picker enforces exactly three perks and updates the estimated value as perks and spend change.
- Design changes update the live card preview immediately.
- The review and final screens match the user's choices.
- The user can go back through the steps without losing their choices.
- The website works at desktop and mobile viewport sizes, in light and dark mode.
- No core interaction depends on a real banking integration.

---

## 3. Target users

The prototype is designed around four illustrative user types. They map directly to the four answers to "What matters most to you in a credit card?".

### 3.1 The credit builder

Getting a first card or making a fresh start. Wants help building a credit score.

### 3.2 The everyday spender

Wants money back on groceries, bills and day-to-day spending.

### 3.3 The frequent traveller

Wants miles, airport lounges and cheaper spending abroad.

### 3.4 The cost spreader

Has a big purchase coming up or wants to move a balance, and values 0% periods.

These personas represent potential use cases, not researched or validated customer segments.

---

## 4. Core user journey

Landing → Let's get to know you (6 questions) → Building your card (eligibility result) → Pick your three perks → Make it yours (design) → Check and apply → Your North card is ready

The four main steps (About you, Perks, Design, Review) are shown in a progress bar with a label such as "Step 2 of 4 · Perks".

Users can go back with the Back button at any step, including question by question within "About you". All answers, perks and design choices are kept.

---

## 5. Functional requirements

### 5.1 Landing page

Purpose: Introduce North and get customers started.

#### Requirements

- North logo (a compass-style mark) and wordmark in the top bar, with a "Prototype" tag.
- Headline: "A credit card built around how you live."
- Supporting copy about perks, design and a two-minute eligibility check.
- A live example card.
- Three key points:
  - **Choose 3 perks**: cashback, travel, 0% offers or credit building. Swap them every 90 days in the app.
  - **Design it yourself**: colour, pattern, finish and how your name appears.
  - **No annual fee**: only premium travel perks carry a small monthly fee, shown upfront.
- Primary CTA: "Start building".
- Footnote: "North is a fictional bank. This is a hackathon prototype."

#### Acceptance criteria

- "Start building" opens the first question.
- No login or registration is required.

### 5.2 Let's get to know you

Purpose: Understand what the customer wants and simulate an eligibility check.

Questions are shown one at a time, with a "Question X of 6" counter and a thin progress track. The Continue button stays disabled until the current question is answered. On the last question it reads "Build my card".

#### Questions

1. **What matters most to you in a credit card?** One choice, with an icon and short description:
   - Build my credit score: my first card, or a fresh start.
   - Get money back on everyday spending: groceries, bills, the usual.
   - Earn travel rewards: miles, lounges, spending abroad.
   - Spread the cost of something: a big purchase or moving a balance.
2. **A couple of quick checks.** "Are you 18 or over?" and "Do you live in the UK?" (Yes/No). Both must be Yes to continue. A No shows: "You need to be 18 or over and live in the UK to get a North card."
3. **What's your employment status?** Employed, Self-employed, Student, Retired, or Not working right now.
4. **What's your yearly income before tax?** Slider from £0 to £150,000 in £1,000 steps, default £32,000.
5. **How much do you pay for rent or mortgage each month?** Slider from £0 to £3,000 in £25 steps, default £850.
6. **In the last 6 years, have you had a CCJ, bankruptcy or IVA?** Yes/No, with an explanation of what a CCJ is and a note that answering yes doesn't stop you applying.

Footnote throughout: "None of this affects your credit score."

#### Acceptance criteria

- Choosing a goal preselects three recommended perks for that goal. Changing the goal replaces them with the new goal's recommendations.
- Users cannot continue past the eligibility checks unless both answers are Yes.
- Back moves to the previous question.

### 5.3 Building your card (holding screen)

Purpose: Make the simulated soft search feel real and reveal the result.

#### Requirements

- Title "Building your card…" with a spinner.
- Three steps tick off one after another, about 0.9 seconds each:
  1. Checking your eligibility with a soft search.
  2. Matching perks to what matters to you.
  3. Working out your credit limit.
- The title then changes to "Good news" and a result panel shows:
  - "Likely to be approved".
  - "Credit limit up to £X".
  - The representative APR and a sentence confirming three perks have been picked to match the customer's goal.
- CTA: "See my perks".

#### Illustrative offer logic

All values are fictional.

- Credit limit starts at a share of income set by employment status: employed 22%, self-employed 18%, retired 15%, student 8%, not working 6%. It is capped at £15,000.
- If yearly housing costs are more than 40% of income, the limit is reduced by 40%.
- Credit builders are capped at £1,200.
- A CCJ, bankruptcy or IVA caps the limit at £500.
- The limit is rounded to the nearest £50, with a minimum of £250.
- Representative APR (variable): 34.9% with a CCJ, bankruptcy or IVA; 29.9% for credit builders and students; otherwise 24.9%.

### 5.4 Pick your three perks

Purpose: Let customers choose the perks that matter to them and see what they're worth.

#### Requirements

- A "Recommended for you" panel with three slot indicators that fill as perks are picked, and the customer's representative APR.
- A slider: "How much do you put on a card each month?" from £200 to £5,000 in £100 steps, default £1,200.
- A dark "What your perks could earn you" panel showing an estimated value per year after monthly fees, with a line-by-line breakdown. It updates live as perks or spend change.
- Perks shown in groups as selectable tiles, with "Recommended" and monthly fee badges where relevant.
- Exactly three perks must be picked. Once three are selected, the other tiles fade and shake if tapped. Tapping a selected perk removes it.
- The CTA reads "Pick N more" until three are picked, then "Design my card".

#### Perks

All rates, fees and values are fictional and illustrative.

| Group | Perk | Detail | Estimated value / fee |
|---|---|---|---|
| Cashback | 1% cashback on everything | Paid into your account every month | 1% of yearly spend |
| Cashback | 3% back at supermarkets | Based on about a quarter of your spend | 3% of 25% of yearly spend |
| Cashback | Round-ups to savings | Spare change moves to a 4.1% AER pot | Shown as "Builds savings" |
| Travel | North Miles | 1 mile per £1, 3 per £1 on flights and hotels | About 1.2% of yearly spend |
| Travel | No foreign transaction fees | Saves 2.99% on spending abroad | 2.99% of 8% of yearly spend |
| Travel | 4 airport lounge passes a year | Over 1,300 lounges worldwide | £128 a year, £4/month fee |
| Travel | Worldwide travel insurance | Includes winter sports and gadgets | £95 a year, £3/month fee |
| Spread the cost | 0% on purchases for 12 months | Then the standard rate applies | Shown as "0% for 12 mo" |
| Spread the cost | 0% on balance transfers for 18 months | 3% transfer fee | Shown as "0% for 18 mo" |
| Credit building | Credit Builder | Monthly score updates and a limit review every 6 months | Shown as "Included" |

#### Recommended perks by goal

- Build my credit score: Credit Builder, Round-ups to savings, 1% cashback.
- Everyday spending: 1% cashback, 3% back at supermarkets, Round-ups to savings.
- Travel rewards: North Miles, No foreign transaction fees, Lounge passes.
- Spread the cost: 0% on purchases, 0% on balance transfers, Credit Builder.

#### Card tier

The card is given a tier name from the chosen perks, shown on the card and in the summaries:

- **Explorer**: lounge passes or travel insurance.
- **Foundation**: Credit Builder.
- **Voyager**: North Miles or no foreign transaction fees.
- **Flex**: either 0% offer.
- **Everyday**: anything else.

#### Acceptance criteria

- Users can select and deselect perks, up to a maximum of three.
- The estimated value and fee figures match the selected perks and spend.
- Selected perks are kept when navigating between steps.
- The interface does not imply that choosing a perk guarantees approval.

### 5.5 Make it yours (design)

Purpose: Let customers personalise how their card looks.

#### Requirements

Users can choose:

- **Colour** (7): Aurora (default), Aurora Bright, Polar Night, Fjord, Midnight Sun, Glacier White, Arctic Basalt. Aurora and Aurora Bright have a slow-moving shimmer, like the northern lights. The chosen colour's name is shown beside the label.
- **Pattern** (6): Fjord peaks (default), Boreal forest, Aurora curtains, Polaris (the Plough pointing to the North Star), Top of the world, Clean.
- **Material** (3): Recycled plastic (free, default), Brushed steel (£49 one-off), Birch wood (£25 one-off). A hint explains that steel and birch are charged once when the card is made. Birch shows wood grain lightly tinted with the chosen colour.
- **Finish** (2): Matte (default), Gloss.
- **Orientation** (2): Landscape (default), Portrait.
- **Name on card**: text field, up to 24 characters, default "Alex Morgan", shown in capitals.

**Surprise me** (button beside the heading) picks a random colour, pattern (never Clean) and finish, each different from the current one. It picks portrait about a quarter of the time, and the card flips in with a short animation.

CTA: "Looks good".

#### Live card preview

The card preview:

- Has a realistic payment card shape (1.586 ratio), rotating for portrait.
- Shows the North logo, the tier name, a chip, a contactless symbol, a fictional masked number (•••• 4821), the name on the card and a network mark.
- Updates immediately when any design choice or the name changes.
- Uses gradients, sheen and shadows for depth. Steel adds brushed lines and a bright edge.
- Has an accessible label describing the tier, material, colour and finish.

All payment card details are fictional.

#### Acceptance criteria

- Every design control visibly updates the preview immediately.
- An empty name shows "YOUR NAME". Long names are capped at 24 characters and truncate with an ellipsis if they don't fit.
- Design choices are kept when navigating between steps.

### 5.6 Check and apply (review)

Purpose: Show everything in one place before the customer applies.

#### Requirements

- The card preview.
- A summary listing: Card (North + tier), Perks, Design (colour, pattern, finish), Material, Credit limit ("Up to £X"), Monthly fee, One-off card fee, and Representative APR.
- A representative example: "assumed credit limit of £1,200. Purchase rate X% p.a. (variable). X% APR representative (variable)."
- CTA: "Apply and get my card".
- Footnote: "Applying runs a full credit check. All figures are illustrative." (No real check is run.)

#### Acceptance criteria

- All summary details match the user's choices.
- Back returns to the design step with everything kept.

### 5.7 Your North card is ready (final reveal)

Purpose: Give users a satisfying conclusion.

#### Requirements

- A wallet animation: the finished card drops into a phone wallet marked "Ready for contactless". This is a visual simulation only.
- A summary: Card (tier and masked number), Material, Credit limit, and Estimated value per year.
- Next steps:
  1. Use it now. Your card is in your phone wallet and the North app.
  2. Your physical card arrives in 3 to 5 working days.
  3. Swap a perk any time after 90 days from the Card tab.
- "Build another card" button.

#### Acceptance criteria

- All displayed details match the user's choices.
- "Build another card" returns to the landing page and clears the questionnaire answers and perks. Design choices and slider values are kept.

---

## 6. User interface and visual design

### 6.1 Brand identity

- **Brand:** North
- **Product:** North Card Builder
- **Headline:** A credit card built around how you live.
- **Theme:** the far north. Aurora, fjords, polar nights, glaciers, birch and the North Star run through the colour names, patterns and logo.

#### Brand personality

- Confident.
- Modern.
- Considered.
- Customer-led.
- Premium without being intimidating.

### 6.2 Visual direction

A contemporary, app-first fintech look with a calm interface and expressive card designs.

#### Core palette

- Frost (#eef3f6) background and white surfaces in light mode.
- Polar navy (#0d1b2e) for text and the desktop studio panel.
- Aurora teal (#0f9e8a) as the brand accent for buttons, selection and progress.
- A full dark mode that follows the device setting, with deeper navy surfaces and a brighter teal.
- Card colours are separate from the interface and look the same in both themes.

#### Typography

- Bricolage Grotesque for headings and the wordmark.
- Figtree for body text.
- JetBrains Mono for the card number and name on card.

#### Design principles

1. Visual first: the card preview is the focal point.
2. Immediate feedback: every selection has an obvious visual result.
3. Low cognitive load: one question per view, clear labels, short descriptions.
4. Concrete value: perk value is shown in pounds, after fees.
5. Accessible interaction: clear focus states, readable text and sufficient contrast.
6. Responsive by default: designed app-first, with a richer desktop layout.

### 6.3 Layout

On mobile and narrow screens:

- One phone-width column of steps (up to 520px).
- Top bar with Back button or logo, and a "Prototype" tag.
- Card preview shown within the relevant steps.
- Primary action in a sticky bar at the bottom.

On desktop (960px and wider):

- The step column on the left.
- A sticky dark "studio" panel on the right labelled "Your card, live", showing the live card and three stats: Perks (X / 3), Est. value / yr, and Monthly fee.
- During "About you" the studio shows an empty dashed card outline, so the card's first appearance is saved for later.

---

## 7. Non-functional requirements

### 7.1 Performance

- A single static HTML file with inline CSS and JavaScript. The only external assets are Google Fonts.
- No frameworks or build step.
- Card art and patterns are inline SVG and CSS gradients, not images.

### 7.2 Accessibility

- Semantic HTML, with labels on the sliders and name field.
- All controls are buttons and keyboard accessible, using `aria-pressed` for selection.
- Visible focus outlines.
- Selection is shown with ticks, filled radios and borders as well as colour.
- The card preview has a descriptive accessible label. The perk value panel is announced politely when it changes.
- All animations and transitions are switched off when the user prefers reduced motion.

### 7.3 Responsiveness

- Supports common desktop and mobile viewport sizes, including safe areas on notched phones.
- No horizontal scrolling.

### 7.4 Reliability

- All primary buttons perform their stated actions.
- State is kept while navigating through the flow.
- Core functionality has no external dependencies.
- Sensible defaults let a user complete the journey quickly.

### 7.5 Privacy and security

- Fictional data only.
- Nothing entered is stored or sent anywhere. All state is in memory and is lost on refresh.
- No real credit check, payment processing or application.

---

## 8. Technical requirements

### 8.1 Implementation

- One file: `index.html`. Open it in a browser or serve it from any static host such as GitHub Pages.
- Vanilla HTML, CSS and JavaScript.
- Screens are `<section>` elements switched with a `go(n)` function. Screen 7 is the holding screen that sits inside step 1.
- Data is defined as constants: `GOALS`, `PERKS`, `COLORS`, `PATTERNS`, `MATERIALS`, `FINISHES`, `ORIENT`, `EMP`.
- `cardHTML()` renders the card wherever it appears (landing, design, review, studio panel and wallet).
- `offer()` works out the credit limit and APR. `totals()` works out perk value and fees. `tierName()` picks the tier.

### 8.2 Application state

A single `state` object holds:

- Navigation: `step`, `q` (current question).
- About you: `goal`, `adult`, `uk`, `emp`, `income`, `housing`, `ccj`.
- Perks: `perks` (up to three IDs), `spend`.
- Design: `color`, `pattern`, `material`, `finish`, `orient`, `name`.

### 8.3 Persistence

In-memory only. Refreshing the page starts again.

---

## 9. Out of scope

The following are excluded from the hackathon MVP:

- Real bank accounts.
- Real credit applications, soft searches, credit checks or affordability assessments.
- Real eligibility decisions. The "Likely to be approved" result and credit limit are simulated.
- Actual payment processing.
- Real credit limits, APRs or financial advice.
- Actual Apple Pay or Google Wallet provisioning.
- Live cashback, miles or rewards transactions.
- Real customer authentication.
- Data storage of any kind.
- Integration with banking systems.

Any fees, rates, limits, rewards or benefits displayed must be labelled as fictional or illustrative.

---

## 10. Measurement and evaluation

As this is a hackathon prototype, success is assessed through demonstration and basic usability rather than commercial performance.

#### Evaluation criteria

- **Journey completion:** can someone complete the flow without help?
- **Clarity:** do users understand the questions, the eligibility result and the difference between perks?
- **Value:** does the pounds-per-year estimate help users choose perks?
- **Customisation quality:** does the preview respond correctly to every design choice?
- **Consistency:** do the review and final screens match the choices made?
- **Visual quality:** does the experience feel cohesive and presentation-ready?
- **Technical reliability:** can the core flow be demonstrated without errors?

If time allows, ask a colleague to complete the journey and observe where they hesitate.

---

## 11. Delivery status

### Phase 1: Foundation (done)

- Single-file static site, visual foundation, light and dark themes.
- Landing page and screen structure.

### Phase 2: Core functionality (done)

- One-question-at-a-time "About you" flow with validation.
- Simulated soft search holding screen and offer logic.
- Perk picker with three-perk limit, recommendations, spend slider and live value.
- Card designer with live preview.
- Back navigation with state kept.

### Phase 3: Completion (done)

- Review screen with summary and representative example.
- Wallet reveal and "Build another card".
- Desktop studio panel.

### Phase 4: Polish (done)

- Aurora shimmer, card patterns, steel and birch materials.
- "Surprise me" on the design step.
- Reduced-motion support.

---

## 12. Acceptance checklist

- [x] North branding and headline are visible.
- [x] "Start building" opens the questionnaire.
- [x] Each question must be answered before continuing.
- [x] Under-18s and non-UK residents cannot continue.
- [x] The holding screen shows a simulated eligibility result, credit limit and APR.
- [x] Choosing a goal preselects three recommended perks.
- [x] Users must pick exactly three perks.
- [x] Estimated value updates with perks and spend, after fees.
- [x] Users can choose from seven card colours and six patterns.
- [x] Users can choose material, finish and orientation.
- [x] Users can personalise the name on the card.
- [x] The live preview updates immediately.
- [x] "Surprise me" generates a new design.
- [x] User choices persist throughout the journey.
- [x] The review and final screens show the correct details.
- [x] Users can go back and edit at any step.
- [x] Users can build another card.
- [x] The website is responsive and supports dark mode.
- [x] The demo works without a live banking integration.

---

## 13. Three-minute presentation plan

### 0:00–0:30 | The opportunity

"Credit cards come as fixed packages, and you often don't know if you'll get one until you apply. North explores a different idea: what if you could check first, then build a card around how you live?"

### 0:30–2:00 | The demonstration

- Start on the landing page.
- Pick a goal and run through the quick questions.
- Show the soft search result and credit limit.
- Swap a perk and move the spend slider to show the value change.
- Design the card: try Aurora, a pattern, brushed steel, and "Surprise me".
- Review the summary and apply.
- Finish on the card dropping into the wallet.

### 2:00–3:00 | The bigger picture

"This prototype brings together an upfront eligibility check, perks you choose with their value shown in pounds, and a card you design yourself. The longer-term opportunity is to make financial products feel more relevant and transparent without making them more complicated."

Close with the finished card on screen.

---

## 14. Instructions for the AI development assistant

Treat this PRD as the description of the current prototype.

When making changes:

1. Keep it a single static `index.html` with no build step.
2. Add new options (colours, patterns, perks, materials) to the data constants so they flow through the card, summaries and studio panel.
3. Keep every rate, fee and limit labelled as illustrative.
4. Test the complete journey on desktop and mobile, in light and dark mode, after each change.
5. Update this PRD and the README when the flow changes.

---

## 15. Changes from version 1.0

### What changed

- **Name and headline:** "NORTH Card Studio" with the tagline "Your money. Your rules. Your card." became "North Card Builder" with the headline "A credit card built around how you live."
- **Journey order:** v1.0 was Design → Features → Format → Review → Reveal. The build is About you → Eligibility result → Perks → Design → Review → Wallet.
- **Eligibility:** v1.0 put credit scoring, eligibility and APR out of scope. The build includes a simulated questionnaire, soft search result, credit limit and representative APR, all illustrative.
- **Features:** v1.0 let users pick any number of feature categories. The build asks for exactly three specific perks, recommends three from the user's goal, and shows their value per year after fees.
- **Design options:** v1.0 asked for five colours and optional finishes. The build has seven colours, six patterns, three materials with one-off fees, two finishes and two orientations.
- **Surprise me:** moved from the landing page to the design step, and changes the look only (not perks).
- **Landing CTA:** "Design your card" became "Start building".

### v1.0 items not built yet

- **Card format choice** (physical, digital-only or both). The final screen assumes both.
- **"Edit my card" on the final screen.** Users can edit using Back before applying, but not after.
- **"Surprise me" on the landing page**, and AI-generated concepts with a name and description such as "The Weekend Wanderer".
- **"Start again" fully resetting the design.** "Build another card" clears answers and perks but keeps the design.
