# Product Requirements Document

**NORTH Card Studio**

- **Version:** 1.0
- **Status:** Hackathon MVP
- **Product:** Interactive credit card customisation website
- **Brand:** NORTH
- **Primary deliverable:** Working, responsive web prototype
- **Deadline:** End of hackathon day

---

## 1. Executive summary

### 1.1 Product vision

NORTH is a fictional digital bank exploring a more personal approach to credit cards.

NORTH Card Studio is an interactive website that enables customers to design their own credit card, choose features that suit their lifestyle and preview their finished creation.

Instead of choosing from a fixed range of predefined products, customers can personalise the appearance, format and benefits of their card.

The experience should feel engaging, intuitive and visually distinctive, combining the creativity of a design tool with the clarity of a modern fintech product.

### 1.2 Product tagline

Your money. Your rules. Your card.

### 1.3 Problem statement

Traditional credit card experiences typically require customers to select from predefined products with fixed features and limited personalisation.

This concept explores whether giving customers greater control over their card's appearance and selected features could make the experience feel more personal, engaging and relevant.

This is a product hypothesis to demonstrate, not a validated customer research finding.

### 1.4 Proposed solution

NORTH Card Studio gives customers four connected capabilities:

1. Design a card that reflects their personality.
2. Choose the features and benefits that matter to them.
3. Select a physical, digital or combined card format.
4. Reveal a personalised card design and summary.

An optional AI-assisted feature can generate a suggested design and feature combination.

---

## 2. Goals and success criteria

### 2.1 Product goals

- Demonstrate a customer-led credit card customisation experience.
- Provide immediate visual feedback as customers make choices.
- Allow customers to combine relevant features rather than choose one fixed package.
- Create a cohesive, premium fintech brand experience.
- Demonstrate how AI-assisted development can bring a product concept to life quickly.
- Deliver an end-to-end journey that can be presented in three minutes.

### 2.2 Hackathon success criteria

The prototype is successful when:

- A user can complete the main journey without assistance.
- Card customisation works and updates the preview immediately.
- Feature selections are reflected in the final summary.
- Physical and digital format selections work.
- The user can return to edit their design.
- The website works at desktop and mobile viewport sizes.
- The final reveal is visually compelling and presentation-ready.
- No core interaction is dependent on a real banking integration.

---

## 3. Target users

The prototype is designed around four illustrative user types.

### 3.1 The design-conscious customer

Wants a card that reflects their personality and aesthetic preferences.

### 3.2 The rewards-focused customer

Wants benefits such as cashback and rewards that align with their priorities.

### 3.3 The frequent traveller

Values travel-related benefits and useful information about spending abroad.

### 3.4 The financially mindful customer

Values budgeting tools, spending insights, payment reminders and credit education.

These personas represent potential use cases, not researched or validated customer segments.

---

## 4. Core user journey

The primary journey should follow a clear sequence.

Landing page → Design your card → Choose your features → Choose your format → Review your card → Finished card reveal

The experience should feel like one continuous design process rather than a series of disconnected application forms.

Users must be able to navigate backwards and change their choices without losing previously entered information.

---

## 5. Functional requirements

### 5.1 Landing page

Purpose: Introduce NORTH and encourage customers to begin designing their card.

#### Requirements

- Display NORTH branding prominently.
- Display the tagline: “Your money. Your rules. Your card.”
- Include supporting copy explaining the customisation concept.
- Include a primary CTA: “Design your card”.
- Include a secondary CTA: “Surprise me”.
- Show an attractive example card or card collection.
- Introduce the idea of personalising appearance, benefits and format.

#### Acceptance criteria

- Selecting “Design your card” opens the customisation experience.
- Selecting “Surprise me” generates a suggested configuration or selects a predefined concept.
- The landing page is visually polished and responsive.
- No login or registration is required.

### 5.2 Card design studio

Purpose: Allow customers to personalise the appearance of their card.

#### Requirements

Users must be able to:

- Choose from a minimum of five card colours.
- Enter a personalised card name or phrase.
- See their selections reflected immediately in a live preview.

