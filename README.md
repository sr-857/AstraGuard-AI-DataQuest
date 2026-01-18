# AstraGuard AI – DataQuest 2026 Submission

**Event:** DataQuest 2026, hosted by Megalith 2026 at Indian Institute of Technology (IIT), Kharagpur  
**Track:** Agentic AI (Applied GenAI)  

AstraGuard AI is an autonomous fault detection and recovery system for CubeSats, implementing a **Retrieval-Augmented Generation (RAG)** pipeline optimized for real-time telemetry streams. Built on **Pathway's streaming engine**, it moves beyond static data analysis to detect anomalies, recall historical context, and execute recovery actions with sub-second latency.

---

## 🎯 Problem Alignment

### The Challenge
Satellites generate continuous streams of telemetry data. Traditional ground-station monitoring is often too slow to prevent catastrophic failures, while onboard systems lack the reasoning capability to handle novel anomalies.

### The Solution: Real-Time RAG
AstraGuard implements a streaming RAG pipeline that:
1. **Ingests** telemetry data in real-time.
2. **Retrieves** relevant historical context using active memory.
3. **Generates** intelligent recovery decisions using LLMs.
4. **Acts** autonomously to stabilize the spacecraft.

### Use Case & Data Sources
- **Practical Use Case:** Autonomous fault management for Low Earth Orbit (LEO) CubeSats.
- **Data Sources:** Simulated satellite telemetry (Voltage, Temperature, Gyroscope) streamed via CSV/TCP buffers.

---

## 🏗️ System Architecture

### Components
1. **Ingestion Layer:** Captures live telemetry data streams.
2. **Pathway Streaming Layer:** The core engine that processes data windows, handles temporal joins, and manages state.
3. **Retrieval Module:** Fetches relevant historical embeddings based on current anomaly signatures.
4. **LLM Generation:** Analyzes retrieved context + current state to formulate a decision.
5. **Orchestrator:** translates decisions into concrete system commands.
6. **Dashboard:** Real-time visualization of the decision pipeline.

### Data Flow
1. **Stream Input** -> **Pathway Engine** -> **Embedding Encoder**
2. **Encoded Event** -> **Vector Search** (against History) -> **Context Retrieval**
3. **Context + Event** -> **LLM Agent** -> **Reasoning & Decision**
4. **Decision** -> **Response Orchestrator** -> **System Action**

### Technology Stack
- **Pathway:** Chosen for its ability to handle continuous data streams and unify batch/streaming logic.
- **OpenAI/Gemini API:** For high-level reasoning and decision generation.
- **Streamlit:** For a responsive, real-time mission control dashboard.
- **Python:** Core language for integration and logic.

---

## ✨ Features

- **Real-time Ingestion:** Processes telemetry at high frequency (5Hz+) without lag.
- **Context-Aware Retrieval:** Uses adaptive memory to prioritize recent and recurring anomalies.
- **Scalable Generation:** Decouples reasoning from ingestion to ensure the stream never blocks.
- **Self-Healing:** Automatically triggers recovery protocols (e.g., "Switch to Battery B", "Detumble").

---

## 📊 Evaluation Metrics

We evaluate the system based on:
- **Detection Latency:** Time from anomaly onset to system flag (< 500ms).
- **Recovery Latency:** Time from detection to action execution (< 2s).
- **Decision Accuracy:** % of correct recovery actions chosen by the agent (Target: >95%).
- **System Stability:** CPU/Memory footprint during high-load streaming.

---

## 🚀 Setup & Execution

### Prerequisites
- Python 3.9+
- Docker (optional, for containerized run)
- API Key (OpenAI or Google Gemini)

### Environment Variables
Create a `.env` file in the root directory:
```bash
OPENAI_API_KEY=sk-...
# OR
GEMINI_API_KEY=AIza...
PATHWAY_LICENSE_KEY=...
```

### Run Locally (Step-by-Step)

1. **Clone the Repository**
   ```bash
   git clone https://github.com/sr-857/AstraGuard-AI-DataQuest.git
   cd AstraGuard-AI-DataQuest
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the Data Stream (Simulation)**
   ```bash
   python examples/stream_generator.py
   ```

4. **Run the AstraGuard Engine**
    In a separate terminal:
   ```bash
   python main.py
   ```

5. **Launch the Dashboard**
   ```bash
   streamlit run dashboard/app.py
   ```

### Testing Streaming Behavior
- Observe the dashboard "Live Telemetry" graph.
- Inject a fault (e.g., manually trigger a high-temp toggle in the generator).
- Verify that the "System Status" changes from **NOMINAL** to **CRITICAL**.
- Watch the "Agent Action" log for the recovery command.

**Sample Input:** `Temp: 85°C, Voltage: 12V`  
**Expected Output:** `Action: ACTIVATE_COOLING_PUMP, Confidence: 0.98`

---

## 🎥 Demonstration

Our **3-minute demo video** illustrates the live pipeline in action. It captures:
1. Normal operation with green status indicators.
2. Sudden voltage drop injection.
3. The RAG pipeline retrieving similar past voltage events.
4. The agent instantly commanding a power bus reset.
5. System return to nominal state.

📂 **Demo Assets Location:**  
Video and screenshots are available in the `docs/demo_assets/` directory and on the project landing page.

---

## ⚖️ Evaluation & Limitations

### Current Performance
- **Latency:** Average end-to-end response time is 1.2 seconds.
- **Throughput:** Handles up to 500 events/second on standard hardware.

### Limitations
- Currently relies on cloud LLMs (latency bottleneck). Future versions will use SLMs (Small Language Models) on-edge.
- Memory context window is fixed; moving to sliding windows for long-duration missions.

### Future Improvements
- Porting the inference engine to NVIDIA Jetson for true edge capability.
- Integrating fine-tuned LLaMA models for satellite-specific jargon.

---

**Developed for DataQuest 2026 @ IIT Kharagpur.**  
*Pushing the frontiers of autonomous space systems.*
