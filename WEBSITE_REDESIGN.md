# AstraGuard Website Redesign - Round 2 Proposal

**Objective:** Redesign AstraGuard into a website experience that feels smart, real, and technically grounded.

---

## User Experience Pillars

1. **Instant Comprehension** - Understand the product in under 10 seconds
2. **Visible Intelligence** - Show reasoning, not just results
3. **Memory as a Feature** - Make adaptive memory tangible and visual
4. **Security-First but Human-Friendly** - Confident, not intimidating
5. **Fast and Lightweight** - Real-time feel without heavy animations or clutter

---

## Information Architecture

### 1. Homepage

#### Hero Section
**Headline:**
```
AstraGuard watches streams, remembers patterns, and responds in seconds.
```

**Subtext:**
```
Live input → Anomaly detection → Memory recall → Intelligent decision → Automated action

AstraGuard doesn't just detect. It decides and acts, with memory of what came before.
The system learns from streams, not snapshots. It forgets safely, remembers intelligently, 
and responds automatically.
```

#### Live Element (Lightweight)
- Minimal real-time log ticker with monospaced font
- Subtle waveform that pulses when anomalies detected
- No heavy animations, just clean visual feedback

#### CTAs
- **Dashboard** (primary - large button)
- **Memory Layer** (secondary)
- **Architecture** (secondary)
- **Use Cases** (tertiary)

---

### 2. Live Dashboard (Main Product Experience)

#### 5-Panel Connected Layout

```
┌─────────────────────────────────────────────────────────────────────┐
│                        ASTRAGUARD DASHBOARD                          │
├──────────────────────┬──────────────────────┬───────────────────────┤
│   STREAM FEED        │   ANOMALY RADAR      │   MEMORY GRAPH        │
│                      │                      │                       │
│ > voltage: 7.2V ⚠️   │        ▲             │      ●━━━●            │
│ > temp: 28.5°C       │       ╱ ╲            │     ╱      ╲          │
│ > gyro: 0.02 rad/s   │      ╱   ╲           │    ●        ●         │
│ > current: 1.1A      │     ╱     ╲          │   Past    Similar     │
│ > wheel: 5000 RPM    │    ╱       ╲         │  Anomaly  Incidents   │
│                      │   ╱         ╲        │                       │
│ [Live ticker scroll] │  [Real-time spikes]  │ [Node-based visual]   │
├──────────────────────┴──────────────────────┴───────────────────────┤
│                     REASONING CONSOLE                                │
│                                                                      │
│ 🧠 Agent Decision:                                                   │
│ Voltage drop detected (7.2V < 7.3V threshold). Similar incident     │
│ occurred 2 days ago with successful auto-recovery. Memory match      │
│ score: 0.87. High confidence (94%). Severity: HIGH.                  │
│                                                                      │
│ Chosen Response: IMMEDIATE_RECOVERY                                  │
│ [Expand Reasoning ▼]                                                 │
├──────────────────────────────────────────────────────────────────────┤
│                    RESPONSE ORCHESTRATOR                             │
│                                                                      │
│ ● Queued → ● Running → ● Resolved → ● Learned into Memory           │
│                                                                      │
│ Action: Safe mode activated                                          │
│ Status: ✅ Resolved (2.1s)                                            │
│ Cooldown: 30s remaining                                              │
└──────────────────────────────────────────────────────────────────────┘

METRICS BAR:
┌──────────────┬──────────────┬──────────────┬──────────────┬──────────────┐
│ Confidence   │ Severity     │ Recurrence   │ Memory Match │ Time to      │
│    94%       │    HIGH      │     3x       │    0.87      │ Decision     │
│              │              │              │              │   325ms      │
└──────────────┴──────────────┴──────────────┴──────────────┴──────────────┘
```

#### Dashboard Features
- **Decision Trace:** Natural language, not JSON
- **Action Status Badges:** Queued → Running → Resolved → Learned
- **Timeline Slider:** Replay past incidents like a security flight recorder
- **Reasoning Toggle:** Expand to see full LLM explanation

---

### 3. Adaptive Memory Page

#### Interactive Memory Timeline