#### Suggested default colours

- Midnight charcoal.
- Forest green.
- Ocean blue.
- Violet.
- Ruby red.

If time permits, users should also be able to choose between matte, metallic and holographic-inspired finishes.

#### Live card preview

The card preview should:

- Resemble a realistic payment card.
- Display NORTH branding.
- Display a chip and contactless symbol.
- Display the personalised card name.
- Update when the colour or name changes.
- Maintain a consistent aspect ratio.
- Use tasteful shadows, gradients or highlights to create depth.

All payment card details must be fictional.

#### Acceptance criteria

- Colour selections visibly update the preview immediately.
- Text entered into the card name field updates the preview.
- Empty or excessively long names are handled gracefully.
- Customisation remains intact when navigating between steps.

### 5.3 Feature selection

Purpose: Let customers select a combination of features that reflects their priorities.

Users should be able to select multiple compatible features.

Feature category A: Everyday spending

Possible features:

- Spending insights and categorisation.
- Budgeting tools.
- Payment reminders.

Feature category B: Travel

Possible features:

- Travel spending insights.
- Foreign transaction fee information.
- Travel-related perks.
- Notifications about spending abroad.

Feature category C: Cashback and rewards

Possible features:

- Selectable rewards categories.
- Illustrative cashback rewards.
- A projected rewards summary.

Feature category D: Credit builder

Possible features:

- Payment reminders.
- Credit education.
- Progress tracking.
- Tools to encourage healthy repayment habits.

#### Interaction requirements

- Display each category as a selectable card or tile.
- Include a short description of each category.
- Make selected and unselected states visually distinct.
- Allow users to select multiple categories.
- Reflect selections in a persistent order summary.
- Provide a way to deselect a category.

#### Acceptance criteria

- Users can select and deselect feature categories.
- Multiple selections can coexist.
- Selected features are retained when navigating between steps.
- The final summary accurately reflects all selected categories.
- The interface does not imply that selecting a feature guarantees eligibility for a financial product.

For the MVP, selecting a category is sufficient. Building a detailed configuration interface for every individual benefit is optional.

### 5.4 Card format selection

Purpose: Allow customers to choose how their card would be issued or used.

#### Options

Physical card: A physical payment card.

Digital-only: A digital card concept designed for mobile use.

Both: A physical card and a digital version.

#### Requirements

- Present all three options clearly.
- Use simple illustrations or icons to distinguish the formats.
- Provide a visible selected state.
- Retain the selection throughout the journey.
- Reflect the selection in the final summary.

If time permits, include a digital wallet-style preview.

#### Acceptance criteria

- Only one format can be selected at a time.
- The chosen format appears in the final summary.
- Any wallet preview is explicitly a visual simulation.

Actual Apple Pay and Google Wallet integrations are out of scope.

### 5.5 AI-assisted personalisation

Purpose: Demonstrate how AI could help customers discover a card concept without designing everything manually.

This is a stretch feature, not a dependency for the MVP.

#### Primary interaction

The user selects “Surprise me” or “Generate my card concept”.

The prototype generates a suggested configuration containing:

- A creative card name.
- A suggested colour and design direction.
- A suitable feature combination.
- A short description of the concept.
- A concise explanation of why the suggested combination fits the selected preferences, if provided.

Example:

The Weekend Wanderer

A midnight-blue card concept with travel-focused features and a rewards theme.

#### Requirements

- Display the generated suggestion clearly.
- Allow users to apply the suggested design.
- Allow users to continue editing after applying it.
- Avoid overwriting existing customisation without a clear user action.

#### Implementation approach

Prefer a real AI integration only if the environment and available time support it.

Otherwise, use a small library of predefined concepts with varied copy and configurations. The interaction must work reliably in the live demo.

If using an external AI service, never expose secret API keys in client-side code.

### 5.6 Final reveal and summary

Purpose: Give users a satisfying conclusion to the design process.

#### Requirements

Display:

- The completed card preview.
- The personalised card name.
- The selected colour and finish, if applicable.
- The selected format.
- All selected feature categories.
- A clear summary of the design.

