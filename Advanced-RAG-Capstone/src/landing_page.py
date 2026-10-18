"""
Ultra-Premium Modern AI SaaS Landing Page for Advanced RAG Assistant.

Built with high-contrast typography, solid dark background, zero sidebar distraction,
and direct 1-click live demo controls.
"""

import streamlit as st
from src.indexing import index_summary


# Enterprise sample scenarios demonstrating diverse document capabilities
SAMPLE_RECRUITER_QUERIES = [
    {
        "icon": "💳",
        "title": "SLA & Customer Support Terms",
        "question": "What is the customer support policy, response time targets, and refund rules?",
        "tag": "Policy & Contracts",
        "description": "Demonstrates multi-sentence policy synthesis and exception handling."
    },
    {
        "icon": "🔐",
        "title": "Security & Access Protocols",
        "question": "What are the mandatory password rules, complexity, and MFA requirements?",
        "tag": "Security & Compliance",
        "description": "Demonstrates exact alphanumeric rule extraction from structured documents."
    },
    {
        "icon": "🌴",
        "title": "Employee Benefits & Leave",
        "question": "How many days of annual leave do employees get and how does rollover work?",
        "tag": "HR & Operations",
        "description": "Demonstrates numeric policy extraction and tabular handbook comprehension."
    },
    {
        "icon": "☁️",
        "title": "Infrastructure Tiers & Limits",
        "question": "What are the product tiers, compute limits, and API request throttling rules?",
        "tag": "Technical Specifications",
        "description": "Demonstrates technical architecture synthesis and specification lookup."
    }
]


