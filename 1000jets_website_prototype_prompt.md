# 1000jets.com Website Prototype Prompt
## Build a High-Converting Landing & Booking Experience

---

## PROJECT OVERVIEW

**Project Name:** 1000jets.com - Website Prototype
**Brand Tagline:** "Private Aviation. Transparent. Accessible."
**Brand Promise:** Book Today, Fly Today — Guaranteed same-day confirmation within 4 hours

**Goal:** Build a memorable, conversion-focused website that positions 1000jets as the technology-first, transparent alternative to legacy brokers (NetJets, Flexjet, Wheels). The site must serve three core audiences with differentiated messaging while maintaining visual and functional consistency.

---

## CORE VALUE PROPOSITIONS

1. **Transparent All-In Pricing** — No hidden fees. Every quote shows base charter cost, fuel, airport handling, and platform fee separately.
2. **Same-Day Booking Guarantee** — Quote to confirmation within 4 hours, or money back. Powered by real-time aircraft availability.
3. **Technology-First Experience** — Mobile-friendly booking flow. Real-time search. Instant quotes. Digital contracting.

---

## THREE CORE AUDIENCES

### Audience 1: Tech-Savvy Founders & Young Entrepreneurs
- **Profile:** Age 28-42, $5M-50M net worth (self-made), check size $15K-40K per trip
- **Psychology:** Value time over money. Impatient with process. Want proof of speed & transparency.
- **Key Messaging:**
  - "Book in 3 minutes from your phone"
  - "See all-in pricing upfront"
  - "Guarantee: 4-hour confirmation or refund"
- **Design Tone:** Modern, data-driven, minimal friction, dark mode native
- **Call-to-Action:** "Search Flights" → immediate availability + price breakdown

### Audience 2: Old Money & Legacy Wealth
- **Profile:** Age 55-75, $50M+ net worth (inherited/established business), check size $50K+ per trip
- **Psychology:** Prefer safety & heritage. Value relationships. Skeptical of technology but respect efficiency. Don't want surprises.
- **Key Messaging:**
  - "Certified. Audited. Transparent."
  - "37 years of combined aviation expertise on our safety team"
  - "Your flight details itemized, explained"
- **Design Tone:** Refined, trustworthy, data-transparent, emphasize credentials & compliance
- **Call-to-Action:** "Get a Quote" → detailed breakdown + safety credentials visible upfront

### Audience 3: Corporate & Executive Teams
- **Profile:** Finance managers, C-suite travel, recurring contracts, check size $100K-$500K+ annually
- **Psychology:** Need audit trails, reporting, budget visibility, volume discounts, white-glove service.
- **Key Messaging:**
  - "Every flight itemized for accounting"
  - "Annual contracts with volume savings"
  - "Real-time spend analytics dashboard"
- **Design Tone:** Professional, data-focused, process-driven, emphasize reporting & compliance
- **Call-to-Action:** "Corporate Packages" → pricing tiers, case studies, ROI calculator

---

## INFORMATION ARCHITECTURE

### Navigation Structure (Desktop & Mobile)

**Primary Navigation:**
- Logo/Home
- Search Flights (prominence: hero CTA)
- How It Works (2-min explainer, safety credentials, pricing model)
- Corporate (dedicated page: pricing, contracts, case studies, ROI)
- Membership (tier info: costs, benefits, empty-leg access)
- About (team, safety record, sustainability)
- Account / Sign In

**Secondary Navigation (Footer):**
- Legal (Privacy, Terms, Safety, Compliance)
- Support (Contact, FAQ, Flight Tracking)
- Social (LinkedIn, Twitter, Instagram)

---

## PAGE STRUCTURE & CONVERSION FLOW

### 1. HOMEPAGE
**Goal:** Segment audiences → route to appropriate flow

**Above the Fold (Hero):**
- Headline: "Private Aviation. Transparent. Accessible."
- Subhead: "Book Today, Fly Today — 4-hour guarantee"
- Hero CTA: "Search Flights" (primary) + "See How It Works" (secondary)
- Visual: Dynamic map showing live available aircraft (or animation of booking flow)
- Real-time trust signal: "347 flights booked this week" (live counter)

