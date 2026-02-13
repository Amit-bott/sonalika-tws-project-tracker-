# import streamlit as st
# import pandas as pd
# from datetime import date
# import streamlit.components.v1 as components

# # ================= CONFIG =================
# st.set_page_config(
#     page_title="TWS Project – Exports",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# DATA_FILE = "tws_exports.csv"
# COLUMNS = [
#     "Email","Project Code","Project Description","Start of Project","Platform",
#     "Continent/Country","SCR No","SCR Issue in CFT","Model","Aggregate",
#     "Aggregate Lead","Implementation Month","R&D PMO","Feasibility Uploaded",
#     "G1 Drg Release","Material Avl","Proto Fitment","Testing Start",
#     "Interim Testing Go Ahead","G1 ORC Drg","G1 ORC Material","G1 ORC Proto",
#     "G2 Go Ahead","G2 Material","5 Tractors Online","PRR Sign-off",
#     "Pre ERN","Go Ahead ERN","BOM Change","BCR Number","BCR Date","Cut-off Number"
# ]

# # ================= CURSOR REVEAL BACKGROUND =================
# def create_cursor_reveal_background():
#     cursor_html = '''
#     <!DOCTYPE html>
# <html lang="en">
# <head>
# <meta charset="UTF-8">
# <meta name="viewport" content="width=device-width, initial-scale=1.0">
# <title>Interactive Cursor Reveal Background</title>

# <style>
#   :root {
#     --circle-size: 400px;
#     --gradient-color-1: rgba(29, 78, 216, 0.95);
#     --gradient-color-2: rgba(37, 99, 235, 0.85);
#     --gradient-color-3: rgba(59, 130, 246, 0.75);
#   }
  
#   * {
#     margin: 0;
#     padding: 0;
#     box-sizing: border-box;
#   }
  
#   body {
#     margin: 0;
#     height: 100vh;
#     background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
#     overflow: hidden;
#     font-family: 'Segoe UI', system-ui, sans-serif;
#     display: flex;
#     justify-content: center;
#     align-items: center;
#   }

#   .background-container {
#     position: fixed;
#     top: 0;
#     left: 0;
#     width: 100%;
#     height: 100%;
#     z-index: -1;
#   }

#   .page {
#     position: absolute;
#     top: 0;
#     left: 0;
#     width: 100%;
#     height: 100%;
#     display: flex;
#     justify-content: center;
#     align-items: center;
#     opacity: 0;
#     pointer-events: none;
#     transition: opacity 0.8s cubic-bezier(0.4, 0, 0.2, 1);
#   }

#   .page.active {
#     opacity: 1;
#     pointer-events: all;
#   }

#   .container {
#     position: relative;
#     width: 100vw;
#     height: 100vh;
#     background-size: cover;
#     background-position: center;
#     overflow: hidden;
#     transform-style: preserve-3d;
#     perspective: 1000px;
#   }

#   .overlay {
#     position: absolute;
#     inset: 0;
#     background: white;
#     pointer-events: none;
#     transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
#     opacity: 0.98;
#   }

#   /* Page 1 Background */
#   .page1 .container {
#     background-image: url("https://images.unsplash.com/photo-1490474418585-ba9bad8fd0ea?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80");
#   }

#   /* Page 2 Background */
#   .page2 .container {
#     background-image: url("https://images.unsplash.com/photo-1500382017468-9049fed747ef?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80");
#   }

#   .content {
#     position: absolute;
#     inset: 0;
#     z-index: 20;
#     padding: 40px;
#     color: white;
#     display: flex;
#     flex-direction: column;
#     justify-content: center;
#     pointer-events: none;
#   }

#   .page1 .content {
#     background: linear-gradient(135deg, 
#       rgba(107, 33, 168, 0.7) 0%, 
#       rgba(168, 85, 247, 0.5) 100%);
#   }

#   .page2 .content {
#     background: linear-gradient(135deg, 
#       rgba(21, 94, 117, 0.7) 0%, 
#       rgba(56, 189, 248, 0.5) 100%);
#   }

#   .years-badge {
#     font-size: 2.5rem;
#     font-weight: 700;
#     margin-bottom: 10px;
#     text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
#   }

#   .main-heading {
#     font-size: 3.5rem;
#     font-weight: 800;
#     margin-bottom: 20px;
#     text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.7);
#     line-height: 1.2;
#   }

#   .sub-heading {
#     font-size: 1.5rem;
#     font-weight: 300;
#     margin-bottom: 30px;
#     text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
#     opacity: 0.9;
#     line-height: 1.6;
#   }

#   .highlight-text {
#     font-size: 1.8rem;
#     font-weight: 600;
#     color: #ffd700;
#     text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
#     border-left: 4px solid #ffd700;
#     padding-left: 15px;
#     margin-top: 20px;
#   }

#   .timeline-container {
#     display: flex;
#     justify-content: space-between;
#     align-items: center;
#     margin-top: 30px;
#     padding: 0 20px;
#   }

#   .timeline-item {
#     text-align: center;
#     flex: 1;
#   }

#   .year {
#     font-size: 3rem;
#     font-weight: 700;
#     color: #ffd700;
#     text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
#   }

#   .year-label {
#     font-size: 1.2rem;
#     font-weight: 300;
#     margin-top: 5px;
#     opacity: 0.9;
#   }

#   .timeline-line {
#     flex: 2;
#     height: 2px;
#     background: linear-gradient(90deg, 
#       rgba(255, 215, 0, 0.3) 0%, 
#       rgba(255, 215, 0, 0.7) 50%, 
#       rgba(255, 215, 0, 0.3) 100%);
#     margin: 0 20px;
#   }

#   .commitment-text {
#     font-size: 1.4rem;
#     font-weight: 400;
#     text-align: center;
#     margin-top: 20px;
#     color: #ffd700;
#     text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
#   }

#   .cursor-tracer {
#     position: absolute;
#     width: 40px;
#     height: 40px;
#     border: 2px solid rgba(255, 215, 0, 0.8);
#     border-radius: 50%;
#     pointer-events: none;
#     z-index: 100;
#     opacity: 0;
#     transition: transform 0.2s, opacity 0.2s;
#     mix-blend-mode: screen;
#     filter: blur(1px);
#   }

#   .cursor-dot {
#     position: absolute;
#     width: 8px;
#     height: 8px;
#     background: #ffd700;
#     border-radius: 50%;
#     pointer-events: none;
#     z-index: 101;
#     box-shadow: 0 0 20px #ffd700;
#     opacity: 0;
#   }

#   .glow {
#     position: absolute;
#     width: var(--circle-size);
#     height: var(--circle-size);
#     border-radius: 50%;
#     background: radial-gradient(
#       circle at center,
#       rgba(255, 215, 0, 0.6) 0%,
#       rgba(255, 215, 0, 0.4) 30%,
#       rgba(255, 215, 0, 0.2) 50%,
#       transparent 70%
#     );
#     filter: blur(40px);
#     opacity: 0;
#     pointer-events: none;
#     transition: opacity 0.3s;
#     mix-blend-mode: screen;
#   }

#   .instruction {
#     position: absolute;
#     bottom: 30px;
#     left: 50%;
#     transform: translateX(-50%);
#     color: rgba(255, 255, 255, 0.7);
#     font-size: 0.9rem;
#     text-align: center;
#     z-index: 1000;
#     background: rgba(0, 0, 0, 0.3);
#     padding: 8px 16px;
#     border-radius: 20px;
#     backdrop-filter: blur(5px);
#   }

#   .page-indicator {
#     position: absolute;
#     top: 30px;
#     right: 30px;
#     display: flex;
#     gap: 10px;
#     z-index: 1000;
#   }

#   .indicator-dot {
#     width: 12px;
#     height: 12px;
#     border-radius: 50%;
#     background: rgba(255, 255, 255, 0.3);
#     cursor: pointer;
#     transition: all 0.3s ease;
#   }

#   .indicator-dot.active {
#     background: #ffd700;
#     transform: scale(1.2);
#     box-shadow: 0 0 10px rgba(255, 215, 0, 0.5);
#   }

#   .ripple {
#     position: absolute;
#     border: 2px solid rgba(255, 215, 0, 0.3);
#     border-radius: 50%;
#     pointer-events: none;
#     animation: ripple 1.5s infinite;
#   }

#   @keyframes ripple {
#     0% { transform: scale(0.8); opacity: 1; }
#     100% { transform: scale(2); opacity: 0; }
#   }
# </style>
# </head>

# <body>
# <div class="background-container" id="backgroundContainer">
#   <!-- Page 1 -->
#   <div class="page page1 active">
#     <div class="container" id="box1">
#       <div class="overlay" id="overlay1"></div>
#       <div class="content">
#         <div class="years-badge">30 YEARS OF TRUST</div>
#         <div class="main-heading">जिव्ही ऐसे...</div>
#         <div class="sub-heading">
#           मिट्टी को सोना बनाते हैं हम<br>
#           किसान को वक्त की ताकत आज थमाते हैं हम...
#         </div>
#         <div class="highlight-text">
#           युवियां ऐसी - जो मिट्टी से सोना बनायें
#         </div>
#       </div>
#       <div class="cursor-tracer" id="cursorTracer1"></div>
#       <div class="cursor-dot" id="cursorDot1"></div>
#       <div class="glow" id="glow1"></div>
#     </div>
#   </div>

#   <!-- Page 2 -->
#   <div class="page page2">
#     <div class="container" id="box2">
#       <div class="overlay" id="overlay2"></div>
#       <div class="content">
#         <div class="years-badge">30 YEARS OF TRUST</div>
#         <div class="timeline-container">
#           <div class="timeline-item">
#             <div class="year">1996</div>
#             <div class="year-label">DUM KA<br>PEHLA<br>KADAM</div>
#           </div>
#           <div class="timeline-line"></div>
#           <div class="timeline-item">
#             <div class="year">2026</div>
#             <div class="year-label">DUM<br>SABSE AAGE<br>REHNE KA</div>
#           </div>
#         </div>
#         <div class="commitment-text">THREE DECADES<br>ONE COMMITMENT</div>
#       </div>
#       <div class="cursor-tracer" id="cursorTracer2"></div>
#       <div class="cursor-dot" id="cursorDot2"></div>
#       <div class="glow" id="glow2"></div>
#     </div>
#   </div>

#   <!-- Page Indicator -->
#   <div class="page-indicator">
#     <div class="indicator-dot active" onclick="showPage(1)"></div>
#     <div class="indicator-dot" onclick="showPage(2)"></div>
#   </div>

#   <!-- Instruction -->
#   <div class="instruction">Move cursor over the image to reveal background</div>
# </div>

# <script>
#   let currentPage = 1;
#   const pages = document.querySelectorAll('.page');
#   const indicators = document.querySelectorAll('.indicator-dot');

#   // Initialize all pages with cursor effects
#   initializePage(1);
#   initializePage(2);

#   function showPage(pageNumber) {
#     // Hide all pages
#     pages.forEach(page => {
#       page.classList.remove('active');
#     });
    
#     // Show selected page
#     document.querySelector(`.page${pageNumber}`).classList.add('active');
    
#     // Update indicators
#     indicators.forEach((indicator, index) => {
#       indicator.classList.toggle('active', index === pageNumber - 1);
#     });
    
#     currentPage = pageNumber;
#   }

#   function initializePage(pageNumber) {
#     const box = document.getElementById(`box${pageNumber}`);
#     const overlay = document.getElementById(`overlay${pageNumber}`);
#     const cursorTracer = document.getElementById(`cursorTracer${pageNumber}`);
#     const cursorDot = document.getElementById(`cursorDot${pageNumber}`);
#     const glow = document.getElementById(`glow${pageNumber}`);

#     function setMask(x, y) {
#       const mask = `
#         radial-gradient(
#           circle at ${x}px ${y}px,
#           transparent 0%,
#           rgba(0,0,0,0.95) 30%,
#           rgba(0,0,0,0.85) 45%,
#           rgba(255,255,255,0.1) 60%,
#           rgba(255,255,255,0.3) 70%,
#           white 85%
#         )
#       `;

#       overlay.style.maskImage = mask;
#       overlay.style.webkitMaskImage = mask;
      
#       // Add CSS filter for depth
#       overlay.style.filter = `
#         drop-shadow(0 0 30px rgba(255, 215, 0, 0.3))
#         brightness(1.1)
#       `;
#     }

#     function updateCursorElements(x, y) {
#       if (!cursorTracer || !cursorDot || !glow) return;
      
#       cursorTracer.style.left = `${x - 20}px`;
#       cursorTracer.style.top = `${y - 20}px`;
#       cursorTracer.style.opacity = '1';
#       cursorTracer.style.transform = `scale(${1 + Math.sin(Date.now() * 0.01) * 0.1})`;
      
#       cursorDot.style.left = `${x - 4}px`;
#       cursorDot.style.top = `${y - 4}px`;
#       cursorDot.style.opacity = '1';
      
#       glow.style.left = `${x - 200}px`;
#       glow.style.top = `${y - 200}px`;
#       glow.style.opacity = '0.7';
      
#       // Create ripple effect occasionally
#       if (Math.random() > 0.8) {
#         const ripple = document.createElement("div");
#         ripple.className = "ripple";
#         ripple.style.left = `${x}px`;
#         ripple.style.top = `${y}px`;
#         box.appendChild(ripple);
#         setTimeout(() => ripple.remove(), 1500);
#       }
#     }

#     function handleMouseMove(e) {
#       const rect = box.getBoundingClientRect();
#       const x = e.clientX - rect.left;
#       const y = e.clientY - rect.top;
      
#       setMask(x, y);
#       updateCursorElements(x, y);
      
#       // Parallax effect
#       box.style.transform = `
#         perspective(1000px)
#         rotateY(${(x - rect.width / 2) / 50}deg)
#         rotateX(${-(y - rect.height / 2) / 50}deg)
#       `;
#     }

#     function handleMouseLeave() {
#       overlay.style.maskImage = "none";
#       overlay.style.webkitMaskImage = "none";
#       overlay.style.filter = "none";
#       if (cursorTracer) cursorTracer.style.opacity = '0';
#       if (cursorDot) cursorDot.style.opacity = '0';
#       if (glow) glow.style.opacity = '0';
#       box.style.transform = "perspective(1000px) rotateY(0deg) rotateX(0deg)";
#     }

#     // Add event listeners
#     box.addEventListener("mousemove", handleMouseMove);
#     box.addEventListener("mouseleave", handleMouseLeave);
    
#     // Touch support
#     box.addEventListener("touchmove", (e) => {
#       e.preventDefault();
#       const touch = e.touches[0];
#       const rect = box.getBoundingClientRect();
#       const x = touch.clientX - rect.left;
#       const y = touch.clientY - rect.top;
      
#       setMask(x, y);
#       updateCursorElements(x, y);
#     });
    
#     box.addEventListener("touchend", handleMouseLeave);
#   }

#   // Auto-switch pages every 10 seconds
#   setInterval(() => {
#     currentPage = currentPage === 1 ? 2 : 1;
#     showPage(currentPage);
#   }, 10000);
# </script>
# </body>
# </html>
#     '''
#     return cursor_html

# # ================= STYLE =================
# st.markdown("""
# <style>
#     /* White Background Theme */
#     .stApp {
#         background-color: transparent !important;
#     }
    
