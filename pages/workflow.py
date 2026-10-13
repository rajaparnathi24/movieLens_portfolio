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

st.title("🔀 MovieLens Data Mining Workflow")
st.markdown("""
<div style="margin-top:-10px; margin-bottom:24px;">
    <span class="badge" style="background:#D1FAE5; color:#065F46; font-weight:700;">MovieLens 1M Dataset</span>
    <p style="font-size:1.05rem; margin-top:8px; color:#64748B;">
        From raw movie ratings to meaningful insights through data preprocessing, exploratory analysis, association rule mining, dimensionality reduction, and interactive visualization.
    </p>
</div>
""", unsafe_allow_html=True)

# SECTION 1: Flowchart Architecture Diagram
st.subheader("1. Flowchart Architecture Diagram")

bg_svg = "#0B132B" if dark_mode else "#FFFFFF"
border_svg = "rgba(59, 130, 246, 0.25)" if dark_mode else "#E2E8F0"
node_bg = "#072B56" if dark_mode else "#EFF6FF"
node_stroke = "#1E4E8C" if dark_mode else "#3B82F6"
node_text = "#FFFFFF" if dark_mode else "#1E3A8A"
line_color = "#64748B" if dark_mode else "#94A3B8"
arrow_color = "#94A3B8" if dark_mode else "#64748B"

st.markdown(f"""
<div style="background:{bg_svg}; border:1px solid {border_svg}; border-radius:14px; padding:28px 16px; margin-bottom:28px; box-shadow:0 8px 24px rgba(0,0,0,0.06); overflow-x:auto;">
  <svg viewBox="0 0 1000 660" style="display:block; width:100%; min-width:760px; max-width:1000px; margin:0 auto;" fill="none" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <marker id="st-flow-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="{arrow_color}"/>
      </marker>
    </defs>

    <!-- Connectors -->
    <path d="M 500 78 L 500 108" stroke="{line_color}" stroke-width="1.5" marker-end="url(#st-flow-arrow)"/>
    <path d="M 500 158 L 500 188" stroke="{line_color}" stroke-width="1.5" marker-end="url(#st-flow-arrow)"/>

    <!-- Stage 3 -> 4 Parallel Branches (Clean 2-tier non-overlapping routing) -->
    <path d="M 440 244 L 440 264 L 135 264 L 135 308" stroke="{line_color}" stroke-width="1.5" marker-end="url(#st-flow-arrow)"/>
    <path d="M 480 244 L 480 286 L 380 286 L 380 308" stroke="{line_color}" stroke-width="1.5" marker-end="url(#st-flow-arrow)"/>
    <path d="M 520 244 L 520 286 L 620 286 L 620 308" stroke="{line_color}" stroke-width="1.5" marker-end="url(#st-flow-arrow)"/>
    <path d="M 560 244 L 560 264 L 865 264 L 865 408" stroke="{line_color}" stroke-width="1.5" marker-end="url(#st-flow-arrow)"/>

    <path d="M 135 358 L 135 408" stroke="{line_color}" stroke-width="1.5" marker-end="url(#st-flow-arrow)"/>
    <path d="M 380 358 L 380 408" stroke="{line_color}" stroke-width="1.5" marker-end="url(#st-flow-arrow)"/>
    <path d="M 620 358 L 620 408" stroke="{line_color}" stroke-width="1.5" marker-end="url(#st-flow-arrow)"/>

    <path d="M 135 458 L 135 496 L 445 496 L 445 558" stroke="{line_color}" stroke-width="1.5" marker-end="url(#st-flow-arrow)"/>
    <path d="M 380 458 L 380 522 L 480 522 L 480 558" stroke="{line_color}" stroke-width="1.5" marker-end="url(#st-flow-arrow)"/>
    <path d="M 620 458 L 620 522 L 520 522 L 520 558" stroke="{line_color}" stroke-width="1.5" marker-end="url(#st-flow-arrow)"/>
    <path d="M 865 458 L 865 496 L 555 496 L 555 558" stroke="{line_color}" stroke-width="1.5" marker-end="url(#st-flow-arrow)"/>

    <!-- Nodes -->
    <g>
      <rect x="405" y="30" width="190" height="48" rx="10" fill="{node_bg}" stroke="{node_stroke}" stroke-width="1.5"/>
      <text x="500" y="54" fill="{node_text}" font-family="'Plus Jakarta Sans', sans-serif" font-size="13.5" font-weight="600" text-anchor="middle" dominant-baseline="central">MovieLens 1M Dataset</text>
    </g>
    <g>
      <rect x="405" y="110" width="190" height="48" rx="10" fill="{node_bg}" stroke="{node_stroke}" stroke-width="1.5"/>
      <text x="500" y="134" fill="{node_text}" font-family="'Plus Jakarta Sans', sans-serif" font-size="13.5" font-weight="600" text-anchor="middle" dominant-baseline="central">Load and Parse Files</text>
    </g>
    <g>
      <rect x="385" y="190" width="230" height="54" rx="10" fill="{node_bg}" stroke="{node_stroke}" stroke-width="1.5"/>
      <text x="500" y="209" fill="{node_text}" font-family="'Plus Jakarta Sans', sans-serif" font-size="13" font-weight="600" text-anchor="middle" dominant-baseline="central">Data Cleaning and</text>
      <text x="500" y="226" fill="{node_text}" font-family="'Plus Jakarta Sans', sans-serif" font-size="13" font-weight="600" text-anchor="middle" dominant-baseline="central">Preprocessing</text>
    </g>

    <g>
      <rect x="40" y="310" width="190" height="48" rx="10" fill="{node_bg}" stroke="{node_stroke}" stroke-width="1.5"/>
      <text x="135" y="334" fill="{node_text}" font-family="'Plus Jakarta Sans', sans-serif" font-size="13" font-weight="600" text-anchor="middle" dominant-baseline="central">Exploratory Data Analysis</text>
    </g>
    <g>
      <rect x="285" y="310" width="190" height="48" rx="10" fill="{node_bg}" stroke="{node_stroke}" stroke-width="1.5"/>
      <text x="380" y="334" fill="{node_text}" font-family="'Plus Jakarta Sans', sans-serif" font-size="13.5" font-weight="600" text-anchor="middle" dominant-baseline="central">Genre Encoding</text>
    </g>
    <g>
      <rect x="525" y="310" width="190" height="48" rx="10" fill="{node_bg}" stroke="{node_stroke}" stroke-width="1.5"/>
      <text x="620" y="334" fill="{node_text}" font-family="'Plus Jakarta Sans', sans-serif" font-size="13.5" font-weight="600" text-anchor="middle" dominant-baseline="central">User-Genre Matrix</text>
    </g>

    <g>
      <rect x="40" y="410" width="190" height="48" rx="10" fill="{node_bg}" stroke="{node_stroke}" stroke-width="1.5"/>
      <text x="135" y="434" fill="{node_text}" font-family="'Plus Jakarta Sans', sans-serif" font-size="13.5" font-weight="600" text-anchor="middle" dominant-baseline="central">Statistical Findings</text>
    </g>
    <g>
      <rect x="285" y="410" width="190" height="48" rx="10" fill="{node_bg}" stroke="{node_stroke}" stroke-width="1.5"/>
      <text x="380" y="434" fill="{node_text}" font-family="'Plus Jakarta Sans', sans-serif" font-size="13" font-weight="600" text-anchor="middle" dominant-baseline="central">Apriori Association Rules</text>
    </g>
    <g>
      <rect x="525" y="410" width="190" height="48" rx="10" fill="{node_bg}" stroke="{node_stroke}" stroke-width="1.5"/>
      <text x="620" y="434" fill="{node_text}" font-family="'Plus Jakarta Sans', sans-serif" font-size="13" font-weight="600" text-anchor="middle" dominant-baseline="central">StandardScaler and PCA</text>
    </g>
    <g>
      <rect x="770" y="410" width="190" height="48" rx="10" fill="{node_bg}" stroke="{node_stroke}" stroke-width="1.5"/>
      <text x="865" y="434" fill="{node_text}" font-family="'Plus Jakarta Sans', sans-serif" font-size="13.5" font-weight="600" text-anchor="middle" dominant-baseline="central">Age and Genre Analysis</text>
    </g>

    <g>
      <rect x="405" y="560" width="190" height="48" rx="10" fill="{node_bg}" stroke="{node_stroke}" stroke-width="1.5"/>
      <text x="500" y="584" fill="{node_text}" font-family="'Plus Jakarta Sans', sans-serif" font-size="13.5" font-weight="600" text-anchor="middle" dominant-baseline="central">Interactive Website</text>
    </g>
  </svg>
</div>
""", unsafe_allow_html=True)ue)

