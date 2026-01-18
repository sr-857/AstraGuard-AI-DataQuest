import streamlit as st
import pandas as pd
import numpy as np
import time

# Initialize session state
if "telemetry_active" not in st.session_state:
    st.session_state.telemetry_active = False
if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(columns=["voltage","temp","gyro","wheel"])
if "logs" not in st.session_state:
    st.session_state.logs = []

# Sidebar controls
st.sidebar.title("Controls")
start_btn = st.sidebar.button("Start Telemetry")
stop_btn = st.sidebar.button("Stop Telemetry")

if start_btn:
    st.session_state.telemetry_active = True
if stop_btn:
    st.session_state.telemetry_active = False

# Fake anomaly detection function
def detect_anomaly(row):
    return row["voltage"] > 4.2 or row["temp"] > 75

# Memory search simulation
def memory_search(row):
    if len(st.session_state.df) < 3:
        return []
    past = st.session_state.df.tail(3)
    results = []
    for _, r in past.iterrows():
        sim = 100 - abs(r["voltage"] - row["voltage"])*10
        results.append({
            "summary": f"Voltage {r['voltage']:.2f}V, Temp {r['temp']:.1f}C",
            "similarity": max(0, min(100, sim)),
            "timestamp": time.strftime("%H:%M:%S")
        })
    return results

# Header
st.title("AstraGuard – Mission Control")
st.caption("Real-time telemetry and anomaly detection")

status = "Telemetry Active" if st.session_state.telemetry_active else "Telemetry Offline"
st.write(f"**System Status:** {status}")

# Main loop
if st.session_state.telemetry_active:
    new_row = {
        "voltage": np.random.uniform(3.5, 5.0),
        "temp": np.random.uniform(20, 90),
        "gyro": np.random.uniform(-5, 5),
        "wheel": np.random.uniform(2000, 8000)
    }
    st.session_state.df = pd.concat([st.session_state.df, pd.DataFrame([new_row])], ignore_index=True)

    anomaly = detect_anomaly(new_row)
    mem = memory_search(new_row)

    # Log event
    log = f"[{time.strftime('%H:%M:%S')}] {'ANOMALY' if anomaly else 'OK'} | {new_row['voltage']:.2f}V | {new_row['temp']:.1f}C"
    st.session_state.logs.append(log)

    # Layout
    col1, col2 = st.columns([2,1])

    with col1:
        st.subheader("Live Telemetry Stream")
        st.line_chart(st.session_state.df[["voltage","temp","gyro","wheel"]])

    with col2:
        st.subheader("Anomaly Radar")
        if anomaly:
            st.error("Anomaly Detected!")
            st.write("**Confidence:** 87.3%")
            st.write("**Severity:** Medium")
            st.write("**Recurrence:** 3×")
        else:
            st.success("All signals normal")

    # Memory Matches
    st.subheader("Memory Matches")
    if mem:
        for m in mem:
            st.write(f"- {m['summary']} (Similarity: {m['similarity']:.1f}%)")
    else:
        st.write("Memory warming up...")

    # Reasoning Console
    st.subheader("Reasoning Console")
    if anomaly:
        reason = f"Voltage spike at {new_row['voltage']:.2f}V exceeds safe threshold. Last 3 events show similar patterns. Triggering recovery."
        st.write(reason)
    else:
        st.write("No anomaly to reason over.")

    # Response Actions
    st.subheader("Response & Recovery")
    if anomaly:
        actions = ["Power Load Balancing","Thermal Regulation","Sensor Recalibration"]
        for a in actions:
            st.write(f"🟢 {a}: Running")
    else:
        st.write("No active recovery actions.")

    # Event Log Stream
    st.subheader("Event Log Stream")
    st.code("\n".join(st.session_state.logs[-10:]))

    time.sleep(0.2)
    st.rerun()
else:
    st.info("Telemetry is offline. Start to view streams.")
