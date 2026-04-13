# 🌐 LAN Chat Application – Computer Networks Mini Project

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![TCP](https://img.shields.io/badge/Protocol-TCP%20Sockets-00C9A7?style=for-the-badge&logo=cisco&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

### 🚀 [**▶ Live Dashboard →**](https://computer-networkminiproject-4umuq8gartcwonfwpn6rcp.streamlit.app/)

*A real-time LAN chat application using Python TCP sockets, with a beautiful interactive Streamlit dashboard.*

</div>

---

## 📌 Overview

This is a **Computer Networks Mini Project** that demonstrates **socket programming** in Python using the **TCP protocol**. It includes:

- A **server** that listens for incoming client connections
- A **client** that connects and exchanges messages
- A **beautiful Streamlit dashboard** for visualizing the socket architecture, simulating chat, and understanding network concepts

---

## 🎯 Features

| Feature | Description |
|---|---|
| 💬 **Chat Simulator** | Interactive chat UI with Client & Server bubble messages |
| 🏗️ **Architecture Diagram** | Live Plotly network diagram showing TCP connection |
| 📊 **Traffic Chart** | Bar chart showing bytes transferred per message |
| 📋 **Event Log** | Real-time connection log (Established / Packets / Closed) |
| 🔧 **Socket Details** | AF_INET, SOCK_STREAM, buffer size, host, port |
| 🤝 **TCP Handshake** | Visual 3-way handshake breakdown |
| 📡 **TCP vs UDP** | Side-by-side protocol comparison bars |
| 📄 **Source Code** | Embedded `server.py` & `client.py` with syntax highlighting |

---

## 🗂️ File Structure

```
Computer-_Network_Mini_Project/
├── server.py           # TCP Server – binds, listens, accepts, and echoes messages
├── client.py           # TCP Client – connects and sends/receives messages
├── dashboard.py        # Streamlit dashboard (interactive UI)
├── requirements.txt    # Python dependencies for deployment
└── README.md           # This file
```

---

## ⚙️ How to Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/Ram-Nayak-16/Computer-_Network_Mini_Project.git
cd Computer-_Network_Mini_Project
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Dashboard
```bash
streamlit run dashboard.py
```
> Open [http://localhost:8501](http://localhost:8501) in your browser.

### 4. Run the Real Chat App (Optional)

**Terminal 1 – Start the server:**
```bash
python server.py
```

**Terminal 2 – Start the client:**
```bash
python client.py
```
> Both terminals can now send and receive messages. Type `exit` to disconnect.

---

## 🔌 How It Works

```
CLIENT                              SERVER
  |                                   |
  |──── SYN ──────────────────────►   |   (Connection request)
  |   ◄──── SYN-ACK ────────────────  |   (Connection acknowledged)
  |──── ACK ──────────────────────►   |   (Connection established)
  |                                   |
  |──── Data (sendall) ───────────►   |   (Message sent)
  |   ◄──── Data (sendall) ──────────  |   (Reply received)
  |                                   |
  |──── FIN ──────────────────────►   |   (Close connection)
  |   ◄──── ACK ────────────────────  |   (Closed)
```

### Key Concepts Used
- **`socket.AF_INET`** – IPv4 addressing
- **`socket.SOCK_STREAM`** – TCP (reliable, ordered, connection-based)
- **`bind()`** – Attach server to IP:Port
- **`listen()`** – Wait for incoming connections
- **`accept()`** – Accept a client connection
- **`connect()`** – Client initiates connection
- **`sendall()`** – Send data reliably
- **`recv(1024)`** – Receive up to 1024 bytes

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.10+ |
| Networking | `socket` (built-in) |
| Dashboard | Streamlit |
| Charts | Plotly |
| Data | Pandas |
| Deployment | Streamlit Community Cloud |

---

## 📸 Dashboard Preview

> Open the [**Live Dashboard**](https://computer-networkminiproject-4umuq8gartcwonfwpn6rcp.streamlit.app/) to interact with the full UI.

---

## 👥 Authors

| Name | Roll |
|---|---|
| **Ram Chandra Nayak** | MMMUT Gorakhpur |
| **Saurabh Singh** | MMMUT Gorakhpur |

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute.

---

<div align="center">
Made with ❤️ for Computer Networks Lab &nbsp;·&nbsp; MMMUT Gorakhpur
</div>