#     /* Form Container Styling */
#     .form-container {
#         background: rgba(255, 255, 255, 0.92);
#         padding: 30px;
#         border-radius: 15px;
#         box-shadow: 0 20px 60px rgba(29, 78, 216, 0.15);
#         border: 1px solid rgba(59, 130, 246, 0.2);
#         margin: 20px 0;
#         position: relative;
#         z-index: 100;
#         backdrop-filter: blur(10px);
#     }
    
#     /* Blue Headers */
#     h1, h2, h3, h4, h5, h6 {
#         color: #1a56db !important;
#         font-weight: 700 !important;
#         font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
#     }
    
#     /* Blue Labels and Text */
#     label, span, p, div {
#         color: #1e40af !important;
#     }
    
#     /* Blue Input Fields */
#     .stTextInput > div > div > input,
#     .stTextArea > div > div > textarea,
#     .stSelectbox > div > div {
#         background-color: rgba(255, 255, 255, 0.9) !important;
#         color: #1e40af !important;
#         border: 1px solid #3b82f6 !important;
#         border-radius: 8px !important;
#     }
    
#     /* Blue Buttons */
#     .stButton > button {
#         background: linear-gradient(135deg, #2563eb, #1d4ed8) !important;
#         color: white !important;
#         border: none !important;
#         border-radius: 8px !important;
#         font-weight: 600 !important;
#         padding: 10px 24px !important;
#         transition: all 0.3s ease !important;
#     }
    
#     .stButton > button:hover {
#         background: linear-gradient(135deg, #1d4ed8, #1e40af) !important;
#         transform: translateY(-2px) !important;
#         box-shadow: 0 4px 12px rgba(29, 78, 216, 0.3) !important;
#     }
    
#     /* Date Input */
#     .stDateInput > div > div > input {
#         background-color: rgba(255, 255, 255, 0.9) !important;
#         color: #1e40af !important;
#         border: 1px solid #3b82f6 !important;
#         border-radius: 8px !important;
#     }
    
#     /* File Uploader */
#     .stFileUploader > div {
#         background-color: rgba(248, 250, 252, 0.9) !important;
#         border: 2px dashed #93c5fd !important;
#         border-radius: 10px !important;
#         padding: 20px !important;
#     }
    
#     /* Success/Error Messages */
#     .stAlert {
#         border-radius: 8px !important;
#         border: 1px solid !important;
#         background-color: rgba(255, 255, 255, 0.9) !important;
#     }
    
#     /* Background Instructions */
#     .bg-instruction {
#         position: fixed;
#         bottom: 20px;
#         left: 50%;
#         transform: translateX(-50%);
#         background: rgba(0, 0, 0, 0.7);
#         color: white;
#         padding: 10px 20px;
#         border-radius: 20px;
#         font-size: 14px;
#         z-index: 50;
#         backdrop-filter: blur(5px);
#     }
    
#     /* Tab Styling */
#     .stTabs [data-baseweb="tab-list"] {
#         gap: 8px;
#         background: rgba(255, 255, 255, 0.9);
#         border-radius: 10px 10px 0 0;
#         padding: 10px;
#     }
    
#     .stTabs [data-baseweb="tab"] {
#         background-color: rgba(255, 255, 255, 0.9) !important;
#         color: #1e40af !important;
#         border: 1px solid rgba(219, 234, 254, 0.8) !important;
#         border-radius: 8px 8px 0 0 !important;
#         padding: 12px 24px !important;
#     }
    
#     .stTabs [data-baseweb="tab"][aria-selected="true"] {
#         background-color: rgba(219, 234, 254, 0.9) !important;
#         color: #1d4ed8 !important;
#         border-bottom: 3px solid #2563eb !important;
#     }
    
#     /* Metrics Styling */
#     [data-testid="stMetric"] {
#         background-color: rgba(240, 249, 255, 0.9) !important;
#         padding: 20px !important;
#         border-radius: 12px !important;
#         border: 1px solid #bae6fd !important;
#         backdrop-filter: blur(5px);
#     }
    
#     [data-testid="stMetricLabel"], [data-testid="stMetricValue"], [data-testid="stMetricDelta"] {
#         color: #1e40af !important;
#     }
    
#     /* Table Styling */
#     .dataframe {
#         background-color: rgba(255, 255, 255, 0.9) !important;
#         color: #1e40af !important;
#         backdrop-filter: blur(5px);
#     }
    
#     /* Sidebar Styling */
#     section[data-testid="stSidebar"] {
#         background-color: rgba(248, 250, 252, 0.95) !important;
#         backdrop-filter: blur(10px);
#     }
# </style>
# """, unsafe_allow_html=True)

# # ================= LOAD / SAVE =================
# def load_data():
#     try:
#         df = pd.read_csv(DATA_FILE)
#         if 'Project Code' in df.columns:
#             df['Project Code'] = df['Project Code'].astype(str)
#         return df
#     except:
#         return pd.DataFrame(columns=COLUMNS)

# def save_data(df):
#     if 'Project Code' in df.columns:
#         df['Project Code'] = df['Project Code'].astype(str)
#     df.to_csv(DATA_FILE, index=False)

# df = load_data()

# # ================= DASHBOARD =================
# def create_dashboard():
#     st.markdown("### 📊 Project Analytics Dashboard")
    
#     if df.empty:
#         st.info("No projects available. Add your first project in the Data Entry tab.")
#         return
    
#     # Metrics Row
#     col1, col2, col3, col4 = st.columns(4)
    
#     with col1:
#         total_projects = len(df)
#         st.metric("Total Projects", total_projects)
    
#     with col2:
#         g1_completed = df["G1 Drg Release"].notna().sum()
#         st.metric("G1 Completed", g1_completed)
    
#     with col3:
#         g2_completed = df["G2 Go Ahead"].notna().sum()
#         st.metric("G2 Completed", g2_completed)
    
#     with col4:
#         active_projects = len(df[df['Implementation Month'].str.strip().str.lower() == pd.Timestamp.now().strftime('%b').lower()]) if 'Implementation Month' in df.columns else 0
#         st.metric("Active This Month", active_projects)
    
#     st.markdown("---")
    
#     # Recent Projects
#     st.markdown("### 📋 Recent Projects")
#     if 'Start of Project' in df.columns:
#         try:
#             df_display = df.copy()
#             df_display['Start of Project'] = pd.to_datetime(df_display['Start of Project'], errors='coerce')
#             recent_df = df_display.sort_values('Start of Project', ascending=False).head(10)
#         except:
#             recent_df = df.head(10)
#     else:
#         recent_df = df.head(10)
    
#     display_cols = ['Project Code', 'Project Description', 'Platform', 'Aggregate', 'Aggregate Lead']
#     display_cols = [col for col in display_cols if col in recent_df.columns]
    
#     if not recent_df.empty:
#         st.dataframe(recent_df[display_cols], width='stretch')

# # ================= MAIN =================
# # Add background instructions
# st.markdown('<div class="bg-instruction">Move cursor over the background to reveal images</div>', unsafe_allow_html=True)

# # Add cursor reveal background
# cursor_html = create_cursor_reveal_background()
# components.html(cursor_html, height=0, width=0)

# # Main content
# st.title("TWS Project – Exports Management")
# st.markdown("**Professional Project Tracking System**")

# tab1, tab2 = st.tabs(["📝 Data Entry Form", "📊 Dashboard"])

# # ================= DATA ENTRY FORM =================
# with tab1:
#     st.markdown('<div class="form-container">', unsafe_allow_html=True)
    
#     st.markdown("### ✨ New Project Entry")
    
#     with st.form("tws_form"):
#         col1, col2 = st.columns(2)
        
#         with col1:
#             email = st.text_input("📧 Email *", placeholder="user@company.com")
#             project_code = st.text_input("🔢 Project Code *", placeholder="PRJ-XXXX-YY")
#             project_desc = st.text_area("📝 Project Description *", height=100)
#             start_project = st.date_input("📅 Start of Project", date.today())
#             platform = st.selectbox(
#                 "🖥️ Platform",
#                 ["Below 30 HP", "30–60 HP", "60–101 HP", "Above 101 HP"]
#             )
#             continent = st.text_input("🌍 Continent / Country", placeholder="North America / USA")
#             scr_no = st.text_input("📄 SCR Number", placeholder="SCR-XXXX")
            
#         with col2:
#             scr_issue = st.text_input("🔧 SCR Issue in CFT", placeholder="Issue discussed in cross-functional team")
#             model = st.text_input("🚜 Model", placeholder="Model name/number")
#             aggregate = st.selectbox(
#                 "🔩 Aggregate",
#                 ["Electrical", "Hydraulic", "Transmission", "Engine", "Vehicle", "Cabin"]
#             )
#             agg_lead = st.text_input("👨‍💼 Aggregate Lead", placeholder="Lead person name")
#             impl_month = st.selectbox(
#                 "📆 Implementation Month",
#                 ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
#             )
#             r_and_d = st.selectbox(
#                 "🔬 R&D PMO",
#                 ["Mohit Rana", "Arashdeep Parmar"]
#             )
        
#         st.markdown("---")
#         st.markdown("#### 📎 Documents & Timeline")
        
#         col1, col2 = st.columns(2)
        
#         with col1:
#             feasibility = st.file_uploader("📎 Feasibility Study", type=['pdf', 'docx', 'doc'])
#             g1 = st.date_input("📐 G1 Drg Release")
#             material = st.date_input("📦 Material Avl")
#             proto = st.date_input("🔧 Proto Fitment")
#             testing = st.date_input("🧪 Testing Start")
#             interim = st.date_input("✅ Interim Testing Go Ahead")
            
#         with col2:
#             g1_orc_drg = st.date_input("🔄 G1 ORC Drg")
#             g1_orc_mat = st.date_input("📦 G1 ORC Material")
#             g1_orc_proto = st.date_input("🔧 G1 ORC Proto")
#             g2_go = st.date_input("🚀 G2 Go Ahead")
#             g2_mat = st.date_input("📦 G2 Material")
        
#         st.markdown("---")
#         st.markdown("#### 🏭 Production & Approvals")
        
#         col1, col2, col3 = st.columns(3)
        
#         with col1:
#             tractors = st.text_input("5 Tractors Online", placeholder="Status")
#             prr = st.text_input("✅ PRR Sign-off", placeholder="Status")
#             pre_ern = st.text_input("📋 Pre ERN", placeholder="Details")
            
#         with col2:
#             go_ern = st.text_input("✅ Go Ahead ERN", placeholder="Details")
#             bom = st.text_input("📊 BOM Change", placeholder="Changes")
#             bcr_no = st.text_input("🔢 BCR Number", placeholder="Reference")
            
#         with col3:
#             bcr_date = st.date_input("📅 BCR Date")
#             cutoff = st.text_input("✂️ Cut-off Number", placeholder="Reference")
        
#         submit = st.form_submit_button("🚀 Submit Project", use_container_width=True)
    
#     st.markdown('</div>', unsafe_allow_html=True)
    
#     if submit:
#         if not email or not project_code or not project_desc:
#             st.error("❌ Please fill all required fields (*)")
#         else:
#             project_code_str = str(project_code)
#             if not df.empty and 'Project Code' in df.columns:
#                 df['Project Code'] = df['Project Code'].astype(str)
#                 if project_code_str in df['Project Code'].values:
#                     st.warning("⚠️ Project Code already exists! Updating existing record...")
#                     idx = df[df['Project Code'] == project_code_str].index[0]
#                     update_record = True
#                 else:
#                     idx = len(df)
#                     update_record = False
#             else:
#                 update_record = False
            
#             def format_date(date_val):
#                 if pd.isna(date_val) or date_val is None:
#                     return ""
#                 return date_val.strftime('%Y-%m-%d') if hasattr(date_val, 'strftime') else str(date_val)
            
#             new_data = {
#                 "Email": str(email),
#                 "Project Code": project_code_str,
#                 "Project Description": str(project_desc),
#                 "Start of Project": format_date(start_project),
#                 "Platform": str(platform),
#                 "Continent/Country": str(continent),
#                 "SCR No": str(scr_no),
#                 "SCR Issue in CFT": str(scr_issue),
#                 "Model": str(model),
#                 "Aggregate": str(aggregate),
#                 "Aggregate Lead": str(agg_lead),
#                 "Implementation Month": str(impl_month),
#                 "R&D PMO": str(r_and_d),
#                 "Feasibility Uploaded": feasibility.name if feasibility else "",
#                 "G1 Drg Release": format_date(g1),
#                 "Material Avl": format_date(material),
#                 "Proto Fitment": format_date(proto),
#                 "Testing Start": format_date(testing),
#                 "Interim Testing Go Ahead": format_date(interim),
#                 "G1 ORC Drg": format_date(g1_orc_drg),
#                 "G1 ORC Material": format_date(g1_orc_mat),
#                 "G1 ORC Proto": format_date(g1_orc_proto),
#                 "G2 Go Ahead": format_date(g2_go),
#                 "G2 Material": format_date(g2_mat),
#                 "5 Tractors Online": str(tractors),
#                 "PRR Sign-off": str(prr),
#                 "Pre ERN": str(pre_ern),
#                 "Go Ahead ERN": str(go_ern),
#                 "BOM Change": str(bom),
#                 "BCR Number": str(bcr_no),
#                 "BCR Date": format_date(bcr_date),
#                 "Cut-off Number": str(cutoff)
#             }
            
#             if update_record:
#                 for key, value in new_data.items():
#                     if key in df.columns:
#                         df.at[idx, key] = value
#                 st.success(f"✅ Project {project_code} updated successfully!")
#             else:
#                 for col in COLUMNS:
#                     if col not in new_data:
#                         new_data[col] = ""
                
#                 df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
#                 st.success(f"✅ New project {project_code} added successfully!")
            
#             save_data(df)
#             df = load_data()

# # ================= DASHBOARD TAB =================
# with tab2:
#     create_dashboard()

# # ================= SIDEBAR =================
# with st.sidebar:
#     st.markdown("### TWS Exports")
#     st.markdown("**Project Management**")
    
#     st.markdown("---")
    
#     st.markdown("### 📈 Quick Stats")
#     if not df.empty and len(df) > 0:
#         total_projects = len(df)
#         active_this_month = len(df[df['Implementation Month'].str.strip().str.lower() == pd.Timestamp.now().strftime('%b').lower()]) if 'Implementation Month' in df.columns else 0
#         g1_complete = df['G1 Drg Release'].notna().sum() if 'G1 Drg Release' in df.columns else 0
        
#         st.metric("Total Projects", total_projects)
#         st.metric("Active This Month", active_this_month)
#         st.metric("G1 Complete", g1_complete)
#     else:
#         st.info("No data yet")
    
#     st.markdown("---")
    
#     st.markdown("### ⚡ Quick Actions")
#     if st.button("➕ Add New Project", use_container_width=True, key="sidebar_new"):
#         st.rerun()
    
#     if not df.empty:
#         csv = df.to_csv(index=False)
#         st.download_button(
#             label="📥 Export Data",
#             data=csv,
#             file_name="tws_exports.csv",
#             mime="text/csv",
#             use_container_width=True,
#             key="sidebar_export"
#         )





















# import streamlit as st
# import pandas as pd
# from datetime import date
# import streamlit.components.v1 as components
# import json
# import base64

