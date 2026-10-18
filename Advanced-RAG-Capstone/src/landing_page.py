"""
Ultra-Premium Modern AI SaaS Landing Page for Advanced RAG Assistant.

Built with a modern AI/SaaS startup aesthetic:
- Modern typography (Plus Jakarta Sans & JetBrains Mono)
- Fluid glassmorphism & subtle ambient glow gradients
- Animated hero headline and interactive application preview mockup
- 6-card feature matrix with hover elevations
- 4-step progressive "How It Works" workflow
- Live 1-click interactive demo sandbox with real-time telemetry
- Universal document upload messaging (PDF, DOCX, TXT)
"""

import streamlit as st
from src.indexing import index_summary



# General enterprise sample scenarios that demonstrate diverse document capabilities
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
    # Custom CSS Design System (AI/SaaS Startup Aesthetic)
    # -------------------------------------------------------------------------
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

        /* Global typography & smooth rendering */
        html, body, [class*="css"] {
            font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
            -webkit-font-smoothing: antialiased;
        }

        /* Ambient Glow Animations */
        @keyframes floatEffect {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-8px); }
            100% { transform: translateY(0px); }
        }

        @keyframes pulseGlow {
            0% { opacity: 0.4; }
            50% { opacity: 0.8; }
            100% { opacity: 0.4; }
        }

        /* Glassmorphic Sticky Navbar */
        .saas-navbar {
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: rgba(15, 23, 42, 0.75);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 16px;
            padding: 14px 24px;
            margin-bottom: 28px;
            box-shadow: 0 4px 20px -4px rgba(0, 0, 0, 0.3);
        }

        .nav-logo {
            display: flex;
            align-items: center;
            gap: 10px;
            font-size: 1.25rem;
            font-weight: 800;
            color: #FFFFFF;
            letter-spacing: -0.02em;
        }

        .nav-logo-icon {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 34px;
            height: 34px;
            border-radius: 10px;
            background: linear-gradient(135deg, #6366F1, #8B5CF6);
            color: #FFFFFF;
            font-size: 1.1rem;
            box-shadow: 0 0 15px rgba(99, 102, 241, 0.5);
        }

        .nav-links {
            display: flex;
            align-items: center;
            gap: 22px;
            font-size: 0.88rem;
            font-weight: 500;
            color: #94A3B8;
        }

        /* Hero Section Container */
        .saas-hero {
            position: relative;
            background: radial-gradient(circle at 10% 20%, rgba(99, 102, 241, 0.22) 0%, transparent 45%),
                        radial-gradient(circle at 90% 25%, rgba(6, 182, 212, 0.18) 0%, transparent 45%),
                        linear-gradient(135deg, rgba(15, 23, 42, 0.95) 0%, rgba(30, 41, 59, 0.85) 100%);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 24px;
            padding: 56px 42px;
            margin-bottom: 40px;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.6), inset 0 1px 0 rgba(255, 255, 255, 0.12);
            overflow: hidden;
        }

        .hero-badge {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(99, 102, 241, 0.12);
            border: 1px solid rgba(99, 102, 241, 0.35);
            padding: 6px 16px;
            border-radius: 9999px;
            font-size: 0.84rem;
            font-weight: 700;
            color: #A5B4FC;
            margin-bottom: 22px;
            letter-spacing: 0.02em;
        }

        .hero-heading {
            font-size: 3.2rem;
            font-weight: 800;
            line-height: 1.12;
            letter-spacing: -0.03em;
            background: linear-gradient(105deg, #FFFFFF 25%, #93C5FD 55%, #C084FC 85%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 20px;
        }

        .hero-lead {
            font-size: 1.22rem;
            color: #CBD5E1;
            line-height: 1.7;
            max-width: 860px;
            margin-bottom: 32px;
            font-weight: 400;
        }

        /* Mockup Container */
        .mockup-window {
            background: rgba(15, 23, 42, 0.92);
            border: 1px solid rgba(255, 255, 255, 0.12);
            border-radius: 18px;
            box-shadow: 0 25px 60px -15px rgba(0, 0, 0, 0.7);
            overflow: hidden;
            margin-top: 28px;
            transition: transform 0.3s ease;
        }

        .mockup-topbar {
            display: flex;
            align-items: center;
            padding: 12px 18px;
            background: rgba(30, 41, 59, 0.6);
            border-bottom: 1px solid rgba(255, 255, 255, 0.06);
            gap: 8px;
        }

        .dot { width: 11px; height: 11px; border-radius: 50%; }
        .dot-red { background: #EF4444; }
        .dot-yellow { background: #F59E0B; }
        .dot-green { background: #10B981; }

        .mockup-url {
            margin-left: 12px;
            background: rgba(15, 23, 42, 0.6);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 8px;
            padding: 3px 14px;
            font-size: 0.75rem;
            color: #94A3B8;
            font-family: 'JetBrains Mono', monospace;
            width: 280px;
        }

        .mockup-body {
            padding: 24px;
            background: linear-gradient(180deg, rgba(15, 23, 42, 0.8) 0%, rgba(30, 41, 59, 0.5) 100%);
        }

        /* Stats Strip */
        .stat-card {
            background: rgba(30, 41, 59, 0.4);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 16px;
            padding: 22px;
            text-align: center;
            height: 100%;
            transition: all 0.25s ease;
        }
        .stat-card:hover {
            border-color: rgba(99, 102, 241, 0.4);
            transform: translateY(-3px);
            background: rgba(30, 41, 59, 0.6);
        }
        .stat-num {
            font-size: 2.2rem;
            font-weight: 800;
            background: linear-gradient(135deg, #60A5FA, #A78BFA);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 4px;
            letter-spacing: -0.02em;
        }
        .stat-label {
            font-size: 0.82rem;
            font-weight: 700;
            color: #94A3B8;
            text-transform: uppercase;
            letter-spacing: 0.06em;
        }

        /* Feature Cards */
        .feature-card {
            background: rgba(30, 41, 59, 0.4);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 18px;
            padding: 26px;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
            transition: all 0.28s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
        }
        .feature-card:hover {
            border-color: rgba(99, 102, 241, 0.45);
            transform: translateY(-4px);
            background: rgba(30, 41, 59, 0.65);
            box-shadow: 0 16px 32px -10px rgba(99, 102, 241, 0.15);
        }
        .feature-icon-box {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 48px;
            height: 48px;
            border-radius: 12px;
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.2), rgba(139, 92, 246, 0.2));
            border: 1px solid rgba(99, 102, 241, 0.3);
            font-size: 1.4rem;
            margin-bottom: 16px;
        }
        .feature-title {
            font-size: 1.2rem;
            font-weight: 700;
            color: #F8FAFC;
            margin-bottom: 10px;
        }
        .feature-desc {
            font-size: 0.92rem;
            color: #94A3B8;
            line-height: 1.65;
        }

        /* Workflow Steps */
        .workflow-step {
            background: rgba(15, 23, 42, 0.55);
            border: 1px solid rgba(255, 255, 255, 0.07);
            border-radius: 16px;
            padding: 22px;
            position: relative;
            height: 100%;
            transition: all 0.25s ease;
        }
        .workflow-step:hover {
            border-color: rgba(6, 182, 212, 0.4);
            transform: translateY(-2px);
        }
        .workflow-badge {
            display: inline-block;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.78rem;
            font-weight: 800;
            color: #38BDF8;
            background: rgba(6, 182, 212, 0.12);
            padding: 4px 10px;
            border-radius: 6px;
            margin-bottom: 12px;
            border: 1px solid rgba(6, 182, 212, 0.25);
        }

        /* Live Sandbox Container */
        .sandbox-container {
            background: radial-gradient(circle at 50% 0%, rgba(99, 102, 241, 0.15) 0%, transparent 60%),
                        rgba(15, 23, 42, 0.75);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 32px;
            margin-top: 24px;
            margin-bottom: 36px;
        }

        .scenario-card {
            background: rgba(30, 41, 59, 0.5);
            border: 1px solid rgba(255, 255, 255, 0.08);
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
            color: #F8FAFC;
            margin-bottom: 4px;
        }
        .scenario-tag {
            font-size: 0.75rem;
            font-weight: 600;
            color: #818CF8;
            margin-bottom: 6px;
        }
        .scenario-desc {
            font-size: 0.82rem;
            color: #94A3B8;
            line-height: 1.45;
            margin-bottom: 12px;
        }

        /* Final High-Impact CTA */
        .cta-banner {
            background: radial-gradient(circle at 50% 50%, rgba(99, 102, 241, 0.3) 0%, transparent 70%),
                        linear-gradient(135deg, rgba(15, 23, 42, 0.95) 0%, rgba(30, 41, 59, 0.9) 100%);
            border: 1px solid rgba(99, 102, 241, 0.35);
            border-radius: 24px;
            padding: 48px 36px;
            text-align: center;
            box-shadow: 0 20px 40px -15px rgba(99, 102, 241, 0.25);
            margin-top: 40px;
            margin-bottom: 30px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # =========================================================================
    # 1. NAVBAR
    # =========================================================================
    st.markdown(
        """
        <div class="saas-navbar">
            <div class="nav-logo">
                <div class="nav-logo-icon">⚡</div>
                <span>OmniRAG Intelligence</span>
            </div>
            <div class="nav-links">
                <span>Features</span>
                <span>•</span>
                <span>How It Works</span>
                <span>•</span>
                <span>Architecture</span>
                <span>•</span>
                <span>Any Document Ready</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # =========================================================================
    # 2. HERO SECTION
    # =========================================================================
    st.markdown(
        """
        <div class="saas-hero">
            <div class="hero-badge">
                <span>✨</span> Enterprise Document Intelligence • Zero Hallucination Guarantee
            </div>
            <div class="hero-heading">
                Transform Any Document Into<br>Verifiable, Cited Intelligence
            </div>
            <div class="hero-lead">
                Upload any corporate PDF, Word manual, technical specification, or compliance policy. 
                Our 5-stage hybrid retrieval engine combines <b>Multi-Query Expansion</b>, <b>BM25 + FAISS Hybrid Fusion</b>, 
                and <b>Local Cross-Encoder Reranking</b> to synthesize accurate, cited answers you can stake your business on.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Hero Action Buttons
    col_btn1, col_btn2, col_btn3 = st.columns([1.6, 1.4, 2])
    with col_btn1:
        if st.button("🚀 Launch Interactive Assistant", type="primary", use_container_width=True):
            navigate_to_chat_func()
    with col_btn2:
        st.markdown(
            """
            <a href="https://github.com/esakhan786/advanced-rag-assistant-" target="_blank" style="text-decoration:none;">
                <button style="width:100%; height:38px; border-radius:8px; border:1px solid rgba(255,255,255,0.18); background:rgba(30,41,59,0.85); color:#F8FAFC; font-weight:600; cursor:pointer;">
                    ⭐ Star on GitHub
                </button>
            </a>
            """,
            unsafe_allow_html=True,
        )

    # Realistic Interactive Application Mockup
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
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px; border-bottom:1px solid rgba(255,255,255,0.06); padding-bottom:10px;">
                    <div style="font-weight:700; color:#F8FAFC; font-size:0.95rem;">
                        📁 Universal Ingestion Engine: <span style="color:#34D399;">PDF, DOCX, TXT</span>
                    </div>
                    <div style="font-family:'JetBrains Mono', monospace; font-size:0.75rem; color:#818CF8; background:rgba(99,102,241,0.15); padding:3px 10px; border-radius:6px;">
                        Hybrid Search + Cross-Encoder Active
                    </div>
                </div>
                <div style="background:rgba(15,23,42,0.6); border:1px solid rgba(255,255,255,0.06); border-radius:10px; padding:16px; margin-bottom:12px;">
                    <div style="font-size:0.8rem; color:#94A3B8; margin-bottom:4px; font-weight:600;">USER INQUIRY</div>
                    <div style="color:#F1F5F9; font-weight:500;">"What is the policy regarding refund eligibility and service credit requests?"</div>
                </div>
                <div style="background:rgba(99,102,241,0.08); border-left:3px solid #6366F1; border-radius:0 10px 10px 0; padding:16px;">
                    <div style="font-size:0.8rem; color:#A5B4FC; margin-bottom:6px; font-weight:700;">VERIFIED SYNTHESIS (GROUNDED IN DOCUMENT SOURCES)</div>
                    <div style="color:#E2E8F0; font-size:0.92rem; line-height:1.6;">
                        Customers on monthly self-service plans may request a full refund within 30 days of invoice date <b>[1]</b>. Usage-based infrastructure fees are non-refundable. Service credits of up to 25% are granted if monthly uptime falls below 99.0% <b>[2]</b>.
                    </div>
                    <div style="display:flex; gap:10px; margin-top:12px;">
                        <span style="font-size:0.75rem; background:rgba(255,255,255,0.08); padding:3px 8px; border-radius:4px; color:#CBD5E1;">[1] Support Policy • Section 5</span>
                        <span style="font-size:0.75rem; background:rgba(255,255,255,0.08); padding:3px 8px; border-radius:4px; color:#CBD5E1;">[2] SLA & Credit Terms • Section 8</span>
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<br><hr>", unsafe_allow_html=True)

    # =========================================================================
    # 3. STATS / TRUST SECTION
    # =========================================================================
    st.markdown("### 📊 Production Reliability & Performance Metrics")
    s1, s2, s3, s4 = st.columns(4)
    with s1:
        st.markdown(
            """
            <div class="stat-card">
                <div class="stat-num">100%</div>
                <div class="stat-label">Source-Grounded</div>
                <p style="font-size:0.8rem; color:#94A3B8; margin-top:4px;">Strict policy prompts forbid ungrounded speculation.</p>
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
                <p style="font-size:0.8rem; color:#94A3B8; margin-top:4px;">Multi-query, hybrid RRF, parent recovery, reranker, budget.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with s3:
        st.markdown(
            """
            <div class="stat-card">
                <div class="stat-num">~0.08s</div>
                <div class="stat-label">Reranker Latency</div>
                <p style="font-size:0.8rem; color:#94A3B8; margin-top:4px;">Local CPU cross-attention scoring on candidates.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with s4:
        st.markdown(
            """
            <div class="stat-card">
                <div class="stat-num">Free Tier</div>
                <div class="stat-label">Operational Cost</div>
                <p style="font-size:0.8rem; color:#94A3B8; margin-top:4px;">Gemini 2.5 Flash Free + local CPU embeddings.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<br><hr>", unsafe_allow_html=True)

    # =========================================================================
    # 4. FEATURES GRID (6 CARDS)
    # =========================================================================
    st.markdown("## ⚡ Built for Real-World Documents")
    st.markdown(
        "Standard tutorials use toy vector search that breaks on real business documents. "
        "Here is the feature set that makes this system enterprise-ready:"
    )

    f_col1, f_col2, f_col3 = st.columns(3)
    with f_col1:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon-box">📄</div>
                <div class="feature-title">Universal Document Ingestion</div>
                <div class="feature-desc">
                    Drop in any document: company handbooks, compliance manuals, financial audit reports, legal contracts, or technical papers in PDF, DOCX, or TXT format.
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
                <div class="feature-title">Cross-Encoder Attention Reranking</div>
                <div class="feature-desc">
                    Processes query and passage jointly via cross-attention layers (ms-marco-MiniLM on CPU), scoring whether the text actually answers the prompt.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with f_col6:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon-box">🛡️</div>
                <div class="feature-title">Context Budgeting & Citations</div>
                <div class="feature-desc">
                    Drops negative-score noise, trims context to an 8,000-character budget, and enforces strict verifiable numeric citations ([1], [2]) for auditing.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<br><hr>", unsafe_allow_html=True)

    # =========================================================================
    # 5. HOW IT WORKS (4-STEP WORKFLOW)
    # =========================================================================
    st.markdown("## 🔄 How It Works: The 4-Step Pipeline")
    st.markdown("From raw unstructured documents to verifiable, cited intelligence:")

    w1, w2, w3, w4 = st.columns(4)
    with w1:
        st.markdown(
            """
            <div class="workflow-step">
                <div class="workflow-badge">STEP 01</div>
                <div style="font-weight:700; color:#F8FAFC; margin-bottom:8px; font-size:1.05rem;">Upload & Ingest</div>
                <div style="font-size:0.85rem; color:#94A3B8; line-height:1.6;">
                    Upload any PDF, Word (.docx), or plain text file. Text splitters parse structure and preserve section headers.
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
                <div style="font-weight:700; color:#F8FAFC; margin-bottom:8px; font-size:1.05rem;">Hierarchical Indexing</div>
                <div style="font-size:0.85rem; color:#94A3B8; line-height:1.6;">
                    Large parent blocks store complete context, while small child chunks are embedded into local FAISS vector space.
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
                <div style="font-weight:700; color:#F8FAFC; margin-bottom:8px; font-size:1.05rem;">Hybrid RRF & Rerank</div>
                <div style="font-size:0.85rem; color:#94A3B8; line-height:1.6;">
                    Multi-queries search dense FAISS and sparse BM25 simultaneously. A Cross-Encoder model joint-ranks the top passages.
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
                <div style="font-weight:700; color:#F8FAFC; margin-bottom:8px; font-size:1.05rem;">Cited Generation</div>
                <div style="font-size:0.85rem; color:#94A3B8; line-height:1.6;">
                    Google Gemini 2.5 Flash synthesizes answers strictly using refined context, citing numbered sources for instant verification.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<br><hr>", unsafe_allow_html=True)

    # =========================================================================
    # 6. INTERACTIVE 1-CLICK LIVE DEMO SANDBOX
    # =========================================================================
    st.markdown("## ⚡ Live Interactive Demo Sandbox")
    st.markdown(
        "Test the live pipeline right here. Click a sample business inquiry or test with your own question:"
    )

    demo_cols = st.columns(4)
    selected_query = None

    for idx, sc in enumerate(SAMPLE_RECRUITER_QUERIES):
        with demo_cols[idx]:
            st.markdown(
                f"""
                <div class="scenario-card">
                    <div>
                        <div class="scenario-title">{sc['icon']} {sc['title']}</div>
                        <div class="scenario-tag">{sc['tag']}</div>
                        <div class="scenario-desc">{sc['description']}</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            if st.button(f"Test Query #{idx + 1}", key=f"saas_demo_btn_{idx}", use_container_width=True):
                selected_query = sc["question"]

    st.markdown("<br>", unsafe_allow_html=True)
    custom_inquiry = st.text_input(
        "Or enter any question to search against your knowledge base:",
        placeholder="e.g. What are the support hours and escalation paths?",
        key="saas_custom_input_box"
    )
    if st.button("🚀 Run Live Pipeline", key="saas_run_custom_btn"):
        if custom_inquiry.strip():
            selected_query = custom_inquiry.strip()

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
                        <div style="background: linear-gradient(135deg, rgba(15, 23, 42, 0.95) 0%, rgba(30, 41, 59, 0.85) 100%); border: 1px solid rgba(99, 102, 241, 0.35); border-radius: 14px; padding: 22px; margin-top: 14px; box-shadow: 0 10px 30px rgba(0,0,0,0.4);">
                            <div style="font-size:0.82rem; color:#10B981; font-weight:700; letter-spacing:0.04em; margin-bottom:8px;">
                                🟢 FACTUAL ANSWER (SYNTHESIZED WITH STRICT CITATIONS)
                            </div>
                            <div style="font-size:1.02rem; color:#F8FAFC; line-height:1.7;">
                                {result['answer']}
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

                    # Render ground-truth sources
                    if result.get("sources"):
                        st.markdown("##### 📄 Verified Ground-Truth Sources")
                        for s_i, src_name in enumerate(result["sources"], start=1):
                            st.markdown(f"- **[{s_i}]** `{src_name}`")

                    # Real-time Telemetry
                    debug = result.get("debug", {})
                    with st.expander("🔬 Real-Time Pipeline Telemetry & Reranking Scores", expanded=True):
                        tel_col1, tel_col2 = st.columns(2)
                        with tel_col1:
                            st.markdown("**1. Generated Query Variants (Multi-Query Expansion):**")
                            for q in debug.get("generated_queries", []):
                                st.markdown(f"- `{q}`")
                        with tel_col2:
                            st.markdown("**2. Cross-Encoder Joint Relevance Scoring:**")
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

                    # CTA box
                    box1, box2 = st.columns([3, 1.2])
                    with box1:
                        st.info("💡 Want multi-turn chat history, or to upload your own files via browser?")
                    with box2:
                        if st.button("👉 Open Full Chat Assistant", key="open_chat_from_sandbox", type="primary", use_container_width=True):
                            navigate_to_chat_func()

                except Exception as e:
                    st.error(f"Error during query execution: {e}")

    st.markdown("<br><hr>", unsafe_allow_html=True)

    # =========================================================================
    # 7. HIGH-IMPACT FINAL CALL TO ACTION & FOOTER
    # =========================================================================
    st.markdown(
        """
        <div class="cta-banner">
            <h2 style="font-size:2.4rem; font-weight:800; color:#FFFFFF; margin-bottom:12px; letter-spacing:-0.02em;">
                Ready to Experience Verifiable Document Intelligence?
            </h2>
            <p style="color:#CBD5E1; font-size:1.1rem; max-width:650px; margin:0 auto 26px auto; line-height:1.6;">
                Upload your own PDFs, Word documents, or text files, test multi-turn conversation memory, and inspect real-time retrieval telemetry.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    f_b1, f_b2, f_b3 = st.columns([1.5, 2, 1.5])
    with f_b2:
        if st.button("🚀 Launch Full Chat Assistant Now", key="btn_final_cta", type="primary", use_container_width=True):
            navigate_to_chat_func()

    st.markdown(
        """
        <div style="text-align:center; padding:32px 0 10px 0; color:#64748B; font-size:0.85rem; border-top:1px solid rgba(255,255,255,0.06); margin-top:40px;">
            <b>OmniRAG Intelligence</b> • Built with Python, LangChain, Google Gemini, FAISS, and Streamlit • 100% Free Tier Compute Ready
        </div>
        """,
        unsafe_allow_html=True,
    )