```
MEMORY TIMELINE (Horizontal Scroll)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━→ Time

7 days ago          5 days ago        2 days ago         Now
    ○ ─ ─ ─            ●━━━━━            ⭐━━━━━━━         [Live]
  (fading)          (recurring)        (critical)
  
  Old Anomaly       Repeated Event    Pinned Incident
  Decay: 0.3        Weight: 0.9       Permanent
  
  [Hover to see details]
```

#### Hover Card Example
```
┌─────────────────────────────────────┐
│ Power Fault - 2 days ago            │
│                                     │
│ Description: Voltage drop to 6.8V   │
│ Why stored: Critical severity       │
│ Action taken: Auto-recovery         │
│ Decision time: 1.8s                 │
│ Recurrence: 3x in last week         │
│                                     │
│ Memory weight: 0.87 (high)          │
└─────────────────────────────────────┘
```

#### Decay Curve Visualization
```
Importance
    ▲
1.0 │⭐━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ (Critical - pinned)
    │
0.8 │    ●━━━━━━━━━━━━━━━━━━━━━━━━━ (Recurring - reinforced)
    │
0.6 │
    │
0.4 │        ○ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ (Old - fading)
    │
0.2 │                ○ ─ ─ ─ ─ ─ ─ ─ (Very old - nearly gone)
    │
0.0 └────────────────────────────────────────────────────────→ Time
```

**Bottom Takeaway:**
```
Memory updates itself. No manual tagging. 
What repeats matters more. What's irrelevant decays away.
```

---

### 4. System Architecture Page

#### Clean Vertical Flow Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    PATHWAY STREAM                            │
│                 Handles the live stream                      │
│              (Telemetry, logs, events)                       │
└──────────────────────┬──────────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────────────────┐
│                   EMBEDDING ENCODER                          │
│            Converts events to vector space                   │
│                  (< 20ms latency)                            │
└──────────────────────┬──────────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────────────────┐
│                 ADAPTIVE MEMORY STORE                        │
│        Auto-updates with time + recurrence weights           │
│         Decay curves prune safely, critical stays            │
└──────────────────────┬──────────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────────────────┐
│                  REASONING AGENT                             │
│              Reasons before acting, not just                 │
│               classifying. LLM-assisted.                     │
└──────────────────────┬──────────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────────────────┐
│                  RESPONSE ENGINE                             │
│         Triggers workflows, monitors execution               │
│              Actions feed back into memory                   │
└──────────────────────┬──────────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────────────────┐
│                   DASHBOARD UI                               │
│           Real-time observability and control                │
└─────────────────────────────────────────────────────────────┘
```

**Annotations (No Jargon):**
- Pathway handles the stream continuously
- Memory auto-updates with temporal weighting
- Agent reasons before acting, explains decisions
- Actions feed back into memory when useful
- Sub-2-second end-to-end latency

---

### 5. Impact & Use Cases

#### Use Case Cards

**1. Satellite Fault Defense**
```
┌────────────────────────────────────────────────────────────┐
│ 🛰️ SATELLITE FAULT DEFENSE                                 │
│                                                            │
│ Problem: CubeSats operate autonomously with limited        │
│ ground contact. Faults escalate quickly.                   │
│                                                            │
│ Why real-time + memory: Prevents recurring issues,         │
│ enables predictive maintenance based on patterns.          │
│                                                            │
│ Expected latency: < 2s detection to recovery               │
│ Automated action: Safe mode, system reset, alert           │
└────────────────────────────────────────────────────────────┘
```

**2. Security Log Intrusion Auto-Response**
```
┌────────────────────────────────────────────────────────────┐
│ 🔒 SECURITY LOG INTRUSION AUTO-RESPONSE                    │
│                                                            │
│ Problem: Millions of log entries daily. Intrusions         │
│ spread fast if not caught immediately.                     │
│                                                            │
│ Why real-time + memory: Recognizes attack pattern          │
│ variations, learns new signatures without manual rules.    │
│                                                            │
│ Expected latency: < 500ms detection to containment         │
│ Automated action: Isolate node, block IP, escalate         │
└────────────────────────────────────────────────────────────┘
```

**3. IoT Anomaly-Triggered Recovery**
```
┌────────────────────────────────────────────────────────────┐
│ 📡 IOT ANOMALY-TRIGGERED RECOVERY                          │
│                                                            │
│ Problem: Connected devices vulnerable to coordinated       │
│ attacks. Lateral movement spreads rapidly.                 │
│                                                            │
│ Why real-time + memory: Correlates multi-stage attacks,    │
│ prevents network-wide compromise.                          │
│                                                            │
│ Expected latency: < 1s detection to isolation              │
│ Automated action: Device quarantine, network segment       │
└────────────────────────────────────────────────────────────┘
```

**4. Fraud Pattern Memory Learning**
```
┌────────────────────────────────────────────────────────────┐
│ 💳 FRAUD PATTERN MEMORY LEARNING                           │
│                                                            │
│ Problem: Fraud patterns evolve constantly. Static rules    │
│ become obsolete quickly.                                   │
│                                                            │
│ Why real-time + memory: Adapts to new fraud tactics,       │
│ remembers successful detection patterns.                   │
│                                                            │
│ Expected latency: < 300ms detection to flag                │
│ Automated action: Transaction hold, user verification      │
└────────────────────────────────────────────────────────────┘
```

---

## Out-of-the-Box UX Elements

### Security Flight Recorder

**Purpose:** Replay past anomaly sequences like a black box recorder

```
INCIDENT REPLAY: Power Fault - Dec 23, 14:32:15
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Timeline:
14:32:15.000  Stream: voltage=7.8V, temp=28°C, gyro=0.02
14:32:15.200  Stream: voltage=7.2V ⚠️ (threshold breach)
14:32:15.250  Anomaly detected (confidence: 94%)
14:32:15.300  Memory retrieval: 3 similar incidents found
14:32:15.400  Reasoning: High confidence, recurring pattern
14:32:15.500  Decision: IMMEDIATE_RECOVERY
14:32:15.600  Action triggered: Safe mode activation
14:32:17.100  Action resolved: System recovered
14:32:17.200  Memory updated: Incident stored with weight 0.87