# # ================= CONFIG =================
# st.set_page_config(
#     page_title="TWS Project – Exports",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# DATA_FILE = "tws_exports.csv"
# COLUMNS = [
#     "Email","Project Code","Project Description","Start of Project","Platform",
#     "Continent/Country","SCR No","SCR Issue in CFT","Model","Aggregate",
#     "Aggregate Lead","Implementation Month","R&D PMO","Feasibility Uploaded",
#     "G1 Drg Release","Material Avl","Proto Fitment","Testing Start",
#     "Interim Testing Go Ahead","G1 ORC Drg","G1 ORC Material","G1 ORC Proto",
#     "G2 Go Ahead","G2 Material","5 Tractors Online","PRR Sign-off",
#     "Pre ERN","Go Ahead ERN","BOM Change","BCR Number","BCR Date","Cut-off Number"
# ]

# # ================= PREMIUM 3D BACKGROUND ANIMATION =================
# def create_premium_3d_background():
#     cursor_html = '''
#     <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Premium 3D Animation Background</title>
    
#     <style>
#         * {
#             margin: 0;
#             padding: 0;
#             box-sizing: border-box;
#         }
        
#         body {
#             margin: 0;
#             height: 100vh;
#             background: linear-gradient(45deg, #0a0a0f 0%, #1a1a2e 50%, #16213e 100%);
#             overflow: hidden;
#             font-family: 'Segoe UI', system-ui, sans-serif;
#         }

#         .scene {
#             position: fixed;
#             width: 100%;
#             height: 100%;
#             perspective: 1200px;
#             transform-style: preserve-3d;
#             overflow: hidden;
#         }

#         .particles-container {
#             position: absolute;
#             width: 100%;
#             height: 100%;
#             z-index: 1;
#         }

#         .particle {
#             position: absolute;
#             width: 4px;
#             height: 4px;
#             background: radial-gradient(circle at center, #3b82f6 0%, #1d4ed8 50%, transparent 70%);
#             border-radius: 50%;
#             box-shadow: 0 0 20px #3b82f6, 0 0 40px #1d4ed8;
#             animation: float 15s infinite linear;
#         }

#         .floating-element {
#             position: absolute;
#             background: linear-gradient(45deg, rgba(59, 130, 246, 0.1), rgba(29, 78, 216, 0.05));
#             border: 1px solid rgba(59, 130, 246, 0.3);
#             border-radius: 20px;
#             backdrop-filter: blur(10px);
#             animation: floatElement 20s infinite ease-in-out;
#             transform-style: preserve-3d;
#         }

#         .floating-element:nth-child(1) {
#             width: 300px;
#             height: 200px;
#             top: 10%;
#             left: 5%;
#             animation-delay: 0s;
#             box-shadow: 0 20px 60px rgba(59, 130, 246, 0.2);
#         }

#         .floating-element:nth-child(2) {
#             width: 200px;
#             height: 300px;
#             top: 60%;
#             right: 10%;
#             animation-delay: -5s;
#             box-shadow: 0 20px 60px rgba(29, 78, 216, 0.2);
#         }

#         .floating-element:nth-child(3) {
#             width: 250px;
#             height: 150px;
#             bottom: 20%;
#             left: 20%;
#             animation-delay: -10s;
#             box-shadow: 0 20px 60px rgba(37, 99, 235, 0.2);
#         }

#         .floating-element:nth-child(4) {
#             width: 150px;
#             height: 250px;
#             top: 20%;
#             right: 20%;
#             animation-delay: -15s;
#             box-shadow: 0 20px 60px rgba(30, 64, 175, 0.2);
#         }

#         .cursor-circle {
#             position: fixed;
#             width: 120px;
#             height: 120px;
#             border: 2px solid rgba(59, 130, 246, 0.8);
#             border-radius: 50%;
#             pointer-events: none;
#             z-index: 9999;
#             transform: translate(-50%, -50%);
#             mix-blend-mode: screen;
#             background: radial-gradient(circle at center, rgba(59, 130, 246, 0.3), transparent 70%);
#             filter: blur(15px);
#             opacity: 0;
#             transition: width 0.3s, height 0.3s, opacity 0.3s;
#             animation: pulse 4s infinite ease-in-out;
#         }

#         .cursor-inner {
#             position: fixed;
#             width: 20px;
#             height: 20px;
#             background: radial-gradient(circle at center, #3b82f6, #1d4ed8);
#             border-radius: 50%;
#             pointer-events: none;
#             z-index: 10000;
#             transform: translate(-50%, -50%);
#             box-shadow: 0 0 30px #3b82f6, 0 0 60px #1d4ed8;
#             opacity: 0;
#             transition: opacity 0.3s;
#         }

#         .light-beam {
#             position: absolute;
#             width: 300px;
#             height: 300px;
#             background: radial-gradient(circle at center, rgba(59, 130, 246, 0.1), transparent 70%);
#             filter: blur(40px);
#             border-radius: 50%;
#             opacity: 0;
#             pointer-events: none;
#             z-index: 9998;
#             transform: translate(-50%, -50%);
#             animation: beamMove 10s infinite linear;
#         }

#         .light-beam:nth-child(2) {
#             animation-delay: -2s;
#             background: radial-gradient(circle at center, rgba(29, 78, 216, 0.1), transparent 70%);
#         }

#         .light-beam:nth-child(3) {
#             animation-delay: -4s;
#             background: radial-gradient(circle at center, rgba(37, 99, 235, 0.1), transparent 70%);
#         }

#         .light-beam:nth-child(4) {
#             animation-delay: -6s;
#             background: radial-gradient(circle at center, rgba(30, 64, 175, 0.1), transparent 70%);
#         }

#         .light-beam:nth-child(5) {
#             animation-delay: -8s;
#             background: radial-gradient(circle at center, rgba(59, 130, 246, 0.1), transparent 70%);
#         }

#         .neon-grid {
#             position: absolute;
#             width: 100%;
#             height: 100%;
#             background-image: 
#                 linear-gradient(rgba(59, 130, 246, 0.1) 1px, transparent 1px),
#                 linear-gradient(90deg, rgba(59, 130, 246, 0.1) 1px, transparent 1px);
#             background-size: 50px 50px;
#             z-index: 0;
#             opacity: 0.3;
#             animation: gridMove 20s infinite linear;
#         }

#         .shooting-star {
#             position: absolute;
#             width: 3px;
#             height: 100px;
#             background: linear-gradient(to bottom, transparent, #3b82f6, #1d4ed8, transparent);
#             border-radius: 50%;
#             filter: blur(1px);
#             animation: shootStar 8s infinite linear;
#             opacity: 0;
#         }

#         @keyframes float {
#             0%, 100% { transform: translateY(0) rotate(0deg); opacity: 0; }
#             10% { opacity: 1; }
#             50% { opacity: 0.7; }
#             90% { opacity: 0; }
#         }

#         @keyframes floatElement {
#             0%, 100% { 
#                 transform: translateY(0px) rotateX(0deg) rotateY(0deg); 
#                 box-shadow: 0 20px 60px rgba(59, 130, 246, 0.2);
#             }
#             25% { 
#                 transform: translateY(-50px) rotateX(5deg) rotateY(5deg); 
#                 box-shadow: 0 40px 80px rgba(29, 78, 216, 0.3);
#             }
#             50% { 
#                 transform: translateY(0px) rotateX(0deg) rotateY(10deg); 
#                 box-shadow: 0 20px 60px rgba(37, 99, 235, 0.2);
#             }
#             75% { 
#                 transform: translateY(50px) rotateX(-5deg) rotateY(5deg); 
#                 box-shadow: 0 40px 80px rgba(30, 64, 175, 0.3);
#             }
#         }

#         @keyframes pulse {
#             0%, 100% { transform: translate(-50%, -50%) scale(1); opacity: 0.6; }
#             50% { transform: translate(-50%, -50%) scale(1.2); opacity: 0.8; }
#         }

#         @keyframes beamMove {
#             0% { transform: translate(-50%, -50%) rotate(0deg) scale(1); opacity: 0.3; }
#             50% { transform: translate(-50%, -50%) rotate(180deg) scale(1.5); opacity: 0.1; }
#             100% { transform: translate(-50%, -50%) rotate(360deg) scale(1); opacity: 0.3; }
#         }

#         @keyframes gridMove {
#             0% { transform: translate(0, 0); }
#             100% { transform: translate(50px, 50px); }
#         }

#         @keyframes shootStar {
#             0% { 
#                 transform: translateX(-100px) translateY(-100px) rotate(45deg); 
#                 opacity: 0; 
#             }
#             10% { opacity: 1; }
#             100% { 
#                 transform: translateX(2000px) translateY(2000px) rotate(45deg); 
#                 opacity: 0; 
#             }
#         }

#         .text-float {
#             position: absolute;
#             color: rgba(255, 255, 255, 0.1);
#             font-size: 4rem;
#             font-weight: 900;
#             opacity: 0.05;
#             z-index: 0;
#             animation: textFloat 25s infinite linear;
#             text-shadow: 0 0 50px rgba(59, 130, 246, 0.5);
#             pointer-events: none;
#             user-select: none;
#         }

#         .text-float:nth-child(1) {
#             top: 10%;
#             left: 5%;
#             animation-delay: 0s;
#         }

#         .text-float:nth-child(2) {
#             top: 30%;
#             right: 10%;
#             animation-delay: -5s;
#         }

#         .text-float:nth-child(3) {
#             bottom: 20%;
#             left: 15%;
#             animation-delay: -10s;
#         }

#         .text-float:nth-child(4) {
#             bottom: 40%;
#             right: 20%;
#             animation-delay: -15s;
#         }

#         @keyframes textFloat {
#             0% { transform: translateY(0px) rotate(0deg) scale(1); opacity: 0.05; }
#             25% { transform: translateY(-20px) rotate(90deg) scale(1.1); opacity: 0.03; }
#             50% { transform: translateY(0px) rotate(180deg) scale(1); opacity: 0.05; }
#             75% { transform: translateY(20px) rotate(270deg) scale(0.9); opacity: 0.03; }
#             100% { transform: translateY(0px) rotate(360deg) scale(1); opacity: 0.05; }
#         }

#         .radar-sweep {
#             position: absolute;
#             width: 600px;
#             height: 600px;
#             top: 50%;
#             left: 50%;
#             transform: translate(-50%, -50%);
#             border-radius: 50%;
#             border: 2px solid rgba(59, 130, 246, 0.1);
#             z-index: 0;
#             opacity: 0.1;
#             pointer-events: none;
#         }

#         .radar-sweep::before {
#             content: '';
#             position: absolute;
#             width: 100%;
#             height: 100%;
#             border-radius: 50%;
#             background: conic-gradient(transparent, rgba(59, 130, 246, 0.3), transparent);
#             animation: radarRotate 8s infinite linear;
#             filter: blur(10px);
#         }

#         @keyframes radarRotate {
#             0% { transform: rotate(0deg); }
#             100% { transform: rotate(360deg); }
#         }

#         .interaction-hint {
#             position: fixed;
#             bottom: 20px;
#             left: 50%;
#             transform: translateX(-50%);
#             color: rgba(255, 255, 255, 0.7);
#             font-size: 14px;
#             padding: 10px 20px;
#             background: rgba(0, 0, 0, 0.5);
#             border-radius: 20px;
#             backdrop-filter: blur(10px);
#             z-index: 10000;
#             animation: hintPulse 3s infinite;
#             border: 1px solid rgba(59, 130, 246, 0.3);
#         }

#         @keyframes hintPulse {
#             0%, 100% { opacity: 0.7; transform: translateX(-50%) translateY(0); }
#             50% { opacity: 1; transform: translateX(-50%) translateY(-5px); }
#         }
#     </style>
# </head>
# <body>
#     <div class="scene" id="scene">
#         <div class="particles-container" id="particles"></div>
#         <div class="neon-grid"></div>
        
#         <div class="floating-element"></div>
#         <div class="floating-element"></div>
#         <div class="floating-element"></div>
#         <div class="floating-element"></div>
        
#         <div class="light-beam"></div>
#         <div class="light-beam"></div>
#         <div class="light-beam"></div>
#         <div class="light-beam"></div>
#         <div class="light-beam"></div>
        
#         <div class="radar-sweep"></div>
        
#         <div class="text-float">30 YEARS</div>
#         <div class="text-float">TRUST</div>
#         <div class="text-float">EXCELLENCE</div>
#         <div class="text-float">INNOVATION</div>
        
#         <div class="cursor-circle" id="cursorCircle"></div>
#         <div class="cursor-inner" id="cursorInner"></div>
        
#         <div class="interaction-hint">✨ Move cursor to see 3D effects | Click anywhere for surprise</div>
#     </div>

#     <script>
#         const scene = document.getElementById('scene');
#         const cursorCircle = document.getElementById('cursorCircle');
#         const cursorInner = document.getElementById('cursorInner');
#         const particlesContainer = document.getElementById('particles');
        
#         // Create particles
#         function createParticles() {
#             for (let i = 0; i < 150; i++) {
#                 const particle = document.createElement('div');
#                 particle.className = 'particle';
#                 particle.style.left = `${Math.random() * 100}%`;
#                 particle.style.top = `${Math.random() * 100}%`;
#                 particle.style.width = `${Math.random() * 4 + 1}px`;
#                 particle.style.height = particle.style.width;
#                 particle.style.animationDelay = `${Math.random() * 15}s`;
#                 particle.style.animationDuration = `${Math.random() * 10 + 10}s`;
#                 particlesContainer.appendChild(particle);
#             }
#         }
        
#         // Create shooting stars
#         function createShootingStars() {
#             for (let i = 0; i < 5; i++) {
#                 const star = document.createElement('div');
#                 star.className = 'shooting-star';
#                 star.style.left = `${Math.random() * 100}%`;
#                 star.style.top = `${Math.random() * 100}%`;
#                 star.style.animationDelay = `${Math.random() * 8}s`;
#                 star.style.transform = `rotate(${Math.random() * 360}deg)`;
#                 scene.appendChild(star);
#             }
#         }
        
#         // Mouse move effects
#         function handleMouseMove(e) {
#             const x = e.clientX;
#             const y = e.clientY;
            
#             // Update cursor elements
#             cursorCircle.style.left = `${x}px`;
#             cursorCircle.style.top = `${y}px`;
#             cursorCircle.style.opacity = '1';
            
#             cursorInner.style.left = `${x}px`;
#             cursorInner.style.top = `${y}px`;
#             cursorInner.style.opacity = '1';
            
#             // Parallax effect on floating elements
#             const floatingElements = document.querySelectorAll('.floating-element');
#             floatingElements.forEach(element => {
#                 const speed = 0.02;
#                 const xMove = (x - window.innerWidth / 2) * speed;
#                 const yMove = (y - window.innerHeight / 2) * speed;
#                 element.style.transform += ` translate(${xMove}px, ${yMove}px)`;
#             });
            
#             // Create ripple effect on click
#             if (Math.random() > 0.95) {
#                 createRipple(x, y);
#             }
#         }
        
#         // Create ripple effect
#         function createRipple(x, y) {
#             const ripple = document.createElement('div');
#             ripple.style.position = 'fixed';
#             ripple.style.left = `${x}px`;
#             ripple.style.top = `${y}px`;
#             ripple.style.width = '0px';
#             ripple.style.height = '0px';
#             ripple.style.border = '2px solid rgba(59, 130, 246, 0.5)';
#             ripple.style.borderRadius = '50%';
#             ripple.style.pointerEvents = 'none';
#             ripple.style.zIndex = '9997';
#             ripple.style.transform = 'translate(-50%, -50%)';
#             scene.appendChild(ripple);
            
