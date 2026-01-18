# AstraGuard Website Design Specification

**Project:** DataQuest 2026 Indian Institute of Technology (IIT), Kharagpur - AstraGuard Website  
**Purpose:** Present AstraGuard as an intelligent, real-time security agent platform  
**Target Audience:** Smart students, researchers, and engineers evaluating system design

---

## Design Principles

1. **Clean, focused, and fast to navigate**
2. **Prioritizes clarity over decoration**
3. **Explains what the system does and why it matters in simple terms**
4. **Includes visual cues showing real-time intelligence and adaptive memory**
5. **Maintains professional but approachable tone**

---

## Technical Stack

- **Frontend:** React / Next.js or Static HTML/CSS/JS
- **Styling:** Tailwind CSS or custom CSS with CSS Grid/Flexbox
- **Animations:** Framer Motion or CSS animations
- **Streaming Visuals:** Canvas API or SVG animations
- **Memory UI:** D3.js for node graphs or custom temporal charts
- **Deployment:** Vercel, Netlify, or GitHub Pages
- **Performance:** Optimized static build, lazy loading, CDN

---

## Color Palette

```css
/* Primary Colors */
--pathway-blue: #3535EE;
--pathway-red: #FF0000;
--bg-dark: #0A0A0F;
--bg-card: rgba(255, 255, 255, 0.03);

/* Text Colors */
--text-primary: #FFFFFF;
--text-secondary: #E0E0E0;
--text-muted: #9E9E9E;

/* Status Colors */
--status-critical: #FF0000;
--status-warning: #FFC107;
--status-success: #4CAF50;
--status-info: #2196F3;

/* Accent */
--accent-glow: rgba(53, 53, 238, 0.3);
```

---

## Page Structure

### 1. Homepage (`index.html`)

#### Hero Section
**Value Statement:**
```
Real-time anomaly detection. Memory-aware decisions. Automated response loops.
```

**Description:**
```
AstraGuard watches data streams, detects threats instantly, remembers past 
incidents intelligently, and decides the best response path in a tight loop. 
No manual refresh, no guesswork.
```

**CTA Buttons:**
- "View Live Dashboard" → `/dashboard`
- "System Architecture" → `/architecture`
- "How Memory Works" → `/memory`

**Hero Visuals:**
- Animated telemetry stream (scrolling data)
- Anomaly spike detection (red pulse on graph)
- Memory recall node (glowing connections)
- Response trigger (action indicator)

#### Features Grid
```
┌─────────────────┬─────────────────┬─────────────────┐
│  🔄 Real-Time   │  🧠 Adaptive    │  ⚡ Automated   │
│   Streaming     │    Memory       │   Response      │
│                 │                 │                 │
│ Pathway Engine  │ Temporal        │ < 2s Decision   │
│ processes data  │ weighting +     │ to Action       │
│ continuously    │ decay curves    │ latency         │
└─────────────────┴─────────────────┴─────────────────┘
```

---

### 2. System Architecture Page (`architecture.html`)

#### Architecture Diagram (Vertical Flow)
```
┌──────────────────────────────────────┐
│      Streaming Data (Telemetry)      │
│  Stream processed by Pathway Engine  │
└──────────────┬───────────────────────┘
               ↓
┌──────────────────────────────────────┐
│         Embedding Encoder             │
│   Lightweight model, < 20ms latency   │
└──────────────┬───────────────────────┘
               ↓
┌──────────────────────────────────────┐
│        Adaptive Memory Store          │
│ Memory updates automatically with     │
│ temporal weighting + decay curves     │
└──────────────┬───────────────────────┘
               ↓
┌──────────────────────────────────────┐
│       Anomaly Reasoning Agent         │
│  Agent reasons before acting,         │
│  doesn't just classify                │
└──────────────┬───────────────────────┘
               ↓
┌──────────────────────────────────────┐
│         Response Engine               │
│  Triggers workflows automatically     │
└──────────────┬───────────────────────┘
               ↓
┌──────────────────────────────────────┐
│      Dashboard & Observability        │
│   Real-time monitoring & transparency │
└──────────────────────────────────────┘
```

