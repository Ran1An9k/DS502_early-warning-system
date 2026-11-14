import streamlit as st
import pathlib
import pandas as pd
import html
from sklearn.preprocessing import FunctionTransformer
from sklearn.metrics import precision_score, recall_score


class df:
    """Small dataframe wrapper that centralizes common student-data cleanup."""

    def __init__(self, frame):
        self.frame = frame.copy() if isinstance(frame, pd.DataFrame) else pd.DataFrame(frame)

    @classmethod
    def from_csv(cls, path):
        return cls(pd.read_csv(path))

    def normalize_columns(self):
        self.frame.columns = (
            self.frame.columns.astype(str)
            .str.strip()
            .str.lower()
            .str.replace(r"[^a-z0-9]+", "_", regex=True)
            .str.strip("_")
        )
        return self.frame

    def ensure_academic_risk(self):
        if "academic_risk" in self.frame.columns:
            return self.frame
        if "progression_status" not in self.frame.columns:
            raise KeyError("Required column 'progression_status' was not found.")
        self.frame["academic_risk"] = (
            self.frame["progression_status"]
            .astype(str)
            .str.strip()
            .str.lower()
            .isin(["academic warning", "probation"])
            .astype(int)
        )
        return self.frame

    def build_alerts(self, alert_columns):
        available_alert_columns = [col for col in alert_columns if col in self.frame.columns]
        alerts = self.frame.loc[
            self.frame["academic_risk"].eq(1),
            available_alert_columns,
        ].copy()
        alerts.insert(0, "alert_type", "Academic risk")
        alerts.insert(1, "alert_status", "Pending advisor review")
        return alerts

    def __getattr__(self, name):
        return getattr(self.frame, name)

    def __getitem__(self, key):
        return self.frame[key]

    def __setitem__(self, key, value):
        self.frame[key] = value

    def __len__(self):
        return len(self.frame)


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
data_file = pathlib.Path(__file__).with_name("Cleaned_synthetic_stu_Data.csv")
try:
    dataset = df.from_csv(data_file)
    dataset.normalize_columns()
    dataset.ensure_academic_risk()
    df = dataset.frame
except FileNotFoundError:
    st.error(f"Student data file not found: {data_file}")
    st.info("Place synthetic_student_data.csv beside app.py and rerun the app.")
    st.stop()