**Section 2: Three Value Propositions (Repeating Tiles)**
```
1. ALL-IN PRICING
   Icon: Receipt/List
   Headline: "No hidden fees. Ever."
   Body: "Base charter + fuel + handling + our fee. All shown before you book."
   CTA: "See Example Pricing →"

2. 4-HOUR GUARANTEE
   Icon: Stopwatch
   Headline: "Same-day. Guaranteed."
   Body: "Quote to confirmation in 4 hours or less, or your booking fee is waived."
   CTA: "How It Works →"

3. AIRCRAFT VERIFIED
   Icon: Checkmark/Shield
   Headline: "Safety-first operations."
   Body: "All operators FAA-certified, IS-BAO audited, turbine coverage insured."
   CTA: "Our Standards →"
```

**Section 3: Social Proof & Trust Signals**
- Testimonial cards (3-4) from verified founders, CFOs, executives
- Stats row: "347 flights | 92% on-time | 4.8/5 ⭐"
- Certifications row: FAA | IS-BAO | Wyvern | ARGUS
- Featured in: TechCrunch, Forbes, Aviation Week (logos)

**Section 4: How Pricing Works (Interactive)**
- Headline: "See your full breakdown before booking"
- Interactive accordion/tabs showing:
  - Empty leg example ($14,200 total breakdown)
  - Standard charter example ($35,500 total breakdown)
  - Corporate monthly package example
- Each shows: Base rate → Fuel → Handling → 1000jets fee = Total (in monospace)

**Section 5: CTA Section**
- "Ready to fly?"
- Split CTAs based on implied audience:
  - Founders/Young: "Search Flights Now" (dark button, fast path)
  - Corporate: "Book a Corporate Package" (outline button)
  - Unknown: "Get a Quote" (leads to form)

**Bottom: Newsletter Signup**
- "Empty legs & last-minute deals"
- Email input + "Notify Me" button

---

### 2. SEARCH/BOOKING FLOW (MVP for prototype)
**Goal:** Show the speed & transparency promise in real time

**Step 1: Trip Details**
- Departure city (autocomplete)
- Arrival city (autocomplete)
- Date (calendar picker, minimum 4 hours from now)
- Return? (toggle)
- Passengers (stepper: 1-19)
- CTA: "Search" (primary navy)

**Real-Time Results:**
- Live availability grid showing:
  - Aircraft type (Citation Latitude, Gulfstream G650, etc.)
  - Seats, range, speed
  - Price (all-in, no asterisks)
  - "Empty leg" badge (if applicable)
  - "Verified operator" trust badge
  - CTA: "Book Now" or "Details"

**Aircraft Detail View:**
- Aircraft photo/specs (seats, range, speed, cabin amenities)
- Full pricing breakdown (monospace ledger):
  - Charter base rate
  - Fuel surcharge
  - Airport & handling fees
  - 1000jets platform fee (7%)
  - **= Total**
- Safety credentials (operator FAA cert, last inspection, insurance)
- Booking CTAs:
  - "Confirm Booking" (primary)
  - "Contact Concierge" (secondary)

**Booking Confirmation:**
- Order summary (ledger format, identical to quote)
- Account creation / Login (optional for guests)
- Payment method selection
- Sign & confirm (digital signature)
- Confirmation email with flight details, concierge contact

---

### 3. HOW IT WORKS PAGE
**Goal:** Build confidence in process & safety for old-money and corporate audiences

**Section 1: The 3-Step Process**
```
Step 1: SEARCH & QUOTE
  "Get real-time availability and transparent all-in pricing in seconds."
  Visual: Screenshot of search results with pricing breakdown

Step 2: REVIEW & CUSTOMIZE
  "See your complete cost breakdown, adjust dates/passengers, view safety credentials."
  Visual: Screenshot of booking detail page with ledger visible

Step 3: BOOK & FLY
  "Sign your contract digitally, receive confirmation, fly on your schedule."
  Visual: Timeline showing 4-hour window
```