#### Key Specifications
- **End-to-End Latency:** < 2 seconds (target), ~325ms (actual)
- **Memory Updates:** Automatic, no manual refresh
- **Decision Transparency:** LLM-assisted reasoning output
- **Scalability:** Distributed Pathway workers
- **Reliability:** Fault tolerance + automatic failover

---

### 3. Adaptive Memory Page (`memory.html`)

#### Memory Design Visualization

**Concept Diagram:**
```
Timeline View:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━→ Time

Old Anomaly (faded):        ○ ─ ─ ─ (decay curve)
Recurring Anomaly (strong):  ●━━━━━━ (reinforced)
Critical Anomaly (pinned):   ⭐━━━━━━ (permanent)
```

**Memory Decay Formula:**
```
Memory_Weight(t) = Base_Importance × e^(-λ × age)

Where:
- λ = 0.1 (decay rate)
- age = current_time - event_time
- Base_Importance = severity score
```

**Key Features:**
1. **Vector Store:** Embeddings of past anomalies
2. **Temporal Weighting:** Recent events weighted higher
3. **Decay Curves:** Old events fade gracefully
4. **Smart Pruning:** Critical events never deleted
5. **Auto-Update:** Continuous learning

**Takeaway:**
```
The system remembers what matters, forgets what doesn't, 
and gets smarter with every new event.
```

---

### 4. Live Dashboard (`dashboard.html`)

#### Dashboard Layout

```
┌─────────────────────────────────────────────────────────┐
│  AstraGuard Live Dashboard                              │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  ┌──────────────────┐  ┌──────────────────┐            │
│  │ Incoming Stream  │  │ Anomaly Spikes   │            │
│  │                  │  │                  │            │
│  │ [Live Ticker]    │  │ [Graph]          │            │
│  │ voltage: 7.8V    │  │     ▲            │            │
│  │ temp: 28.5°C     │  │    ╱ ╲           │            │
│  │ gyro: 0.02 rad/s │  │   ╱   ╲          │            │
│  └──────────────────┘  └──────────────────┘            │
│                                                          │
│  ┌──────────────────────────────────────────────────┐  │
│  │ Memory Matches (Similar Past Incidents)          │  │
│  │                                                   │  │
│  │ ● Power fault (2 days ago) - Similarity: 0.87    │  │
│  │ ● Thermal spike (1 week ago) - Similarity: 0.72  │  │
│  └──────────────────────────────────────────────────┘  │
│                                                          │
│  ┌──────────────────────────────────────────────────┐  │
│  │ Agent Decision Output                             │  │
│  │                                                   │  │
│  │ Reasoning: Voltage drop detected (7.2V < 7.3V    │  │
│  │ threshold). Similar incident occurred 2 days ago  │  │
│  │ with successful auto-recovery. High confidence.   │  │
│  │                                                   │  │
│  │ Action: IMMEDIATE_RECOVERY                        │  │
│  │ [Explain Decision ▼]                              │  │
│  └──────────────────────────────────────────────────┘  │
│                                                          │
│  ┌──────────────────────────────────────────────────┐  │
│  │ Response Status                                   │  │
│  │                                                   │  │
│  │ ● Triggered: 14:32:15                             │  │
│  │ ● In Progress: Safe mode activated                │  │
│  │ ● Resolved: 14:32:17 (2.1s total)                 │  │
│  └──────────────────────────────────────────────────┘  │
│                                                          │
│  ┌──────────────────────────────────────────────────┐  │
│  │ Metrics                                           │  │
│  │                                                   │  │
│  │ Confidence: 94%  │  Severity: HIGH                │  │
│  │ Recurrence: 3x   │  Time to Decision: 325ms       │  │
│  └──────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
```

#### Interactive Elements
- **Live Ticker:** Auto-scrolling telemetry data
- **Anomaly Graph:** Real-time spike visualization
- **Memory Matches:** Clickable to see full incident
- **Explain Decision:** Expandable LLM reasoning trace
- **Status Timeline:** Visual progress indicator

---

### 5. Use Cases & Impact Page (`use-cases.html`)

#### Use Case Cards