advisor_alerts = dataset.build_alerts(alert_columns)


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
        """
        fairness_results = []

        for program in fairness_df["program"].unique():
        group = fairness_df[fairness_df["program"] == program]

        fairness_results.append({
        "Program": program,
        "Students": len(group),
        "At Risk": group["actual"].sum(),
        "Predicted At Risk": group["predicted"].sum(),
        "Precision": precision_score(
            group["actual"],
            group["predicted"],
            zero_division=0
        ),
        "Recall": recall_score(
            group["actual"],
            group["predicted"],
            zero_division=0
       )
    })

   fairness_results = pd.DataFrame(fairness_results)

   display(fairness_results)

      """
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
"""
model_path = MODEL_DIR / "baseline_logistic_regression.joblib"
MODEL_DIR.mkdir(parents=True, exist_ok=True)

if not model_path.is_file():
    if "baseline_pipeline" not in globals():
        if "X_train" not in globals() or "y_train" not in globals():
            if "model_df" in globals():
                source_df = model_df.copy()
            elif "df" in globals():
                source_df = df.copy()
            else:
                data_paths = [DATA_PATH]
                if "candidate" in globals():
                    data_paths.append(candidate)

                data_path = next((path for path in data_paths if path.is_file()), None)
                search_roots = list(dict.fromkeys([
                    DATA_PATH.__class__.cwd(),
                    DATA_PATH.__class__.home(),
                ]))
                if data_path is None:
                    for search_root in search_roots:
                        data_path = next(
                            (
                                path
                                for path in search_root.rglob(DATA_PATH.name)
                                if path.is_file()
                            ),
                            None,
                        )
                        if data_path is not None:
                            break

                if data_path is None:
                    checked = ", ".join(str(path) for path in data_paths)
                    searched = ", ".join(str(root) for root in search_roots)
                    raise FileNotFoundError(
                        f"Dataset not found. Checked: {checked}. "
                        f"Also searched under: {searched}. "
                        "Set DATA_PATH to the dataset's actual location."
                    )

                source_df = pd.read_csv(data_path)

            # Match configured names to common dataset column names.
            if TARGET_COLUMN not in source_df.columns and "academic_risk" in source_df.columns:
                TARGET_COLUMN = "academic_risk"
            if TIME_COLUMN and TIME_COLUMN not in source_df.columns and "academic_term" in source_df.columns:
                TIME_COLUMN = "academic_term"

            for expected, actual in {
                "attendance_week_1_4": "attendance",
                "early_assessment_result": "early_assessment_results",
            }.items():
                if expected not in source_df.columns and actual in source_df.columns:
                    source_df = source_df.rename(columns={actual: expected})

            selected_features = NUMERIC_FEATURES + CATEGORICAL_FEATURES
            required = selected_features + [TARGET_COLUMN]
            if TIME_COLUMN and TIME_COLUMN in source_df.columns:
                required.append(TIME_COLUMN)

            missing = sorted(set(required) - set(source_df.columns))
            if missing:
                raise KeyError(f"Required columns are missing: {missing}")

            model_df = source_df.dropna(subset=[TARGET_COLUMN]).copy()
            model_df[TARGET_COLUMN] = pd.to_numeric(
                model_df[TARGET_COLUMN], errors="raise"
            ).astype(int)

            X = model_df[selected_features].copy()
            y = model_df[TARGET_COLUMN].copy()

            if TIME_COLUMN and TIME_COLUMN in model_df.columns:
                order = model_df[TIME_COLUMN].sort_values(kind="stable").index
                X, y = X.loc[order], y.loc[order]
                n = len(X)
                train_end = int(n * (1 - TEST_SIZE - VALIDATION_SIZE))
                valid_end = int(n * (1 - TEST_SIZE))
                X_train, X_valid, X_test = (
                    X.iloc[:train_end], X.iloc[train_end:valid_end], X.iloc[valid_end:]
                )
                y_train, y_valid, y_test = (
                    y.iloc[:train_end], y.iloc[train_end:valid_end], y.iloc[valid_end:]
                )
            else:
                temp_size = TEST_SIZE + VALIDATION_SIZE
                X_train, X_temp, y_train, y_temp = train_test_split(
                    X, y, test_size=temp_size, stratify=y, random_state=RANDOM_STATE
                )
                X_valid, X_test, y_valid, y_test = train_test_split(
                    X_temp,
                    y_temp,
                    test_size=TEST_SIZE / temp_size,
                    stratify=y_temp,
                    random_state=RANDOM_STATE,
                )


        def clean_numeric_features(values):
            values = values.copy()
            values["attendance_week_1_4"] = pd.to_numeric(
            values["attendance_week_1_4"].astype("string").str.rstrip("%"),
            errors="coerce",
            )
            values["early_assessment_result"] = (
            values["early_assessment_result"]
            .astype("string")
            .str.strip()
            .str.lower()
            .map({"fail": 0, "marginal": 1, "pass": 2})
            )
            return values

        numeric_pipeline = Pipeline(steps=[
            ("clean", FunctionTransformer(clean_numeric_features, validate=False)),
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
        ])
        categorical_pipeline = Pipeline(steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore")),
        ])
        preprocessor = ColumnTransformer(transformers=[
            ("numeric", numeric_pipeline, NUMERIC_FEATURES),
            ("categorical", categorical_pipeline, CATEGORICAL_FEATURES),
        ])
        baseline_pipeline = Pipeline(steps=[
            ("preprocessor", preprocessor),
            ("model", LogisticRegression(
            max_iter=2000,
            class_weight="balanced",
            random_state=RANDOM_STATE,
            )),
        ])
        baseline_pipeline.fit(X_train, y_train)

        if "selected_features" not in globals():
            selected_features = NUMERIC_FEATURES + CATEGORICAL_FEATURES
        if "SELECTED_THRESHOLD" not in globals():
            SELECTED_THRESHOLD = DEFAULT_THRESHOLD
    joblib.dump(baseline_pipeline, model_path)

loaded_model = joblib.load(model_path)
try:
    new_students = pd.read_csv("test_predictions.csv")
except FileNotFoundError:
    new_students = X_test.copy()

risk_probability = loaded_model.predict_proba(new_students[selected_features])[:, 1]
risk_flag = (risk_probability >= SELECTED_THRESHOLD).astype(int)
results = pd.DataFrame({
"risk_probability": risk_probability,
"risk_flag": risk_flag,
})
display(results.head())

"""

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
st.header("System academic early wearning Integration")

st.markdown("""

- Logistic Regression predictions
- At Risk level calculation
- Fairness metrics
- Student search
- Advisor workflow
- Monitoring dashboard
- Dataset integration view

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