**Section 2: Safety & Compliance**
- Headline: "Aviation safety, radiating out from every flight"
- Four cards:
  1. **Operator Vetting:** All operators pass FAA checks + IS-BAO audit + Wyvern review
  2. **Aircraft Maintenance:** Real-time maintenance logs visible to customers (verified by operator)
  3. **Insurance & Liability:** Full turbine coverage, $100M+ in liability per flight
  4. **Crew Professionalism:** All crews are professional, required to pass background checks and FAA certifications (note: do NOT claim crew credentials visible, just professional standards)

**Section 3: Why 4 Hours?**
- Explainer: How we guarantee speed
- Real backend (simplified): API connection to 150+ verified operators in real-time
- No phone calls, no manual quotes
- Instant contract generation + digital signing

**Section 4: Empty Legs Explained**
- Definition: Aircraft repositioning flights (you get 30-50% savings)
- How we find them: AI scans operator schedules 24/7
- Example: Citation Latitude LAX→NYC normally $28K, empty leg $14.2K
- Transparency: You always know why the discount (repositioning flight, not discounted service)

---

### 4. CORPORATE PAGE
**Goal:** Lock enterprise contracts with ROI clarity

**Hero:**
- Headline: "Corporate aviation that doesn't hide its costs"
- Subhead: "Volume discounts. Audit-ready reporting. Dedicated support."
- CTA: "Get a Corporate Quote"

**Section 2: Pricing Tiers**
```
Three-column grid:

STARTUP PACK
  • Up to 10 flights/year
  • Base rate + 7% platform fee
  • Monthly spend reports
  • $X monthly commitment
  → "Get Started"

ENTERPRISE
  • Up to 50 flights/year
  • Base rate + 5% platform fee (volume discount)
  • Real-time spend dashboard
  • Dedicated account manager
  • $X monthly commitment
  → "Contact Sales"

UNLIMITED
  • Unlimited flights/year
  • Custom pricing (negotiated)
  • Full spend analytics, seat utilization, ROI per employee
  • White-glove concierge
  → "Contact Sales"
```

**Section 3: Why 1000jets for Corporates?**
- Card 1: "Every expense auditable" — Itemized ledger on every flight for finance teams
- Card 2: "No surprise fees" — All costs quoted upfront, contracts locked in
- Card 3: "Usage analytics" — Dashboard showing spend by department, ROI per flight
- Card 4: "Preferred operators" — Dedicated pool of 50+ vetted operators, all background-checked

**Section 4: Case Study / ROI Calculator**
- Company: [Fictitious startup / real-sounding]
- Challenge: Executives burning out on commercial travel, losing deals
- Solution: 1000jets enterprise contract (20 flights/quarter)
- Result: "35% time savings on travel, 4 deals closed mid-flight, $450K annual platform savings vs NetJets"
- Interactive: "Calculate your potential savings" (inputs: current spend, flights/year)

**Section 5: CTA**
- "Schedule a corporate flight audit"
- Email + phone + timezone dropdown

---

### 5. MEMBERSHIP PAGE
**Goal:** Drive recurring revenue through tiered loyalty

**Hero:**
- Headline: "Fly more, save more"
- Subhead: "Status tiers unlock discounts and empty-leg access"

**Three Membership Tiers:**
```
BRONZE (Free)
  • Base pricing
  • 90-day advance notice to empty legs
  • Mobile booking
  • Monthly spend reports
  → "Join Free"

SILVER ($99/month)
  • 5% discount on all flights
  • 7-day early access to empty legs
  • Lounge access (partner airports)
  • 1000 annual points (1 point = $1 off future flights)
  → "Upgrade to Silver"

GOLD ($299/month)
  • 12% discount on all flights
  • 24-hour early access to empty legs
  • Priority concierge line
  • 3000 annual points
  • Quarterly status bonus flights
  → "Upgrade to Gold"
```

**Section 2: How Empty Legs Work**
- Definition & savings potential (30-50% off standard charter)
- Tiered access (Bronze = 90 days out, Silver = 7 days, Gold = 24 hours)
- Visual: "Last-minute savings" examples

**Section 3: Points Program**
- Earn: 1 point per $1 spent
- Redeem: $1000 points = $100 off
- Bonus: Status milestones (reach Silver → bonus 500 points, reach Gold → bonus 1500 points)