#             const animation = ripple.animate([
#                 { width: '0px', height: '0px', opacity: 1 },
#                 { width: '400px', height: '400px', opacity: 0 }
#             ], {
#                 duration: 1000,
#                 easing: 'ease-out'
#             });
            
#             animation.onfinish = () => ripple.remove();
#         }
        
#         // Click effect
#         function handleClick(e) {
#             const x = e.clientX;
#             const y = e.clientY;
            
#             // Create explosion effect
#             for (let i = 0; i < 20; i++) {
#                 setTimeout(() => {
#                     createExplosionParticle(x, y);
#                 }, i * 50);
#             }
            
#             // Create big ripple
#             createRipple(x, y);
            
#             // Pulse animation on scene
#             scene.animate([
#                 { transform: 'scale(1)' },
#                 { transform: 'scale(1.01)' },
#                 { transform: 'scale(1)' }
#             ], {
#                 duration: 300,
#                 easing: 'ease-out'
#             });
#         }
        
#         // Create explosion particle
#         function createExplosionParticle(x, y) {
#             const particle = document.createElement('div');
#             particle.style.position = 'fixed';
#             particle.style.left = `${x}px`;
#             particle.style.top = `${y}px`;
#             particle.style.width = '10px';
#             particle.style.height = '10px';
#             particle.style.background = 'radial-gradient(circle at center, #3b82f6, #1d4ed8)';
#             particle.style.borderRadius = '50%';
#             particle.style.pointerEvents = 'none';
#             particle.style.zIndex = '9997';
#             particle.style.transform = 'translate(-50%, -50%)';
#             particle.style.boxShadow = '0 0 20px #3b82f6';
#             scene.appendChild(particle);
            
#             const angle = Math.random() * Math.PI * 2;
#             const distance = 100 + Math.random() * 100;
#             const targetX = x + Math.cos(angle) * distance;
#             const targetY = y + Math.sin(angle) * distance;
            
#             particle.animate([
#                 { 
#                     transform: 'translate(-50%, -50%) scale(1) rotate(0deg)', 
#                     opacity: 1 
#                 },
#                 { 
#                     transform: `translate(${targetX - x}px, ${targetY - y}px) scale(0.5) rotate(360deg)`, 
#                     opacity: 0 
#                 }
#             ], {
#                 duration: 1000,
#                 easing: 'ease-out'
#             }).onfinish = () => particle.remove();
#         }
        
#         // Mouse leave
#         function handleMouseLeave() {
#             cursorCircle.style.opacity = '0';
#             cursorInner.style.opacity = '0';
#         }
        
#         // Initialize
#         function init() {
#             createParticles();
#             createShootingStars();
            
#             // Add event listeners
#             document.addEventListener('mousemove', handleMouseMove);
#             document.addEventListener('click', handleClick);
#             document.addEventListener('mouseleave', handleMouseLeave);
            
#             // Auto create ripples
#             setInterval(() => {
#                 if (Math.random() > 0.7) {
#                     const x = Math.random() * window.innerWidth;
#                     const y = Math.random() * window.innerHeight;
#                     createRipple(x, y);
#                 }
#             }, 3000);
#         }
        
#         // Start when page loads
#         window.addEventListener('DOMContentLoaded', init);
        
#         // Resize handler
#         window.addEventListener('resize', () => {
#             particlesContainer.innerHTML = '';
#             createParticles();
#         });
#     </script>
# </body>
# </html>
#     '''
#     return cursor_html

# # ================= PREMIUM 3D FORM ANIMATION =================
# def create_3d_form_animation():
#     form_html = '''
#     <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>3D Form Animation</title>
    
#     <style>
#         * {
#             margin: 0;
#             padding: 0;
#             box-sizing: border-box;
#         }
        
#         body {
#             font-family: 'Segoe UI', system-ui, sans-serif;
#             overflow: hidden;
#         }
        
#         .form-animation-container {
#             position: fixed;
#             top: 0;
#             left: 0;
#             width: 100%;
#             height: 100%;
#             z-index: 9000;
#             pointer-events: none;
#         }
        
#         .form-3d-box {
#             position: absolute;
#             width: 80px;
#             height: 80px;
#             background: linear-gradient(45deg, #3b82f6, #1d4ed8);
#             border-radius: 15px;
#             transform-style: preserve-3d;
#             animation: boxFloat 4s infinite ease-in-out;
#             box-shadow: 
#                 0 10px 30px rgba(59, 130, 246, 0.3),
#                 inset 0 1px 0 rgba(255, 255, 255, 0.2);
#             transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
#             cursor: pointer;
#             pointer-events: all;
#             z-index: 9001;
#         }
        
#         .form-3d-box:hover {
#             transform: translateZ(50px) rotateX(15deg) rotateY(15deg) scale(1.1);
#             box-shadow: 
#                 0 20px 50px rgba(59, 130, 246, 0.4),
#                 inset 0 1px 0 rgba(255, 255, 255, 0.3);
#         }
        
#         .form-3d-box:active {
#             transform: translateZ(30px) scale(0.95);
#             animation: boxClick 0.5s ease;
#         }
        
#         .form-3d-box::before {
#             content: '';
#             position: absolute;
#             top: 5px;
#             left: 5px;
#             right: 5px;
#             bottom: 5px;
#             border: 2px solid rgba(255, 255, 255, 0.1);
#             border-radius: 10px;
#             pointer-events: none;
#         }
        
#         .form-3d-box::after {
#             content: 'NEW';
#             position: absolute;
#             top: 50%;
#             left: 50%;
#             transform: translate(-50%, -50%);
#             color: white;
#             font-weight: bold;
#             font-size: 14px;
#             letter-spacing: 1px;
#             text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
#         }
        
#         .box-trail {
#             position: absolute;
#             width: 100%;
#             height: 100%;
#             pointer-events: none;
#             z-index: 9000;
#         }
        
#         .trail-particle {
#             position: absolute;
#             width: 4px;
#             height: 4px;
#             background: linear-gradient(45deg, #3b82f6, #1d4ed8);
#             border-radius: 50%;
#             pointer-events: none;
#             opacity: 0;
#             animation: trailFade 1s forwards;
#         }
        
#         .form-sparkle {
#             position: absolute;
#             width: 8px;
#             height: 8px;
#             background: white;
#             border-radius: 50%;
#             pointer-events: none;
#             opacity: 0;
#             animation: sparkle 1s forwards;
#             box-shadow: 0 0 10px white;
#         }
        
#         .connection-line {
#             position: absolute;
#             height: 2px;
#             background: linear-gradient(90deg, transparent, #3b82f6, transparent);
#             transform-origin: left center;
#             pointer-events: none;
#             opacity: 0.3;
#             filter: blur(1px);
#         }
        
#         @keyframes boxFloat {
#             0%, 100% { 
#                 transform: translateY(0px) rotateX(0deg) rotateY(0deg); 
#                 box-shadow: 
#                     0 10px 30px rgba(59, 130, 246, 0.3),
#                     inset 0 1px 0 rgba(255, 255, 255, 0.2);
#             }
#             25% { 
#                 transform: translateY(-20px) rotateX(5deg) rotateY(5deg); 
#                 box-shadow: 
#                     0 20px 40px rgba(59, 130, 246, 0.4),
#                     inset 0 1px 0 rgba(255, 255, 255, 0.3);
#             }
#             50% { 
#                 transform: translateY(0px) rotateX(0deg) rotateY(10deg); 
#                 box-shadow: 
#                     0 10px 30px rgba(29, 78, 216, 0.3),
#                     inset 0 1px 0 rgba(255, 255, 255, 0.2);
#             }
#             75% { 
#                 transform: translateY(20px) rotateX(-5deg) rotateY(5deg); 
#                 box-shadow: 
#                     0 20px 40px rgba(37, 99, 235, 0.4),
#                     inset 0 1px 0 rgba(255, 255, 255, 0.3);
#             }
#         }
        
#         @keyframes boxClick {
#             0% { transform: translateZ(50px) scale(1); }
#             50% { transform: translateZ(30px) scale(0.9); }
#             100% { transform: translateZ(50px) scale(1); }
#         }
        
#         @keyframes trailFade {
#             0% { 
#                 transform: translate(0, 0) scale(1); 
#                 opacity: 0.8; 
#             }
#             100% { 
#                 transform: translate(var(--tx), var(--ty)) scale(0); 
#                 opacity: 0; 
#             }
#         }
        
#         @keyframes sparkle {
#             0% { 
#                 transform: scale(0) rotate(0deg); 
#                 opacity: 1; 
#             }
#             50% { 
#                 transform: scale(1) rotate(180deg); 
#                 opacity: 0.5; 
#             }
#             100% { 
#                 transform: scale(0) rotate(360deg); 
#                 opacity: 0; 
#             }
#         }
        
#         .form-notification {
#             position: fixed;
#             top: 100px;
#             right: -400px;
#             background: linear-gradient(45deg, rgba(59, 130, 246, 0.95), rgba(29, 78, 216, 0.95));
#             color: white;
#             padding: 20px 30px;
#             border-radius: 15px;
#             backdrop-filter: blur(10px);
#             border: 1px solid rgba(255, 255, 255, 0.2);
#             box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
#             z-index: 9002;
#             opacity: 0;
#             transform: translateX(0) rotateY(90deg);
#             transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
#             pointer-events: none;
#         }
        
#         .form-notification.show {
#             right: 20px;
#             opacity: 1;
#             transform: translateX(0) rotateY(0deg);
#         }
        
#         .notification-title {
#             font-size: 18px;
#             font-weight: bold;
#             margin-bottom: 5px;
#             display: flex;
#             align-items: center;
#             gap: 10px;
#         }
        
#         .notification-title::before {
#             content: '✨';
#             font-size: 20px;
#         }
        
#         .notification-message {
#             font-size: 14px;
#             opacity: 0.9;
#         }
#     </style>
# </head>
# <body>
#     <div class="form-animation-container" id="formAnimation">
#         <div class="box-trail" id="boxTrail"></div>
#         <div class="form-3d-box" id="formBox"></div>
#     </div>
    
#     <div class="form-notification" id="formNotification">
#         <div class="notification-title">New Project Created!</div>
#         <div class="notification-message">Your project has been successfully added to the database.</div>
#     </div>

#     <script>
#         const formBox = document.getElementById('formBox');
#         const boxTrail = document.getElementById('boxTrail');
#         const formNotification = document.getElementById('formNotification');
        
#         // Initial random position
#         updateBoxPosition();
        
#         // Box click handler
#         formBox.addEventListener('click', function(e) {
#             e.stopPropagation();
            
#             // Click animation
#             this.style.animation = 'none';
#             setTimeout(() => {
#                 this.style.animation = 'boxFloat 4s infinite ease-in-out';
#             }, 500);
            
#             // Create explosion effect
#             createExplosion(e.clientX, e.clientY);
            
#             // Show notification
#             showNotification();
            
#             // Move box to new random position
#             setTimeout(updateBoxPosition, 300);
#         });
        
#         // Box hover effects
#         formBox.addEventListener('mouseenter', function() {
#             createSparkles();
#         });
        
#         formBox.addEventListener('mousemove', function(e) {
#             createTrail(e.clientX, e.clientY);
#         });
        
#         // Update box position
#         function updateBoxPosition() {
#             const maxX = window.innerWidth - 100;
#             const maxY = window.innerHeight - 100;
#             const x = Math.random() * maxX;
#             const y = Math.random() * maxY;
            
#             formBox.style.left = `${x}px`;
#             formBox.style.top = `${y}px`;
            
#             // Create connection lines
#             createConnectionLines(x + 40, y + 40);
#         }
        
#         // Create trail particles
#         function createTrail(x, y) {
#             const rect = formBox.getBoundingClientRect();
#             const boxX = rect.left + rect.width / 2;
#             const boxY = rect.top + rect.height / 2;
            
#             const trail = document.createElement('div');
#             trail.className = 'trail-particle';
            
#             const dx = x - boxX;
#             const dy = y - boxY;
#             const distance = Math.sqrt(dx * dx + dy * dy);
            
#             trail.style.setProperty('--tx', `${dx}px`);
#             trail.style.setProperty('--ty', `${dy}px`);
#             trail.style.left = `${boxX}px`;
#             trail.style.top = `${boxY}px`;
            
#             boxTrail.appendChild(trail);
            
#             setTimeout(() => trail.remove(), 1000);
#         }
        
#         // Create sparkle effect
#         function createSparkles() {
#             const rect = formBox.getBoundingClientRect();
            
#             for (let i = 0; i < 8; i++) {
#                 const sparkle = document.createElement('div');
#                 sparkle.className = 'form-sparkle';
                
#                 const angle = Math.random() * Math.PI * 2;
#                 const distance = 20 + Math.random() * 30;
#                 const x = rect.left + 40 + Math.cos(angle) * distance;
#                 const y = rect.top + 40 + Math.sin(angle) * distance;
                
#                 sparkle.style.left = `${x}px`;
#                 sparkle.style.top = `${y}px`;
#                 sparkle.style.animationDelay = `${i * 0.1}s`;
                
#                 boxTrail.appendChild(sparkle);
                
#                 setTimeout(() => sparkle.remove(), 1000);
#             }
#         }
        
#         // Create explosion effect
#         function createExplosion(x, y) {
#             for (let i = 0; i < 15; i++) {
#                 setTimeout(() => {
#                     const particle = document.createElement('div');
#                     particle.className = 'trail-particle';
#                     particle.style.background = `linear-gradient(45deg, 
#                         hsl(${Math.random() * 60 + 200}, 100%, 65%), 
#                         hsl(${Math.random() * 60 + 200}, 100%, 45%))`;
#                     particle.style.width = '6px';
#                     particle.style.height = '6px';
                    
#                     const angle = Math.random() * Math.PI * 2;
#                     const distance = 50 + Math.random() * 100;
#                     const tx = Math.cos(angle) * distance;
#                     const ty = Math.sin(angle) * distance;
                    
#                     particle.style.setProperty('--tx', `${tx}px`);
#                     particle.style.setProperty('--ty', `${ty}px`);
#                     particle.style.left = `${x}px`;
#                     particle.style.top = `${y}px`;
                    
#                     boxTrail.appendChild(particle);
                    
#                     setTimeout(() => particle.remove(), 1000);
#                 }, i * 30);
#             }
#         }
        
#         // Create connection lines
#         function createConnectionLines(x, y) {
#             // Remove old lines
#             const oldLines = document.querySelectorAll('.connection-line');
#             oldLines.forEach(line => line.remove());
            
#             // Create new lines to corners
#             const corners = [
#                 { x: 20, y: 20 },
#                 { x: window.innerWidth - 20, y: 20 },
#                 { x: 20, y: window.innerHeight - 20 },
#                 { x: window.innerWidth - 20, y: window.innerHeight - 20 }
#             ];
            
#             corners.forEach(corner => {
#                 const line = document.createElement('div');
#                 line.className = 'connection-line';
                
#                 const dx = corner.x - x;
#                 const dy = corner.y - y;
#                 const distance = Math.sqrt(dx * dx + dy * dy);
#                 const angle = Math.atan2(dy, dx) * 180 / Math.PI;
                