Total time: 2.1 seconds
Outcome: ✅ Successful recovery

[◀ Previous] [▶ Next] [⏸ Pause] [⏩ Speed: 1x]
```

---

### Anomaly Constellation View

**Concept:** Space-inspired node constellation where anomalies form patterns

```
                    ⭐ Critical
                   ╱│╲
                  ╱ │ ╲
                 ╱  │  ╲
                ●───●───● Recurring cluster
               ╱     ╲
              ╱       ╲
             ●         ● Related incidents
            ╱           ╲
           ○             ○ Fading old events
          
[Hover any node to see incident details]
[Lines show memory similarity connections]
[Brightness indicates recurrence weight]
```

**Features:**
- Nodes auto-link based on memory similarity
- Constellation patterns reveal attack campaigns
- Zoom and pan for exploration
- Click node to jump to flight recorder view

---

### Reasoning Transparency Mode

**Toggle View:**

**Simple View (Default):**
```
Decision: IMMEDIATE_RECOVERY
Confidence: 94%
```

**Deep Reasoning View (Expanded):**
```
Decision: IMMEDIATE_RECOVERY
Confidence: 94%

Reasoning Trace:
1. Voltage drop detected: 7.2V < 7.3V threshold
2. Severity calculation: HIGH (critical system parameter)
3. Memory retrieval: Found 3 similar incidents
   - 2 days ago: voltage=7.1V, action=recovery, outcome=success
   - 5 days ago: voltage=7.0V, action=recovery, outcome=success
   - 7 days ago: voltage=6.9V, action=recovery, outcome=success
4. Pattern analysis: Recurring issue, successful recovery history
5. Confidence boost: Historical success rate 100%
6. LLM reasoning: "Based on recurring pattern and successful 
   recovery history, immediate action recommended with high 
   confidence. System has demonstrated resilience to this fault."
7. Decision: IMMEDIATE_RECOVERY (auto-triggered)
```

---

## UI Guidelines

### Layout
- Structured grids with clear hierarchy
- Readable density, no chaos
- Panels connect visually but remain distinct

### Typography
```css
--font-primary: 'Inter', sans-serif;
--font-mono: 'JetBrains Mono', monospace;
--font-display: 'Inter', sans-serif;