---

### 6. ABOUT PAGE
**Goal:** Build heritage & trustworthiness for old-money segment

**Hero:**
- Headline: "Flying private. Without the black box."
- Subhead: "37 years of combined aviation expertise. 150+ verified operators. Zero hidden fees."

**Section 2: The Team**
- 4-5 key people (photo, name, title, background)
- Founder/CEO (aviation background or tech? + years in aviation)
- Chief Operations Officer (aviation veteran, 20+ years)
- Chief Pilot / Safety Officer (former airline captain, 30+ years)
- Head of Compliance (aviation attorney, 15+ years)

**Section 3: Safety Record**
- Stat: "0 incidents across 3,247 bookings"
- Certification breakdown: 150+ operators, 100% FAA certified, 100% IS-BAO compliant
- Insurance: $100M+ per flight coverage
- Maintenance: All aircraft pass pre-flight inspections verified by third-party technicians

**Section 4: Sustainability**
- "We offset 100% of flight emissions through Carbonfund partnerships"
- SAF (Sustainable Aviation Fuel) discount: "Choosing SAF-compatible aircraft saves you $X and the planet"
- Carbon stats: "X metric tons offset this year"

**Section 5: Press & Recognition**
- Logo strip: TechCrunch | Forbes | Aviation Week | Wall Street Journal (or similar)
- Quote carousel (2-3 press highlights)

---

## DESIGN SPECIFICATIONS (Using Existing Design System)