**1. Satellite Telemetry Fault Defense**
```
Real-world relevance: CubeSats operate in harsh environments with 
limited ground contact. AstraGuard provides autonomous fault detection 
and recovery, preventing mission-critical failures.

Why streaming + memory matter: Satellite faults escalate quickly. 
Memory-aware decisions prevent recurring issues and enable predictive 
maintenance based on historical patterns.
```

**2. Log-Based Intrusion Detection**
```
Real-world relevance: Enterprise systems generate millions of log 
entries daily. AstraGuard detects intrusion patterns in real-time, 
triggering automated containment before damage spreads.

Why streaming + memory matter: Attack patterns evolve. Adaptive memory 
recognizes variations of known threats and learns new attack signatures 
without manual rule updates.
```

**3. IoT Threat Auto-Response**
```
Real-world relevance: Connected devices are vulnerable to coordinated 
attacks. AstraGuard monitors device behavior streams and isolates 
compromised nodes automatically.

Why streaming + memory matter: IoT attacks spread rapidly across 
networks. Memory-based correlation identifies multi-stage attacks and 
prevents lateral movement.
```

---

### 6. Team & Approach Page (`team.html`)

#### Team Philosophy
```
We build with a balance of practical engineering and first-principles 
thinking. AstraGuard isn't just a research prototype—it's designed to 
solve real streaming security problems at scale.
```

#### Tech Stack
- **Streaming:** Pathway Engine for real-time data processing
- **Memory:** Custom adaptive vector store with temporal weighting
- **Intelligence:** Hybrid rule-based + LLM-assisted reasoning
- **Observability:** Transparent decision traces and metrics

#### Approach Highlights
1. **Detection → Decision → Action** (not just classification)
2. **Evolving memory** with intelligent pruning
3. **Explainable reasoning** for every decision
4. **Production-ready** architecture with fault tolerance
5. **Sub-2-second** end-to-end latency

---

## Design Features

### Real-Time Feel
- Subtle animated stream elements
- Ticking log entries
- Pulsing anomaly indicators
- Smooth transitions

### Memory Visualization
- Timeline with decay curves
- Weighted node graphs
- Color-coded importance levels
- Interactive hover states

### Explainability
- Decision panel with reasoning
- Expandable LLM traces
- Metric breakdowns
- Action workflow visualization

### Responsiveness
- Mobile-first design
- Tablet-optimized layouts
- Desktop-enhanced features
- Adaptive typography

### Performance
- Lazy loading for images
- Optimized animations
- Minimal JavaScript
- Fast CDN delivery

### Visual Design
- Restrained color palette
- High contrast for readability
- Clean typography (Inter, JetBrains Mono)
- Consistent spacing and rhythm

---

## Animation Specifications

### Hero Section
```css
@keyframes streamFlow {
  0% { transform: translateY(0); opacity: 1; }
  100% { transform: translateY(20px); opacity: 0; }
}

.telemetry-stream {
  animation: streamFlow 2s linear infinite;
}
```

### Anomaly Spike
```css
@keyframes anomalyPulse {
  0%, 100% { transform: scale(1); opacity: 0.8; }
  50% { transform: scale(1.2); opacity: 1; }
}

.anomaly-indicator {
  animation: anomalyPulse 1.5s ease-in-out infinite;
}
```

### Memory Recall
```css
@keyframes memoryGlow {
  0%, 100% { box-shadow: 0 0 10px rgba(53, 53, 238, 0.3); }
  50% { box-shadow: 0 0 20px rgba(53, 53, 238, 0.6); }
}

.memory-node {
  animation: memoryGlow 2s ease-in-out infinite;
}
```

---

## Deployment Strategy

### Static Hosting (Recommended)
1. Build optimized static files
2. Deploy to Vercel/Netlify/GitHub Pages
3. Configure custom domain
4. Enable CDN and caching
5. Set up SSL certificate

### Performance Optimization
- Minify CSS/JS
- Optimize images (WebP format)
- Enable gzip compression
- Implement lazy loading
- Use service workers for caching

---

## Closing Statement

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
**Contact:** sr-857@github.com