#                 line.style.width = `${distance}px`;
#                 line.style.left = `${x}px`;
#                 line.style.top = `${y}px`;
#                 line.style.transform = `rotate(${angle}deg)`;
                
#                 boxTrail.appendChild(line);
                
#                 // Animate line
#                 setTimeout(() => {
#                     line.style.opacity = '0';
#                     setTimeout(() => line.remove(), 1000);
#                 }, 2000);
#             });
#         }
        
#         // Show notification
#         function showNotification() {
#             formNotification.classList.add('show');
            
#             setTimeout(() => {
#                 formNotification.classList.remove('show');
#             }, 3000);
#         }
        
#         // Auto move box every 30 seconds
#         setInterval(updateBoxPosition, 30000);
        
#         // Resize handler
#         window.addEventListener('resize', updateBoxPosition);
#     </script>
# </body>
# </html>
#     '''
#     return form_html

# # ================= PROFESSIONAL STYLES =================
# st.markdown("""
# <style>
#     /* Transparent Background */
#     .stApp {
#         background: transparent !important;
#     }
    
#     /* Professional Header */
#     .main-header {
#         background: linear-gradient(135deg, 
#             rgba(29, 78, 216, 0.95), 
#             rgba(37, 99, 235, 0.9),
#             rgba(30, 64, 175, 0.95));
#         padding: 30px 40px;
#         border-radius: 20px;
#         margin: 20px 0 30px 0;
#         box-shadow: 
#             0 20px 60px rgba(29, 78, 216, 0.3),
#             0 0 0 1px rgba(255, 255, 255, 0.1);
#         backdrop-filter: blur(10px);
#         border: 1px solid rgba(255, 255, 255, 0.2);
#         position: relative;
#         overflow: hidden;
#         z-index: 100;
#     }
    
#     .main-header::before {
#         content: '';
#         position: absolute;
#         top: 0;
#         left: 0;
#         right: 0;
#         bottom: 0;
#         background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" preserveAspectRatio="none"><path d="M0,0 L100,0 L100,100 Z" fill="rgba(255,255,255,0.05)"/></svg>');
#         background-size: cover;
#         z-index: -1;
#     }
    
#     /* Premium Form Container */
#     .premium-form {
#         background: linear-gradient(145deg, 
#             rgba(255, 255, 255, 0.98),
#             rgba(248, 250, 252, 0.96));
#         padding: 40px;
#         border-radius: 25px;
#         margin: 20px 0;
#         box-shadow: 
#             0 30px 80px rgba(29, 78, 216, 0.2),
#             0 10px 30px rgba(0, 0, 0, 0.1),
#             inset 0 1px 0 rgba(255, 255, 255, 0.8);
#         backdrop-filter: blur(20px);
#         border: 1px solid rgba(255, 255, 255, 0.3);
#         position: relative;
#         z-index: 100;
#         transform-style: preserve-3d;
#         transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
#     }
    
#     .premium-form:hover {
#         transform: translateY(-5px) perspective(1000px) rotateX(2deg);
#         box-shadow: 
#             0 40px 100px rgba(29, 78, 216, 0.3),
#             0 15px 40px rgba(0, 0, 0, 0.15),
#             inset 0 1px 0 rgba(255, 255, 255, 0.9);
#     }
    
#     /* 3D Input Fields */
#     .stTextInput > div > div > input,
#     .stTextArea > div > div > textarea,
#     .stSelectbox > div > div,
#     .stDateInput > div > div > input {
#         background: linear-gradient(145deg, 
#             rgba(255, 255, 255, 0.95),
#             rgba(248, 250, 252, 0.9)) !important;
#         color: #1e40af !important;
#         border: 2px solid rgba(59, 130, 246, 0.3) !important;
#         border-radius: 12px !important;
#         padding: 14px 20px !important;
#         font-size: 15px !important;
#         transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
#         box-shadow: 
#             inset 0 2px 4px rgba(0, 0, 0, 0.05),
#             0 4px 12px rgba(59, 130, 246, 0.1) !important;
#         backdrop-filter: blur(10px) !important;
#     }
    
#     .stTextInput > div > div > input:focus,
#     .stTextArea > div > div > textarea:focus,
#     .stSelectbox > div > div:focus-within,
#     .stDateInput > div > div > input:focus {
#         border-color: #3b82f6 !important;
#         box-shadow: 
#             inset 0 2px 8px rgba(0, 0, 0, 0.1),
#             0 8px 24px rgba(59, 130, 246, 0.3),
#             0 0 0 3px rgba(59, 130, 246, 0.1) !important;
#         transform: translateY(-2px) scale(1.01) !important;
#         outline: none !important;
#     }
    
#     /* Premium Buttons */
#     .stButton > button {
#         background: linear-gradient(135deg, 
#             #3b82f6 0%, 
#             #2563eb 25%, 
#             #1d4ed8 50%, 
#             #1e40af 100%) !important;
#         color: white !important;
#         border: none !important;
#         border-radius: 12px !important;
#         font-weight: 600 !important;
#         padding: 16px 32px !important;
#         font-size: 16px !important;
#         transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
#         position: relative !important;
#         overflow: hidden !important;
#         box-shadow: 
#             0 10px 30px rgba(59, 130, 246, 0.4),
#             0 5px 15px rgba(29, 78, 216, 0.3) !important;
#         text-shadow: 0 1px 2px rgba(0, 0, 0, 0.2) !important;
#         letter-spacing: 0.5px !important;
#     }
    
#     .stButton > button::before {
#         content: '';
#         position: absolute;
#         top: 0;
#         left: -100%;
#         width: 100%;
#         height: 100%;
#         background: linear-gradient(90deg, 
#             transparent, 
#             rgba(255, 255, 255, 0.2), 
#             transparent);
#         transition: 0.5s;
#     }
    
#     .stButton > button:hover {
#         transform: translateY(-3px) scale(1.02) !important;
#         box-shadow: 
#             0 15px 40px rgba(59, 130, 246, 0.5),
#             0 8px 20px rgba(29, 78, 216, 0.4),
#             inset 0 1px 0 rgba(255, 255, 255, 0.3) !important;
#     }
    
#     .stButton > button:hover::before {
#         left: 100%;
#     }
    
#     .stButton > button:active {
#         transform: translateY(-1px) scale(0.98) !important;
#         box-shadow: 
#             0 5px 20px rgba(59, 130, 246, 0.4),
#             0 3px 10px rgba(29, 78, 216, 0.3) !important;
#     }
    
#     /* Premium Labels */
#     .stTextInput label,
#     .stTextArea label,
#     .stSelectbox label,
#     .stDateInput label,
#     .stFileUploader label {
#         color: #1e40af !important;
#         font-weight: 600 !important;
#         font-size: 14px !important;
#         margin-bottom: 8px !important;
#         display: block !important;
#         text-transform: uppercase !important;
#         letter-spacing: 0.5px !important;
#     }
    
#     /* Section Headers */
#     .section-header {
#         background: linear-gradient(135deg, 
#             rgba(59, 130, 246, 0.1),
#             rgba(29, 78, 216, 0.05));
#         padding: 20px 30px;
#         border-radius: 15px;
#         margin: 25px 0;
#         border-left: 5px solid #3b82f6;
#         position: relative;
#         overflow: hidden;
#     }
    
#     .section-header::before {
#         content: '';
#         position: absolute;
#         top: 0;
#         left: 0;
#         right: 0;
#         bottom: 0;
#         background: linear-gradient(90deg, 
#             transparent, 
#             rgba(255, 255, 255, 0.1), 
#             transparent);
#         transform: translateX(-100%);
#         animation: shimmer 3s infinite;
#     }
    
#     @keyframes shimmer {
#         100% { transform: translateX(100%); }
#     }
    
#     /* File Uploader Styling */
#     .stFileUploader > div {
#         background: linear-gradient(145deg, 
#             rgba(255, 255, 255, 0.95),
#             rgba(248, 250, 252, 0.9)) !important;
#         border: 2px dashed rgba(59, 130, 246, 0.5) !important;
#         border-radius: 15px !important;
#         padding: 30px !important;
#         transition: all 0.3s ease !important;
#     }
    
#     .stFileUploader > div:hover {
#         border-color: #3b82f6 !important;
#         background: linear-gradient(145deg, 
#             rgba(255, 255, 255, 0.98),
#             rgba(248, 250, 252, 0.95)) !important;
#         transform: translateY(-2px);
#         box-shadow: 0 10px 30px rgba(59, 130, 246, 0.2) !important;
#     }
    
#     /* Tab Styling */
#     .stTabs [data-baseweb="tab-list"] {
#         gap: 10px;
#         background: rgba(255, 255, 255, 0.9);
#         border-radius: 15px;
#         padding: 10px;
#         backdrop-filter: blur(10px);
#         border: 1px solid rgba(59, 130, 246, 0.2);
#         box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
#     }
    
#     .stTabs [data-baseweb="tab"] {
#         background: rgba(255, 255, 255, 0.8) !important;
#         color: #1e40af !important;
#         border: 2px solid rgba(59, 130, 246, 0.3) !important;
#         border-radius: 10px !important;
#         padding: 15px 30px !important;
#         font-weight: 600 !important;
#         transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
#         position: relative !important;
#         overflow: hidden !important;
#     }
    
#     .stTabs [data-baseweb="tab"][aria-selected="true"] {
#         background: linear-gradient(135deg, 
#             rgba(59, 130, 246, 0.2),
#             rgba(29, 78, 216, 0.15)) !important;
#         color: #1d4ed8 !important;
#         border-color: #3b82f6 !important;
#         box-shadow: 
#             inset 0 2px 8px rgba(59, 130, 246, 0.2),
#             0 5px 15px rgba(59, 130, 246, 0.2) !important;
#         transform: translateY(-2px) !important;
#     }
    
#     /* Success/Error Messages */
#     .stAlert {
#         border-radius: 15px !important;
#         border: none !important;
#         background: linear-gradient(135deg, 
#             rgba(255, 255, 255, 0.95),
#             rgba(248, 250, 252, 0.9)) !important;
#         backdrop-filter: blur(10px) !important;
#         box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1) !important;
#         border: 1px solid rgba(59, 130, 246, 0.2) !important;
#         padding: 20px !important;
#     }
    
#     /* Metrics/Dashboard Cards */
#     .metric-card {
#         background: linear-gradient(135deg, 
#             rgba(255, 255, 255, 0.95),
#             rgba(248, 250, 252, 0.9));
#         padding: 25px;
#         border-radius: 20px;
#         border: 1px solid rgba(59, 130, 246, 0.2);
#         box-shadow: 
#             0 15px 40px rgba(0, 0, 0, 0.1),
#             inset 0 1px 0 rgba(255, 255, 255, 0.8);
#         backdrop-filter: blur(10px);
#         transition: all 0.3s ease;
#         position: relative;
#         overflow: hidden;
#     }
    
#     .metric-card:hover {
#         transform: translateY(-5px);
#         box-shadow: 
#             0 20px 50px rgba(0, 0, 0, 0.15),
#             inset 0 1px 0 rgba(255, 255, 255, 0.9);
#     }
    
#     /* Glass Effect */
#     .glass-effect {
#         background: rgba(255, 255, 255, 0.1);
#         backdrop-filter: blur(20px);
#         border: 1px solid rgba(255, 255, 255, 0.2);
#         box-shadow: 0 20px 60px rgba(0, 0, 0, 0.2);
#     }
    
#     /* Floating Animation */
#     @keyframes float {
#         0%, 100% { transform: translateY(0px) rotate(0deg); }
#         50% { transform: translateY(-20px) rotate(180deg); }
#     }
    
#     .floating {
#         animation: float 6s ease-in-out infinite;
#     }
    
#     /* Particle Container */
#     .particles-container {
#         position: fixed;
#         top: 0;
#         left: 0;
#         width: 100%;
#         height: 100%;
#         pointer-events: none;
#         z-index: 1;
#     }
# </style>
# """, unsafe_allow_html=True)

# # ================= LOAD / SAVE =================
# def load_data():
#     try:
#         df = pd.read_csv(DATA_FILE)
#         if 'Project Code' in df.columns:
#             df['Project Code'] = df['Project Code'].astype(str)
#         return df
#     except:
#         return pd.DataFrame(columns=COLUMNS)

# def save_data(df):
#     if 'Project Code' in df.columns:
#         df['Project Code'] = df['Project Code'].astype(str)
#     df.to_csv(DATA_FILE, index=False)

# df = load_data()

# # ================= DASHBOARD =================
# def create_dashboard():
#     st.markdown("### 📊 Project Analytics Dashboard")
    
#     if df.empty:
#         st.info("No projects available. Add your first project below!")
#         return
    
#     # Metrics Row with Premium Cards
#     col1, col2, col3, col4 = st.columns(4)
    
#     with col1:
#         total_projects = len(df)
#         st.markdown(f"""
#         <div class="metric-card">
#             <div style="font-size: 28px; font-weight: 700; color: #1d4ed8; margin-bottom: 10px;">{total_projects}</div>
#             <div style="font-size: 14px; color: #6b7280; text-transform: uppercase; letter-spacing: 1px;">Total Projects</div>
#         </div>
#         """, unsafe_allow_html=True)
    
#     with col2:
#         g1_completed = df["G1 Drg Release"].notna().sum()
#         st.markdown(f"""
#         <div class="metric-card">
#             <div style="font-size: 28px; font-weight: 700; color: #10b981; margin-bottom: 10px;">{g1_completed}</div>
#             <div style="font-size: 14px; color: #6b7280; text-transform: uppercase; letter-spacing: 1px;">G1 Completed</div>
#         </div>
#         """, unsafe_allow_html=True)
    
#     with col3:
#         g2_completed = df["G2 Go Ahead"].notna().sum()
#         st.markdown(f"""
#         <div class="metric-card">
#             <div style="font-size: 28px; font-weight: 700; color: #f59e0b; margin-bottom: 10px;">{g2_completed}</div>
#             <div style="font-size: 14px; color: #6b7280; text-transform: uppercase; letter-spacing: 1px;">G2 Completed</div>
#         </div>
#         """, unsafe_allow_html=True)
    
#     with col4:
#         active_projects = len(df[df['Implementation Month'].str.strip().str.lower() == pd.Timestamp.now().strftime('%b').lower()]) if 'Implementation Month' in df.columns else 0
#         st.markdown(f"""
#         <div class="metric-card">
#             <div style="font-size: 28px; font-weight: 700; color: #ef4444; margin-bottom: 10px;">{active_projects}</div>
#             <div style="font-size: 14px; color: #6b7280; text-transform: uppercase; letter-spacing: 1px;">Active This Month</div>
#         </div>
#         """, unsafe_allow_html=True)
    
#     st.markdown("---")
    
#     # Recent Projects
#     st.markdown("### 📋 Recent Projects")
#     if 'Start of Project' in df.columns:
#         try:
#             df_display = df.copy()
#             df_display['Start of Project'] = pd.to_datetime(df_display['Start of Project'], errors='coerce')
#             recent_df = df_display.sort_values('Start of Project', ascending=False).head(10)
#         except:
#             recent_df = df.head(10)
#     else:
#         recent_df = df.head(10)
    
#     display_cols = ['Project Code', 'Project Description', 'Platform', 'Aggregate', 'Aggregate Lead']
#     display_cols = [col for col in display_cols if col in recent_df.columns]
    