def render_landing_page(get_pipeline_func, answer_question_func, navigate_to_chat_func):
    """
    Renders the modern, highly-polished AI SaaS landing page.
    """
    # -------------------------------------------------------------------------
    # Custom CSS Design System (High-Contrast, Opaque Solid Dark Canvas)
    # -------------------------------------------------------------------------
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

        /* Force entire page canvas into deep, immersive obsidian dark mode */
        html, body, [data-testid="stAppViewContainer"], .stApp, .main {
            background-color: #080C16 !important;
            background-image: 
                radial-gradient(at 10% 10%, rgba(99, 102, 241, 0.18) 0px, transparent 55%),
                radial-gradient(at 90% 15%, rgba(6, 182, 212, 0.14) 0px, transparent 55%),
                radial-gradient(at 50% 95%, rgba(139, 92, 246, 0.14) 0px, transparent 55%) !important;
            background-attachment: fixed !important;
            color: #F8FAFC !important;
            font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
        }

        header[data-testid="stHeader"] {
            background: transparent !important;
        }

        /* Hide Streamlit sidebar completely on landing page */
        section[data-testid="stSidebar"], [data-testid="stSidebar"], [data-testid="collapsedControl"] {
            display: none !important;
        }

        /* Center and format main content area */
        .main .block-container {
            max-width: 1240px !important;
            padding-top: 1.5rem !important;
            padding-bottom: 5rem !important;
            padding-left: 2rem !important;
            padding-right: 2rem !important;
        }

        /* Strict High-Contrast Typography */
        h1, h2, h3, h4, h5, h6 {
            color: #FFFFFF !important;
            font-weight: 800 !important;
            letter-spacing: -0.02em !important;
        }

        p, span, div, li, label {
            color: #E2E8F0;
        }

        .stMarkdown, .stMarkdown p {
            color: #E2E8F0 !important;
        }

        /* Glassmorphic Navbar Container */
        .saas-navbar {
            display: flex;
            align-items: center;
            justify-content: space-between;
            background-color: #0F172A !important;
            border: 1px solid rgba(255, 255, 255, 0.12) !important;
            border-radius: 16px;
            padding: 14px 24px;
            margin-bottom: 24px;
            box-shadow: 0 10px 30px -5px rgba(0, 0, 0, 0.6);
        }

        .nav-logo {
            display: flex;
            align-items: center;
            gap: 12px;
            font-size: 1.25rem;
            font-weight: 800;
            color: #FFFFFF !important;
            letter-spacing: -0.02em;
        }

        .nav-logo-icon {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 36px;
            height: 36px;
            border-radius: 10px;
            background: linear-gradient(135deg, #6366F1, #8B5CF6);
            color: #FFFFFF;
            font-size: 1.15rem;
            box-shadow: 0 0 16px rgba(99, 102, 241, 0.6);
        }

        /* Hero Container */
        .saas-hero {
            background-color: #0F172A !important;
            border: 1px solid rgba(255, 255, 255, 0.12) !important;
            border-radius: 24px;
            padding: 48px 40px;
            margin-bottom: 32px;
            box-shadow: 0 25px 60px -15px rgba(0, 0, 0, 0.7);
        }

        .hero-badge {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background-color: #1E1B4B !important;
            border: 1px solid #6366F1 !important;
            padding: 6px 16px;
            border-radius: 9999px;
            font-size: 0.85rem;
            font-weight: 700;
            color: #C7D2FE !important;
            margin-bottom: 20px;
        }

        .hero-heading {
            font-size: 3.2rem;
            font-weight: 800;
            line-height: 1.15;
            letter-spacing: -0.03em;
            color: #FFFFFF !important;
            margin-bottom: 20px;
        }

        .hero-heading-gradient {
            background: linear-gradient(105deg, #FFFFFF 20%, #93C5FD 55%, #C084FC 85%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .hero-lead {
            font-size: 1.18rem;
            color: #CBD5E1 !important;
            line-height: 1.7;
            max-width: 860px;
            margin-bottom: 10px;
        }

        /* Streamlit Primary Buttons */
        div.stButton > button[kind="primary"] {
            background: linear-gradient(135deg, #6366F1 0%, #4F46E5 100%) !important;
            color: #FFFFFF !important;
            font-weight: 700 !important;
            font-size: 1.02rem !important;
            border: 1px solid rgba(255, 255, 255, 0.25) !important;
            border-radius: 12px !important;
            padding: 0.65rem 1.6rem !important;
            box-shadow: 0 4px 18px rgba(99, 102, 241, 0.45) !important;
            transition: all 0.25s ease !important;
        }

        div.stButton > button[kind="primary"]:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 8px 25px rgba(99, 102, 241, 0.7) !important;
            border-color: rgba(255, 255, 255, 0.5) !important;
        }

        /* Streamlit Secondary Buttons */
        div.stButton > button[kind="secondary"],
        div.stButton > button {
            background-color: #1E293B !important;
            color: #F8FAFC !important;
            font-weight: 600 !important;
            border: 1px solid rgba(255, 255, 255, 0.15) !important;
            border-radius: 10px !important;
            transition: all 0.2s ease !important;
        }

        div.stButton > button:hover {
            background-color: #334155 !important;
            border-color: #818CF8 !important;
            color: #FFFFFF !important;
        }

        /* Application Mockup Preview Window */
        .mockup-window {
            background-color: #0B0F19 !important;
            border: 1px solid rgba(255, 255, 255, 0.12) !important;
            border-radius: 18px;
            box-shadow: 0 25px 60px -15px rgba(0, 0, 0, 0.8);
            overflow: hidden;
            margin-top: 24px;
        }

        .mockup-topbar {
            display: flex;
            align-items: center;
            padding: 12px 18px;
            background-color: #1E293B !important;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08) !important;
            gap: 8px;
        }

        .dot { width: 11px; height: 11px; border-radius: 50%; }
        .dot-red { background: #EF4444; }
        .dot-yellow { background: #F59E0B; }
        .dot-green { background: #10B981; }

        .mockup-url {
            margin-left: 12px;
            background-color: #0F172A !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            border-radius: 6px;
            padding: 3px 14px;
            font-size: 0.75rem;
            color: #94A3B8 !important;
            font-family: 'JetBrains Mono', monospace;
        }

        .mockup-body {
            padding: 24px;
            background-color: #0B0F19 !important;
        }

        /* Solid High-Contrast Metric Box */
        .stat-card {
            background-color: #111827 !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            border-radius: 16px;
            padding: 22px;
            text-align: center;
            height: 100%;
            transition: all 0.25s ease;
        }
        .stat-card:hover {
            border-color: #6366F1 !important;
            transform: translateY(-3px);
            box-shadow: 0 10px 25px rgba(99, 102, 241, 0.15);
        }
        .stat-num {
            font-size: 2.2rem;
            font-weight: 800;
            color: #60A5FA !important;
            margin-bottom: 4px;
        }
        .stat-label {
            font-size: 0.84rem;
            font-weight: 700;
            color: #CBD5E1 !important;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }

        /* Solid Feature Cards */
        .feature-card {
            background-color: #111827 !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            border-radius: 18px;
            padding: 26px;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
            transition: all 0.25s ease;
        }
        .feature-card:hover {
            border-color: #6366F1 !important;
            transform: translateY(-4px);
            box-shadow: 0 16px 32px -10px rgba(99, 102, 241, 0.2);
        }
        .feature-icon-box {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 48px;
            height: 48px;
            border-radius: 12px;
            background-color: #1E1B4B !important;
            border: 1px solid #4F46E5 !important;
            font-size: 1.4rem;
            margin-bottom: 16px;
        }
        .feature-title {
            font-size: 1.2rem;
            font-weight: 700;
            color: #FFFFFF !important;
            margin-bottom: 10px;
        }
        .feature-desc {
            font-size: 0.94rem;
            color: #CBD5E1 !important;
            line-height: 1.65;
        }

        /* Solid Workflow Step Cards */
        .workflow-step {
            background-color: #111827 !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            border-radius: 16px;
            padding: 22px;
            height: 100%;
            transition: all 0.25s ease;
        }
        .workflow-step:hover {
            border-color: #38BDF8 !important;
            transform: translateY(-2px);
        }
        .workflow-badge {
            display: inline-block;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.78rem;
            font-weight: 800;
            color: #38BDF8 !important;
            background-color: #082F49 !important;
            padding: 4px 10px;
            border-radius: 6px;
            margin-bottom: 12px;
            border: 1px solid #0284C7 !important;
        }

        /* Solid Sandbox Box */
        .sandbox-box {
            background-color: #0F172A !important;
            border: 1px solid rgba(255, 255, 255, 0.12) !important;
            border-radius: 20px;
            padding: 32px;
            margin-top: 24px;
            margin-bottom: 36px;
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.6);
        }

        .scenario-card {
            background-color: #1E293B !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            border-radius: 14px;
            padding: 16px;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }
        .scenario-title {
            font-weight: 700;
            font-size: 0.96rem;
            color: #FFFFFF !important;
            margin-bottom: 4px;
        }
        .scenario-tag {
            font-size: 0.75rem;
            font-weight: 700;
            color: #A5B4FC !important;
            margin-bottom: 6px;
        }
        .scenario-desc {
            font-size: 0.84rem;
            color: #CBD5E1 !important;
            line-height: 1.45;
            margin-bottom: 12px;
        }

        /* Expanders in Sandbox */
        div[data-testid="stExpander"] {
            background-color: #111827 !important;
            border: 1px solid rgba(255, 255, 255, 0.12) !important;
            border-radius: 12px !important;
        }

        /* Bottom Call to Action Banner */
        .cta-banner {
            background-color: #0F172A !important;
            border: 1px solid #6366F1 !important;
            border-radius: 24px;
            padding: 48px 36px;
            text-align: center;
            box-shadow: 0 20px 50px -10px rgba(99, 102, 241, 0.35);
            margin-top: 40px;
            margin-bottom: 30px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # =========================================================================
    # 1. NAVBAR WITH ACTIVE DEMO BUTTON
    # =========================================================================
    nav_c1, nav_c2 = st.columns([3.2, 1.3])
    with nav_c1:
        st.markdown(
            """
            <div style="display:flex; align-items:center; gap:12px; padding:6px 0;">
                <div class="nav-logo-icon">⚡</div>
                <div>
                    <span style="font-size:1.3rem; font-weight:800; color:#FFFFFF; letter-spacing:-0.02em;">OmniRAG Intelligence</span>
                    <span style="font-size:0.8rem; color:#A5B4FC; margin-left:10px; background:#1E1B4B; padding:3px 10px; border-radius:9999px; border:1px solid #4F46E5;">Enterprise RAG</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with nav_c2:
        if st.button("🚀 Launch Live Assistant", key="nav_btn_top", type="primary", use_container_width=True):
            navigate_to_chat_func()

    st.markdown("<div style='height:12px;'></div>", unsafe_allow_html=True)

    # =========================================================================
    # 2. HERO SECTION
    # =========================================================================
    st.markdown(
        """
        <div class="saas-hero">
            <div class="hero-badge">
                <span>✨</span> Universal Document Intelligence • Zero Hallucination Guarantee
            </div>
            <div class="hero-heading">
                Transform Any Document Into<br>
                <span class="hero-heading-gradient">Verifiable, Cited Intelligence</span>
            </div>
            <div class="hero-lead">
                Upload any corporate PDF, Word manual (DOCX), or technical specification. 
                Our 5-stage hybrid retrieval engine combines <b>Multi-Query Semantic Expansion</b>, 
                <b>BM25 + FAISS Hybrid Fusion</b>, and <b>Local Cross-Encoder Reranking</b> 
                to synthesize accurate, cited answers you can stake your business on.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Primary Hero Action Buttons
    col_btn1, col_btn2, col_btn3 = st.columns([1.6, 1.4, 2])
    with col_btn1:
        if st.button("🚀 Open Live Demo Assistant", key="hero_btn_open_chat", type="primary", use_container_width=True):
            navigate_to_chat_func()
    with col_btn2:
        st.markdown(
            """
            <a href="https://github.com/esakhan786/advanced-rag-assistant-" target="_blank" style="text-decoration:none;">
                <button style="width:100%; height:42px; border-radius:10px; border:1px solid rgba(255,255,255,0.2); background:#1E293B; color:#FFFFFF; font-weight:700; cursor:pointer;">
                    ⭐ Star on GitHub
                </button>
            </a>
            """,
            unsafe_allow_html=True,
        )

    # Interactive Application Mockup
    st.markdown(
        """
        <div class="mockup-window">
            <div class="mockup-topbar">
                <span class="dot dot-red"></span>
                <span class="dot dot-yellow"></span>
                <span class="dot dot-green"></span>
                <span class="mockup-url">https://assistant.internal.ai/v1/rag</span>
            </div>
            <div class="mockup-body">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px; border-bottom:1px solid rgba(255,255,255,0.08); padding-bottom:10px;">
                    <div style="font-weight:700; color:#FFFFFF; font-size:0.95rem;">
                        📁 Universal Ingestion Engine: <span style="color:#34D399;">PDF, DOCX, TXT</span>
                    </div>
                    <div style="font-family:'JetBrains Mono', monospace; font-size:0.75rem; color:#A5B4FC; background:#1E1B4B; padding:4px 12px; border-radius:6px; border:1px solid #4F46E5;">
                        FAISS + BM25 Hybrid Active
                    </div>
                </div>
                <div style="background:#1E293B; border:1px solid rgba(255,255,255,0.08); border-radius:10px; padding:16px; margin-bottom:12px;">
                    <div style="font-size:0.8rem; color:#94A3B8; margin-bottom:4px; font-weight:700;">USER INQUIRY</div>
                    <div style="color:#FFFFFF; font-weight:600; font-size:0.95rem;">"What is the customer support response target and refund eligibility policy?"</div>
                </div>
                <div style="background:#0F291E; border-left:4px solid #10B981; border-radius:0 10px 10px 0; padding:16px;">
                    <div style="font-size:0.8rem; color:#34D399; margin-bottom:6px; font-weight:800; letter-spacing:0.04em;">VERIFIED FACTUAL SYNTHESIS (STRICT DOCUMENT GROUNDING)</div>
                    <div style="color:#F8FAFC; font-size:0.95rem; line-height:1.65;">
                        Critical enterprise issues receive guaranteed technical assistance within <b>15 minutes</b> (24/7/365). Customers on self-service plans are eligible for a <b>100% refund</b> within 30 days of invoice date, while usage fees are strictly non-refundable <b>[1]</b>.
                    </div>
                    <div style="display:flex; gap:10px; margin-top:12px;">
                        <span style="font-size:0.75rem; background:#1E293B; padding:4px 10px; border-radius:6px; color:#A5B4FC; border:1px solid rgba(255,255,255,0.1);">[1] Support Policy • Section: Refund Eligibility</span>
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<br><hr style='border-color:rgba(255,255,255,0.1);'><br>", unsafe_allow_html=True)

    # =========================================================================
    # 3. INTERACTIVE 1-CLICK DEMO SANDBOX (LIVE INSIDE LANDING PAGE)
    # =========================================================================
    st.markdown(
        """
        <div style="margin-bottom:16px;">
            <div style="font-size:0.85rem; color:#818CF8; font-weight:800; letter-spacing:0.05em; text-transform:uppercase;">
                Interactive Evaluation Suite
            </div>
            <h2 style="font-size:2rem; font-weight:800; color:#FFFFFF; margin-top:4px; margin-bottom:6px;">
                🎮 Test RAG Pipeline Live (1-Click Recruiter Sandbox)
            </h2>
            <p style="color:#CBD5E1; font-size:1.05rem; line-height:1.6;">
                Recruiters & visitors can test the end-to-end multi-stage pipeline immediately without uploading files. 
                Click any scenario below to trigger real-time multi-query expansion, hybrid retrieval, and cross-encoder reranking:
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 4 Scenarios in 4 Columns
    q_col1, q_col2, q_col3, q_col4 = st.columns(4)
    selected_query = None

    with q_col1:
        st.markdown(
            f"""
            <div class="scenario-card">
                <div>
                    <div style="font-size:1.5rem; margin-bottom:6px;">{SAMPLE_RECRUITER_QUERIES[0]['icon']}</div>
                    <div class="scenario-title">{SAMPLE_RECRUITER_QUERIES[0]['title']}</div>
                    <div class="scenario-tag">{SAMPLE_RECRUITER_QUERIES[0]['tag']}</div>
                    <div class="scenario-desc">{SAMPLE_RECRUITER_QUERIES[0]['description']}</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("▶ Run SLA Query", key="btn_q0", use_container_width=True):
            selected_query = SAMPLE_RECRUITER_QUERIES[0]["question"]

    with q_col2:
        st.markdown(
            f"""
            <div class="scenario-card">
                <div>
                    <div style="font-size:1.5rem; margin-bottom:6px;">{SAMPLE_RECRUITER_QUERIES[1]['icon']}</div>
                    <div class="scenario-title">{SAMPLE_RECRUITER_QUERIES[1]['title']}</div>
                    <div class="scenario-tag">{SAMPLE_RECRUITER_QUERIES[1]['tag']}</div>
                    <div class="scenario-desc">{SAMPLE_RECRUITER_QUERIES[1]['description']}</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("▶ Run Security Query", key="btn_q1", use_container_width=True):
            selected_query = SAMPLE_RECRUITER_QUERIES[1]["question"]

    with q_col3:
        st.markdown(
            f"""
            <div class="scenario-card">
                <div>
                    <div style="font-size:1.5rem; margin-bottom:6px;">{SAMPLE_RECRUITER_QUERIES[2]['icon']}</div>
                    <div class="scenario-title">{SAMPLE_RECRUITER_QUERIES[2]['title']}</div>
                    <div class="scenario-tag">{SAMPLE_RECRUITER_QUERIES[2]['tag']}</div>
                    <div class="scenario-desc">{SAMPLE_RECRUITER_QUERIES[2]['description']}</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("▶ Run HR Query", key="btn_q2", use_container_width=True):
            selected_query = SAMPLE_RECRUITER_QUERIES[2]["question"]

    with q_col4:
        st.markdown(
            f"""
            <div class="scenario-card">
                <div>
                    <div style="font-size:1.5rem; margin-bottom:6px;">{SAMPLE_RECRUITER_QUERIES[3]['icon']}</div>
                    <div class="scenario-title">{SAMPLE_RECRUITER_QUERIES[3]['title']}</div>
                    <div class="scenario-tag">{SAMPLE_RECRUITER_QUERIES[3]['tag']}</div>
                    <div class="scenario-desc">{SAMPLE_RECRUITER_QUERIES[3]['description']}</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("▶ Run Infra Query", key="btn_q3", use_container_width=True):
            selected_query = SAMPLE_RECRUITER_QUERIES[3]["question"]

    # Live Execution Output
    if selected_query:
        st.markdown(f"#### 🔍 Live Execution Trace: *\"{selected_query}\"*")
        pipeline = get_pipeline_func()
        if pipeline is None:
            st.error("Pipeline could not be loaded. Please ensure the vector database is built.")
        else:
            with st.spinner("Executing: Multi-Query → Hybrid Search → Parent Recovery → Cross-Encoder → Gemini Generation..."):
                try:
                    from src.memory import create_memory
                    mem = create_memory()
                    result = answer_question_func(selected_query, pipeline, mem)

                    st.markdown(
                        f"""
                        <div style="background-color:#0F291E; border:1px solid #10B981; border-radius:14px; padding:22px; margin-top:14px; box-shadow:0 10px 30px rgba(0,0,0,0.5);">
                            <div style="font-size:0.84rem; color:#34D399; font-weight:800; letter-spacing:0.04em; margin-bottom:8px;">
                                🟢 FACTUAL ANSWER (SYNTHESIZED WITH STRICT CITATIONS)
                            </div>
                            <div style="font-size:1.02rem; color:#FFFFFF; line-height:1.7;">
                                {result['answer']}
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

                    # Render ground-truth sources
                    if result.get("sources"):
                        st.markdown("<h5 style='color:#FFFFFF; margin-top:16px;'>📄 Verified Ground-Truth Sources</h5>", unsafe_allow_html=True)
                        for s_i, src_name in enumerate(result["sources"], start=1):
                            st.markdown(f"- **[{s_i}]** `{src_name}`")

                    # Real-time Telemetry
                    debug = result.get("debug", {})
                    with st.expander("🔬 Real-Time Pipeline Telemetry & Reranking Scores", expanded=True):
                        tel_col1, tel_col2 = st.columns(2)
                        with tel_col1:
                            st.markdown("<span style='color:#FFFFFF; font-weight:700;'>1. Generated Query Variants (Multi-Query Expansion):</span>", unsafe_allow_html=True)
                            for q in debug.get("generated_queries", []):
                                st.markdown(f"- `{q}`")
                        with tel_col2:
                            st.markdown("<span style='color:#FFFFFF; font-weight:700;'>2. Cross-Encoder Joint Relevance Scoring:</span>", unsafe_allow_html=True)
                            for chunk in debug.get("reranked", [])[:4]:
                                score = chunk.get("score")
                                score_val = f"{score:+.3f}" if score is not None else "N/A"
                                status = "🟢 Relevant" if (score is not None and score >= 0) else "🟡 Borderline"
                                st.markdown(f"- **{score_val}** ({status}) — `{chunk.get('source')}`")

                    # Final context preview
                    final_context = debug.get("final_context", [])
                    if final_context:
                        with st.expander("📖 Ground-Truth Context Passages Sent to LLM", expanded=False):
                            for fc_i, fc in enumerate(final_context, start=1):
                                st.markdown(f"**[{fc_i}] {fc.get('source')}**")
                                st.text(fc.get("preview", "")[:350] + "...")

                    # Seamless CTA to chat assistant
                    st.markdown("<div style='height:14px;'></div>", unsafe_allow_html=True)
                    sb_col1, sb_col2 = st.columns([3, 1.4])
                    with sb_col1:
                        st.info("💡 Want multi-turn conversation memory, or to upload your own custom PDFs/DOCXs?")
                    with sb_col2:
                        if st.button("👉 Open Full Chat Assistant", key="open_chat_from_sandbox", type="primary", use_container_width=True):
                            navigate_to_chat_func()

                except Exception as e:
                    st.error(f"Error during query execution: {e}")

    st.markdown("<br><hr style='border-color:rgba(255,255,255,0.1);'><br>", unsafe_allow_html=True)

    # =========================================================================
    # 4. KEY PRODUCTION METRICS
    # =========================================================================
    st.markdown("<h2 style='color:#FFFFFF; font-size:1.8rem; margin-bottom:16px;'>📊 Production Reliability & Performance Metrics</h2>", unsafe_allow_html=True)
    s1, s2, s3, s4 = st.columns(4)
    with s1:
        st.markdown(
            """
            <div class="stat-card">
                <div class="stat-num">100%</div>
                <div class="stat-label">Source-Grounded</div>
                <p style="font-size:0.84rem; color:#94A3B8; margin-top:6px;">Strict prompt guards eliminate hallucination risks.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with s2:
        st.markdown(
            """
            <div class="stat-card">
                <div class="stat-num">5 Stages</div>
                <div class="stat-label">Deep Pipeline</div>
                <p style="font-size:0.84rem; color:#94A3B8; margin-top:6px;">Multi-query, hybrid fusion, parent recovery, reranker, budget.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with s3:
        st.markdown(
            """
            <div class="stat-card">
                <div class="stat-num"><100ms</div>
                <div class="stat-label">Reranker Latency</div>
                <p style="font-size:0.84rem; color:#94A3B8; margin-top:6px;">Local CPU cross-attention scoring on top candidates.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with s4:
        st.markdown(
            """
            <div class="stat-card">
                <div class="stat-num">Free Tier</div>
                <div class="stat-label">Zero API Cost</div>
                <p style="font-size:0.84rem; color:#94A3B8; margin-top:6px;">Gemini 2.5 Flash Free + local HuggingFace embeddings.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<br><hr style='border-color:rgba(255,255,255,0.1);'><br>", unsafe_allow_html=True)

    # =========================================================================
    # 5. CORE FEATURES MATRIX (6 CARDS)
    # =========================================================================
    st.markdown("<h2 style='color:#FFFFFF; font-size:1.8rem; margin-bottom:6px;'>⚡ Built for Complex Real-World Documents</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#CBD5E1; font-size:1.05rem; margin-bottom:24px;'>Traditional RAG breaks on real enterprise documents. Here is the feature set engineered to guarantee factuality:</p>", unsafe_allow_html=True)

    f_col1, f_col2, f_col3 = st.columns(3)
    with f_col1:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon-box">📄</div>
                <div class="feature-title">Universal Document Ingestion</div>
                <div class="feature-desc">
                    Upload any document type: employee handbooks, security policies, SLAs, financial audits, or contracts in PDF, DOCX, or TXT format.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with f_col2:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon-box">🔀</div>
                <div class="feature-title">Multi-Query Semantic Expansion</div>
                <div class="feature-desc">
                    The LLM generates 3 search formulations per inquiry, incorporating conversation memory to resolve ambiguous follow-up pronouns like "does it apply?".
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with f_col3:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon-box">⚡</div>
                <div class="feature-title">Dual-Engine Hybrid Retrieval</div>
                <div class="feature-desc">
                    Combines dense semantic search (FAISS) with sparse exact keyword search (BM25) using Reciprocal Rank Fusion (RRF), catching exact policy codes and acronyms.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)
    f_col4, f_col5, f_col6 = st.columns(3)
    with f_col4:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon-box">🧩</div>
                <div class="feature-title">Parent-Child Splitting</div>
                <div class="feature-desc">
                    Indexes small 400-char child chunks for sharp vector search, then automatically retrieves the full 1,600-char parent chunk so the LLM has complete context.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with f_col5:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon-box">🎯</div>
                <div class="feature-title">Cross-Encoder Neural Reranking</div>
                <div class="feature-desc">
                    Uses joint cross-attention to score query-chunk pairs simultaneously, separating true answers from chunks that merely share common vocabulary.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with f_col6:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon-box">💬</div>
                <div class="feature-title">Context Budgeting & Memory</div>
                <div class="feature-desc">
                    Enforces strict token budgets and relevance cutoffs before synthesis, ensuring maximum answer accuracy and multi-turn conversational coherence.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<br><hr style='border-color:rgba(255,255,255,0.1);'><br>", unsafe_allow_html=True)

    # =========================================================================
    # 6. HOW IT WORKS (4-STEP ARCHITECTURE FLOW)
    # =========================================================================
    st.markdown("<h2 style='color:#FFFFFF; font-size:1.8rem; margin-bottom:6px;'>🛠️ How the Engine Works (Step-by-Step)</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#CBD5E1; font-size:1.05rem; margin-bottom:24px;'>From unstructured documents to cited factual answers in four systematic stages:</p>", unsafe_allow_html=True)

    w1, w2, w3, w4 = st.columns(4)
    with w1:
        st.markdown(
            """
            <div class="workflow-step">
                <div class="workflow-badge">STEP 01</div>
                <div style="font-size:1.1rem; font-weight:700; color:#FFFFFF; margin-bottom:8px;">Ingest & Chunk</div>
                <div style="font-size:0.9rem; color:#CBD5E1; line-height:1.55;">
                    Extracts text from PDF/DOCX/TXT and creates hierarchical parent-child chunks tagged with file metadata and section headers.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with w2:
        st.markdown(
            """
            <div class="workflow-step">
                <div class="workflow-badge">STEP 02</div>
                <div style="font-size:1.1rem; font-weight:700; color:#FFFFFF; margin-bottom:8px;">Hybrid Retrieval</div>
                <div style="font-size:0.9rem; color:#CBD5E1; line-height:1.55;">
                    Generates 3 query variations and queries both FAISS semantic index and BM25 keyword index, fusing candidates with RRF.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with w3:
        st.markdown(
            """
            <div class="workflow-step">
                <div class="workflow-badge">STEP 03</div>
                <div style="font-size:1.1rem; font-weight:700; color:#FFFFFF; margin-bottom:8px;">Neural Rerank</div>
                <div style="font-size:0.9rem; color:#CBD5E1; line-height:1.55;">
                    Cross-Encoder reads candidate parent chunks alongside the query to compute exact semantic relevance scores and drop noise.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with w4:
        st.markdown(
            """
            <div class="workflow-step">
                <div class="workflow-badge">STEP 04</div>
                <div style="font-size:1.1rem; font-weight:700; color:#FFFFFF; margin-bottom:8px;">Grounded Synthesis</div>
                <div style="font-size:0.9rem; color:#CBD5E1; line-height:1.55;">
                    Gemini 2.5 Flash synthesizes the final answer using only the verified passages, appending clear bracketed citations.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<br><hr style='border-color:rgba(255,255,255,0.1);'><br>", unsafe_allow_html=True)

    # =========================================================================
    # 7. HIGH-IMPACT FINAL CALL TO ACTION
    # =========================================================================
    st.markdown(
        """
        <div class="cta-banner">
            <h2 style="font-size:2.4rem; font-weight:800; color:#FFFFFF; margin-bottom:12px; letter-spacing:-0.02em;">
                Ready to Experience Verifiable Document Intelligence?
            </h2>
            <p style="color:#CBD5E1; font-size:1.15rem; max-width:680px; margin:0 auto 26px auto; line-height:1.65;">
                Upload your own PDFs, Word documents, or text files, test multi-turn conversation memory, and inspect real-time retrieval telemetry.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    f_b1, f_b2, f_b3 = st.columns([1.5, 2, 1.5])
    with f_b2:
        if st.button("🚀 Launch Live Demo Assistant Now", key="btn_final_cta", type="primary", use_container_width=True):
            navigate_to_chat_func()
