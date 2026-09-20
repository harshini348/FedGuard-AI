import streamlit as st
import pandas as pd
import time

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="FedGuard AI",
    page_icon="🛡️",
    layout="wide"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>
    .main-title {
        font-size: 42px;
        font-weight: 700;
        color: #d4af37;
        margin-bottom: 0;
    }

    .subtitle {
        font-size: 20px;
        color: #94a3b8;
        margin-bottom: 20px;
    }

    .workflow-box {
        text-align: center;
        padding: 18px 8px;
        border-radius: 12px;
        border: 1px solid #334155;
        background-color: #111827;
    }

    .workflow-title {
        font-size: 18px;
        font-weight: 600;
    }

    .workflow-text {
        font-size: 13px;
        color: #94a3b8;
    }
</style>
""", unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">🛡️ FedGuard AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Privacy-Preserving Federated Learning Platform</div>',
    unsafe_allow_html=True
)

st.write(
    "Collaborative AI training across organizations without sharing "
    "sensitive raw data."
)

st.divider()

# =========================================================
# FEDERATED LEARNING WORKFLOW
# =========================================================

st.header("🔄 Federated Learning Workflow")

workflow1, workflow2, workflow3, workflow4, workflow5 = st.columns(5)

with workflow1:
    st.markdown("""
    <div class="workflow-box">
        <div class="workflow-title">🏢 Organizations</div>
        <div class="workflow-text">
        Hospital<br>
        Bank<br>
        College
        </div>
    </div>
    """, unsafe_allow_html=True)

with workflow2:
    st.markdown("""
    <div class="workflow-box">
        <div class="workflow-title">📊 Local Data</div>
        <div class="workflow-text">
        Data stays<br>
        inside each<br>
        organization
        </div>
    </div>
    """, unsafe_allow_html=True)

with workflow3:
    st.markdown("""
    <div class="workflow-box">
        <div class="workflow-title">🤖 Local Training</div>
        <div class="workflow-text">
        Models train<br>
        locally
        </div>
    </div>
    """, unsafe_allow_html=True)

with workflow4:
    st.markdown("""
    <div class="workflow-box">
        <div class="workflow-title">🔐 Secure Aggregation</div>
        <div class="workflow-text">
        Only model<br>
        updates are shared
        </div>
    </div>
    """, unsafe_allow_html=True)

with workflow5:
    st.markdown("""
    <div class="workflow-box">
        <div class="workflow-title">🌐 Global Model</div>
        <div class="workflow-text">
        Collaborative<br>
        AI model
        </div>
    </div>
    """, unsafe_allow_html=True)

st.info(
    "🔒 Key principle: Raw organizational data never leaves its local environment."
)

st.divider()

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🏢 Organization Portal")

organization = st.sidebar.selectbox(
    "Select Organization",
    [
        "Hospital",
        "Bank",
        "College"
    ]
)

organization_data = {

    "Hospital": {
        "use_case": "Disease Prediction",
        "dataset": "Synthetic Patient Records",
        "records": 12500
    },

    "Bank": {
        "use_case": "Fraud Detection",
        "dataset": "Synthetic Bank Transactions",
        "records": 25000
    },

    "College": {
        "use_case": "Student Performance Prediction",
        "dataset": "Synthetic Student Records",
        "records": 8500
    },
}

current = organization_data[organization]

st.sidebar.success("Organization Connected 🔒")

# =========================================================
# 1. ORGANIZATION DASHBOARD
# =========================================================

st.header("1. 🏢 Organization Dashboard")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Organization", organization)

with col2:
    st.metric("AI Use Case", current["use_case"])

with col3:
    st.metric("Local Records", f"{current['records']:,}")

with col4:
    st.metric("Raw Data Sharing", "OFF 🔒")

st.success(
    f"🔒 {organization} stores its raw dataset locally."
)

st.divider()

# =========================================================
# 2. LOCAL DATASET MODULE
# =========================================================

st.header("2. 📊 Local Dataset Module")

st.write(
    f"Sample synthetic dataset for **{organization}**. "
    "No real personal information is used."
)

if organization == "Hospital":

    dataset = pd.DataFrame({
        "Patient ID": ["P001", "P002", "P003", "P004", "P005"],
        "Age": [34, 52, 41, 29, 63],
        "Symptoms": [
            "Fever",
            "Cough",
            "Headache",
            "Fatigue",
            "Fever"
        ],
        "Blood Pressure": [
            "120/80",
            "130/85",
            "118/78",
            "122/82",
            "140/90"
        ],
        "Diagnosis": [
            "Class A",
            "Class B",
            "Class A",
            "Class C",
            "Class B"
        ]
    })

elif organization == "Bank":

    dataset = pd.DataFrame({
        "Transaction ID": ["T001", "T002", "T003", "T004", "T005"],
        "Amount": [2500, 15000, 850, 42000, 3100],
        "Type": [
            "UPI",
            "Card",
            "UPI",
            "Online",
            "Card"
        ],
        "Location": [
            "Chennai",
            "Coimbatore",
            "Madurai",
            "Trichy",
            "Salem"
        ],
        "Fraud": [
            "No",
            "No",
            "No",
            "Yes",
            "No"
        ]
    })

elif organization == "College":

    dataset = pd.DataFrame({
        "Student ID": ["S001", "S002", "S003", "S004", "S005"],
        "Attendance": [92, 75, 88, 61, 95],
        "Internal Marks": [85, 68, 79, 55, 91],
        "Assignment Score": [90, 72, 81, 60, 94],
        "Result": [
            "Pass",
            "Pass",
            "Pass",
            "At Risk",
            "Pass"
        ]
    })

else:

    dataset = pd.DataFrame({
        "Application ID": ["A001", "A002", "A003", "A004", "A005"],
        "Service Type": [
            "Certificate",
            "License",
            "Certificate",
            "Permit",
            "License"
        ],
        "Processing Days": [3, 7, 4, 10, 5],
        "Department": [
            "Revenue",
            "Transport",
            "Revenue",
            "Municipality",
            "Transport"
        ],
        "Status": [
            "Approved",
            "Approved",
            "Pending",
            "Review",
            "Approved"
        ]
    })

st.dataframe(
    dataset,
    use_container_width=True,
    hide_index=True
)

data1, data2, data3 = st.columns(3)

with data1:
    st.metric("Dataset", current["dataset"])

with data2:
    st.metric("Records", f"{current['records']:,}")

with data3:
    st.metric("Storage", "Local 🔒")

st.warning(
    "🚫 Raw Data Sharing: OFF — only model updates can leave the organization."
)

st.divider()

# =========================================================
# 3. LOCAL MODEL TRAINING
# =========================================================

st.header("3. 🤖 Local Model Training")

st.write(
    f"Train the **{organization}** model locally using its private dataset."
)

if st.button(
    "🚀 Train Local Model",
    use_container_width=True
):

    progress = st.progress(0)
    status = st.empty()

    for value in range(0, 101, 10):
        progress.progress(value)
        status.write(
            f"Training local model... {value}%"
        )
        time.sleep(0.04)

    demo_accuracy = {
        "Hospital": 84,
        "Bank": 81,
        "College": 79
    }

    accuracy = demo_accuracy[organization]

    st.success("✅ Local model training completed.")

    train1, train2, train3, train4 = st.columns(4)

    with train1:
        st.metric(
            "Records Used",
            f"{current['records']:,}"
        )

    with train2:
        st.metric(
            "Model Accuracy",
            f"{accuracy}%"
        )

    with train3:
        st.metric(
            "Training Status",
            "Completed"
        )

    with train4:
        st.metric(
            "Model Update",
            "Generated"
        )

    st.success(
        "🔒 Raw data remained inside the organization during training."
    )

st.caption(
    "Prototype/Demo Result: Accuracy values are simulated."
)

st.divider()

# =========================================================
# 4. PRIVACY & SECURITY PROTECTION
# =========================================================

st.header("4. 🔐 Privacy & Security Protection")

st.write(
    "The privacy layer ensures that organizations collaborate "
    "without directly sharing their raw datasets."
)

p1, p2, p3 = st.columns(3)

with p1:
    st.markdown("### 🏢 Local Model")
    st.write("Training happens locally.")
    st.success("Raw data stays local")

with p2:
    st.markdown("### 🔐 Secure Aggregation")
    st.write("Model updates are combined.")
    st.success("Enabled")

with p3:
    st.markdown("### 🌐 Global Model")
    st.write("Aggregated model is generated.")
    st.success("Updated")

st.markdown("---")

security1, security2, security3 = st.columns(3)

with security1:
    st.success("🔐 Secure Aggregation\n\n**ENABLED**")

with security2:
    st.success("🛡️ Differential Privacy\n\n**ENABLED**")

with security3:
    st.error("🚫 Raw Data Sharing\n\n**OFF**")

st.info(
    "Prototype note: Advanced cryptographic privacy mechanisms are "
    "represented as a simulated MVP workflow."
)

st.divider()

# =========================================================
# 5. CENTRAL AGGREGATION SERVER
# =========================================================

st.header("5. 🖥️ Central Aggregation Server")

st.write(
    "Only model updates from participating organizations are "
    "processed by the central aggregation layer."
)

st.code("""
Hospital Model Update ─────────┐
                               │