#     if not recent_df.empty:
#         st.dataframe(
#             recent_df[display_cols],
#             height=300,
#             use_container_width=True
#         )

# # ================= MAIN =================
# # Add 3D Background Animation
# bg_html = create_premium_3d_background()
# components.html(bg_html, height=0, width=0)

# # Add 3D Form Animation (Floating Box)
# form_anim_html = create_3d_form_animation()
# components.html(form_anim_html, height=0, width=0)

# # Main Header
# st.markdown("""
# <div class="main-header">
#     <h1 style="color: white; margin: 0; font-size: 2.5rem; text-shadow: 0 2px 10px rgba(0,0,0,0.3);">🚀 TWS Project Management</h1>
#     <p style="color: rgba(255,255,255,0.9); margin: 10px 0 0 0; font-size: 1.1rem;">Professional Project Tracking System with Premium 3D Effects</p>
# </div>
# """, unsafe_allow_html=True)

# # Tabs
# tab1, tab2 = st.tabs(["✨ New Project Entry", "📊 Dashboard"])

# # ================= DATA ENTRY FORM =================
# with tab1:
#     st.markdown('<div class="premium-form">', unsafe_allow_html=True)
    
#     st.markdown("""
#     <div class="section-header">
#         <h3 style="color: #1d4ed8; margin: 0; display: flex; align-items: center; gap: 10px;">
#             <span style="font-size: 24px;">✨</span> Create New Project
#         </h3>
#         <p style="color: #6b7280; margin: 5px 0 0 0; font-size: 14px;">Fill in the details below to create a new project entry</p>
#     </div>
#     """, unsafe_allow_html=True)
    
#     with st.form("tws_form", clear_on_submit=True):
#         col1, col2 = st.columns(2)
        
#         with col1:
#             email = st.text_input("📧 Email Address *", placeholder="your.email@company.com")
#             project_code = st.text_input("🔢 Project Code *", placeholder="PRJ-2024-001")
#             project_desc = st.text_area("📝 Project Description *", height=100, 
#                                       placeholder="Enter detailed project description here...")
#             start_project = st.date_input("📅 Project Start Date", date.today())
#             platform = st.selectbox(
#                 "🖥️ Platform Category",
#                 ["Below 30 HP", "30–60 HP", "60–101 HP", "Above 101 HP", "Custom Platform"]
#             )
#             continent = st.text_input("🌍 Region / Country", placeholder="North America / USA")
#             scr_no = st.text_input("📄 SCR Reference Number", placeholder="SCR-XXXX-YYYY")
            
#         with col2:
#             scr_issue = st.text_input("🔧 CFT Issue Details", placeholder="Describe the cross-functional team issue...")
#             model = st.text_input("🚜 Model Specification", placeholder="Model name and variant")
#             aggregate = st.selectbox(
#                 "🔩 Aggregate Type",
#                 ["Electrical System", "Hydraulic System", "Transmission", "Engine Components", 
#                  "Vehicle Assembly", "Cabin Features", "Custom Aggregate"]
#             )
#             agg_lead = st.text_input("👨‍💼 Aggregate Lead Name", placeholder="Full name of lead person")
#             impl_month = st.selectbox(
#                 "📆 Target Implementation Month",
#                 ["January", "February", "March", "April", "May", "June", 
#                  "July", "August", "September", "October", "November", "December"]
#             )
#             r_and_d = st.selectbox(
#                 "🔬 R&D Project Manager",
#                 ["Mohit Rana", "Arashdeep Parmar", "Other R&D Specialist"]
#             )
        
#         st.markdown("""
#         <div class="section-header">
#             <h4 style="color: #1d4ed8; margin: 0;">📎 Documents & Development Timeline</h4>
#         </div>
#         """, unsafe_allow_html=True)
        
#         col1, col2 = st.columns(2)
        
#         with col1:
#             feasibility = st.file_uploader("📎 Upload Feasibility Study", type=['pdf', 'docx', 'doc', 'xlsx'])
#             g1 = st.date_input("📐 G1 Drawing Release Date")
#             material = st.date_input("📦 Material Availability Date")
#             proto = st.date_input("🔧 Prototype Fitment Date")
#             testing = st.date_input("🧪 Testing Start Date")
#             interim = st.date_input("✅ Interim Testing Approval Date")
            
#         with col2:
#             g1_orc_drg = st.date_input("🔄 G1 ORC Drawing Date")
#             g1_orc_mat = st.date_input("📦 G1 ORC Material Date")
#             g1_orc_proto = st.date_input("🔧 G1 ORC Prototype Date")
#             g2_go = st.date_input("🚀 G2 Go-Ahead Date")
#             g2_mat = st.date_input("📦 G2 Material Date")
        
#         st.markdown("""
#         <div class="section-header">
#             <h4 style="color: #1d4ed8; margin: 0;">🏭 Production & Final Approvals</h4>
#         </div>
#         """, unsafe_allow_html=True)
        
#         col1, col2, col3 = st.columns(3)
        
#         with col1:
#             tractors = st.text_input("5 Tractors Online Status", placeholder="Completed / Pending / In Progress")
#             prr = st.text_input("✅ PRR Sign-off Status", placeholder="Status and remarks")
#             pre_ern = st.text_input("📋 Pre-ERN Details", placeholder="Pre-ERN specifications")
            
#         with col2:
#             go_ern = st.text_input("✅ Go-Ahead ERN Status", placeholder="Approval details")
#             bom = st.text_input("📊 BOM Changes", placeholder="Bill of Material modifications")
#             bcr_no = st.text_input("🔢 BCR Reference Number", placeholder="BCR-XXXX-YYYY")
            
#         with col3:
#             bcr_date = st.date_input("📅 BCR Date")
#             cutoff = st.text_input("✂️ Cut-off Number", placeholder="Cut-off reference")
        
#         col1, col2, col3 = st.columns([1, 2, 1])
#         with col2:
#             submit = st.form_submit_button("🚀 Create New Project", use_container_width=True)
    
#     st.markdown('</div>', unsafe_allow_html=True)
    
#     if submit:
#         if not email or not project_code or not project_desc:
#             st.error("❌ Please fill all required fields (*)")
#         else:
#             project_code_str = str(project_code)
            
#             # Check for duplicate project code
#             duplicate = False
#             if not df.empty and 'Project Code' in df.columns:
#                 df['Project Code'] = df['Project Code'].astype(str)
#                 if project_code_str in df['Project Code'].values:
#                     duplicate = True
            
#             if duplicate:
#                 st.warning(f"⚠️ Project Code '{project_code}' already exists!")
                
#                 # Show existing projects with similar codes
#                 similar_projects = df[df['Project Code'].str.contains(project_code_str[:6], na=False)]
#                 if not similar_projects.empty:
#                     st.info("📋 Similar existing projects:")
#                     st.dataframe(similar_projects[['Project Code', 'Project Description', 'Start of Project']])
#             else:
#                 # Prepare new data
#                 def format_date(date_val):
#                     if pd.isna(date_val) or date_val is None:
#                         return ""
#                     return date_val.strftime('%Y-%m-%d') if hasattr(date_val, 'strftime') else str(date_val)
                
#                 new_data = {
#                     "Email": str(email),
#                     "Project Code": project_code_str,
#                     "Project Description": str(project_desc),
#                     "Start of Project": format_date(start_project),
#                     "Platform": str(platform),
#                     "Continent/Country": str(continent),
#                     "SCR No": str(scr_no),
#                     "SCR Issue in CFT": str(scr_issue),
#                     "Model": str(model),
#                     "Aggregate": str(aggregate),
#                     "Aggregate Lead": str(agg_lead),
#                     "Implementation Month": str(impl_month),
#                     "R&D PMO": str(r_and_d),
#                     "Feasibility Uploaded": feasibility.name if feasibility else "",
#                     "G1 Drg Release": format_date(g1),
#                     "Material Avl": format_date(material),
#                     "Proto Fitment": format_date(proto),
#                     "Testing Start": format_date(testing),
#                     "Interim Testing Go Ahead": format_date(interim),
#                     "G1 ORC Drg": format_date(g1_orc_drg),
#                     "G1 ORC Material": format_date(g1_orc_mat),
#                     "G1 ORC Proto": format_date(g1_orc_proto),
#                     "G2 Go Ahead": format_date(g2_go),
#                     "G2 Material": format_date(g2_mat),
#                     "5 Tractors Online": str(tractors),
#                     "PRR Sign-off": str(prr),
#                     "Pre ERN": str(pre_ern),
#                     "Go Ahead ERN": str(go_ern),
#                     "BOM Change": str(bom),
#                     "BCR Number": str(bcr_no),
#                     "BCR Date": format_date(bcr_date),
#                     "Cut-off Number": str(cutoff)
#                 }
                
#                 # Ensure all columns exist
#                 for col in COLUMNS:
#                     if col not in new_data:
#                         new_data[col] = ""
                
#                 df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
#                 save_data(df)
#                 df = load_data()
                
#                 # Show success with premium animation
#                 st.markdown(f"""
#                 <div style="background: linear-gradient(135deg, #10b981, #059669); 
#                             padding: 25px; border-radius: 15px; color: white; 
#                             margin: 20px 0; text-align: center; animation: fadeIn 0.5s ease;">
#                     <h3 style="color: white; margin: 0 0 10px 0;">✨ Project Created Successfully!</h3>
#                     <p style="margin: 0; opacity: 0.9;">Project <strong>{project_code_str}</strong> has been added to the database.</p>
#                 </div>
#                 <style>
#                 @keyframes fadeIn {{
#                     from {{ opacity: 0; transform: translateY(-20px); }}
#                     to {{ opacity: 1; transform: translateY(0); }}
#                 }}
#                 </style>
#                 """, unsafe_allow_html=True)
                
#                 # Trigger JavaScript animation
#                 js_code = """
#                 <script>
#                 // Show notification animation
#                 setTimeout(() => {
#                     if (window.parent && window.parent.document) {
#                         const notification = window.parent.document.querySelector('.form-notification');
#                         if (notification) {
#                             notification.classList.add('show');
#                             setTimeout(() => notification.classList.remove('show'), 3000);
#                         }
#                     }
#                 }, 100);
#                 </script>
#                 """
#                 components.html(js_code, height=0, width=0)

# # ================= DASHBOARD TAB =================
# with tab2:
#     create_dashboard()

# # ================= SIDEBAR =================
# with st.sidebar:
#     st.markdown("""
#     <div style="background: linear-gradient(135deg, rgba(59, 130, 246, 0.95), rgba(29, 78, 216, 0.9));
#                 padding: 25px; border-radius: 15px; color: white; margin-bottom: 20px; text-align: center;">
#         <h3 style="color: white; margin: 0 0 10px 0;">🚀 TWS Exports</h3>
#         <p style="margin: 0; opacity: 0.9; font-size: 14px;">Premium Project Management</p>
#     </div>
#     """, unsafe_allow_html=True)
    
#     st.markdown("---")
    
#     # Quick Stats - FIXED VERSION
#     st.markdown("### 📈 Quick Stats")
    
#     if not df.empty and len(df) > 0:
#         total_projects = len(df)
#         active_this_month = len(df[df['Implementation Month'].str.strip().str.lower() == pd.Timestamp.now().strftime('%b').lower()]) if 'Implementation Month' in df.columns else 0
#         g1_complete = df['G1 Drg Release'].notna().sum() if 'G1 Drg Release' in df.columns else 0
        
#         col1, col2 = st.columns(2)
#         with col1:
#             st.metric("Total", total_projects)
#         with col2:
#             st.metric("Active", active_this_month)
        
#         # Calculate percentage safely
#         if total_projects > 0:
#             completion_rate = (g1_complete / total_projects) * 100
#         else:
#             completion_rate = 0
        
#         # Fixed progress bar without f-string error
#         progress_html = f"""
#         <div style="background: rgba(59, 130, 246, 0.1); padding: 15px; border-radius: 10px; margin: 10px 0;">
#             <div style="font-size: 12px; color: #6b7280; text-transform: uppercase;">G1 Completion</div>
#             <div style="display: flex; align-items: center; gap: 10px; margin-top: 5px;">
#                 <div style="flex: 1; height: 6px; background: rgba(59, 130, 246, 0.2); border-radius: 3px; overflow: hidden;">
#                     <div style="width: {completion_rate}%; height: 100%; background: linear-gradient(90deg, #3b82f6, #1d4ed8); border-radius: 3px;"></div>
#                 </div>
#                 <div style="font-size: 14px; font-weight: 600; color: #1d4ed8;">{int(completion_rate)}%</div>
#             </div>
#         </div>
#         """
#         st.markdown(progress_html, unsafe_allow_html=True)
#     else:
#         st.info("📭 No data yet")
    
#     st.markdown("---")
    
#     # Quick Actions
#     st.markdown("### ⚡ Quick Actions")
    
#     if st.button("✨ New Project", use_container_width=True, key="sidebar_new"):
#         st.rerun()
    
#     if not df.empty:
#         csv = df.to_csv(index=False)
#         st.download_button(
#             label="📥 Export Data",
#             data=csv,
#             file_name=f"tws_exports_{date.today()}.csv",
#             mime="text/csv",
#             use_container_width=True,
#             key="sidebar_export"
#         )
    
#     st.markdown("---")
    
#     # Recent Activity
#     st.markdown("### 📅 Recent Activity")
#     if not df.empty and len(df) > 0:
#         try:
#             if 'Start of Project' in df.columns:
#                 df_recent = df.copy()
#                 df_recent['Start of Project'] = pd.to_datetime(df_recent['Start of Project'], errors='coerce')
#                 recent = df_recent.sort_values('Start of Project', ascending=False).head(3)
#             else:
#                 recent = df.head(3)
            
#             for _, row in recent.iterrows():
#                 project_code = str(row.get('Project Code', 'N/A'))
#                 platform = str(row.get('Platform', 'N/A'))
#                 st.markdown(f"""
#                 <div style="background: rgba(59, 130, 246, 0.05); 
#                             padding: 12px; border-radius: 8px; margin: 8px 0;">
#                     <div style="font-weight: 600; color: #1d4ed8;">{project_code}</div>
#                     <div style="font-size: 12px; color: #6b7280;">{platform}</div>
#                 </div>
#                 """, unsafe_allow_html=True)
#         except:
#             st.info("No recent activity")















# import streamlit as st
# import pandas as pd
# from datetime import date
# import plotly.express as px
# import plotly.graph_objects as go
# from io import StringIO
# import streamlit.components.v1 as components

# # ================= CONFIG =================
# st.set_page_config(
#     page_title="TWS Project – Exports",

#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# DATA_FILE = "tws_exports.csv"

# COLUMNS = [
#     "Email","Project Code","Project Description","Start of Project","Platform",
#     "Continent/Country","SCR No","SCR Issue in CFT","Model","Aggregate",
#     "Aggregate Lead","Implementation Month","R&D PMO","Feasibility Uploaded",
#     "G1 Drg Release","Material Avl","Proto Fitment","Testing Start",
#     "Interim Testing Go Ahead","G1 ORC Drg","G1 ORC Material","G1 ORC Proto",
#     "G2 Go Ahead","G2 Material","5 Tractors Online","PRR Sign-off",
#     "Pre ERN","Go Ahead ERN","BOM Change","BCR Number","BCR Date","Cut-off Number"
# ]

