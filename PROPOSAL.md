# DataQuest 2026 Indian Institute of Technology (IIT), Kharagpur – Build-athon Proposal

**Track:** Agentic AI (Applied GenAI)  
**Project Title:** AstraGuard – Real-Time Threat Detection and Adaptive Response System  
**Team:** Subhajit Roy  
**Institution:** Indian Institute of Technology (IIT), Madras

---

## Executive Summary

AstraGuard will be transformed into a **streaming-aware AI agent** that detects anomalies in real time, reasons over evolving memory, and triggers automated response workflows with low latency and clear system observability. The system prioritizes **continuous situational awareness** instead of one-shot classification.

---

## Problem Approach

Traditional anomaly detection systems operate in isolation, flagging threats without context or adaptive memory. AstraGuard addresses this by:

- **Real-time streaming analysis** using Pathway Engine
- **Adaptive memory** that learns from past incidents
- **Agentic decision-making** that explains and executes response workflows
- **Production-ready architecture** designed for reliability and observability

---

## System Design

### 1. Live Data Ingestion
- **Technology:** Pathway Engine
- **Process:** Continuous telemetry and system log ingestion
- **Features:**
  - Data validation at entry point
  - Automatic timestamping
  - Instant routing to inference pipeline

### 2. Embedding and Context Encoding
- **Approach:** Lightweight embedding model or external API
- **Optimization:** Speed, stability, and memory-efficient representation
- **Output:** Compact vector representations of events

### 3. Adaptive Memory Layer

**Core Innovation:** Real-time updatable vector store with biological inspiration

**Features:**
- **Temporal Weighting:** Prioritize recurring or recent threats
- **Memory Decay Curves:** Prevent saturation while preserving high-impact incidents
- **Auto-Update:** Continuous learning without manual intervention
- **Context Serving:** Provides historical similarity during decision cycles

**Mathematical Foundation:**
```
Memory_Weight(t) = Base_Importance × e^(-λ × (current_time - event_time))
```
Where λ controls decay rate, balancing recency with historical significance.

### 4. Anomaly Reasoning Agent

**Agentic Decision Loop evaluates:**
- Severity score
- Recurrence patterns
- Confidence level
- Historical similarity from memory

**Hybrid Approach:**
- Rule-guided logic for deterministic responses
- LLM assistance for explainability and edge cases
- Decision output includes reasoning trace

**Not just detection – intelligent action selection**

### 5. Response and Recovery Engine

**Automated Workflows:**
- Alert escalation to operators
- System auto-recovery actions
- Risk scoring updates
- Incident tagging for future memory context

**Workflow Types:**
- **Immediate:** < 2s response for critical threats
- **Scheduled:** Batched analysis for pattern detection
- **Manual Override:** Human-in-the-loop for uncertain cases

### 6. Dashboard and Observability

**Enhanced UI displays:**
- Anomaly confidence scores
- Memory match history
- Chosen action path with reasoning
- Response status and timeline
- System health metrics

**Transparency:** Every decision is traceable and explainable

---

## Technical Goals

| Metric | Target | Implementation |
|--------|--------|----------------|
| **Detection → Decision → Response** | < 2 seconds | Optimized Pathway pipeline |
| **Memory Updates** | Auto-updating | Continuous vector store refresh |
| **Context Retrieval** | Temporal weighting | Priority queue with decay |
| **Explainability** | LLM-assisted | Reasoning output for each decision |
| **Reliability** | Production-grade | Minimal overhead, fault tolerance |

---

## Ecosystem Impact

AstraGuard's architecture extends beyond CubeSats to:

1. **Satellite Telemetry Monitoring** – Real-time orbital threat detection
2. **Connected Device Defense** – IoT security at scale
3. **Large-Scale Log Analysis** – Enterprise security operations
4. **Critical Infrastructure** – Power grid, water systems anomaly response

**Value Proposition:** Solves actual streaming security problems, not just flags them.

---

## Differentiation from Standard Submissions

| Standard Approach | AstraGuard Innovation |
|-------------------|----------------------|
| Detection only | Detection → Decision → Action |
| Static models | Evolving memory with intelligent pruning |
| Black-box alerts | Reasoning visibility and explainability |
| Academic prototype | Production-leaning reliability |
| One-shot classification | Continuous situational awareness |

---

## Implementation Roadmap

### Phase 1: Foundation (Week 1)
- [x] Integrate Pathway Engine for streaming input
- [x] Deploy embedding encoder for incoming events
- [ ] Implement basic vector store

### Phase 2: Intelligence (Week 2)
- [ ] Implement adaptive memory store
- [ ] Add temporal weighting logic
- [ ] Integrate memory decay curves
- [ ] Upgrade anomaly module into decision agent loop

### Phase 3: Action (Week 3)
- [ ] Connect agent decisions to response workflows
- [ ] Implement workflow orchestration
- [ ] Add LLM reasoning integration

### Phase 4: Observability (Week 4)
- [ ] Ship enhanced dashboard with reasoning visibility
- [ ] Add memory visualization
- [ ] Implement action trace logging
- [ ] Performance optimization

---

## Success Metrics

**Technical:**
- Sub-2-second end-to-end latency
- 95%+ uptime during continuous operation
- Memory efficiency: < 500MB for 10K events

**Functional:**
- Accurate threat prioritization
- Explainable decision paths
- Successful auto-recovery rate > 80%

**Innovation:**
- Novel memory architecture implementation
- Production-ready agent framework
- Ecosystem extensibility demonstration

---

## Conclusion

AstraGuard represents a paradigm shift from **reactive detection** to **proactive defense**. By combining Pathway's streaming engine with biologically-inspired memory and agentic reasoning, we create a system that doesn't just identify threats—it understands, remembers, and responds intelligently.

This is not a research prototype. This is a **production-ready security agent** designed to protect real systems in real time.

---

**Repository:** https://github.com/sr-857/AstraGuard  
**Contact:** sr-857@github.com  
**Hackathon:** DataQuest 2026 Indian Institute of Technology (IIT), Kharagpur
