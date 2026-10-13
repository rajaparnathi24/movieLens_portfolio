import streamlit as st
import sys
from pathlib import Path

# Ensure utils can be imported
parent_dir = str(Path(__file__).parent.parent)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from utils.data_loader import inject_custom_css

dark_mode = st.session_state.get("dark_mode", False)
inject_custom_css(dark_mode)

st.title("🎯 Where Movie Data Becomes Insight")
st.markdown(
    "<p style='font-size:1.05rem; margin-top:-10px; margin-bottom:24px; color:#64748B;'>"
    "Discover how movie rating and genre analysis helps understand audience preferences, uncover patterns, and support data-driven decisions."
    "</p>",
    unsafe_allow_html=True
)

# SECTION 1: Real-World Applications
st.subheader("1. Real-World Applications")

col_a1, col_a2, col_a3 = st.columns(3)

with col_a1:
    st.markdown("""
    <div class="analysis-card" style="height:100%;">
        <div style="font-size:1.6rem; margin-bottom:8px;">⭐</div>
        <div class="analysis-title">Movie Rating Analysis</div>
        <div class="analysis-subtitle">Audience consensus & quality distribution</div>
        <p style="font-size:0.875rem; line-height:1.6; margin-top:8px;">
            Analyze average ratings, rating distributions, and highly rated movies to establish true quality benchmarks across diverse catalogs.
        </p>
        <span class="badge" style="margin-top:12px;">Volume Skew: 57.5% Positivity</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="analysis-card" style="height:100%; margin-top:16px;">
        <div style="font-size:1.6rem; margin-bottom:8px;">🎯</div>
        <div class="analysis-title">Recommendation Systems</div>
        <div class="analysis-subtitle">Rule mining for personalized discovery</div>
        <p style="font-size:0.875rem; line-height:1.6; margin-top:8px;">
            Explain how discovered patterns can support personalized movie recommendations by providing prerequisite co-occurrence rules and taste similarity matrices.
        </p>
        <span class="badge" style="background:#FEF3C7; color:#92400E; margin-top:12px;">Potential / Future Application</span>
    </div>
    """, unsafe_allow_html=True)

with col_a2:
    st.markdown("""
    <div class="analysis-card" style="height:100%;">
        <div style="font-size:1.6rem; margin-bottom:8px;">🎭</div>
        <div class="analysis-title">Genre Pattern Mining</div>
        <div class="analysis-subtitle">Combinatorial synergy & frequency</div>
        <p style="font-size:0.875rem; line-height:1.6; margin-top:8px;">
            Discover genre popularity and relationships between movie genres and ratings to uncover how multi-genre pairings impact critical and audience reception.
        </p>
        <span class="badge" style="margin-top:12px;">Apriori Max Lift: 12.38x</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="analysis-card" style="height:100%; margin-top:16px;">
        <div style="font-size:1.6rem; margin-bottom:8px;">📺</div>
        <div class="analysis-title">OTT Platform Analytics</div>
        <div class="analysis-subtitle">Acquisition strategy & audience retention</div>
        <p style="font-size:0.875rem; line-height:1.6; margin-top:8px;">
            Understand audience interests and viewing preferences to support content decisions, optimize streaming catalog curation, and balance mass-market vs niche titles.
        </p>
        <span class="badge" style="margin-top:12px;">Market Volume vs Acclaim</span>
    </div>
    """, unsafe_allow_html=True)

with col_a3:
    st.markdown("""
    <div class="analysis-card" style="height:100%;">
        <div style="font-size:1.6rem; margin-bottom:8px;">👥</div>
        <div class="analysis-title">Audience Preference Analysis</div>
        <div class="analysis-subtitle">Latent taste clusters & demographic cohorts</div>
        <p style="font-size:0.875rem; line-height:1.6; margin-top:8px;">
            Explore similarities in user rating behavior and identify audience segments through unsupervised dimensionality reduction (PCA) and demographic cross-tabulation.
        </p>
        <span class="badge" style="margin-top:12px;">PCA 2D Variance: 38.6%</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="analysis-card" style="height:100%; margin-top:16px;">
        <div style="font-size:1.6rem; margin-bottom:8px;">📊</div>
        <div class="analysis-title">Business Intelligence</div>
        <div class="analysis-subtitle">Executive decision support & reporting</div>
        <p style="font-size:0.875rem; line-height:1.6; margin-top:8px;">
            Turn movie datasets into meaningful visual insights for data-driven decisions, transforming raw transactional log records into clear executive scorecards.
        </p>
        <span class="badge" style="margin-top:12px;">Interactive Visual KPIs</span>
    </div>
    """, unsafe_allow_html=True)