# # ================= CLEAN WHITE STYLE WITH BLUE THEME =================
# st.markdown("""
# <style>
#     /* White Background Theme */
#     .stApp {
#         background-color: #ffffff !important;
#     }
    
#     /* Blue Headers */
#     h1, h2, h3, h4, h5, h6 {
#         color: #1a56db !important;
#         font-weight: 700 !important;
#         font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
#     }
    
#     /* Blue Labels and Text */
#     label, span, p, div {
#         color: #1e40af !important;
#     }
    
#     /* Dataframe Styling */
#     .stDataFrame {
#         border: 2px solid #1d4ed8 !important;
#         border-radius: 10px !important;
#     }
    
#     /* Blue Input Fields */
#     input, textarea, select {
#         background-color: #ffffff !important;
#         color: #1e40af !important;
#         border: 1px solid #3b82f6 !important;
#         border-radius: 8px !important;
#     }
    
#     /* Blue Buttons */
#     .stButton > button {
#         background: linear-gradient(135deg, #2563eb, #1d4ed8) !important;
#         color: white !important;
#         border: none !important;
#         border-radius: 8px !important;
#         font-weight: 600 !important;
#         padding: 10px 24px !important;
#         transition: all 0.3s ease !important;
#     }
    
#     .stButton > button:hover {
#         background: linear-gradient(135deg, #1d4ed8, #1e40af) !important;
#         transform: translateY(-2px) !important;
#         box-shadow: 0 4px 12px rgba(29, 78, 216, 0.3) !important;
#     }
    
#     /* Tab Styling */
#     .stTabs [data-baseweb="tab-list"] {
#         gap: 8px;
#     }
    
#     .stTabs [data-baseweb="tab"] {
#         background-color: #ffffff !important;
#         color: #1e40af !important;
#         border: 1px solid #dbeafe !important;
#         border-radius: 8px 8px 0 0 !important;
#         padding: 12px 24px !important;
#     }
    
#     .stTabs [data-baseweb="tab"][aria-selected="true"] {
#         background-color: #dbeafe !important;
#         color: #1d4ed8 !important;
#         border-bottom: 3px solid #2563eb !important;
#     }
    
#     /* Metrics Styling */
#     [data-testid="stMetric"] {
#         background-color: #f0f9ff !important;
#         padding: 20px !important;
#         border-radius: 12px !important;
#         border: 1px solid #bae6fd !important;
#     }
    
#     [data-testid="stMetricLabel"], [data-testid="stMetricValue"], [data-testid="stMetricDelta"] {
#         color: #1e40af !important;
#     }
    
#     /* Radio Buttons */
#     .stRadio > div {
#         background-color: #f8fafc !important;
#         padding: 15px !important;
#         border-radius: 10px !important;
#         border: 1px solid #e2e8f0 !important;
#     }
    
#     /* File Uploader */
#     .stFileUploader > div {
#         background-color: #f8fafc !important;
#         border: 2px dashed #93c5fd !important;
#         border-radius: 10px !important;
#         padding: 20px !important;
#     }
    
#     /* Success/Error Messages */
#     .stAlert {
#         border-radius: 8px !important;
#         border: 1px solid !important;
#     }
    
#     /* Sidebar Styling */
#     section[data-testid="stSidebar"] {
#         background-color: #f8fafc !important;
#     }
    
#     /* Table Styling */
#     .dataframe {
#         background-color: #ffffff !important;
#         color: #1e40af !important;
#     }
    
#     /* Select Box */
#     div[data-baseweb="select"] > div {
#         background-color: #ffffff !important;
#         color: #1e40af !important;
#         border: 1px solid #3b82f6 !important;
#     }
    
#     /* Checkbox */
#     .stCheckbox > label {
#         color: #1e40af !important;
#     }
    
#     /* Divider */
#     hr {
#         border-color: #dbeafe !important;
#     }
    
#     /* Card-like containers */
#     .st-expander {
#         background-color: #f8fafc !important;
#         border: 1px solid #dbeafe !important;
#         border-radius: 10px !important;
#     }
    
#     /* Blue Scrollbar */
#     ::-webkit-scrollbar {
#         width: 8px;
#         height: 8px;
#     }
    
#     ::-webkit-scrollbar-track {
#         background: #f1f5f9;
#         border-radius: 4px;
#     }
    
#     ::-webkit-scrollbar-thumb {
#         background: linear-gradient(135deg, #3b82f6, #1d4ed8);
#         border-radius: 4px;
#     }
    
#     ::-webkit-scrollbar-thumb:hover {
#         background: #1d4ed8;
#     }
    
#     /* Status Badges */
#     .status-badge {
#         display: inline-block;
#         padding: 4px 12px;
#         border-radius: 20px;
#         font-size: 12px;
#         font-weight: 600;
#     }
    
#     .status-complete {
#         background-color: #dcfce7;
#         color: #166534;
#     }
    
#     .status-pending {
#         background-color: #fef3c7;
#         color: #92400e;
#     }
    
#     .status-progress {
#         background-color: #dbeafe;
#         color: #1e40af;
#     }
# </style>
# """, unsafe_allow_html=True)

# # ================= LOAD / SAVE =================
# def load_data():
#     try:
#         df = pd.read_csv(DATA_FILE)
#         # Ensure Project Code is string type
#         if 'Project Code' in df.columns:
#             df['Project Code'] = df['Project Code'].astype(str)
#         return df
#     except:
#         return pd.DataFrame(columns=COLUMNS)

# def save_data(df):
#     # Ensure Project Code is string before saving
#     if 'Project Code' in df.columns:
#         df['Project Code'] = df['Project Code'].astype(str)
#     df.to_csv(DATA_FILE, index=False)

# df = load_data()

# # ================= LOTTIE ANIMATION =================
# def display_lottie_animation():
#     lottie_html = """
#     <script src="https://unpkg.com/@lottiefiles/dotlottie-wc@0.8.11/dist/dotlottie-wc.js" type="module"></script>
#     <dotlottie-wc src="https://lottie.host/8dd2e6af-9e9a-4464-ad99-41e7c2a723e2/AzY19wIzNy.lottie" style="width: 100px; height: 100px" autoplay loop></dotlottie-wc>
#     """
#     components.html(lottie_html, height=120)

# # ================= PROFESSIONAL DASHBOARD =================
# def create_dashboard():
#     st.markdown("### 📊 Project Analytics Dashboard")
    
#     # Display Lottie Animation in a nice layout
#     col1, col2, col3 = st.columns([1, 2, 1])
#     with col2:
#         display_lottie_animation()
    
#     # Metrics Row
#     col1, col2, col3, col4 = st.columns(4)
    
#     with col1:
#         total_projects = len(df)
#         st.metric(
#             "Total Projects", 
#             total_projects,
#             delta=f"+{len(df[df['Start of Project'] == pd.Timestamp(date.today()).strftime('%Y-%m-%d')])} today" if total_projects > 0 else None
#         )
    
#     with col2:
#         g1_completed = df["G1 Drg Release"].notna().sum()
#         completion_rate = (g1_completed / total_projects * 100) if total_projects > 0 else 0
#         st.metric(
#             "G1 Completed", 
#             g1_completed,
#             delta=f"{completion_rate:.1f}%",
#             delta_color="normal"
#         )
    
#     with col3:
#         g2_completed = df["G2 Go Ahead"].notna().sum()
#         g2_rate = (g2_completed / total_projects * 100) if total_projects > 0 else 0
#         st.metric(
#             "G2 Completed", 
#             g2_completed,
#             delta=f"{g2_rate:.1f}%"
#         )
    
#     with col4:
#         active_projects = len(df[df['Implementation Month'].str.strip().str.lower() == pd.Timestamp.now().strftime('%b').lower()]) if 'Implementation Month' in df.columns else 0
#         st.metric(
#             "Active This Month", 
#             active_projects
#         )
    
#     st.markdown("---")
    
#     # Charts Row
#     if not df.empty:
#         col1, col2 = st.columns(2)
        
#         with col1:
#             if 'Platform' in df.columns:
#                 platform_counts = df['Platform'].value_counts()
#                 fig = go.Figure(data=[
#                     go.Bar(
#                         x=platform_counts.index,
#                         y=platform_counts.values,
#                         marker_color='#2563eb',
#                         text=platform_counts.values,
#                         textposition='auto',
#                     )
#                 ])
#                 fig.update_layout(
#                     title='Projects by Platform',
#                     paper_bgcolor='white',
#                     plot_bgcolor='white',
#                     font=dict(color='#1e40af'),
#                     height=400
#                 )
#                 st.plotly_chart(fig, use_container_width=True)
        
#         with col2:
#             if 'Aggregate' in df.columns:
#                 aggregate_counts = df['Aggregate'].value_counts()
#                 fig = go.Figure(data=[
#                     go.Pie(
#                         labels=aggregate_counts.index,
#                         values=aggregate_counts.values,
#                         hole=.3,
#                         marker=dict(colors=['#2563eb', '#1d4ed8', '#1e40af', '#3730a3', '#312e81']),
#                     )
#                 ])
#                 fig.update_layout(
#                     title='Projects by Aggregate Type',
#                     paper_bgcolor='white',
#                     plot_bgcolor='white',
#                     font=dict(color='#1e40af'),
#                     height=400
#                 )
#                 st.plotly_chart(fig, use_container_width=True)
    
#     # Recent Projects Table
#     st.markdown("### 📋 Recent Projects")
#     if not df.empty and len(df) > 0:
#         if 'Start of Project' in df.columns:
#             try:
#                 # Try to convert to datetime for sorting
#                 df_display = df.copy()
#                 df_display['Start of Project'] = pd.to_datetime(df_display['Start of Project'], errors='coerce')
#                 recent_df = df_display.sort_values('Start of Project', ascending=False).head(10)
#             except:
#                 recent_df = df.head(10)
#         else:
#             recent_df = df.head(10)
        
#         display_cols = ['Project Code', 'Project Description', 'Platform', 'Aggregate', 'Aggregate Lead', 'Implementation Month']
#         display_cols = [col for col in display_cols if col in recent_df.columns]
        
#         st.dataframe(
#             recent_df[display_cols],
#             width='stretch'
#         )
#     else:
#         st.info("No projects available. Add your first project in the Data Entry tab.")

# # ================= MAIN =================
# # Header with Lottie Animation
# col1, col2 = st.columns([1, 4])
# with col1:
#     display_lottie_animation()
# with col2:
#     st.title("TWS Project – Exports Management")
#     st.markdown("**Professional Project Tracking System**")

# tab1, tab2, tab3 = st.tabs(["📝 Data Entry Form", "📊 Dashboard", "📁 Data Management"])

# # ================= FORM TAB =================
# with tab1:
#     st.markdown("### ✨ New Project Entry")
    
#     with st.form("tws_form"):
#         col1, col2 = st.columns(2)
        
#         with col1:
#             email = st.text_input("📧 Email *", placeholder="user@company.com")
#             project_code = st.text_input("🔢 Project Code *", placeholder="PRJ-XXXX-YY")
#             project_desc = st.text_area("📝 Project Description *", height=100)
#             start_project = st.date_input("📅 Start of Project", date.today())
#             platform = st.selectbox(
#                 "🖥️ Platform",
#                 ["Below 30 HP", "30–60 HP", "60–101 HP", "Above 101 HP"]
#             )
#             continent = st.text_input("🌍 Continent / Country", placeholder="North America / USA")
#             scr_no = st.text_input("📄 SCR Number", placeholder="SCR-XXXX")
            
#         with col2:
#             scr_issue = st.text_input("🔧 SCR Issue in CFT", placeholder="Issue discussed in cross-functional team")
#             model = st.text_input("🚜 Model", placeholder="Model name/number")
#             aggregate = st.selectbox(
#                 "🔩 Aggregate",
#                 ["Electrical", "Hydraulic", "Transmission", "Engine", "Vehicle", "Cabin"]
#             )
#             agg_lead = st.text_input("👨‍💼 Aggregate Lead", placeholder="Lead person name")

#             imp_month = st.date_input("📅 Implementation Month", date.today())
#             # impl_month = st.selectbox(
#             #     "📆 Implementation Month",
#             #     ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
#             # )
#             r_and_d = st.selectbox(
#                 "🔬 R&D PMO",
#                 ["Mohit Rana", "Arashdeep Parmar"]
#             )
        
#         st.markdown("---")
#         st.markdown("#### 📎 Documents & Timeline")
        
#         col1, col2 = st.columns(2)
        
#         with col1:
#             feasibility = st.file_uploader("📎 Feasibility Study", type=['pdf', 'docx', 'doc'])
#             g1 = st.date_input("📐 G1 Drg Release")
#             material = st.date_input("📦 Material Avl")
#             proto = st.date_input("🔧 Proto Fitment")
#             testing = st.date_input("🧪 Testing Start")
#             interim = st.date_input("✅ Interim Testing Go Ahead")
            
#         with col2:
#             g1_orc_drg = st.date_input("🔄 G1 ORC Drg")
#             g1_orc_mat = st.date_input("📦 G1 ORC Material")
#             g1_orc_proto = st.date_input("🔧 G1 ORC Proto")
#             g2_go = st.date_input("🚀 G2 Go Ahead")
#             g2_mat = st.date_input("📦 G2 Material")
        
#         st.markdown("---")
#         st.markdown("#### 🏭 Production & Approvals")
        
#         col1, col2, col3 = st.columns(3)
        
#         with col1:
#             bcr_no = st.text_input("🔢 BCR Number", placeholder="Reference")
            
#         # with col3:
#             bcr_date = st.date_input("📅 BCR Date")
#             cutoff = st.text_input("✂️ Cut-off Number", placeholder="Reference")
        
#         submit = st.form_submit_button("🚀 Submit Project", use_container_width=True)
    
#     if submit:
#         if not email or not project_code or not project_desc:
#             st.error("❌ Please fill all required fields (*)")
#         else:
#             # Check if project code already exists
#             project_code_str = str(project_code)
#             if not df.empty and 'Project Code' in df.columns:
#                 df['Project Code'] = df['Project Code'].astype(str)
#                 if project_code_str in df['Project Code'].values:
#                     st.warning("⚠️ Project Code already exists! Updating existing record...")
#                     idx = df[df['Project Code'] == project_code_str].index[0]
#                     update_record = True
#                 else:
#                     idx = len(df)
#                     update_record = False
#             else:
#                 update_record = False
            
#             # Prepare data with proper date handling
#             def format_date(date_val):
#                 if pd.isna(date_val) or date_val is None:
#                     return ""
#                 return date_val.strftime('%Y-%m-%d') if hasattr(date_val, 'strftime') else str(date_val)
            