Bank Model Update ─────────────┼──> 🔐 Secure Aggregation
                               │
College Model Update ──────────┘
                                      ↓
                                🌐 Global Model
""")

server1, server2, server3, server4 = st.columns(4)

with server1:
    st.metric("Organizations", "3")

with server2:
    st.metric("Updates Received", "3")

with server3:
    st.metric("Aggregation Status", "Completed")

with server4:
    st.metric("Global Model", "v1.0")

if st.button(
    "🔄 Run Secure Aggregation",
    use_container_width=True
):

    aggregation_progress = st.progress(0)
    aggregation_status = st.empty()

    for value in range(0, 101, 20):
        aggregation_progress.progress(value)
        aggregation_status.write(
            f"Secure aggregation in progress... {value}%"
        )
        time.sleep(0.05)

    st.success(
        "✅ Secure aggregation completed."
    )

    st.success(
        "🌐 Global Model v1.0 generated."
    )

st.divider()

# =========================================================
# 6. MALICIOUS UPDATE DETECTION
# =========================================================

st.header("6. ⚠️ Model Update Security")

st.write(
    "FedGuard monitors incoming model updates and identifies "
    "potentially anomalous updates before aggregation."
)

security_data = pd.DataFrame({
    "Organization": [
        "Hospital",
        "Bank",
        "College"
    ],
    "Update Status": [
        "✓ Normal",
        "✓ Normal",
        "⚠ Suspicious"
    ],
    "Action": [
        "Accepted",
        "Accepted",
        "Blocked"
    ]
})

st.table(security_data)

st.warning(
    "⚠️ College Model Update: Suspicious behaviour detected."
)

st.error(
    "🚫 Update Blocked — Anomalous behaviour detected."
)

st.info(
    "The suspicious update is prevented from participating "
    "in the global aggregation."
)

st.divider()

# =========================================================
# 7. GLOBAL MODEL PERFORMANCE
# =========================================================

st.header("7. 📈 Global Model Performance")

st.caption(
    "⚠️ Prototype/Demo Results — simulated values for demonstration."
)

performance_data = pd.DataFrame({
    "Model": [
        "Hospital Local Model",
        "Bank Local Model",
        "College Local Model",
        "Federated Global Model"
    ],
    "Accuracy (%)": [
        84,
        81,
        79,
        89
    ]
})

st.bar_chart(
    performance_data.set_index("Model")
)

st.table(performance_data)

st.success(
    "🌐 Federated Global Model generated from collaborative model updates."
)

st.divider()

# =========================================================
# 8. PRIVACY & SECURITY DASHBOARD
# =========================================================

st.header("8. 🔒 Privacy & Security Dashboard")

dash1, dash2, dash3 = st.columns(3)

with dash1:
    st.metric(
        "🔒 Raw Data Shared",
        "0"
    )

with dash2:
    st.metric(
        "🏢 Participating Organizations",
        "3"
    )

with dash3:
    st.metric(
        "⚠️ Suspicious Updates",
        "1 Blocked"
    )

dash4, dash5, dash6 = st.columns(3)

with dash4:
    st.metric(
        "🔐 Secure Aggregation",
        "Enabled"
    )

with dash5:
    st.metric(
        "🛡️ Differential Privacy",
        "Enabled"
    )

with dash6:
    st.metric(
        "🤖 Global Model",
        "Updated"
    )

st.success(
    "🔒 Privacy Status: Protected"
)

st.divider()

# =========================================================
# FOOTER
# =========================================================

st.caption(
    "FedGuard AI | Privacy-Preserving Federated Learning | Hackathon MVP"
)

st.caption(
    "Synthetic data and simulated prototype results are used for demonstration."
)