# North Card Builder

Clickable prototype for **North**, a fictional app-first bank where customers design their own credit card.

Built for a work hackathon. North is not a real bank, and every rate, limit, fee and perk value is illustrative.

## The flow

1. **Landing**: "A credit card built around how you live."
2. **Let's get to know you**: one question at a time covering what matters most, age and UK residency, employment, income, rent or mortgage, and any CCJs. A "Building your card" screen then shows a simulated soft-search result.
3. **Pick 3 perks**: a spend slider estimates what your perks are worth per year, after fees.
4. **Design**: colour, pattern, finish, orientation and the name on the card.
5. **Review**: a summary with credit limit and representative APR, then apply.
6. **Card ready**: the card drops into your phone wallet.

## Product requirements

[`overview.html`](overview.html) is a one-page summary: who it's for, the problem, what it does, and a button and QR code to open the app.


The full PRD lives in [`docs/PRD.md`](docs/PRD.md). It's also published on the site as [`prd.html`](prd.html), linked from the landing page.

After editing the Markdown, regenerate the page with `python3 tools/build_prd.py .` (needs `pip install markdown`).

## Run it

It's a single static file. Open `index.html` in a browser, or serve the folder with any static host such as GitHub Pages.