#             new_data = {
#                 "Email": str(email),
#                 "Project Code": project_code_str,
#                 "Project Description": str(project_desc),
#                 "Start of Project": format_date(start_project),
#                 "Platform": str(platform),
#                 "Continent/Country": str(continent),
#                 "SCR No": str(scr_no),
#                 "SCR Issue in CFT": str(scr_issue),
#                 "Model": str(model),
#                 "Aggregate": str(aggregate),
#                 "Aggregate Lead": str(agg_lead),
#                 # "Implementation Month": str(impl_month),
#                 "R&D PMO": str(r_and_d),
#                 "Feasibility Uploaded": feasibility.name if feasibility else "",
#                 "G1 Drg Release": format_date(g1),
#                 "Material Avl": format_date(material),
#                 "Proto Fitment": format_date(proto),
#                 "Testing Start": format_date(testing),
#                 "Interim Testing Go Ahead": format_date(interim),
#                 "G1 ORC Drg": format_date(g1_orc_drg),
#                 "G1 ORC Material": format_date(g1_orc_mat),
#                 "G1 ORC Proto": format_date(g1_orc_proto),
#                 "G2 Go Ahead": format_date(g2_go),
#                 "G2 Material": format_date(g2_mat),
#                 # "5 Tractors Online": str(tractors),
#                 # "PRR Sign-off": str(prr),
#                 # "Pre ERN": str(pre_ern),
#                 # "Go Ahead ERN": str(go_ern),
#                 # "BOM Change": str(bom),
#                 "BCR Number": str(bcr_no),
#                 "BCR Date": format_date(bcr_date),
#                 "Cut-off Number": str(cutoff)
#             }
            
#             if update_record:
#                 for key, value in new_data.items():
#                     if key in df.columns:
#                         df.at[idx, key] = value
#                 st.success(f"✅ Project {project_code} updated successfully!")
#             else:
#                 # Ensure all columns exist
#                 for col in COLUMNS:
#                     if col not in new_data:
#                         new_data[col] = ""
                
#                 df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
#                 st.success(f"✅ New project {project_code} added successfully!")
            
#             save_data(df)
#             df = load_data()

# # ================= DASHBOARD TAB =================
# with tab2:
#     create_dashboard()

# # ================= DATA MANAGEMENT TAB =================
# with tab3:
#     st.markdown("### 📁 Data Management Center")
    
#     # Display Lottie Animation
#     col1, col2, col3 = st.columns([1, 2, 1])
#     with col2:
#         display_lottie_animation()
    
#     # Tabs for different data management operations
#     mgmt_tab1, mgmt_tab2, mgmt_tab3 = st.tabs(["📊 View & Edit All Data", "📤 Import from Google Sheets", "⚙️ Bulk Operations"])
    
#     with mgmt_tab1:
#         st.markdown("#### 📋 Complete Project Database")
        
#         if not df.empty and len(df) > 0:
#             # Search and Filter
#             col1, col2 = st.columns([3, 1])
#             with col1:
#                 search_term = st.text_input("🔍 Search across all columns:", placeholder="Type to search...", key="search_all")
            
#             # Show all columns by default
#             show_cols = st.multiselect(
#                 "Filter Columns:",
#                 options=df.columns.tolist(),
#                 default=df.columns.tolist()[:min(8, len(df.columns))] if len(df.columns) > 8 else df.columns.tolist(),
#                 key="filter_cols"
#             )
            
#             # Display dataframe with search
#             if search_term:
#                 mask = df.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)
#                 display_df = df[mask]
#             else:
#                 display_df = df
            
#             if not show_cols:
#                 show_cols = df.columns.tolist()
            
#             st.markdown(f"**Showing {len(display_df)} of {len(df)} records**")
            
#             # Display data - NOT editable for now to avoid errors
#             st.dataframe(
#                 display_df[show_cols],
#                 width='stretch'
#             )
            
#             # Action buttons
#             col1, col2, col3 = st.columns(3)
            
#             with col1:
#                 if st.button("🔄 Refresh Data", use_container_width=True, key="refresh_all"):
#                     df = load_data()
#                     st.rerun()
            
#             with col2:
#                 if st.button("📥 Export to CSV", use_container_width=True, key="export_csv"):
#                     csv = df.to_csv(index=False)
#                     st.download_button(
#                         label="⬇️ Download CSV",
#                         data=csv,
#                         file_name=f"tws_exports_{date.today()}.csv",
#                         mime="text/csv",
#                         use_container_width=True
#                     )
            
#             with col3:
#                 # Delete individual record
#                 if not df.empty:
#                     project_to_delete = st.selectbox(
#                         "Select project to delete:",
#                         options=df['Project Code'].astype(str).tolist(),
#                         key="delete_select"
#                     )
                    
#                     if st.button("🗑️ Delete Selected", use_container_width=True, key="delete_btn"):
#                         df = df[df['Project Code'].astype(str) != project_to_delete]
#                         save_data(df)
#                         st.success(f"✅ Project {project_to_delete} deleted successfully!")
#                         st.rerun()
#         else:
#             st.info("📭 No data available. Add your first project or import data.")
    
#     with mgmt_tab2:
#         st.markdown("#### 📤 Import from Google Sheets/CSV")
#         st.info("Upload a CSV file exported from Google Sheets to update your database.")
        
#         uploaded_file = st.file_uploader(
#             "Choose a CSV file",
#             type=['csv'],
#             help="Upload CSV file with matching column names",
#             key="csv_uploader"
#         )
        
#         if uploaded_file is not None:
#             try:
#                 # Read uploaded file
#                 new_data = pd.read_csv(uploaded_file)
                
#                 # Show preview
#                 st.markdown("##### 📄 File Preview (First 5 rows):")
#                 st.dataframe(new_data.head(), width='stretch')
                
#                 st.markdown(f"**File contains {len(new_data)} rows and {len(new_data.columns)} columns**")
                
#                 # Check for required columns
#                 if 'Project Code' not in new_data.columns:
#                     st.error("❌ CSV must contain 'Project Code' column!")
#                 else:
#                     # Show column mapping
#                     st.markdown("##### 🔄 Column Mapping")
#                     mapping_df = pd.DataFrame({
#                         'CSV Columns': new_data.columns,
#                         'Database Columns': [col if col in COLUMNS else '❌ No match' for col in new_data.columns]
#                     })
#                     st.dataframe(mapping_df, width='stretch')
                    
#                     # Import options
#                     st.markdown("##### ⚙️ Import Options")
                    
#                     import_mode = st.radio(
#                         "Select import mode:",
#                         ["Update Existing & Add New", "Replace Entire Database", "Add New Only"],
#                         key="import_mode"
#                     )
                    
#                     conflict_resolution = st.radio(
#                         "If project exists:",
#                         ["Update with new data", "Keep existing data", "Skip record"],
#                         key="conflict_res"
#                     )
                    
#                     if st.button("🚀 Process Import", use_container_width=True, key="process_import"):
#                         with st.spinner("Processing import..."):
#                             if import_mode == "Replace Entire Database":
#                                 df = new_data
#                                 save_data(df)
#                                 st.success("✅ Database replaced successfully!")
                            
#                             else:
#                                 updated_count = 0
#                                 added_count = 0
#                                 skipped_count = 0
                                
#                                 # Ensure Project Code is string
#                                 new_data['Project Code'] = new_data['Project Code'].astype(str)
#                                 if not df.empty:
#                                     df['Project Code'] = df['Project Code'].astype(str)
                                
#                                 for idx, row in new_data.iterrows():
#                                     project_code = str(row.get('Project Code', ''))
                                    
#                                     if not df.empty and project_code in df['Project Code'].values:
#                                         # Update existing
#                                         if import_mode == "Update Existing & Add New":
#                                             if conflict_resolution == "Update with new data":
#                                                 db_idx = df[df['Project Code'] == project_code].index[0]
#                                                 for col in new_data.columns:
#                                                     if col in df.columns and pd.notna(row[col]):
#                                                         df.at[db_idx, col] = row[col]
#                                                 updated_count += 1
#                                             elif conflict_resolution == "Skip record":
#                                                 skipped_count += 1
#                                             else:  # Keep existing data
#                                                 skipped_count += 1
#                                     else:
#                                         # Add new
#                                         if import_mode in ["Update Existing & Add New", "Add New Only"]:
#                                             new_row = {}
#                                             for col in COLUMNS:
#                                                 if col in new_data.columns:
#                                                     new_row[col] = row[col] if pd.notna(row.get(col)) else ""
#                                                 else:
#                                                     new_row[col] = ""
#                                             df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
#                                             added_count += 1
                                
#                                 save_data(df)
                                
#                                 st.success(f"""
#                                 ✅ **Import Completed!**
                                
#                                 **Summary:**
#                                 - 📝 Records updated: **{updated_count}**
#                                 - ➕ New records added: **{added_count}**
#                                 - ⏭️ Records skipped: **{skipped_count}**
#                                 - 📊 Total records now: **{len(df)}**
#                                 """)
                        
#                         st.rerun()
            
#             except Exception as e:
#                 st.error(f"❌ Error reading file: {str(e)}")
    
#     with mgmt_tab3:
#         st.markdown("#### ⚙️ Bulk Operations")
        
#         col1, col2 = st.columns(2)
        
#         with col1:
#             st.markdown("##### 🗑️ Delete Operations")
            
#             if not df.empty:
#                 # Delete by project code
#                 st.markdown("**Delete by Project Code:**")
#                 projects_to_delete = st.multiselect(
#                     "Select projects to delete:",
#                     options=df['Project Code'].astype(str).tolist(),
#                     help="Select projects to delete",
#                     key="bulk_delete"
#                 )
                
#                 if projects_to_delete and st.button("🗑️ Delete Selected Projects", use_container_width=True, key="bulk_delete_btn"):
#                     df = df[~df['Project Code'].astype(str).isin(projects_to_delete)]
#                     save_data(df)
#                     st.success(f"✅ Deleted {len(projects_to_delete)} projects!")
#                     st.rerun()
                
#                 # Delete duplicates
#                 st.markdown("**Clean Duplicates:**")
#                 if st.button("🔍 Find & Remove Duplicates", use_container_width=True, key="remove_dups"):
#                     if not df.empty and 'Project Code' in df.columns:
#                         duplicates = df.duplicated(subset=['Project Code'], keep='first')
#                         if duplicates.any():
#                             st.warning(f"Found {duplicates.sum()} duplicate project codes!")
#                             df = df.drop_duplicates(subset=['Project Code'], keep='first')
#                             save_data(df)
#                             st.success("✅ Duplicates removed!")
#                         else:
#                             st.info("✅ No duplicates found!")
        
#         with col2:
#             st.markdown("##### 🔄 Batch Update")
            
#             if not df.empty:
#                 st.markdown("**Update Field for Multiple Projects:**")
#                 update_field = st.selectbox(
#                     "Select field to update:",
#                     options=[col for col in df.columns if col not in ['Project Code', 'Email']],
#                     key="batch_field"
#                 )
                
#                 update_value = st.text_input(f"New value for {update_field}:", placeholder="Enter new value...", key="batch_value")
                
#                 projects_to_update = st.multiselect(
#                     "Select projects to update:",
#                     options=df['Project Code'].astype(str).tolist(),
#                     key="batch_projects"
#                 )
                
#                 if update_value and projects_to_update and st.button("🔄 Apply Batch Update", use_container_width=True, key="batch_update_btn"):
#                     df.loc[df['Project Code'].astype(str).isin(projects_to_update), update_field] = update_value
#                     save_data(df)
#                     st.success(f"✅ Updated {len(projects_to_update)} projects!")
#                     st.rerun()
        
#         st.markdown("---")
#         st.markdown("##### 🚨 Database Management")
        
#         col1, col2, col3 = st.columns(3)
        
#         with col1:
#             if st.button("📊 Backup Database", use_container_width=True, key="backup_btn"):
#                 backup_file = f"tws_backup_{date.today()}.csv"
#                 df.to_csv(backup_file, index=False)
#                 st.success(f"✅ Backup saved as {backup_file}")
        
#         with col2:
#             if st.button("🧹 Clear All Data", use_container_width=True, key="clear_all"):
#                 confirm = st.checkbox("⚠️ I understand this will delete ALL data permanently", key="confirm_clear")
#                 if confirm:
#                     df = pd.DataFrame(columns=COLUMNS)
#                     save_data(df)
#                     st.error("🗑️ All data cleared!")
#                     st.rerun()
        
#         with col3:
#             if st.button("🔍 Validate Data", use_container_width=True, key="validate_btn"):
#                 if not df.empty:
#                     # Check for missing required fields
#                     missing_email = df['Email'].isna().sum() if 'Email' in df.columns else 0
#                     missing_code = df['Project Code'].isna().sum() if 'Project Code' in df.columns else 0
                    
#                     if missing_email + missing_code == 0:
#                         st.success("✅ All data is valid!")
#                     else:
#                         st.warning(f"""
#                         ⚠️ **Data Issues Found:**
#                         - Missing Email: {missing_email}
#                         - Missing Project Code: {missing_code}
#                         """)

# # ================= SIDEBAR =================
# with st.sidebar:
#     # Display smaller Lottie in sidebar
#     lottie_sidebar = """
#     <script src="https://unpkg.com/@lottiefiles/dotlottie-wc@0.8.11/dist/dotlottie-wc.js" type="module"></script>
#     <dotlottie-wc src="https://lottie.host/8dd2e6af-9e9a-4464-ad99-41e7c2a723e2/AzY19wIzNy.lottie" style="width: 80px; height: 80px" autoplay loop></dotlottie-wc>
#     """
#     components.html(lottie_sidebar, height=100)
    
#     st.markdown("### TWS Exports")
#     st.markdown("**Project Management**")
    
#     st.markdown("---")
    
#     st.markdown("### 📈 Quick Stats")
#     if not df.empty and len(df) > 0:
#         total_projects = len(df)
#         active_this_month = len(df[df['Implementation Month'].str.strip().str.lower() == pd.Timestamp.now().strftime('%b').lower()]) if 'Implementation Month' in df.columns else 0
#         g1_complete = df['G1 Drg Release'].notna().sum() if 'G1 Drg Release' in df.columns else 0
        
#         st.metric("Total Projects", total_projects)
#         st.metric("Active This Month", active_this_month)
#         st.metric("G1 Complete", g1_complete)
#     else:
#         st.info("No data yet")
    
#     st.markdown("---")
    
#     st.markdown("### ⚡ Quick Actions")
#     if st.button("➕ Add New Project", use_container_width=True, key="sidebar_new"):
#         # This will focus on the form tab
#         st.session_state.current_tab = "📝 Data Entry Form"
#         st.rerun()
    
#     if not df.empty:
#         csv = df.to_csv(index=False)
#         st.download_button(
#             label="📥 Export Data",
#             data=csv,
#             file_name="tws_exports.csv",
#             mime="text/csv",
#             use_container_width=True,
#             key="sidebar_export"
#         )
    
#     st.markdown("---")
    
#     st.markdown("### 📅 Recent Activity")
#     if not df.empty and len(df) > 0:
#         # Get recent projects
#         try:
#             if 'Start of Project' in df.columns:
#                 df_recent = df.copy()
#                 df_recent['Start of Project'] = pd.to_datetime(df_recent['Start of Project'], errors='coerce')
#                 recent = df_recent.sort_values('Start of Project', ascending=False).head(3)
#             else:
#                 recent = df.head(3)
            
#             for _, row in recent.iterrows():
#                 project_code = str(row.get('Project Code', 'N/A'))
#                 platform = str(row.get('Platform', 'N/A'))
#                 aggregate = str(row.get('Aggregate', 'N/A'))
#                 st.markdown(f"**{project_code}**")
#                 st.markdown(f"*{platform} - {aggregate}*")
#                 st.markdown("---")
#         except:
#             st.info("Could not load recent activity")
    
#     st.markdown("---")
    
#     st.markdown("#### 📊 Database Info")
#     if not df.empty:
#         st.markdown(f"""
#         - **Size:** {len(df)} records
#         - **Last Updated:** {date.today()}
#         - **Columns:** {len(df.columns)}
#         """)





