### Color Application
- **Navy (#0B2540):** Primary buttons, headers, navigation, trusted elements
- **Brass (#C08A28):** Secondary CTAs, premium highlights, accent elements
- **Teal (#0B8A9B):** Trust badges, verified operators, transparency signals
- **Error (#D64545):** Warnings, limited availability
- **Success (#1D9A6C):** Confirmation, booking complete
- **Amber (#FFB238):** Urgency, "empty leg" badges, time-sensitive offers

### Typography Application
- **Fraunces (Display font):** Page headlines (H1, H2), brand moments
- **Inter (Body font):** Navigation, body copy, CTAs, form labels
- **IBM Plex Mono:** All pricing numbers, ledgers, confirmation codes, data

### Component Patterns
- Jet card (aircraft availability): Image placeholder → Aircraft name → Specs → Price (monospace) → CTA
- Stat card: Large number (monospace) + label below
- Ledger (pricing breakdown): Monospace rows with left-aligned label, right-aligned amount, final total with top border
- Badge: "Empty leg" (amber), "Verified operator" (teal), "4-hour guarantee" (brass)
- Button states: Default, Hover (darker/more shadow), Active, Disabled (grayed)

### Responsive Behavior
- **Mobile (320px-640px):** Single column, full-width CTAs, touch-friendly 44px button heights, collapsible nav
- **Tablet (641px-1024px):** Two columns where appropriate, grid layouts adjust
- **Desktop (1025px+):** Full 3-column grids, sticky header, hover states visible

### Dark Mode
- Dark mode toggle (bottom-right corner of page)
- Navy → Nearly-black (#0B0E13) for backgrounds
- Text → Light gray (#EDEFF3)
- Accents (brass, teal) remain consistent
- All contrast ratios maintained (WCAG AA)

---

## HIGH-CONVERSION PRINCIPLES

### Audience Routing
- First visitor → Show hero with all three CTAs (Search, Quote, Corporate)
- Return visitor (identified by cookie/login) → Route to personalized dashboard

### Friction Reduction
- Search results appear instantly (no loading states, pre-load data)
- Price ledger visible immediately (no "click for pricing" pattern)
- Booking flow is 3 steps max (Trip → Review → Confirm)
- Mobile-optimized throughout (assume founder is booking from phone)

### Trust Signals, Placed Strategically
- Safety credentials appear in search results (verified operator badge)
- Pricing breakdown visible before clicking "book"
- Team bios (especially safety officer background) on about page
- Press logos + quote carousel on homepage and about page
- Real-time booking counter ("347 flights booked this week")

### Retention Patterns
- Membership tiers incentivize repeat bookings (5%, 12% discounts)
- Empty-leg early access creates urgency (FOMO)
- Points program gamifies spending
- Email reminders for saved trips or favorite routes

### Copy Principles
- Avoid jargon: "All-in pricing" not "bundled services"
- Emphasize speed: "4-hour guarantee," "Search in 3 minutes"
- Emphasize transparency: "See your breakdown," "No hidden fees"
- Personalize to audience: Founders get "fast path," corporates get "ROI," old money gets "safety."

---

## PROTOTYPE DELIVERY CHECKLIST

### Pages to Build (HTML/CSS)
- [ ] Homepage (hero + sections outlined above)
- [ ] Search Results (live availability mock)
- [ ] Aircraft Detail & Booking Flow (3-step modal)
- [ ] How It Works (explainer sections)
- [ ] Corporate Page (tier comparison + calculator)
- [ ] Membership Page (tier cards)
- [ ] About Page (team + safety record)
- [ ] Footer (consistent across all pages)

### Interactive Elements
- [ ] Working search form (client-side demo, no backend required)
- [ ] Functioning price ledger (shows breakdown, updates dynamically)
- [ ] Responsive navigation (hamburger menu on mobile)
- [ ] Dark mode toggle (switches all CSS variables)
- [ ] Tab switching (How It Works sections, membership tier details)
- [ ] Modal for booking flow (3-step process visible)
- [ ] Smooth scroll navigation (anchor links to sections)

### Design System Integration
- [ ] All colors using CSS variables (--navy-900, --brass-500, etc.)
- [ ] Typography using specified fonts (Fraunces, Inter, IBM Plex Mono)
- [ ] Shadow system applied (--sh-1, --sh-2 for cards)
- [ ] Spacing consistent (multiples of 8px)
- [ ] Border radius consistent (--r-md, --r-lg)

### Mobile & Accessibility
- [ ] Fully responsive (tested at 320px, 640px, 1024px, 1440px)
- [ ] Touch-friendly buttons (44px minimum height)
- [ ] Keyboard navigation (tab order logical, focus visible)
- [ ] Color contrast passing WCAG AA (4.5:1 minimum)
- [ ] Alt text on all images
- [ ] Semantic HTML (headings, nav, main, footer landmarks)

### Performance & Polish
- [ ] CSS variables documented
- [ ] Dark mode fully supported
- [ ] Smooth animations (300ms transitions, ease timing)
- [ ] No placeholder images (use gradient backgrounds or icons)
- [ ] Loading states minimal (emphasize instant results)

---

## TONE & VOICE

- **Professional but not stiff.** Trustworthy without being corporate-speak.
- **Data-driven.** Show numbers, show breakdowns, show credentials.
- **Transparent.** No hidden fees, no hidden complexity. Ledgers are your best friend.
- **Ambitious for the customer.** Position 1000jets as "your time is worth more than gold."
- **Segmented by audience.** Use the same design language, but adapt messaging: founders see speed, legacy sees safety, corporates see audit trails.

---

## SUCCESS METRICS (Post-Launch, Not for Prototype)

- Conversion rate (visitor → booking): Target 2-3%
- Search-to-quote time: < 10 seconds
- Quote-to-booking time: < 4 hours (guarantee)
- Repeat booking rate: 25% within 6 months
- Membership sign-up rate: 40% of new customers
- Corporate pipeline: $XXX MRR from contracts

---

## NOTES FOR CLAUDE DESIGN / DEVELOPER

1. **No backend required** — Prototype uses mock data for search results, pricing, and bookings.
2. **Use provided design system** — Reference the existing 1000jets Design System HTML for colors, typography, components.
3. **Prioritize speed** — Don't over-engineer animations; focus on conversion flow.
4. **Make it real** — Use realistic aircraft names, pricing, routes (LAX↔NYC, SF→Miami, etc.).
5. **Show the ledger** — Every example should include the monospace price breakdown. This is the brand differentiator.
6. **Mobile-first mindset** — Build for 375px viewport first, then enhance for desktop.
7. **Dark mode is built-in** — Include the theme toggle from day one; it's part of the brand promise (tech-first).

---

**Ready to build. Let's make private aviation transparent.**
