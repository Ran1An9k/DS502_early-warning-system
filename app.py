import streamlit as st
import pathlib
import pandas as pd
import html
# CONFIGURATION
st.set_page_config(
    page_title="Academic Early Warning System",
    layout="wide"
)

alert_columns = [
    "anonymous_student_identifier",
    "academic_term",
    "program",
    "progression_status",
    "attendance",
    "early_assessment_results",
    "repeated_courses",
    "withdrawals",
]

# Load the data file beside this app, regardless of the current working folder.
data_file = pathlib.Path(__file__).with_name("synthetic_student_data.csv")
try:
    df = pd.read_csv(data_file)
except FileNotFoundError:
    st.error(f"Student data file not found: {data_file}")
    st.info("Place synthetic_student_data.csv beside app.py and rerun the app.")
    st.stop()

# Standardize column names so they match alert_columns.
df.columns = (
    df.columns.astype(str)
    .str.strip()
    .str.lower()
    .str.replace(r"[^a-z0-9]+", "_", regex=True)
    .str.strip("_")
)

# Create the target if it has not already been created.
if "academic_risk" not in df.columns:
    if "progression_status" not in df.columns:
        raise KeyError("Required column 'progression_status' was not found.")
    df["academic_risk"] = df["progression_status"].astype(str).str.strip().str.lower().isin(
        ["academic warning", "probation"]
    ).astype(int)

available_alert_columns = [col for col in alert_columns if col in df.columns]

advisor_alerts = df.loc[
    df["academic_risk"].eq(1),
    available_alert_columns
].copy()

advisor_alerts.insert(0, "alert_type", "Academic risk")
advisor_alerts.insert(1, "alert_status", "Pending advisor review")


# choosing the CUSTOM THEME
st.markdown("""
<style>
.main {
    background-color: #f1f5f9;
  
    
    }

.card {
    background: white;
    padding: 20px;
    border-radius: 20px;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.05);
}

.metric-box {
    background: white;
    padding: 20px;
    border-radius: 20px;
    text-align: center;
}

.title {
    font-size: 32px;
    font-weight: bold;
}

.subtitle {
    color: gray;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    """
<div class='card'>
    <div class='title'>
        Academic Early Warning System
    </div>

    <div class='subtitle'>
        Alerts • Advisor Review • Intervention Tracking
    </div>
</div>
""",
    unsafe_allow_html=True
)

st.write("")

# KPI SECTION

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Alerts", f"{len(advisor_alerts):,}")

with col2:
    st.metric(
        "Under Review",
        f"{len(advisor_alerts):,}"
    )

with col3:
    st.metric(
        "Active Interventions",
        "0"
    )

st.divider()

# ALERTS SECTION

st.header("Academic alert **")

st.caption("Students with an academic warning or probation status are shown for advisor review.")

alerts_df = advisor_alerts

st.dataframe(
    alerts_df,
    use_container_width=True
)

st.divider()


st.header(" Advisor Review")

student_id = st.text_input(
    "Student ID"
)

advisor_name = st.text_input(
    "Advisor Name"
)

review_notes = st.text_area(
    "Review Notes"
)

decision = st.selectbox(
    "Advisor Decision",
    [
        "Select Decision",
        "Confirm Risk",
        "Dismiss Alert",
        "Monitor Student"
    ]
)

if st.button("Save Review"):
    st.success(
        "Review Saved"
    )

st.divider()

# INTERVENTION TRACKING

st.header("Intervention Tracking")

student_intervention = st.text_input(
    "Student ID ",
    key="intervention_student"
)

intervention_type = st.selectbox(
    "Intervention Type",
    [
        "Academic Advising",
        "Tutoring",
        "Learning Support",
        "Mentoring",
        "Custom"
    ]
)

intervention_notes = st.text_area(
    "Intervention Notes"
)

follow_up_date = st.date_input(
    "Follow-up Date"
)

status = st.selectbox(
    "Intervention Status",
    [
        "Planned",
        "In Progress",
        "Completed"
    ]
)

if st.button(
    "Save Intervention"
):
    st.success(
        "Intervention Saved"
    )

st.divider()

# FUTURE WORK AREA
st.header("Future Integration")

st.markdown("""
Replace this section with:

- Logistic Regression predictions
- SHAP explanations
- Risk level calculation
- Fairness metrics
- Student search
- Advisor workflow
- Monitoring dashboard
- Database integration

Everything below can be customized.
""")

# Downloadable standalone page for viewing the current results outside Streamlit.
def html_value(value):
        value = str(value).strip()
        return html.escape(value) if value else "Not provided"


report_html = f"""<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Academic Early Warning System</title>
    <style>
        body {{ font: 16px Arial, sans-serif; background: #f1f5f9; color: #1e293b; margin: 0; padding: 32px; }}
        main {{ max-width: 900px; margin: auto; }}
        section {{ background: white; padding: 20px; margin: 16px 0; border-radius: 12px; box-shadow: 0 2px 10px #0000000d; }}
        h1, h2 {{ color: #0f172a; }}
        .metrics {{ display: flex; gap: 16px; flex-wrap: wrap; }}
        .metric {{ flex: 1; min-width: 160px; }}
        .label {{ color: #64748b; }}
        pre {{ white-space: pre-wrap; overflow-wrap: anywhere; }}
    </style>
</head>
<body><main>
    <h1>Academic Early Warning System</h1>
    <p class="label">Alerts • Advisor Review • Intervention Tracking</p>
    <section class="metrics">
        <div class="metric"><span class="label">Total Alerts</span><h2>--</h2></div>
        <div class="metric"><span class="label">Under Review</span><h2>--</h2></div>
        <div class="metric"><span class="label">Active Interventions</span><h2>--</h2></div>
    </section>
    <section><h2>Academic Alerts</h2><p>Alert records are not connected in this scaffold yet.</p></section>
    <section><h2>Advisor Review</h2>
        <p><strong>Student ID:</strong> {html_value(student_id)}</p>
        <p><strong>Advisor:</strong> {html_value(advisor_name)}</p>
        <p><strong>Decision:</strong> {html_value(decision)}</p>
        <p><strong>Notes:</strong></p><pre>{html_value(review_notes)}</pre>
    </section>
    <section><h2>Intervention</h2>
        <p><strong>Student ID:</strong> {html_value(student_intervention)}</p>
        <p><strong>Type:</strong> {html_value(intervention_type)}</p>
        <p><strong>Follow-up date:</strong> {html_value(follow_up_date)}</p>
        <p><strong>Status:</strong> {html_value(status)}</p>
        <p><strong>Notes:</strong></p><pre>{html_value(intervention_notes)}</pre>
    </section>
</main></body></html>"""

st.download_button(
        "Download results as HTML",
        data=report_html,
        file_name="academic_early_warning_results.html",
        mime="text/html",
)