# SECTION 2: Data Mining Workflow
st.subheader("2. Data Mining Workflow")

workflow_steps = [
    ("Step 1", "MovieLens Dataset", "1M+ raw ratings, 3,883 movies, 6,040 users"),
    ("Step 2", "Data Preprocessing", "Latin-1 decode, multi-label genre explosion, demographics"),
    ("Step 3", "Exploratory Data Analysis", "Rating distributions, skewness, 5-star concentration"),
    ("Step 4", "Pattern Discovery", "Apriori frequent itemsets (Lift 12.38) & 2D PCA reduction"),
    ("Step 5", "Insights", "Strategic synthesis for streaming acquisitions & segmentation")
]

wf_cols = st.columns(5)
for i, col in enumerate(wf_cols):
    step_num, step_title, step_desc = workflow_steps[i]
    with col:
        st.markdown(f"""
        <div class="analysis-card" style="text-align:center; padding:16px 12px; height:100%;">
            <div style="font-size:0.75rem; font-weight:800; color:#4F46E5; text-transform:uppercase;">{step_num}</div>
            <div style="font-weight:700; font-size:0.95rem; margin:6px 0;">{step_title}</div>
            <div style="font-size:0.8rem; color:#64748B; line-height:1.4;">{step_desc}</div>
        </div>
        """, unsafe_allow_html=True)

# SECTION 3: Project Benefits
st.subheader("3. Project Benefits & Learning Outcomes")

b_col1, b_col2 = st.columns(2)

with b_col1:
    st.markdown("""
    <div class="analysis-card">
        <div style="display:flex; align-items:flex-start; gap:12px;">
            <div style="font-size:1.5rem;">🎯</div>
            <div>
                <div class="analysis-title">Understand Audience Rating Behavior</div>
                <div class="analysis-subtitle">Empirical behavioral modeling</div>
                <p style="font-size:0.875rem; line-height:1.6; color:#475569; margin-top:6px;">
                    Reveals the underlying psychology of moviegoers: a distinct positive rating mode (Rating 4 represents 34.9% of feedback) and generational leniency where older demographics (56+) give systematically higher scores.
                </p>
            </div>
        </div>
    </div>
    <div class="analysis-card" style="margin-top:16px;">
        <div style="display:flex; align-items:flex-start; gap:12px;">
            <div style="font-size:1.5rem;">⚙️</div>
            <div>
                <div class="analysis-title">Practice Real-World Data Mining Techniques</div>
                <div class="analysis-subtitle">Rigorous unsupervised methodology</div>
                <p style="font-size:0.875rem; line-height:1.6; color:#475569; margin-top:6px;">
                    Demonstrates authentic implementation of core data science algorithms: multi-label incidence transformations, association rule mining with Apriori (Support, Confidence, Lift), and covariance decomposition with PCA.
                </p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with b_col2:
    st.markdown("""
    <div class="analysis-card">
        <div style="display:flex; align-items:flex-start; gap:12px;">
            <div style="font-size:1.5rem;">🎬</div>
            <div>
                <div class="analysis-title">Identify Popular Genres and Rating Trends</div>
                <div class="analysis-subtitle">Volume vs. critical acclaim paradox</div>
                <p style="font-size:0.875rem; line-height:1.6; color:#475569; margin-top:6px;">
                    Disentangles sheer commercial engagement from critical quality: Comedy and Drama command over 70% of total volume, while niche categories like Film-Noir (mean 4.08) and Documentary (mean 3.93) command the highest acclaim.
                </p>
            </div>
        </div>
    </div>
    <div class="analysis-card" style="margin-top:16px;">
        <div style="display:flex; align-items:flex-start; gap:12px;">
            <div style="font-size:1.5rem;">📈</div>
            <div>
                <div class="analysis-title">Communicate Insights Through Data Visualization</div>
                <div class="analysis-subtitle">Executive storytelling & dashboard design</div>
                <p style="font-size:0.875rem; line-height:1.6; color:#475569; margin-top:6px;">
                    Converts dense, million-row tabular datasets into clear, interactive Plotly visualizations and an accessible portfolio layout suitable for business stakeholders and technical reviewers alike.
                </p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
