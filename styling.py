import streamlit as st


def apply_custom_theme():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@500;600;700&family=DM+Sans:wght@300;400;500;600&family=DM+Mono:wght@400;500&display=swap');

    /* ── TOKENS ─────────────────────────────────────────────────────────── */
    :root {
        --bg:           #080B09;
        --surface:      #0E1410;
        --surface-2:    #141C16;
        --border:       #1A2E1D;
        --border-hi:    #2A4A2E;

        --text:         #E8EDE9;
        --text-2:       #8A9E8D;
        --text-3:       #4D5E50;

        --green:        #00E5A0;
        --green-dim:    #00B87E;
        --green-glow:   rgba(0, 229, 160, 0.15);
        --green-glow-2: rgba(0, 229, 160, 0.06);

        --amber:        #F5A623;
        --amber-glow:   rgba(245, 166, 35, 0.15);

        --red:          #E8503A;
        --red-glow:     rgba(232, 80, 58, 0.15);

        --blue:         #4A9EE8;
        --blue-glow:    rgba(74, 158, 232, 0.15);

        --good:         #00E5A0;
        --warn:         #F5A623;
        --poor:         #E8503A;
        --info:         #4A9EE8;
    }

    /* ── KEYFRAME ANIMATIONS ─────────────────────────────────────────────── */
    @keyframes pulse-green {
        0%, 100% { box-shadow: 0 0 0 0 rgba(0, 229, 160, 0); }
        50%       { box-shadow: 0 0 18px 2px rgba(0, 229, 160, 0.18); }
    }

    @keyframes shimmer {
        0%   { background-position: -200% center; }
        100% { background-position: 200% center; }
    }

    @keyframes fadeSlideUp {
        from { opacity: 0; transform: translateY(8px); }
        to   { opacity: 1; transform: translateY(0); }
    }

    @keyframes borderPulse {
        0%, 100% { border-color: #1A2E1D; }
        50%       { border-color: #00E5A0; }
    }

    @keyframes glowLine {
        0%   { opacity: 0.4; width: 30%; }
        50%  { opacity: 1;   width: 100%; }
        100% { opacity: 0.4; width: 30%; }
    }

    /* ── BASE ────────────────────────────────────────────────────────────── */
    .stApp {
        background:
            radial-gradient(ellipse at 10% 0%, rgba(0,229,160,0.04) 0%, transparent 50%),
            radial-gradient(ellipse at 90% 100%, rgba(0,184,126,0.03) 0%, transparent 50%),
            #080B09 !important;
        color: var(--text);
        font-family: 'DM Sans', sans-serif;
        font-size: 0.9rem;
        animation: fadeSlideUp 0.4s ease both;
    }

    /* ── SIDEBAR ─────────────────────────────────────────────────────────── */
    [data-testid="stSidebar"] {
        background:
            linear-gradient(180deg, #060908 0%, #080B09 100%) !important;
        border-right: 1px solid var(--border) !important;
        box-shadow: 4px 0 24px rgba(0,0,0,0.4) !important;
    }

    [data-testid="stSidebar"] .stTitle,
    [data-testid="stSidebar"] h1 {
        font-family: 'Rajdhani', sans-serif !important;
        font-weight: 700 !important;
        font-size: 1.4rem !important;
        letter-spacing: 0.1em !important;
        background: linear-gradient(90deg, #00E5A0, #00B87E, #4AE8B0) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        background-clip: text !important;
        text-transform: uppercase;
        background-size: 200% auto;
        animation: shimmer 3s linear infinite;
    }

    /* ── HEADINGS ────────────────────────────────────────────────────────── */
    h1 {
        font-family: 'Rajdhani', sans-serif !important;
        font-weight: 700 !important;
        font-size: 2.2rem !important;
        letter-spacing: 0.05em !important;
        background: linear-gradient(135deg, #E8EDE9 0%, #00E5A0 60%, #00B87E 100%) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        background-clip: text !important;
        text-transform: uppercase;
        line-height: 1.1 !important;
    }

    h2 {
        font-family: 'DM Sans', sans-serif !important;
        font-weight: 500 !important;
        font-size: 0.68rem !important;
        text-transform: uppercase !important;
        letter-spacing: 0.16em !important;
        color: var(--text-3) !important;
        border: none !important;
        background: none !important;
        -webkit-text-fill-color: var(--text-3) !important;
        padding: 0 0 10px 0 !important;
        margin-top: 2.5rem !important;
        margin-bottom: 1rem !important;
        border-bottom: 1px solid var(--border) !important;
        position: relative;
    }

    h2::after {
        content: '';
        position: absolute;
        bottom: -1px; left: 0;
        height: 1px;
        background: linear-gradient(90deg, var(--green), transparent);
        animation: glowLine 3s ease-in-out infinite;
    }

    h3 {
        font-family: 'Rajdhani', sans-serif !important;
        font-weight: 600 !important;
        font-size: 1.15rem !important;
        letter-spacing: 0.04em !important;
        color: var(--text) !important;
        text-transform: uppercase;
    }

    /* ── METRIC CARDS — the main event ──────────────────────────────────── */
    [data-testid="stMetric"] {
        background:
            linear-gradient(135deg, #0E1410 0%, #111810 100%) !important;
        border: 1px solid var(--border) !important;
        border-radius: 10px !important;
        padding: 20px 22px 16px 22px !important;
        position: relative;
        overflow: hidden;
        transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow:
            0 1px 3px rgba(0,0,0,0.4),
            0 0 0 0 rgba(0,229,160,0) !important;
        animation: fadeSlideUp 0.5s ease both;
    }

    /* animated corner accent */
    [data-testid="stMetric"]::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 2px;
        background: linear-gradient(90deg,
            transparent 0%,
            var(--green) 40%,
            var(--green-dim) 60%,
            transparent 100%);
        opacity: 0;
        transition: opacity 0.3s ease;
    }

    /* subtle inner glow bottom */
    [data-testid="stMetric"]::after {
        content: '';
        position: absolute;
        bottom: 0; left: 0; right: 0;
        height: 40%;
        background: linear-gradient(to top, rgba(0,229,160,0.03), transparent);
        pointer-events: none;
    }

    [data-testid="stMetric"]:hover {
        border-color: rgba(0,229,160,0.4) !important;
        background:
            linear-gradient(135deg, #111810 0%, #141C14 100%) !important;
        transform: translateY(-2px) !important;
        box-shadow:
            0 8px 24px rgba(0,0,0,0.5),
            0 0 20px rgba(0,229,160,0.08),
            inset 0 1px 0 rgba(0,229,160,0.1) !important;
    }

    [data-testid="stMetric"]:hover::before {
        opacity: 1;
    }

    [data-testid="stMetricValue"] {
        font-family: 'Rajdhani', sans-serif !important;
        font-weight: 700 !important;
        background: linear-gradient(135deg, #E8EDE9 0%, #00E5A0 100%) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        background-clip: text !important;
        font-size: 2.1rem !important;
        font-variant-numeric: tabular-nums !important;
        line-height: 1.1 !important;
    }

    [data-testid="stMetricLabel"] {
        font-family: 'DM Sans', sans-serif !important;
        color: var(--text-3) !important;
        font-size: 0.64rem !important;
        text-transform: uppercase !important;
        letter-spacing: 0.12em !important;
        font-weight: 600 !important;
    }

    [data-testid="stMetricDelta"] {
        font-family: 'DM Mono', monospace !important;
        font-size: 0.76rem !important;
    }

    /* ── ALERTS ──────────────────────────────────────────────────────────── */
    [data-testid="stAlert"] {
        border-radius: 8px !important;
        border: 1px solid var(--border) !important;
        background: var(--surface) !important;
        font-size: 0.87rem !important;
        transition: all 0.2s ease !important;
        animation: fadeSlideUp 0.4s ease both;
    }

    [data-testid="stAlert"]:hover {
        transform: translateX(3px) !important;
    }

    div[data-baseweb="notification"][kind="positive"],
    .stSuccess {
        border-left: 3px solid var(--good) !important;
        background: linear-gradient(135deg, rgba(0,229,160,0.07) 0%, rgba(0,229,160,0.02) 100%) !important;
        box-shadow: inset 0 0 20px rgba(0,229,160,0.03) !important;
    }

    div[data-baseweb="notification"][kind="warning"],
    .stWarning {
        border-left: 3px solid var(--warn) !important;
        background: linear-gradient(135deg, rgba(245,166,35,0.07) 0%, rgba(245,166,35,0.02) 100%) !important;
        box-shadow: inset 0 0 20px rgba(245,166,35,0.03) !important;
    }

    div[data-baseweb="notification"][kind="negative"],
    .stError {
        border-left: 3px solid var(--poor) !important;
        background: linear-gradient(135deg, rgba(232,80,58,0.07) 0%, rgba(232,80,58,0.02) 100%) !important;
        box-shadow: inset 0 0 20px rgba(232,80,58,0.03) !important;
    }

    div[data-baseweb="notification"][kind="info"],
    .stInfo {
        border-left: 3px solid var(--info) !important;
        background: linear-gradient(135deg, rgba(74,158,232,0.07) 0%, rgba(74,158,232,0.02) 100%) !important;
        box-shadow: inset 0 0 20px rgba(74,158,232,0.03) !important;
    }

    .stSuccess > div, .stWarning > div,
    .stError > div,  .stInfo > div { color: var(--text) !important; }

    /* ── CHARTS ──────────────────────────────────────────────────────────── */
    [data-testid="stPlotlyChart"] {
        background: linear-gradient(135deg, #0E1410 0%, #111810 100%) !important;
        border: 1px solid var(--border) !important;
        border-radius: 10px !important;
        padding: 6px !important;
        box-shadow: 0 4px 20px rgba(0,0,0,0.3) !important;
        transition: box-shadow 0.25s ease !important;
    }

    [data-testid="stPlotlyChart"]:hover {
        box-shadow:
            0 8px 32px rgba(0,0,0,0.4),
            0 0 16px rgba(0,229,160,0.06) !important;
    }

    /* ── EXPANDER ────────────────────────────────────────────────────────── */
    [data-testid="stExpander"] {
        background: linear-gradient(135deg, #0E1410, #111810) !important;
        border: 1px solid var(--border) !important;
        border-radius: 8px !important;
        margin-bottom: 8px !important;
        transition: all 0.2s ease !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.3) !important;
    }

    [data-testid="stExpander"]:hover {
        border-color: rgba(0,229,160,0.3) !important;
        box-shadow: 0 4px 16px rgba(0,0,0,0.4), 0 0 12px rgba(0,229,160,0.05) !important;
    }

    details summary p {
        font-family: 'DM Sans', sans-serif !important;
        font-weight: 500 !important;
        font-size: 0.88rem !important;
        color: var(--text-2) !important;
        letter-spacing: 0.01em !important;
    }

    /* ── PROGRESS BAR ────────────────────────────────────────────────────── */
    .stProgress > div > div > div {
        background: linear-gradient(90deg,
            #00B87E 0%,
            #00E5A0 50%,
            #4AE8B0 100%) !important;
        border-radius: 4px !important;
        box-shadow: 0 0 8px rgba(0,229,160,0.4) !important;
        transition: width 0.6s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }

    .stProgress > div > div {
        background: rgba(26,46,29,0.6) !important;
        border-radius: 4px !important;
        height: 5px !important;
    }

    /* ── BUTTONS ─────────────────────────────────────────────────────────── */
    .stButton > button {
        background: transparent !important;
        color: var(--green) !important;
        border: 1px solid rgba(0,229,160,0.4) !important;
        border-radius: 6px !important;
        font-family: 'DM Sans', sans-serif !important;
        font-weight: 600 !important;
        font-size: 0.82rem !important;
        letter-spacing: 0.08em !important;
        text-transform: uppercase !important;
        padding: 0.45rem 1.2rem !important;
        transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
        position: relative;
        overflow: hidden;
    }

    .stButton > button::before {
        content: '';
        position: absolute;
        inset: 0;
        background: linear-gradient(135deg, rgba(0,229,160,0.1), transparent);
        opacity: 0;
        transition: opacity 0.2s ease;
    }

    .stButton > button:hover {
        border-color: var(--green) !important;
        box-shadow: 0 0 16px rgba(0,229,160,0.2), inset 0 0 16px rgba(0,229,160,0.05) !important;
        transform: translateY(-1px) !important;
        color: var(--green) !important;
    }

    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #00E5A0, #00B87E) !important;
        color: #080B09 !important;
        border-color: transparent !important;
        box-shadow: 0 4px 16px rgba(0,229,160,0.3) !important;
        font-weight: 700 !important;
    }

    .stButton > button[kind="primary"]:hover {
        background: linear-gradient(135deg, #00F0AA, #00C986) !important;
        box-shadow: 0 6px 24px rgba(0,229,160,0.4) !important;
        transform: translateY(-2px) !important;
    }

    /* ── NAV MENU — full redesign ────────────────────────────────────────── */

    /* kill the default option-menu container bg */
    ul.nav.nav-pills {
        background: transparent !important;
        padding: 4px 0 !important;
        gap: 2px !important;
        display: flex !important;
        flex-direction: column !important;
    }

    /* every nav item */
    .nav-link {
        font-family: 'DM Sans', sans-serif !important;
        font-weight: 500 !important;
        font-size: 0.8rem !important;
        color: #4D5E50 !important;
        border-radius: 6px !important;
        letter-spacing: 0.04em !important;
        text-transform: uppercase !important;
        padding: 10px 14px !important;
        margin: 1px 0 !important;
        border: 1px solid transparent !important;
        background: transparent !important;
        display: flex !important;
        align-items: center !important;
        gap: 10px !important;
        transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
        position: relative !important;
        overflow: hidden !important;
    }

    /* hover shimmer sweep */
    .nav-link::before {
        content: '' !important;
        position: absolute !important;
        inset: 0 !important;
        background: linear-gradient(90deg,
            transparent 0%,
            rgba(0,229,160,0.06) 50%,
            transparent 100%) !important;
        transform: translateX(-100%) !important;
        transition: transform 0.35s ease !important;
    }

    .nav-link:hover::before {
        transform: translateX(100%) !important;
    }

    .nav-link:hover {
        color: #E8EDE9 !important;
        background: rgba(0,229,160,0.05) !important;
        border-color: rgba(0,229,160,0.15) !important;
        transform: translateX(3px) !important;
        box-shadow: -2px 0 0 rgba(0,229,160,0.3) !important;
    }

    /* icon in nav */
    .nav-link i, .nav-link svg {
        opacity: 0.5 !important;
        transition: opacity 0.2s ease, color 0.2s ease !important;
        font-size: 0.9rem !important;
    }

    .nav-link:hover i, .nav-link:hover svg {
        opacity: 1 !important;
        color: #00E5A0 !important;
    }

    /* SELECTED state — the money shot */
    .nav-link-selected {
        background: linear-gradient(135deg,
            rgba(0,229,160,0.14) 0%,
            rgba(0,229,160,0.06) 100%) !important;
        color: #00E5A0 !important;
        border-color: rgba(0,229,160,0.25) !important;
        font-weight: 700 !important;
        box-shadow:
            -3px 0 0 #00E5A0,
            0 0 20px rgba(0,229,160,0.08),
            inset 0 1px 0 rgba(0,229,160,0.1) !important;
        transform: translateX(0) !important;
        letter-spacing: 0.06em !important;
    }

    .nav-link-selected::before {
        display: none !important;
    }

    .nav-link-selected i,
    .nav-link-selected svg,
    .nav-link .icon-selected {
        opacity: 1 !important;
        color: #00E5A0 !important;
        filter: drop-shadow(0 0 4px rgba(0,229,160,0.5)) !important;
    }

    /* remove the gross default selected pill background */
    .nav-pills .nav-link.active,
    .nav-pills .show > .nav-link {
        background: transparent !important;
        color: inherit !important;
    }

    /* ── DIVIDER ─────────────────────────────────────────────────────────── */
    hr {
        border: none !important;
        height: 1px !important;
        background: linear-gradient(90deg,
            transparent 0%,
            var(--border) 20%,
            rgba(0,229,160,0.2) 50%,
            var(--border) 80%,
            transparent 100%) !important;
        margin: 2rem 0 !important;
    }

    /* ── FILE UPLOADER ───────────────────────────────────────────────────── */
    [data-testid="stFileUploader"] {
        background: linear-gradient(135deg, rgba(0,229,160,0.03), transparent) !important;
        border: 1.5px dashed rgba(0,229,160,0.25) !important;
        border-radius: 10px !important;
        padding: 1rem !important;
        transition: all 0.25s ease !important;
    }

    [data-testid="stFileUploader"]:hover {
        border-color: rgba(0,229,160,0.6) !important;
        background: rgba(0,229,160,0.06) !important;
        box-shadow: 0 0 24px rgba(0,229,160,0.08) !important;
    }

    /* ── CAPTION ─────────────────────────────────────────────────────────── */
    .stCaption, small, caption {
        font-family: 'DM Sans', sans-serif !important;
        color: var(--text-3) !important;
        font-size: 0.74rem !important;
        letter-spacing: 0.01em !important;
    }

    /* ── TEXT AREA ───────────────────────────────────────────────────────── */
    .stTextArea textarea {
        background: var(--surface) !important;
        border: 1px solid var(--border) !important;
        border-radius: 6px !important;
        color: var(--text-2) !important;
        font-family: 'DM Mono', monospace !important;
        font-size: 0.8rem !important;
        transition: border-color 0.2s ease !important;
    }

    .stTextArea textarea:focus {
        border-color: rgba(0,229,160,0.4) !important;
        box-shadow: 0 0 12px rgba(0,229,160,0.08) !important;
    }

    /* ── SPINNER ─────────────────────────────────────────────────────────── */
    .stSpinner > div {
        border-top-color: var(--green) !important;
        box-shadow: 0 0 8px rgba(0,229,160,0.3) !important;
    }

    /* ── SCROLLBAR ───────────────────────────────────────────────────────── */
    ::-webkit-scrollbar { width: 4px; height: 4px; }
    ::-webkit-scrollbar-track { background: var(--bg); }
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(var(--green-dim), var(--border-hi));
        border-radius: 2px;
    }
    ::-webkit-scrollbar-thumb:hover { background: var(--green); }

    /* ── SELECTBOX / INPUTS ──────────────────────────────────────────────── */
    [data-testid="stSelectbox"] > div > div,
    [data-testid="stTextInput"] > div > div {
        background: var(--surface) !important;
        border: 1px solid var(--border) !important;
        border-radius: 6px !important;
        color: var(--text) !important;
        transition: border-color 0.2s ease !important;
    }

    [data-testid="stSelectbox"] > div > div:focus-within,
    [data-testid="stTextInput"] > div > div:focus-within {
        border-color: rgba(0,229,160,0.4) !important;
        box-shadow: 0 0 12px rgba(0,229,160,0.08) !important;
    }

    /* ── DATAFRAME ───────────────────────────────────────────────────────── */
    [data-testid="stDataFrame"] {
        border: 1px solid var(--border) !important;
        border-radius: 8px !important;
        overflow: hidden !important;
        box-shadow: 0 4px 16px rgba(0,0,0,0.3) !important;
    }

    /* ── CONTAINER GLOW on main sections ────────────────────────────────── */
    [data-testid="stVerticalBlock"] > [data-testid="stVerticalBlock"] {
        animation: fadeSlideUp 0.4s ease both;
    }

    </style>
    """, unsafe_allow_html=True)


# ── Helper utilities ──────────────────────────────────────────────────────────

def signal_color(score: float, good: float = 70, mid: float = 40) -> str:
    if score >= good:
        return "#00E5A0"
    elif score >= mid:
        return "#F5A623"
    return "#E8503A"


def render_hero_stat(score, label: str, sublabel: str = ""):
    color = signal_color(score)
    glow  = color.replace("#", "")
    r, g, b = int(glow[0:2],16), int(glow[2:4],16), int(glow[4:6],16)
    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, #0E1410 0%, #111C12 100%);
        border: 1px solid rgba({r},{g},{b},0.3);
        border-top: 3px solid {color};
        border-radius: 10px;
        padding: 30px 30px 24px 30px;
        position: relative;
        overflow: hidden;
        box-shadow: 0 8px 32px rgba(0,0,0,0.4), 0 0 40px rgba({r},{g},{b},0.08);
        transition: all 0.3s ease;
    ">
        <div style="
            position: absolute; top: 0; left: 0; right: 0; bottom: 0;
            background: radial-gradient(ellipse at top left, rgba({r},{g},{b},0.06) 0%, transparent 60%);
            pointer-events: none;
        "></div>
        <div style="
            font-family: 'DM Sans', sans-serif;
            font-size: 0.62rem;
            text-transform: uppercase;
            letter-spacing: 0.16em;
            color: #4D5E50;
            font-weight: 600;
            margin-bottom: 10px;
        ">{label}</div>
        <div style="
            font-family: 'Rajdhani', sans-serif;
            font-weight: 700;
            font-size: 4.5rem;
            color: {color};
            line-height: 1;
            font-variant-numeric: tabular-nums;
            letter-spacing: -0.02em;
            text-shadow: 0 0 30px rgba({r},{g},{b},0.4);
        ">{score}</div>
        <div style="
            font-family: 'DM Sans', sans-serif;
            font-size: 0.82rem;
            color: #8A9E8D;
            margin-top: 8px;
            font-weight: 300;
            letter-spacing: 0.02em;
        ">{sublabel}</div>
    </div>
    """, unsafe_allow_html=True)


def render_stat_pill(label: str, value: str, color: str = "#00E5A0"):
    h = color.lstrip("#")
    r, g, b = int(h[0:2],16), int(h[2:4],16), int(h[4:6],16)
    st.markdown(f"""
    <span style="
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba({r},{g},{b},0.08);
        border: 1px solid rgba({r},{g},{b},0.25);
        border-radius: 4px;
        padding: 4px 12px;
        font-family: 'DM Mono', monospace;
        font-size: 0.8rem;
        color: {color};
        margin: 3px;
        box-shadow: 0 0 8px rgba({r},{g},{b},0.1);
        transition: all 0.2s ease;
    ">
        <span style="
            color: #4D5E50;
            font-family: 'DM Sans', sans-serif;
            font-size: 0.68rem;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            font-weight: 600;
        ">{label}</span>
        {value}
    </span>
    """, unsafe_allow_html=True)


def patch_sidebar_banners():
    """Call this after apply_custom_theme() to fix sidebar status banners."""
    st.markdown("""
    <style>
    [data-testid="stSidebar"] [data-testid="stAlert"] {
        background: rgba(0,229,160,0.05) !important;
        border: 1px solid rgba(0,229,160,0.2) !important;
        border-left: 3px solid #00E5A0 !important;
        border-radius: 6px !important;
        font-size: 0.78rem !important;
        box-shadow: none !important;
    }
    [data-testid="stSidebar"] .stSuccess > div,
    [data-testid="stSidebar"] .stInfo > div {
        color: #8A9E8D !important;
        font-size: 0.78rem !important;
    }
    </style>
    """, unsafe_allow_html=True)
