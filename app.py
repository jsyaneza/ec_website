import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
from datetime import datetime, timedelta

# Page Configuration
st.set_page_config(
    page_title="Juan Sebastián Yáñez - Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        border-left: 4px solid #0284c7;
    }
    </style>
    """, unsafe_allow_html=True)

# Header
st.markdown("# 📊 Research & Analytics Dashboard")
st.markdown("### Juan Sebastián Yáñez Albarracín - Academic Portfolio")
st.markdown("---")

# Sidebar Navigation
st.sidebar.markdown("## 📋 Dashboard Sections")
section = st.sidebar.radio(
    "Select a section:",
    ["Overview", "Research Analytics", "Skills Assessment", "Project Progress", "Publications"]
)

# ============== SECTION 1: OVERVIEW ==============
if section == "Overview":
    st.markdown("## 🎯 Academic Overview")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 🎓 Education")
        st.info("""
        **Current:** Master's in International Development
        - Nagoya University, Japan
        - GSID (Graduate School of International Development)
        
        **Background:**
        - B.S. Biology (UNAL)
        - B.S. Visual Arts (UDFJC)
        """)
    
    with col2:
        st.markdown("### 💼 Professional Experience")
        st.success("""
        **UNOSEIS18 (Startup)**
        - CFO & Business Development Manager
        - Duration: Dec 2012 - Present (11+ years)
        
        **Expertise:**
        - Financial Analysis
        - Strategic Planning
        - Business Development
        """)
    
    with col3:
        st.markdown("### 🔬 Research Focus")
        st.warning("""
        **Regional Econometrics**
        - Spatial Analysis
        - Economic Geography
        - Development Economics
        
        **Geographic Focus:**
        - Colombian Regions
        - Productivity Gaps
        - Infrastructure Impact
        """)
    
    st.markdown("---")
    
    # Key Metrics
    st.markdown("## 📈 Key Metrics")
    
    metric1, metric2, metric3, metric4 = st.columns(4)
    
    with metric1:
        st.metric("Years in Business", "11+", "+2 years")
    
    with metric2:
        st.metric("Research Areas", "3", "Major focus areas")
    
    with metric3:
        st.metric("Technical Skills", "8", "Tools mastered")
    
    with metric4:
        st.metric("Education Degrees", "2", "Bachelor's degrees")

# ============== SECTION 2: RESEARCH ANALYTICS ==============
elif section == "Research Analytics":
    st.markdown("## 📚 Research Analytics")
    
    st.markdown("### Research Areas Distribution")
    
    research_areas = {
        "Regional Econometrics": 40,
        "Spatial Analysis": 35,
        "Transport Networks": 15,
        "Development Economics": 10
    }
    
    fig_pie = go.Figure(data=[go.Pie(
        labels=list(research_areas.keys()),
        values=list(research_areas.values()),
        marker=dict(colors=['#0284c7', '#38bdf8', '#7dd3fc', '#bfdbfe'])
    )])
    
    fig_pie.update_layout(
        title="Research Focus Distribution",
        height=400,
        showlegend=True
    )
    
    st.plotly_chart(fig_pie, use_container_width=True)
    
    # Research Progress Timeline
    st.markdown("### Research Development Timeline")
    
    timeline_data = {
        "Phase": ["Literature Review", "Data Collection", "Analysis", "Writing", "Publication"],
        "Progress": [100, 75, 50, 30, 10],
        "Status": ["✅ Completed", "🔄 In Progress", "🔄 In Progress", "⏳ Pending", "📅 Planned"]
    }
    
    timeline_df = pd.DataFrame(timeline_data)
    
    fig_bar = go.Figure(data=[
        go.Bar(
            x=timeline_df["Phase"],
            y=timeline_df["Progress"],
            marker=dict(color=['#10b981', '#f59e0b', '#f59e0b', '#ef4444', '#6b7280']),
            text=[f"{p}%" for p in timeline_df["Progress"]],
            textposition="auto"
        )
    ])
    
    fig_bar.update_layout(
        title="Research Progress by Phase",
        xaxis_title="Phase",
        yaxis_title="Progress (%)",
        height=400,
        showlegend=False
    )
    
    st.plotly_chart(fig_bar, use_container_width=True)
    
    # Status Table
    st.markdown("### Project Status Details")
    st.dataframe(timeline_df, use_container_width=True, hide_index=True)

# ============== SECTION 3: SKILLS ASSESSMENT ==============
elif section == "Skills Assessment":
    st.markdown("## 🛠️ Technical & Professional Skills")
    
    # Skills Data
    technical_skills = {
        "Power BI": 92,
        "R Software": 75,
        "Python": 45,
        "MatLab": 25,
        "Database Management": 70,
        "Sharp 3D": 45
    }
    
    professional_skills = {
        "Strategic Planning": 75,
        "Financial Analysis": 85,
        "Business Development": 80,
        "Design": 75,
        "Research": 70,
        "Leadership": 80
    }
    
    # Create tabs for skills
    tab1, tab2 = st.tabs(["Technical Skills", "Professional Skills"])
    
    with tab1:
        st.markdown("### Technical Proficiency Level")
        
        fig_tech = go.Figure(data=[
            go.Bar(
                y=list(technical_skills.keys()),
                x=list(technical_skills.values()),
                orientation='h',
                marker=dict(color='#0284c7'),
                text=[f"{v}%" for v in technical_skills.values()],
                textposition="auto"
            )
        ])
        
        fig_tech.update_layout(
            title="Technical Skills Proficiency",
            xaxis_title="Proficiency Level (%)",
            height=400,
            showlegend=False,
            xaxis=dict(range=[0, 100])
        )
        
        st.plotly_chart(fig_tech, use_container_width=True)
    
    with tab2:
        st.markdown("### Professional Skills Proficiency")
        
        fig_prof = go.Figure(data=[
            go.Bar(
                y=list(professional_skills.keys()),
                x=list(professional_skills.values()),
                orientation='h',
                marker=dict(color='#38bdf8'),
                text=[f"{v}%" for v in professional_skills.values()],
                textposition="auto"
            )
        ])
        
        fig_prof.update_layout(
            title="Professional Skills Proficiency",
            xaxis_title="Proficiency Level (%)",
            height=400,
            showlegend=False,
            xaxis=dict(range=[0, 100])
        )
        
        st.plotly_chart(fig_prof, use_container_width=True)
    
    # Skills Summary
    st.markdown("### Skills Summary")
    col1, col2 = st.columns(2)
    
    with col1:
        avg_technical = np.mean(list(technical_skills.values()))
        st.metric("Average Technical Proficiency", f"{avg_technical:.1f}%")
    
    with col2:
        avg_professional = np.mean(list(professional_skills.values()))
        st.metric("Average Professional Proficiency", f"{avg_professional:.1f}%")

# ============== SECTION 4: PROJECT PROGRESS ==============
elif section == "Project Progress":
    st.markdown("## 🚀 Project Progress")
    
    st.markdown("### Main Research Project")
    st.info("""
    **Title:** Analysis of the Impact of Road Infrastructure on Regional Development in Colombia
    
    **Status:** 🔄 In Progress
    
    **Duration:** 2024 - 2025 (Expected completion)
    """)
    
    # Project Milestones
    st.markdown("### Project Milestones")
    
    milestones = {
        "Milestone": [
            "Project Proposal",
            "Literature Review Complete",
            "Data Collection Started",
            "Preliminary Analysis",
            "Results Compilation",
            "Thesis Writing",
            "Final Defense"
        ],
        "Completion": [100, 100, 85, 50, 25, 10, 0],
        "Target Date": [
            "Jan 2024",
            "Mar 2024",
            "May 2024",
            "Jul 2024",
            "Sep 2024",
            "Nov 2024",
            "Jan 2025"
        ]
    }
    
    milestones_df = pd.DataFrame(milestones)
    
    fig_milestone = go.Figure(data=[
        go.Scatter(
            x=milestones_df["Target Date"],
            y=milestones_df["Completion"],
            mode='lines+markers+text',
            name='Progress',
            marker=dict(size=10, color='#0284c7'),
            text=[f"{c}%" for c in milestones_df["Completion"]],
            textposition="top center",
            line=dict(color='#0284c7', width=3)
        )
    ])
    
    fig_milestone.update_layout(
        title="Project Timeline & Completion Status",
        xaxis_title="Target Date",
        yaxis_title="Completion (%)",
        height=400,
        hovermode='x unified',
        yaxis=dict(range=[0, 110])
    )
    
    st.plotly_chart(fig_milestone, use_container_width=True)
    
    # Deliverables
    st.markdown("### Project Deliverables")
    
    deliverables = pd.DataFrame({
        "Deliverable": [
            "Research Proposal",
            "Literature Review Paper",
            "Data Analysis Report",
            "Methodology Document",
            "Findings Presentation",
            "Final Thesis"
        ],
        "Status": [
            "✅ Completed",
            "✅ Completed",
            "🔄 In Progress",
            "🔄 In Progress",
            "⏳ Pending",
            "📅 Planned"
        ],
        "Due Date": [
            "Jan 2024",
            "Mar 2024",
            "Jul 2024",
            "Aug 2024",
            "Dec 2024",
            "Jan 2025"
        ]
    })
    
    st.dataframe(deliverables, use_container_width=True, hide_index=True)

# ============== SECTION 5: PUBLICATIONS ==============
elif section == "Publications":
    st.markdown("## 📰 Academic Work & Publications")
    
    st.markdown("### Publications & Presentations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 📄 Research Papers")
        st.success("""
        **Status:** In Preparation
        
        - Regional Productivity Gaps in Colombia
        - Road Infrastructure & Economic Development
        - Spatial Analysis of Colombian Municipalities
        """)
    
    with col2:
        st.markdown("#### 🎓 Academic Work")
        st.info("""
        **Completed:**
        - Bachelor's Thesis (Visual Arts) - "Frío Sólido"
        - Multiple Research Projects
        
        **Current:**
        - Master's Thesis (In Progress)
        - Capstone Project Supervision
        """)
    
    st.markdown("---")
    
    st.markdown("### Research Interests & Topics")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**Regional Econometrics**")
        st.write("""
        - Productivity Analysis
        - Regional Disparities
        - Development Gaps
        """)
    
    with col2:
        st.markdown("**Spatial Analysis**")
        st.write("""
        - Geographic Patterns
        - Transport Networks
        - Agglomeration Effects
        """)
    
    with col3:
        st.markdown("**Development Economics**")
        st.write("""
        - Economic Growth
        - Territorial Development
        - Infrastructure Impact
        """)
    
    st.markdown("---")
    
    # Contact Information
    st.markdown("### 📧 Contact & Social")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write("**Email**")
        st.code("jsyaneza@unal.edu.co")
    
    with col2:
        st.write("**Phone**")
        st.code("+57 (316) 520 8921")
    
    with col3:
        st.write("**Location**")
        st.code("Bogotá DC, Colombia")
    
    st.markdown("**Current Institution:** Nagoya University, Japan - GSID")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>Dashboard created with Streamlit | Last updated: 2024</p>
    <p>Juan Sebastián Yáñez Albarracín - Academic Portfolio</p>
</div>
""", unsafe_allow_html=True)