# SECTION 2: Stage Breakdown
st.subheader("2. Stage Breakdown & Methodological Logic")

col_w1, col_w2 = st.columns(2)

with col_w1:
    st.markdown("""
    <div class="analysis-card">
        <div class="analysis-title">Stage 1 to 3: Ingestion & Preprocessing</div>
        <div class="analysis-subtitle">Foundational data structuring</div>
        <ul style="font-size:0.875rem; line-height:1.75; margin-top:8px; padding-left:18px;">
            <li><b>Input:</b> Ingested 1,000,209 ratings, 3,883 movies, and 6,040 user profiles from double-colon delimited <code>.dat</code> flat files.</li>
            <li><b>Parsing:</b> Applied Latin-1 charset decoding to preserve catalog titles and parsed timestamps to ISO standard dates.</li>
            <li><b>Cleaning:</b> Handled multi-label pipe-separated genres by exploding into 18 atomic genre entities.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col_w2:
    st.markdown("""
    <div class="analysis-card">
        <div class="analysis-title">Four Parallel Analytical Branches</div>
        <div class="analysis-subtitle">Specialized unsupervised data mining workflows</div>
        <ul style="font-size:0.875rem; line-height:1.75; margin-top:8px; padding-left:18px;">
            <li><b>Branch A (EDA):</b> Evaluated rating score skewness (Mode 4 ★ = 34.9%) and benchmarked volume vs critical acclaim.</li>
            <li><b>Branch B (Apriori):</b> Built a binary transaction matrix and mined frequent itemsets (Min Support: 0.02, Lift up to 12.38x).</li>
            <li><b>Branch C (PCA):</b> Constructed a 6,040 × 18 User-Genre matrix, normalized via StandardScaler, and projected onto 2 principal components.</li>
            <li><b>Branch D (Demographics):</b> Cross-tabulated demographic age cohorts with genre preferences to uncover leniency gradients.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