/* Hierarchy */
h1: 2.5rem, bold, letter-spacing: -0.02em
h2: 2rem, semibold
h3: 1.5rem, medium
body: 1rem, regular
code: 0.875rem, monospace
```

### Visual Motion
- Subtle real-time cues (pulse, fade, slide)
- Never overwhelming
- Performance-optimized (CSS transforms, GPU-accelerated)
- Respects `prefers-reduced-motion`

### Mobile Responsive
- Dashboard collapses to vertical stack
- Panels become accordion-style
- Touch-friendly controls
- Readable on small screens

### Accessibility
- Strong contrast (WCAG AAA where possible)
- Labels on every metric
- Keyboard navigable
- Screen reader friendly
- Focus indicators

---

## Tone for Copy

**Write like you're explaining to a sharp engineer:**

✅ Good:
- "AstraGuard doesn't just detect. It decides and acts, with memory of what came before."
- "The system learns from streams, not snapshots."
- "It forgets safely, remembers intelligently, and responds automatically."

❌ Avoid:
- "Revolutionary AI-powered platform"
- "Cutting-edge machine learning"
- "Next-generation technology"

---

## Example Decision Flows

### Flow 1: Power Fault Auto-Recovery

```
EVENT: Voltage drop to 7.2V
  ↓
ANOMALY DETECTION: Threshold breach (< 7.3V)
  ↓
MEMORY RECALL: 3 similar incidents, all resolved successfully
  ↓
REASONING: High confidence (94%), recurring pattern, proven recovery
  ↓
DECISION: IMMEDIATE_RECOVERY
  ↓
ACTION: Safe mode activation
  ↓
OUTCOME: System recovered in 2.1s
  ↓
MEMORY UPDATE: Incident stored with weight 0.87
```

### Flow 2: Unknown Anomaly Escalation

```
EVENT: Unusual gyro reading pattern
  ↓
ANOMALY DETECTION: Statistical outlier, no threshold breach
  ↓
MEMORY RECALL: No similar incidents found
  ↓
REASONING: Low confidence (62%), unknown pattern, requires human review
  ↓
DECISION: ALERT_ESCALATION
  ↓
ACTION: Notify operators, continue monitoring
  ↓
OUTCOME: Human confirms false positive
  ↓
MEMORY UPDATE: Pattern learned as benign, future confidence increased
```

---

## Deliverables Checklist for Round 2 Proposal

### Required Deliverables

- [x] **Homepage Mock Screenshot** - Hero section with live ticker
- [x] **Dashboard Layout Screenshot** - 5-panel connected view
- [x] **Memory Timeline Mock** - Interactive decay curve visualization
- [x] **Architecture Diagram** - Clean vertical flow with annotations
- [x] **Decision Flow Examples** - 2 plain-language flows (above)

### Additional Deliverables

- [x] **Security Flight Recorder** - Incident replay interface spec
- [x] **Anomaly Constellation View** - Space-inspired node graph
- [x] **Reasoning Transparency Mode** - Toggle between simple/deep views
- [x] **Use Case Cards** - 4 realistic scenarios with latency specs
- [x] **UX Pillars** - 5 core principles documented
- [x] **UI Guidelines** - Typography, motion, accessibility specs

---

## Implementation Notes

### Technology Stack
- **Frontend:** React + Next.js or Svelte for performance
- **Styling:** Tailwind CSS + custom components
- **Animations:** Framer Motion (lightweight)
- **Charts:** D3.js for memory graph, Recharts for metrics
- **Real-time:** WebSocket for live updates
- **Deployment:** Vercel (optimized static + serverless)

### Performance Targets
- First Contentful Paint: < 1s
- Time to Interactive: < 2s
- Lighthouse Score: > 95
- Bundle size: < 200KB gzipped

---

**Website Philosophy:**
```
The website mirrors the system's philosophy: real-time intelligence, 
evolving memory, and transparent decision making. Every UI element ties 
back to function, not fluff, and prioritizes usability, observability, 
and credibility.
```

---

**Repository:** https://github.com/sr-857/AstraGuard  
**Hackathon:** DataQuest 2026 Indian Institute of Technology (IIT), Kharagpur  
**Round:** 2 - Enhanced Proposal
