import streamlit as st
from datetime import datetime
import plotly.graph_objects as go
import pandas as pd

# ─────────────────────────────────────────────
#  Page Config
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="LAN Chat Dashboard | CN Mini Project",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────
#  Custom CSS – Dark Glassmorphism Theme
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap');

html, body, [data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0a0e1a 0%, #0d1b2a 40%, #0f2033 100%) !important;
    font-family: 'Inter', sans-serif;
}
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0d1117 0%, #0f1e2e 100%) !important;
    border-right: 1px solid rgba(56,189,248,0.15);
}
#MainMenu, footer, header { visibility: hidden; }

.top-banner {
    background: linear-gradient(90deg, #0ea5e9 0%, #6366f1 50%, #8b5cf6 100%);
    padding: 2px; border-radius: 16px; margin-bottom: 1.5rem;
}
.top-banner-inner {
    background: #0a0e1a; border-radius: 14px; padding: 1.6rem 2rem;
    display: flex; align-items: center; gap: 1rem;
}
.banner-title {
    font-size: 2rem; font-weight: 800;
    background: linear-gradient(90deg, #38bdf8, #818cf8, #c084fc);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin: 0;
}
.banner-sub { color: #94a3b8; font-size: 0.9rem; margin: 0; }

.metric-card {
    background: rgba(255,255,255,0.04); border: 1px solid rgba(56,189,248,0.18);
    border-radius: 16px; padding: 1.4rem 1.6rem; backdrop-filter: blur(10px);
    transition: all 0.3s ease; text-align: center;
}
.metric-card:hover {
    border-color: rgba(56,189,248,0.5); background: rgba(56,189,248,0.07);
    transform: translateY(-3px); box-shadow: 0 8px 32px rgba(56,189,248,0.12);
}
.metric-icon { font-size: 2rem; margin-bottom: 0.4rem; }
.metric-value {
    font-size: 1.8rem; font-weight: 800;
    background: linear-gradient(90deg, #38bdf8, #818cf8);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent; line-height: 1;
}
.metric-label { color: #64748b; font-size: 0.78rem; font-weight:500; margin-top: 0.3rem;
    letter-spacing: 0.05em; text-transform: uppercase; }

.section-header {
    font-size: 1.1rem; font-weight: 700; color: #e2e8f0; margin-bottom: 1rem;
    display: flex; align-items: center; gap: 0.5rem;
}
.section-header::after {
    content: ''; flex: 1; height: 1px;
    background: linear-gradient(90deg, rgba(56,189,248,0.3), transparent);
}

.chat-wrap {
    background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.07);
    border-radius: 16px; padding: 1.2rem; max-height: 380px;
    overflow-y: auto; scroll-behavior: smooth;
}
.bubble-row { display:flex; margin-bottom: 0.8rem; align-items: flex-end; gap: 0.5rem; }
.bubble-row.srv { flex-direction: row-reverse; }
.avatar { width: 32px; height: 32px; border-radius: 50%; display:flex;
    align-items:center; justify-content:center; font-size: 1rem; flex-shrink: 0; }
.avatar.clt { background: linear-gradient(135deg,#0ea5e9,#6366f1); }
.avatar.srv { background: linear-gradient(135deg,#8b5cf6,#ec4899); }
.bubble { max-width: 72%; padding: 0.65rem 1rem; border-radius: 16px;
    font-size: 0.88rem; line-height: 1.5; font-family: 'Inter', sans-serif; }
.bubble.cb {
    background: linear-gradient(135deg, rgba(14,165,233,0.25), rgba(99,102,241,0.25));
    border: 1px solid rgba(14,165,233,0.3); color: #e2e8f0; border-bottom-left-radius: 4px;
}
.bubble.sb {
    background: linear-gradient(135deg, rgba(139,92,246,0.25), rgba(236,72,153,0.25));
    border: 1px solid rgba(139,92,246,0.3); color: #e2e8f0; border-bottom-right-radius: 4px;
}
.bubble-time { font-size: 0.7rem; color: #475569; margin-top: 0.2rem; }

.code-block {
    background: #0d1117; border: 1px solid rgba(56,189,248,0.2); border-radius: 12px;
    padding: 1rem 1.2rem; font-family: 'JetBrains Mono', monospace; font-size: 0.82rem;
    color: #7dd3fc; overflow-x: auto; line-height: 1.7;
}
.badge { display:inline-flex; align-items:center; gap:0.35rem;
    padding: 0.25rem 0.8rem; border-radius: 999px; font-size: 0.78rem; font-weight: 600; }
.bg  { background:rgba(34,197,94,0.15);  color:#4ade80; border:1px solid rgba(34,197,94,0.3); }
.bb  { background:rgba(56,189,248,0.15); color:#38bdf8; border:1px solid rgba(56,189,248,0.3); }
.bp  { background:rgba(139,92,246,0.15); color:#a78bfa; border:1px solid rgba(139,92,246,0.3); }
.br  { background:rgba(239,68,68,0.15);  color:#f87171; border:1px solid rgba(239,68,68,0.3); }

.info-panel {
    background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.07);
    border-radius: 14px; padding: 1.2rem 1.4rem; margin-bottom: 1rem;
}
.sidebar-logo { text-align:center; padding: 1rem 0 0.5rem; }
.sidebar-logo .li { font-size: 3rem; }
.sidebar-logo .lt {
    font-size: 1.1rem; font-weight: 700;
    background: linear-gradient(90deg, #38bdf8, #818cf8);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.ss { color:#475569; font-size:0.72rem; font-weight:600;
    text-transform:uppercase; letter-spacing:0.08em; margin:1.2rem 0 0.5rem; }
.pb { margin-bottom: 0.5rem; }
.pbl { display:flex; justify-content:space-between; color:#94a3b8; font-size:0.8rem; margin-bottom:0.2rem; }
.pbt { background:rgba(255,255,255,0.06); border-radius:99px; height:6px; overflow:hidden; }
.pbf { height:6px; border-radius:99px; }

.stTextInput > div > div > input {
    background: rgba(255,255,255,0.05) !important;
    border: 1px solid rgba(56,189,248,0.25) !important;
    border-radius: 10px !important; color: #e2e8f0 !important;
    font-family: 'Inter', sans-serif !important;
}
.stButton > button {
    background: linear-gradient(135deg, #0ea5e9, #6366f1) !important;
    border: none !important; border-radius: 10px !important; color: white !important;
    font-weight: 600 !important; font-family: 'Inter', sans-serif !important;
    transition: all 0.25s ease !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(14,165,233,0.35) !important;
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  Session State
# ─────────────────────────────────────────────
for key, val in [("chat_log", []), ("msg_count", 0), ("bytes_sent", 0),
                 ("server_running", False), ("connection_log", []),
                 ("active_sender", "Client")]:
    if key not in st.session_state:
        st.session_state[key] = val

# ─────────────────────────────────────────────
#  Sidebar
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div class="sidebar-logo">
        <div class="li">🌐</div>
        <div class="lt">CN Dashboard</div>
    </div>""", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown('<div class="ss">Network Config</div>', unsafe_allow_html=True)
    host = st.text_input("Server HOST", value="127.0.0.1", key="host_input")
    port = st.number_input("PORT", value=5000, min_value=1024, max_value=65535, step=1, key="port_input")
    protocol = st.selectbox("Protocol", ["TCP (SOCK_STREAM)", "UDP (SOCK_DGRAM)"], key="protocol_select")
    buf_size = st.selectbox("Buffer Size", ["512 bytes", "1024 bytes", "2048 bytes", "4096 bytes"], index=1)

    st.markdown("---")
    st.markdown('<div class="ss">Simulation Control</div>', unsafe_allow_html=True)
    active_sender = st.radio("Active Sender", ["Client → Server", "Server → Client"], key="sender_radio")
    st.session_state.active_sender = "Client" if "Client" in active_sender else "Server"

    st.markdown("---")
    st.markdown('<div class="ss">About</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style='color:#475569; font-size:0.78rem; line-height:1.8;'>
    📚 CN Mini Project<br>🔌 TCP Socket Programming<br>
    👨‍💻 Ram Chandra Nayak<br>🎓 MMMUT Gorakhpur
    </div>""", unsafe_allow_html=True)

    st.markdown("")
    if st.button("🔄  Reset Session", key="reset_btn"):
        st.session_state.chat_log = []
        st.session_state.msg_count = 0
        st.session_state.bytes_sent = 0
        st.session_state.connection_log = []
        st.session_state.server_running = False
        st.rerun()

# ─────────────────────────────────────────────
#  Top Banner
# ─────────────────────────────────────────────
st.markdown("""
<div class="top-banner">
  <div class="top-banner-inner">
    <span style="font-size:2.5rem;">🌐</span>
    <div>
      <p class="banner-title">LAN Chat Application Dashboard</p>
      <p class="banner-sub">Computer Networks Mini Project &nbsp;·&nbsp; Python TCP Socket Programming &nbsp;·&nbsp; Real-time Simulation</p>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  Metric Cards
# ─────────────────────────────────────────────
c1, c2, c3, c4 = st.columns(4)
proto_label = "TCP" if "TCP" in protocol else "UDP"

for col, icon, val, label in [
    (c1, "💬", st.session_state.msg_count, "Messages Sent"),
    (c2, "📦", st.session_state.bytes_sent, "Bytes Transferred"),
    (c3, "🔌", f"{host}:{int(port)}", "Endpoint"),
    (c4, "⚡", proto_label, "Active Protocol"),
]:
    with col:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-icon">{icon}</div>
            <div class="metric-value">{val}</div>
            <div class="metric-label">{label}</div>
        </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  Main Row: Chat | Architecture
# ─────────────────────────────────────────────
left_col, right_col = st.columns([3, 2], gap="large")

# ── Chat Simulator ──
with left_col:
    st.markdown('<div class="section-header">💬 Chat Simulator</div>', unsafe_allow_html=True)

    chat_html = '<div class="chat-wrap">'
    if not st.session_state.chat_log:
        chat_html += '<p style="color:#334155;text-align:center;margin-top:4rem;font-size:0.85rem;">No messages yet. Start chatting below! 👇</p>'
    else:
        for e in st.session_state.chat_log:
            if e["sender"] == "Client":
                chat_html += f"""
                <div class="bubble-row">
                  <div class="avatar clt">👤</div>
                  <div>
                    <div class="bubble cb">{e["msg"]}</div>
                    <div class="bubble-time">Client · {e["time"]}</div>
                  </div>
                </div>"""
            else:
                chat_html += f"""
                <div class="bubble-row srv">
                  <div class="avatar srv">🖥️</div>
                  <div style="text-align:right;">
                    <div class="bubble sb">{e["msg"]}</div>
                    <div class="bubble-time">Server · {e["time"]}</div>
                  </div>
                </div>"""
    chat_html += "</div>"
    st.markdown(chat_html, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    with st.form(key="chat_form", clear_on_submit=True):
        fc1, fc2 = st.columns([5, 1])
        with fc1:
            user_msg = st.text_input(
                "Message",
                placeholder=f"Type as {st.session_state.active_sender}… (type 'exit' to disconnect)",
                label_visibility="collapsed",
                key="msg_inp"
            )
        with fc2:
            sent = st.form_submit_button("Send 📤")

    if sent and user_msg.strip():
        ts = datetime.now().strftime("%H:%M:%S")
        st.session_state.chat_log.append({"sender": st.session_state.active_sender, "msg": user_msg.strip(), "time": ts})
        st.session_state.msg_count += 1
        st.session_state.bytes_sent += len(user_msg.strip().encode())
        st.session_state.server_running = True
        if len(st.session_state.connection_log) == 0:
            st.session_state.connection_log.append({"event": "Connection Established", "time": ts, "detail": f"{host}:{int(port)} · TCP Handshake ✅"})
        st.session_state.connection_log.append({"event": f"Packet Sent ({st.session_state.active_sender})", "time": ts, "detail": f"{len(user_msg.strip().encode())} bytes · seq={st.session_state.msg_count}"})
        if user_msg.strip().lower() == "exit":
            st.session_state.connection_log.append({"event": "Connection Closed", "time": ts, "detail": "FIN/ACK · Socket closed gracefully"})
            st.session_state.server_running = False
        st.rerun()

    # Quick Presets
    st.markdown('<div class="section-header" style="margin-top:1.2rem;">⚡ Quick Messages</div>', unsafe_allow_html=True)
    q1, q2, q3, q4 = st.columns(4)
    for col, (label, val) in zip([q1, q2, q3, q4],
                                  [("👋 Hello!", "Hello!"), ("🔥 How are you?", "How are you?"), ("✅ ACK", "ACK"), ("🚪 Exit", "exit")]):
        with col:
            if st.button(label, key=f"q_{val}"):
                ts = datetime.now().strftime("%H:%M:%S")
                st.session_state.chat_log.append({"sender": st.session_state.active_sender, "msg": val, "time": ts})
                st.session_state.msg_count += 1
                st.session_state.bytes_sent += len(val.encode())
                st.session_state.server_running = True
                st.rerun()

# ── Architecture ──
with right_col:
    st.markdown('<div class="section-header">🏗️ Network Architecture</div>', unsafe_allow_html=True)

    fig = go.Figure()
    fig.add_shape(type="line", x0=0.22, y0=0.5, x1=0.78, y1=0.5,
                  line=dict(color="#38bdf8", width=3, dash="dot"))
    fig.add_trace(go.Scatter(
        x=[0.1], y=[0.5], mode="markers+text",
        marker=dict(size=55, color="#0ea5e9", symbol="circle", line=dict(color="#38bdf8", width=3)),
        text=["CLIENT"], textposition="bottom center",
        textfont=dict(color="#e2e8f0", size=12, family="Inter"),
        hovertemplate="<b>Client</b><br>IP: 127.0.0.1<br>Role: Sender/Receiver<extra></extra>",
        name=""
    ))
    fig.add_trace(go.Scatter(
        x=[0.9], y=[0.5], mode="markers+text",
        marker=dict(size=55, color="#8b5cf6", symbol="square", line=dict(color="#a78bfa", width=3)),
        text=["SERVER"], textposition="bottom center",
        textfont=dict(color="#e2e8f0", size=12, family="Inter"),
        hovertemplate="<b>Server</b><br>IP: 127.0.0.1<br>Port: 5000<br>Role: Listen/Accept<extra></extra>",
        name=""
    ))
    fig.add_annotation(x=0.5, y=0.60, text="TCP · Port 5000", showarrow=False,
                       font=dict(color="#38bdf8", size=10, family="JetBrains Mono"),
                       bgcolor="rgba(10,14,26,0.85)", borderpad=4)
    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(visible=False, range=[-0.05, 1.05]),
        yaxis=dict(visible=False, range=[0.2, 0.85]),
        showlegend=False, height=210,
        margin=dict(l=0, r=0, t=8, b=28),
    )
    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

    # Socket Details
    st.markdown('<div class="section-header">🔧 Socket Details</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="info-panel">
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:0.8rem;">
        <div><div style="color:#475569;font-size:0.72rem;text-transform:uppercase;">Address Family</div>
             <div style="color:#38bdf8;font-weight:600;font-family:'JetBrains Mono';">AF_INET (IPv4)</div></div>
        <div><div style="color:#475569;font-size:0.72rem;text-transform:uppercase;">Socket Type</div>
             <div style="color:#a78bfa;font-weight:600;font-family:'JetBrains Mono';">SOCK_STREAM</div></div>
        <div><div style="color:#475569;font-size:0.72rem;text-transform:uppercase;">Transport</div>
             <div style="color:#4ade80;font-weight:600;font-family:'JetBrains Mono';">TCP</div></div>
        <div><div style="color:#475569;font-size:0.72rem;text-transform:uppercase;">Buffer</div>
             <div style="color:#fb923c;font-weight:600;font-family:'JetBrains Mono';">{buf_size}</div></div>
        <div><div style="color:#475569;font-size:0.72rem;text-transform:uppercase;">Host</div>
             <div style="color:#f472b6;font-weight:600;font-family:'JetBrains Mono';">{host}</div></div>
        <div><div style="color:#475569;font-size:0.72rem;text-transform:uppercase;">Port</div>
             <div style="color:#34d399;font-weight:600;font-family:'JetBrains Mono';">{int(port)}</div></div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # TCP Handshake
    st.markdown('<div class="section-header">🤝 TCP 3-Way Handshake</div>', unsafe_allow_html=True)
    for step, desc, clr in [
        ("SYN", "Client → Server", "#38bdf8"),
        ("SYN-ACK", "Server → Client", "#a78bfa"),
        ("ACK", "Client → Server", "#4ade80"),
        ("DATA TRANSFER", "Bidirectional", "#fb923c"),
        ("FIN / ACK", "Graceful Close", "#f87171"),
    ]:
        st.markdown(f"""
        <div style="display:flex;align-items:center;gap:0.7rem;margin-bottom:0.5rem;">
          <span style="background:{clr}22;border:1px solid {clr}55;color:{clr};
                       padding:0.15rem 0.6rem;border-radius:6px;font-family:'JetBrains Mono';
                       font-size:0.72rem;font-weight:700;min-width:110px;text-align:center;">{step}</span>
          <span style="color:#64748b;font-size:0.8rem;">{desc}</span>
        </div>""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  Row 2: Traffic Chart | Connection Log & Code
# ─────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
ch_col, lg_col = st.columns(2, gap="large")

with ch_col:
    st.markdown('<div class="section-header">📊 Message Traffic</div>', unsafe_allow_html=True)

    if st.session_state.chat_log:
        df = pd.DataFrame([
            {"time": e["time"], "bytes": len(e["msg"].encode()), "sender": e["sender"]}
            for e in st.session_state.chat_log
        ])
        fig2 = go.Figure()
        for sender, clr in [("Client", "#0ea5e9"), ("Server", "#8b5cf6")]:
            sub = df[df["sender"] == sender]
            if not sub.empty:
                fig2.add_trace(go.Bar(
                    x=sub["time"], y=sub["bytes"], name=sender,
                    marker_color=clr,
                    marker_line_color="rgba(255,255,255,0.08)",
                    marker_line_width=1,
                ))
        fig2.update_layout(
            barmode="group",
            plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)",
            font=dict(color="#94a3b8", family="Inter"),
            legend=dict(orientation="h", yanchor="bottom", y=1.02,
                        xanchor="right", x=1, font=dict(color="#94a3b8")),
            xaxis=dict(showgrid=False, zeroline=False, tickfont=dict(size=9)),
            yaxis=dict(showgrid=True, gridcolor="rgba(255,255,255,0.05)",
                       zeroline=False,
                       title=dict(text="Bytes", font=dict(color="#475569", size=11))),
            height=250,
            margin=dict(l=0, r=0, t=28, b=0),
        )
        st.plotly_chart(fig2, use_container_width=True, config={"displayModeBar": False})
    else:
        st.markdown("""
        <div style="text-align:center;padding:4rem 0;color:#334155;font-size:0.85rem;
                    border:1px dashed rgba(255,255,255,0.07);border-radius:12px;">
            📊 Traffic chart will appear after messages are sent
        </div>""", unsafe_allow_html=True)

    # TCP vs UDP bars
    st.markdown('<div class="section-header" style="margin-top:1rem;">📡 TCP vs UDP Comparison</div>', unsafe_allow_html=True)
    for lbl, tcp_v, udp_v in [("Reliability", 95, 30), ("Speed", 60, 95), ("Overhead", 75, 20), ("Ordering", 98, 15)]:
        st.markdown(f"""
        <div class="pb">
          <div class="pbl"><span>{lbl}</span>
            <span><span style="color:#38bdf8;">TCP {tcp_v}%</span>&nbsp;/&nbsp;<span style="color:#f87171;">UDP {udp_v}%</span></span>
          </div>
          <div class="pbt"><div class="pbf" style="width:{tcp_v}%;background:linear-gradient(90deg,#38bdf8,#38bdf888);"></div></div>
        </div>""", unsafe_allow_html=True)

with lg_col:
    st.markdown('<div class="section-header">📋 Connection Event Log</div>', unsafe_allow_html=True)

    log_html = '<div class="chat-wrap">'
    if not st.session_state.connection_log:
        log_html += '<p style="color:#334155;text-align:center;margin-top:3rem;font-size:0.85rem;">Events will appear here as messages are sent 📡</p>'
    else:
        for ev in reversed(st.session_state.connection_log):
            if "Established" in ev["event"]:
                badge = '<span class="badge bg">🟢</span>'
            elif "Closed" in ev["event"]:
                badge = '<span class="badge br">🔴</span>'
            elif "Server" in ev["event"]:
                badge = '<span class="badge bp">🖥️</span>'
            else:
                badge = '<span class="badge bb">👤</span>'
            log_html += f"""
            <div style="border-bottom:1px solid rgba(255,255,255,0.04);padding:0.6rem 0.2rem;">
              <div style="display:flex;align-items:center;justify-content:space-between;">
                <div style="display:flex;align-items:center;gap:0.5rem;">
                  {badge}
                  <span style="color:#e2e8f0;font-size:0.84rem;font-weight:500;">{ev["event"]}</span>
                </div>
                <span style="color:#475569;font-size:0.75rem;font-family:'JetBrains Mono';">{ev["time"]}</span>
              </div>
              <div style="color:#475569;font-size:0.76rem;margin-top:0.2rem;
                          padding-left:1.5rem;font-family:'JetBrains Mono';">{ev["detail"]}</div>
            </div>"""
    log_html += "</div>"
    st.markdown(log_html, unsafe_allow_html=True)

    # Source Code
    st.markdown('<div class="section-header" style="margin-top:1.2rem;">📄 Source Code</div>', unsafe_allow_html=True)
    tab_s, tab_c = st.tabs(["🖥️ server.py", "👤 client.py"])
    with tab_s:
        st.code("""\
import socket
HOST = '127.0.0.1'
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()
print(f"Server started on {HOST}:{PORT}")

conn, addr = server_socket.accept()
print(f"Connected by {addr}")

while True:
    data = conn.recv(1024).decode()
    if not data or data.lower() == 'exit':
        print("Client disconnected.")
        break
    print(f"Client: {data}")
    msg = input("You: ")
    conn.sendall(msg.encode())
    if msg.lower() == 'exit':
        break

conn.close()
server_socket.close()""", language="python")
    with tab_c:
        st.code("""\
import socket
HOST = '127.0.0.1'
PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
print("Connected to the server. Type 'exit' to end chat.")

while True:
    msg = input("You: ")
    client_socket.sendall(msg.encode())
    if msg.lower() == 'exit':
        break
    data = client_socket.recv(1024).decode()
    if not data or data.lower() == 'exit':
        print("Server disconnected.")
        break
    print(f"Server: {data}")

client_socket.close()""", language="python")

# ─────────────────────────────────────────────
#  How to Run
# ─────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<div class="section-header">🚀 How to Run the Real Application</div>', unsafe_allow_html=True)
r1, r2, r3 = st.columns(3)
for col, num, title, cmd, desc in [
    (r1, "1️⃣", "Install Dashboard Deps", "pip install streamlit plotly pandas", "Only needed once. The chat server/client use only Python's built-in socket."),
    (r2, "2️⃣", "Start the Server",       "python server.py",                   "Run in Terminal 1. Server binds to 127.0.0.1:5000 and waits for a client."),
    (r3, "3️⃣", "Connect the Client",     "python client.py",                   "Run in Terminal 2. Client connects. Type messages → Enter to send. 'exit' to quit."),
]:
    with col:
        st.markdown(f"""
        <div class="info-panel" style="text-align:center;">
          <div style="font-size:2rem;margin-bottom:0.5rem;">{num}</div>
          <div style="color:#e2e8f0;font-weight:700;margin-bottom:0.5rem;">{title}</div>
          <div class="code-block" style="text-align:left;margin-bottom:0.6rem;">{cmd}</div>
          <div style="color:#64748b;font-size:0.78rem;">{desc}</div>
        </div>""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  Footer
# ─────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align:center;padding:1.5rem;border-top:1px solid rgba(255,255,255,0.06);">
  <p style="color:#334155;font-size:0.8rem;margin:0;">
    🌐 LAN Chat Application &nbsp;·&nbsp; Computer Networks Mini Project &nbsp;·&nbsp;
    <span style="color:#38bdf8;">Ram Chandra Nayak</span> &amp;
    <span style="color:#a78bfa;">Saurabh Singh</span> &nbsp;·&nbsp; MMMUT Gorakhpur
  </p>
</div>
""", unsafe_allow_html=True)