Include two actions:

- Edit my card: Return to the customisation flow with existing selections preserved.
- Start again: Reset the configuration and begin a new design.

The reveal should use a visually distinctive layout and, if practical, a subtle entrance animation.

#### Acceptance criteria

- All displayed details match the user's selections.
- Users can return to editing without losing their configuration.
- Starting again resets the design.
- The final screen works at mobile and desktop sizes.

---

## 6. User interface and visual design

### 6.1 Brand identity

Brand: NORTH

Product: NORTH Card Studio

Tagline: Your money. Your rules. Your card.

#### Brand personality

- Confident.
- Modern.
- Considered.
- Customer-led.
- Premium without being intimidating.

### 6.2 Visual direction

Use a contemporary fintech aesthetic with a restrained interface and expressive card designs.

#### Core palette

- Charcoal or near-black for depth and contrast.
- Off-white for clean content surfaces.
- Muted sage as a recognisable brand accent.
- Additional vivid colours for user-created cards.

The core interface should remain consistent even when customers choose very different card colours.

#### Design principles

1. Visual first: Make the card preview the focal point.
2. Immediate feedback: Every selection should have an obvious visual result.
3. Low cognitive load: Use clear labels, concise descriptions and a small number of decisions per step.
4. Progressive disclosure: Show advanced options only when needed.
5. Accessible interaction: Provide clear focus states, readable text and sufficient contrast.
6. Responsive by default: Design for desktop presentation while ensuring mobile usability.

### 6.3 Suggested layout

On desktop:

- Main content and configuration controls on one side.
- Persistent card preview on the other.
- Clear progress indicator across the top.
- Final summary and primary action at the bottom.

On mobile:

- Card preview near the top.
- Configuration controls underneath.
- Full-width primary action.
- Compact progress indicator.

---

## 7. Non-functional requirements

### 7.1 Performance

- The website should load quickly in a modern browser.
- Core interactions should respond immediately.
- Avoid heavy dependencies or unnecessary assets.
- Prefer lightweight CSS effects over complex animations.

### 7.2 Accessibility

- Use semantic HTML elements.
- Ensure controls are keyboard accessible.
- Provide visible focus states.
- Do not communicate selection using colour alone.
- Use accessible labels for form fields and controls.
- Respect reduced-motion preferences for animations where practical.

### 7.3 Responsiveness

- Support common desktop and mobile viewport sizes.
- Avoid horizontal scrolling.
- Ensure the preview and controls remain usable on small screens.

### 7.4 Reliability

- All primary buttons must perform their stated actions.
- State must persist while navigating through the design flow.
- The demo must not depend on external services for core functionality.
- Provide sensible defaults so a user can complete the journey quickly.

### 7.5 Privacy and security

- Use fictional data only.
- Do not collect real financial, identity or payment information.
- Do not implement real payment processing or credit applications.
- Do not expose secrets or API keys in client-side code.

---

## 8. Technical requirements

The prototype will be built using Claude-assisted development and GitHub.

#### Implementation principles

- Choose a straightforward frontend stack supported by the existing project environment.
- Reuse existing project configuration where possible.
- Use reusable components for the card preview, feature tiles and navigation.
- Keep the user configuration in application state.
- Avoid introducing a backend unless it is necessary for an optional feature.
- Ensure the application can run locally and be demonstrated reliably.

#### Suggested component structure

- `LandingPage`
- `CardDesigner`
- `CardPreview`
- `FeatureSelector`
- `FormatSelector`
- `ProgressIndicator`
- `CardSummary`
- `FinalReveal`

Component names may be adapted to the chosen framework.

#### Suggested application state

Maintain a single card configuration object containing:

- `cardName`
- `cardColour`
- `cardFinish`
- `selectedFeatures`
- `cardFormat`

Use sensible defaults for optional values.

#### Persistence

For the MVP, in-memory state is sufficient. Browser storage can be added if time permits, but is not required.

---

## 9. Out of scope

The following are explicitly excluded from the hackathon MVP:

- Real bank accounts.
- Credit applications and affordability assessments.
- Credit scoring or eligibility decisions.
- Actual payment processing.
- Real credit limits, APR calculations or financial advice.
- Actual Apple Pay or Google Wallet provisioning.
- Live cashback or rewards transactions.
- Real customer authentication.
- Production data storage.
- Integration with banking systems.

Any fees, rates, rewards or benefits displayed must be labelled as fictional or illustrative.

---

## 10. Measurement and evaluation

As this is a hackathon prototype, success should be assessed through demonstration and basic usability rather than commercial performance.

#### Evaluation criteria

Journey completion: Can someone complete a design without help?

Customisation quality: Does the preview respond correctly to user choices?

Clarity: Can users understand the difference between the available feature categories?

Consistency: Does the finished card match the selected configuration?

Visual quality: Does the experience feel cohesive and presentation-ready?

Technical reliability: Can the core flow be demonstrated without errors?

If time allows, ask a colleague to complete the journey and observe where they hesitate.

---

## 11. Delivery plan

### Phase 1: Foundation

- Inspect the existing project.
- Confirm the framework and run commands.
- Establish the visual foundation.
- Create the landing page and application structure.

### Phase 2: Core functionality

- Implement the live card preview.
- Implement colour and name customisation.
- Implement feature selection.
- Implement format selection.
- Add navigation and state persistence.

### Phase 3: Completion

- Build the final reveal and summary.
- Add edit and reset functionality.
- Test the entire journey.
- Check desktop and mobile layouts.

### Phase 4: Polish

- Refine typography, spacing and card styling.
- Add subtle transitions.
- Implement “Surprise me” if time allows.
- Prepare a reliable demonstration path.

Phases are prioritised in order. The AI feature must not delay completion of the core experience.

---

## 12. Acceptance checklist

The MVP is ready to present when all mandatory items are complete.

- [ ] NORTH branding and tagline are visible.
- [ ] Landing page CTA opens the designer.
- [ ] Users can choose from at least five card colours.
- [ ] Users can personalise the card name.
- [ ] The live preview updates immediately.
- [ ] Users can select multiple feature categories.
- [ ] Users can choose physical, digital-only or both.
- [ ] User selections persist throughout the journey.
- [ ] The final reveal displays the correct configuration.
- [ ] Users can edit their card.
- [ ] Users can start again.
- [ ] Core buttons and controls work.
- [ ] The website is responsive.
- [ ] The demo works without a live banking integration.

---

## 13. Three-minute presentation plan

### 0:00–0:30 | The opportunity

“Traditional credit cards come in predefined packages. NORTH explores a different idea: what if customers could design a card around their own personality and priorities?”

### 0:30–2:00 | The demonstration

- Introduce the card studio.
- Change the colour and personalise the name.
- Select feature categories.
- Choose the card format.
- Reveal the finished card.
- Demonstrate AI personalisation if available.

### 2:00–3:00 | The bigger picture

“This prototype brings together visual personalisation and flexible feature selection. The longer-term opportunity is to explore how financial products can feel more relevant and engaging without making the experience more complicated.”

Close with the finished card on screen and the tagline:

NORTH. Your money. Your rules. Your card.

---

## 14. Instructions for the AI development assistant

Treat this PRD as the source of truth for the prototype.

Start by inspecting the existing repository and identifying the current framework, project structure and available scripts.

Then:

1. Recommend the simplest implementation approach that fits the existing project.
2. Build the mandatory MVP features in priority order.
3. Make sensible design decisions without requiring approval for every detail.
4. Keep the visual design polished and the interactions functional.
5. Test the complete user journey and fix errors before adding optional features.
6. Add the AI-assisted concept generation only after the core flow works.
7. Explain any commands or manual steps I need to perform.
8. Help prepare the finished project for a live three-minute demonstration.

Do not stop at a static mockup or a list of suggestions. Implement a working website, verify its functionality and prioritise a complete, cohesive experience over unnecessary complexity.

The final deliverable should be a polished, interactive NORTH Card Studio prototype that can be run locally and presented confidently at the end of the hackathon.
