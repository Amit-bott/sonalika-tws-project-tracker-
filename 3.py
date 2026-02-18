# import streamlit as st
# import pandas as pd
# from datetime import date, datetime
# import plotly.express as px
# import plotly.graph_objects as go
# import streamlit.components.v1 as components
# import time

# # ================= CONFIGURATION =================
# st.set_page_config(
#     page_title="TWS Project – Exports",
#     layout="wide",
#     initial_sidebar_state="expanded",
#     page_icon="🚜"
# )

# DATA_FILE = "tws_exports.csv"

# COLUMNS = [
#     "Email", "Project Code", "Project Description", "Start of Project", "Platform",
#     "Continent/Country", "SCR No", "SCR Issue in CFT", "Model", "Aggregate",
#     "Aggregate Lead", "Implementation Month", "R&D PMO", 
#     "Feasibility Study", "G1 Drg Release", "Material Avl", "Proto Fitment", "Testing Start",
#     "Interim Testing Go Ahead", "G1 ORC Drg Release", "G1 ORC Material Avl", "G1 ORC Proto Fitment",
#     "G2 Go Ahead", "G2 Material Avl", "5 Tractors Making on line", "PRR Sing-Off 5 nos",
#     "Pre ERN", "Go Ahead ERN", "BOM Change", 
#     "BCR Number", "BCR Date", "Cut-off Number",
#     "Status", "Due Date" 
# ]

# # ================= PREMIUM CSS =================
# st.markdown("""
# <style>
#     @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;800&display=swap');

#     .stApp {
#         background: radial-gradient(circle at 10% 20%, rgb(239, 246, 255) 0%, rgb(219, 234, 254) 90%);
#         font-family: 'Poppins', sans-serif;
#     }

#     h1, h2, h3 {
#         background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
#         -webkit-background-clip: text;
#         -webkit-text-fill-color: transparent;
#         font-weight: 800 !important;
#     }

#     /* Cards */
#     div[data-testid="stMetric"], .stForm {
#         background: rgba(255, 255, 255, 0.65) !important;
#         backdrop-filter: blur(16px);
#         border: 1px solid rgba(255, 255, 255, 0.8);
#         border-radius: 20px !important;
#         box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
#     }
    
#     /* Input Fields */
#     .stTextInput input, .stDateInput input, .stSelectbox div[data-baseweb="select"] {
#         background-color: white !important;
#         border-radius: 8px !important;
#         border: 1px solid #cbd5e1 !important;
#     }
    
#     /* Fired Alert */
#     .fired-alert {
#         padding: 15px;
#         background: #fee2e2;
#         border-left: 5px solid #dc2626;
#         color: #991b1b;
#         font-weight: bold;
#         border-radius: 8px;
#         margin-bottom: 20px;
#         animation: pulse 2s infinite;
#     }
    
#     @keyframes pulse {
#         0% { box-shadow: 0 0 0 0 rgba(220, 38, 38, 0.4); }
#         70% { box-shadow: 0 0 0 10px rgba(220, 38, 38, 0); }
#         100% { box-shadow: 0 0 0 0 rgba(220, 38, 38, 0); }
#     }

# </style>
# """, unsafe_allow_html=True)

# # ================= HELPERS =================

# def load_data():
#     try:
#         df = pd.read_csv(DATA_FILE)
#         if 'Project Code' in df.columns:
#             df['Project Code'] = df['Project Code'].astype(str)
#         for col in COLUMNS:
#             if col not in df.columns:
#                 df[col] = ""
#         df = df.fillna("")
        
#         # Calculate Fired Logic
#         def check(row):
#             status = str(row.get('Status', '')).strip().lower()
#             due = str(row.get('Due Date', '')).strip()
#             if due and status != 'completed':
#                 try:
#                     if pd.to_datetime(due).date() < date.today():
#                         return True
#                 except:
#                     pass
#             return False
            
#         df['is_fired_calc'] = df.apply(check, axis=1)
#         return df
#     except:
#         return pd.DataFrame(columns=COLUMNS)

# def save_data(df):
#     try:
#         # Remove helper col if exists
#         save_df = df.copy()
#         if 'is_fired_calc' in save_df.columns:
#             del save_df['is_fired_calc']
        
#         if 'Project Code' in save_df.columns:
#             save_df['Project Code'] = save_df['Project Code'].astype(str)
            
#         for col in COLUMNS:
#             if col not in save_df.columns:
#                 save_df[col] = ""
                
#         save_df = save_df[COLUMNS]
#         save_df.to_csv(DATA_FILE, index=False)
#         return True
#     except Exception as e:
#         st.error(str(e))
#         return False

# # ================= MAIN =================

# def main():
#     # Header
#     col1, col2 = st.columns([1,5])
#     with col1:
#          # Lottie Animation
#         components.html("""
#         <script src="https://unpkg.com/@lottiefiles/dotlottie-wc@0.8.11/dist/dotlottie-wc.js" type="module"></script>
#         <dotlottie-wc src="https://lottie.host/8dd2e6af-9e9a-4464-ad99-41e7c2a723e2/AzY19wIzNy.lottie" autoplay loop style="width: 100px; height: 100px;"></dotlottie-wc>
#         """, height=120)
#     with col2:
#         st.title("TWS Project Exports")
#         st.caption("Premium Tracking System")

#     df = load_data()
    
#     # Check Fired Count
#     fired_count = 0
#     if not df.empty and 'is_fired_calc' in df.columns:
#         fired_count = df['is_fired_calc'].sum()
        
#     if fired_count > 0:
#         st.markdown(f'<div class="fired-alert">🔥 ALERT: {fired_count} Projects are FIRED (Overdue & Incomplete)</div>', unsafe_allow_html=True)

#     # Navigation
#     tab1, tab2, tab3 = st.tabs(["📝 Form", "📈 Dashboard", "🗃️ Professional Database"])

#     # === TAB 1: FORM ===
#     with tab1:
#         with st.form("main_form", clear_on_submit=False):
#             # Block 1
#             st.info("📋 **Basic Details**")
#             with st.expander("General Info", expanded=True):
#                 c1, c2, c3 = st.columns(3)
#                 email = c1.text_input("📧 Email")
#                 pcode = c1.text_input("🔢 Project Code")
#                 desc = c1.text_area("📝 Description")
#                 start = c1.date_input("📅 Start Date", value=None)
                
#                 plat = c2.selectbox("Platform", ["Below 30 HP", "30–60 HP", "60–101 HP", "Above 101 HP"])
#                 cont = c2.text_input("Continent")
#                 scr = c2.text_input("SCR No")
#                 scri = c2.text_input("SCR Issue")
                
#                 mod = c3.text_input("Model")
#                 agg = c3.selectbox("Aggregate", ["Engine", "Transmission", "Hydraulics", "Electrical", "Vehicle", "Cabin"])
#                 owner = c3.text_input("Owner / Lead")
#                 imp = c3.date_input("Imp Month", value=None)
                
#                 c2.markdown("**Status**")
#                 stat = c2.selectbox("Status", ["Pending", "In Progress", "Completed"])
#                 due = c3.date_input("Due Date", value=None)
#                 rnd = c3.selectbox("RnD PMO", ["Mohit Rana", "Arashdeep Parmar"])

#             # Block 2
#             st.success("🏗️ **Milestones**")
#             with st.expander("Milestone Tracking", expanded=True):
#                 c1, c2, c3 = st.columns(3)
#                 # G1
#                 feas = c1.file_uploader("Feasibility")
#                 g1d = c1.date_input("G1 Drg Release", value=None)
#                 mat = c1.date_input("Material Avl", value=None)
#                 pro = c1.date_input("Proto Fitment", value=None)
#                 tst = c1.date_input("Test Start", value=None)
#                 int_g = c1.date_input("Interim Go", value=None)
                
#                 # ORC / G2
#                 orc_d = c2.date_input("G1 ORC Drg", value=None)
#                 orc_m = c2.date_input("G1 ORC Mat", value=None)
#                 orc_p = c2.date_input("G1 ORC Proto", value=None)
#                 g2_g = c2.date_input("G2 Go Ahead", value=None)
#                 g2_m = c2.date_input("G2 Material", value=None)
#                 trac = c2.date_input("5 Tractors Online", value=None)
                
#                 # ERN
#                 prr = c3.date_input("PRR Signoff", value=None)
#                 pre = c3.date_input("Pre ERN", value=None)
#                 goe = c3.date_input("Go Ahead ERN", value=None)
#                 bom = c3.text_input("BOM Change")

#             # Block 3
#             st.warning("📈 **Implementation**")
#             with st.expander("Final Phase", expanded=True):
#                 x1, x2, x3 = st.columns(3)
#                 bcrn = x1.text_input("BCR No")
#                 bcrd = x2.date_input("BCR Date", value=None)
#                 cutn = x3.text_input("Cutoff No")
                
#             submitted = st.form_submit_button("🚀 Save Project")
#             if submitted:
#                 if not email or not pcode:
#                     st.error("Email and Code required!")
#                 else:
#                     def fmt(d): return d.strftime("%Y-%m-%d") if d else ""
#                     # Create dict
#                     data = {
#                         "Email": email, "Project Code": pcode, "Project Description": desc, "Start of Project": fmt(start),
#                         "Platform": plat, "Continent/Country": cont, "SCR No": scr, "SCR Issue in CFT": scri,
#                         "Model": mod, "Aggregate": agg, "Aggregate Lead": owner, "Implementation Month": fmt(imp),
#                         "R&D PMO": rnd, "Status": stat, "Due Date": fmt(due),
#                         "Feasibility Study": f"File: {feas.name}" if feas else "",
#                         "G1 Drg Release": fmt(g1d), "Material Avl": fmt(mat), "Proto Fitment": fmt(pro),
#                         "Testing Start": fmt(tst), "Interim Testing Go Ahead": fmt(int_g),
#                         "G1 ORC Drg Release": fmt(orc_d), "G1 ORC Material Avl": fmt(orc_m), "G1 ORC Proto Fitment": fmt(orc_p),
#                         "G2 Go Ahead": fmt(g2_g), "G2 Material Avl": fmt(g2_m), "5 Tractors Making on line": fmt(trac),
#                         "PRR Sing-Off 5 nos": fmt(prr), "Pre ERN": fmt(pre), "Go Ahead ERN": fmt(goe), "BOM Change": bom,
#                         "BCR Number": bcrn, "BCR Date": fmt(bcrd), "Cut-off Number": cutn
#                     }
                    
#                     # Save Logic
#                     if not df.empty and pcode in df['Project Code'].values:
#                         idx = df[df['Project Code']==pcode].index[0]
#                         for k,v in data.items(): df.at[idx,k] = v
#                         st.toast("Updated!")
#                     else:
#                         new_row = pd.DataFrame([data])
#                         df = pd.concat([df, new_row], ignore_index=True)
#                         st.toast("Created!")
                    
#                     save_data(df)
#                     time.sleep(1)
#                     st.rerun()

#     # === TAB 2: DASHBOARD (Simplified) ===
#     with tab2:
#         if not df.empty:
#             m1, m2, m3 = st.columns(3)
#             m1.metric("Total", len(df))
#             m2.metric("Fired", fired_count)
#             m3.metric("Completed", len(df[df['Status']=='Completed']))
            
#             # Simple Chart
#             st.plotly_chart(px.bar(df['Platform'].value_counts(), title="By Platform", color_discrete_sequence=['#2563eb']), use_container_width=True)

#     # === TAB 3: PROFESSIONAL TABLE ===
#     with tab3:
#         st.markdown("### 🗃️ Professional Database View")
        
#         # Search
#         term = st.text_input("🔍 Search", placeholder="Project Code, Model, etc...")
        
#         view_df = df.copy()
#         if term:
#             mask = view_df.astype(str).apply(lambda x: x.str.contains(term, case=False)).any(axis=1)
#             view_df = view_df[mask]
            
#         if not view_df.empty:
#             # HTML GENERATION
#             rows_html = ""
#             for _, row in view_df.iterrows():
#                 # Logic
#                 stat = str(row.get('Status','')).capitalize()
#                 fired = row.get('is_fired_calc', False)
                
#                 row_style = ""
#                 badge_style = "background: #e2e8f0; color: #475569;" # default grey
                
#                 # Strikethrough Logic
#                 if fired:
#                     row_style = "text-decoration: line-through; background-color: #fef2f2 !important; color: #991b1b;"
#                     badge_style = "background: #fee2e2; color: #991b1b;"
#                     stat = "FIRED"
#                 elif stat == "Completed":
#                     row_style = "text-decoration: line-through; background-color: #f8fafc; color: #94a3b8;"
#                     badge_style = "background: #dcfce7; color: #166534;"
#                 elif stat == "In progress":
#                     badge_style = "background: #dbeafe; color: #1e40af;"

#                 # Build row
#                 rows_html += f"""
#                 <tr style="{row_style}; border-bottom: 1px solid #f1f5f9; transition: all 0.2s;">
#                     <td style="padding: 12px;"><span style="{badge_style} padding: 4px 8px; border-radius: 4px; font-size: 12px; font-weight: 600;">{stat}</span></td>
#                     <td style="padding: 12px; font-weight: 600;">{row.get('Project Code','')}</td>
#                     <td style="padding: 12px;">{row.get('Email','')}</td>
#                     <td style="padding: 12px;">{row.get('Platform','')}</td>
#                     <td style="padding: 12px;">{row.get('Model','')}</td>
#                     <td style="padding: 12px;">{row.get('Aggregate Lead','')}</td>
#                     <td style="padding: 12px;">{row.get('Due Date','')}</td>
#                 </tr>
#                 """
            
#             # Full Table
#             table_html = f"""
#             <div style="overflow-x: auto; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); border: 1px solid #e2e8f0;">
#                 <table style="width: 100%; border-collapse: collapse; font-family: 'Poppins', sans-serif; font-size: 14px; background: white;">
#                     <thead style="background: linear-gradient(90deg, #1e3a8a, #2563eb); color: white;">
#                         <tr>
#                             <th style="padding: 14px; text-align: left;">Status</th>
#                             <th style="padding: 14px; text-align: left;">Code</th>
#                             <th style="padding: 14px; text-align: left;">Email</th>
#                             <th style="padding: 14px; text-align: left;">Platform</th>
#                             <th style="padding: 14px; text-align: left;">Model</th>
#                             <th style="padding: 14px; text-align: left;">Owner</th>
#                             <th style="padding: 14px; text-align: left;">Due Date</th>
#                         </tr>
#                     </thead>
#                     <tbody>
#                         {rows_html}
#                     </tbody>
#                 </table>
#             </div>
#             """
#             st.markdown(table_html, unsafe_allow_html=True)
            
#             # Export
#             st.download_button("📥 Download Data", view_df.to_csv(index=False), "data.csv")
            
#             # Bulk Delete (Optional)
#             with st.expander("Delete Options"):
#                 entry = st.text_input("Verify Code to Delete")
#                 if st.button("Delete") and entry:
#                     if entry in df['Project Code'].values:
#                         df = df[df['Project Code']!=entry]
#                         save_data(df)
#                         st.balloons()
#                         st.rerun()

# if __name__ == "__main__":
#     main()







import streamlit as st
import pandas as pd
from datetime import date
import plotly.express as px
import plotly.graph_objects as go
import streamlit.components.v1 as components
import time

# ================= CONFIGURATION =================
st.set_page_config(
    page_title="TWS Project – Exports",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🚜"
)

DATA_FILE = "tws_exports.csv"

COLUMNS = [
    "Email", "Project Code", "Project Description", "Start of Project", "Platform",
    "Continent/Country", "SCR No", "SCR Issue in CFT", "Model", "Aggregate",
    "Aggregate Lead", "Implementation Month", "R&D PMO", "Feasibility Uploaded",
    "G1 Drg Release", "Material Avl", "Proto Fitment", "Testing Start",
    "Interim Testing Go Ahead", "G1 ORC Drg", "G1 ORC Material", "G1 ORC Proto",
    "G2 Go Ahead", "G2 Material", "5 Tractors Online", "PRR Sign-off",
    "Pre ERN", "Go Ahead ERN", "BOM Change", "BCR Number", "BCR Date", "Cut-off Number"
]

# ================= PREMIUM 3D CSS & ANIMATIONS =================
st.markdown("""
<style>
    /* Import Premium Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;800&display=swap');

    /* Global Theme */
    .stApp {
        background: radial-gradient(circle at 10% 20%, rgb(239, 246, 255) 0%, rgb(219, 234, 254) 90%);
        font-family: 'Poppins', sans-serif;
    }

    /* 3D Headers with Gradient Text */
    h1, h2, h3 {
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800 !important;
        text-shadow: 2px 4px 8px rgba(30, 58, 138, 0.1);
        animation: floatIn 1s cubic-bezier(0.25, 0.46, 0.45, 0.94) both;
    }

    /* Animations */
    @keyframes floatIn {
        0% { opacity: 0; transform: translateY(30px) scale(0.95); }
        100% { opacity: 1; transform: translateY(0) scale(1); }
    }
    
    @keyframes pulseGlow {
        0% { box-shadow: 0 0 0 0 rgba(59, 130, 246, 0.4); }
        70% { box-shadow: 0 0 0 10px rgba(59, 130, 246, 0); }
        100% { box-shadow: 0 0 0 0 rgba(59, 130, 246, 0); }
    }

    /* 3D Glassmorphism Cards (Metrics & Forms) */
    div[data-testid="stMetric"], .stForm {
        background: rgba(255, 255, 255, 0.65) !important;
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.8);
        border-radius: 20px !important;
        box-shadow: 
            0 10px 30px rgba(0, 0, 0, 0.08), 
            0 4px 8px rgba(0, 0, 0, 0.04), 
            inset 0 0 0 1px rgba(255, 255, 255, 0.5);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    
    div[data-testid="stMetric"]:hover {
        transform: translateY(-8px) rotateX(2deg);
        box-shadow: 
            0 20px 40px rgba(37, 99, 235, 0.15), 
            0 8px 16px rgba(37, 99, 235, 0.1);
        border-color: #3b82f6;
    }

    /* 3D Inputs */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stDateInput > div > div > input,
    .stSelectbox > div > div > div {
        background-color: rgba(255, 255, 255, 0.9);
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        box-shadow: inset 2px 2px 5px rgba(0,0,0,0.03), inset -2px -2px 5px rgba(255,255,255,0.8);
        transition: all 0.3s ease;
        padding: 10px;
    }
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        transform: translateY(-2px);
        box-shadow: 0 8px 16px rgba(59, 130, 246, 0.2), 0 0 0 2px #3b82f6;
        border-color: #3b82f6;
    }

    /* 3D Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #2563eb, #1d4ed8);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.8rem 1.5rem;
        font-weight: 600;
        letter-spacing: 0.5px;
        box-shadow: 0 4px 6px rgba(37, 99, 235, 0.3), 0 1px 3px rgba(37, 99, 235, 0.2);
        transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    
    .stButton > button:hover {
        transform: translateY(-4px) scale(1.02);
        box-shadow: 0 12px 20px rgba(37, 99, 235, 0.4), 0 4px 8px rgba(37, 99, 235, 0.3);
        background: linear-gradient(135deg, #3b82f6, #2563eb);
    }
    
    .stButton > button:active {
        transform: translateY(2px);
        box-shadow: 0 2px 4px rgba(37, 99, 235, 0.2);
    }

    /* Custom Tables */
    .stDataFrame {
        border-radius: 15px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        border: none;
        overflow: hidden;
    }
    
    /* Expander animation */
    .streamlit-expanderHeader {
        background-color: rgba(255,255,255,0.5);
        border-radius: 12px;
        transition: all 0.2s;
        font-weight: 600;
        color: #1e40af;
    }
    .streamlit-expanderHeader:hover {
        background-color: #f1f5f9;
        transform: translateX(5px);
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background: rgba(255,255,255,0.5);
        padding: 10px;
        border-radius: 15px;
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 10px;
        background-color: transparent;
        transition: all 0.3s;
    }
    
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background-color: #ffffff;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        color: #2563eb;
        transform: scale(1.05);
    }

</style>
""", unsafe_allow_html=True)

# ================= HELPER FUNCTIONS =================

def load_data():
    try:
        df = pd.read_csv(DATA_FILE)
        # 1. Ensure Project Code is string
        if 'Project Code' in df.columns:
            df['Project Code'] = df['Project Code'].astype(str)
        
        # 2. Fix "None" / NaN display by replacing with empty string
        df = df.fillna("")
        return df
    except FileNotFoundError:
        return pd.DataFrame(columns=COLUMNS)
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame(columns=COLUMNS)

def save_data(df):
    try:
        if 'Project Code' in df.columns:
            df['Project Code'] = df['Project Code'].astype(str)
        df.to_csv(DATA_FILE, index=False)
        return True
    except Exception as e:
        st.error(f"Error saving data: {e}")
        return False

# Sidebar Stats
def sidebar_stats(df):
    st.sidebar.markdown("---")
    st.sidebar.subheader("📊 Live Stats")
    if not df.empty:
        total = len(df)
        this_month = pd.Timestamp.now().strftime('%b')
        if 'Implementation Month' in df.columns:
             active = len(df[df['Implementation Month'].astype(str).str.contains(this_month, case=False, na=False)])
        else:
            active = 0
            
        col1, col2 = st.sidebar.columns(2)
        col1.metric("Total", total)
        col2.metric("Active", active)
        
        # Completion Bar
        if 'G1 Drg Release' in df.columns:
            completed = df['G1 Drg Release'].replace("", pd.NA).notna().sum()
            progress = completed / total if total > 0 else 0
            st.sidebar.markdown(f"**G1 Completion Rate**")
            st.sidebar.progress(progress)
            st.sidebar.caption(f"{int(progress*100)}% ({completed}/{total})")

# ================= MAIN APP =================

def main():
    # Header Section with Animation
    col_logo, col_title = st.columns([1, 4])
    with col_logo:
        # 3D Rotating Logo Effect using Lottie
        lottie_html_mini = """
        <script src="https://unpkg.com/@lottiefiles/dotlottie-wc@0.8.11/dist/dotlottie-wc.js" type="module"></script>
        <div style="filter: drop-shadow(0 10px 15px rgba(37, 99, 235, 0.3));">
            <dotlottie-wc src="https://lottie.host/8dd2e6af-9e9a-4464-ad99-41e7c2a723e2/AzY19wIzNy.lottie" autoplay loop style="width: 120px; height: 120px;"></dotlottie-wc>
        </div>
        """
        components.html(lottie_html_mini, height=140)
    
    with col_title:
        st.markdown("""
        <div style="padding-top: 30px;">
            <h1 style="margin-bottom: 0; font-size: 3rem;">TWS Project Exports</h1>
            <p style="color: #64748b; font-size: 1.2rem; font-weight: 500;">
                Premium Project Tracking Dashboard
            </p>
        </div>
        """, unsafe_allow_html=True)

    df = load_data()
    
    # Navigation Tabs
    tab_form, tab_dash, tab_data = st.tabs(["📝 Project Entry", "📈 Dashboard Analytics", "🗃️ Data Management"])

    # --- TAB 1: DATA ENTRY ---
    with tab_form:
        st.markdown("### ✨ New Project Registration")
        
        with st.form("project_form", clear_on_submit=False):
            
            # --- Section 1: Basic Information ---
            with st.expander("📌 Project Information", expanded=True):
                c1, c2, c3 = st.columns(3)
                with c1:
                    email = st.text_input("📧 Email Address *", placeholder="user@sonalika.com")
                    project_code = st.text_input("🔢 Project Code *", placeholder="e.g., PRJ-2024-001")
                with c2:
                    project_desc = st.text_area("📝 Project Description", height=100)
                with c3:
                    start_date = st.date_input("📅 Start of Project", value=None)
                    platform = st.selectbox("🖥️ Platform", ["Below 30 HP", "30–60 HP", "60–101 HP", "Above 101 HP"])
                    continent = st.text_input("🌍 Continent / Country", placeholder="e.g., North America")

            # --- Section 2: Technical Specifications ---
            with st.expander("🔧 Technical Specifications", expanded=False):
                c1, c2, c3 = st.columns(3)
                with c1:
                    model = st.text_input("🚜 Model")
                    aggregate = st.selectbox("🔩 Aggregate Type", ["Engine", "Transmission", "Hydraulics", "Electrical", "Chassis", "Cabin"])
                with c2:
                    scr_no = st.text_input("📄 SCR Number")
                    scr_issue = st.text_input("🔧 SCR Issue in CFT")
                with c3:
                    agg_lead = st.text_input("👨‍💼 Aggregate Lead")
                    # R&D Logic
                    default_rnd = "Mohit Rana"
                    if "60–101 HP" in platform:
                        default_rnd = "Arashdeep Parmar"
                    rnd_pmo = st.selectbox("🔬 R&D PMO", ["Mohit Rana", "Arashdeep Parmar"], index=0 if default_rnd == "Mohit Rana" else 1)

            # --- Section 3: G1 Milestones ---
            with st.expander("🏗️ G1 Milestones", expanded=False):
                col_a, col_b, col_c = st.columns(3)
                with col_a:
                    feasibility = st.file_uploader("📎 Feasibility Study", type=["pdf", "docx"])
                    g1_drg = st.date_input("📐 G1 Drg Release", value=None)
                with col_b:
                    mat_avl = st.date_input("📦 Material Availability", value=None)
                    proto_fit = st.date_input("🔧 Proto Fitment", value=None)
                with col_c:
                    test_start = st.date_input("🧪 Testing Start", value=None)
                    interim_go = st.date_input("✅ Interim Testing Go Ahead", value=None)
            
            # --- Section 4: ORC Milestones ---
            with st.expander("🔄 ORC Milestones", expanded=False):
                col_a, col_b, col_c = st.columns(3)
                with col_a:
                    g1_orc_drg = st.date_input("📐 G1 ORC Drg Release", value=None)
                with col_b:
                    g1_orc_mat = st.date_input("📦 G1 ORC Material Avl", value=None)
                with col_c:
                    g1_orc_proto = st.date_input("🔧 G1 ORC Proto Fitment", value=None)

            # --- Section 5: G2 & Production ---
            with st.expander("🏭 G2 & Production", expanded=False):
                col_a, col_b, col_c = st.columns(3)
                with col_a:
                    g2_go = st.date_input("🚀 G2 Go Ahead", value=None)
                    g2_mat_avl = st.date_input("📦 G2 Material Avl", value=None)
                with col_b:
                    tractors_online = st.date_input("🚜 5 Tractors Online", value=None)
                    prr_sign = st.date_input("✅ PRR Sign-off", value=None)
                with col_c:
                    imp_month = st.date_input("📅 Implementation Month", date.today())
            
            # --- Section 6: ERN & Approvals ---
            with st.expander("📋 ERN & Approvals", expanded=False):
                col_a, col_b, col_c = st.columns(3)
                with col_a:
                    pre_ern = st.date_input("📝 Pre ERN", value=None)
                    go_ahead_ern = st.date_input("✅ Go Ahead ERN", value=None)
                with col_b:
                    bom_change = st.text_input("📑 BOM Change Details")
                    bcr_no = st.text_input("🔢 BCR Number")
                with col_c:
                    bcr_date = st.date_input("📅 BCR Date", value=None)
                    cutoff_no = st.text_input("✂️ Cut-off Number")
            
            # Form Actions
            st.markdown("---")
            submitted = st.form_submit_button("🚀 Submit Project")
            
            if submitted:
                if not email or not project_code:
                    st.toast("❌ Email and Project Code are required!", icon="⚠️")
                else:
                    # Helper
                    def fmt(d): return d.strftime("%Y-%m-%d") if d else ""
                    
                    # File Handling
                    feasibility_status = ""
                    if feasibility is not None:
                        feasibility_status = "✅ Uploaded: " + feasibility.name

                    entry_data = {
                        "Email": email,
                        "Project Code": str(project_code),
                        "Project Description": project_desc,
                        "Start of Project": fmt(start_date),
                        "Platform": platform,
                        "Continent/Country": continent,
                        "SCR No": scr_no,
                        "SCR Issue in CFT": scr_issue,
                        "Model": model,
                        "Aggregate": aggregate,
                        "Aggregate Lead": agg_lead,
                        "Implementation Month": fmt(imp_month),
                        "R&D PMO": rnd_pmo,
                        "Feasibility Uploaded": feasibility_status, # SAVING STATUS, NOT RAW FILE
                        "G1 Drg Release": fmt(g1_drg),
                        "Material Avl": fmt(mat_avl),
                        "Proto Fitment": fmt(proto_fit),
                        "Testing Start": fmt(test_start),
                        "Interim Testing Go Ahead": fmt(interim_go),
                        "G1 ORC Drg": fmt(g1_orc_drg),
                        "G1 ORC Material": fmt(g1_orc_mat),
                        "G1 ORC Proto": fmt(g1_orc_proto),
                        "G2 Go Ahead": fmt(g2_go),
                        "G2 Material": fmt(g2_mat_avl),
                        "5 Tractors Online": fmt(tractors_online),
                        "PRR Sign-off": fmt(prr_sign),
                        "Pre ERN": fmt(pre_ern),
                        "Go Ahead ERN": fmt(go_ahead_ern),
                        "BOM Change": bom_change,
                        "BCR Number": bcr_no,
                        "BCR Date": fmt(bcr_date),
                        "Cut-off Number": cutoff_no
                    }
                    
                    p_code = entry_data["Project Code"]
                    
                    # Logic to Update or Append
                    if not df.empty and p_code in df['Project Code'].values:
                        idx = df[df['Project Code'] == p_code].index[0]
                        for col, val in entry_data.items():
                            if col in df.columns:
                                df.at[idx, col] = val
                        st.balloons()
                        st.toast(f"✅ Updated Project: {p_code}", icon="🔄")
                    else:
                        new_row = pd.DataFrame([entry_data])
                        df = pd.concat([df, new_row], ignore_index=True)
                        st.balloons()
                        st.toast(f"✅ Created Project: {p_code}", icon="🎉")
                    
                    save_data(df)
                    time.sleep(1.5)
                    st.rerun()

    # --- TAB 2: DASHBOARD ---
    with tab_dash:
        st.markdown("### 📊 Analytics Overview")
        if df.empty:
            st.info("No data available to generate insights.")
        else:
            # Top Metrics Row
            m1, m2, m3, m4 = st.columns(4)
            total_p = len(df)
            g2_done = df['G2 Go Ahead'].replace("", pd.NA).notna().sum() if 'G2 Go Ahead' in df.columns else 0
            
            m1.metric("Total Projects", total_p,delta="Active Database")
            m2.metric("G2 Completed", g2_done, delta=f"{int(g2_done/total_p*100)}%" if total_p else "0%")
            
            # Charts with 3D colors
            c1, c2 = st.columns(2)
            with c1:
                if 'Platform' in df.columns:
                    plat_counts = df['Platform'].value_counts().reset_index()
                    plat_counts.columns = ['Platform', 'Count']
                    fig_plat = px.bar(plat_counts, x='Platform', y='Count', 
                                      color='Count', 
                                      color_continuous_scale='Deep',
                                      title="Projects by Platform")
                    fig_plat.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font=dict(family='Poppins'))
                    st.plotly_chart(fig_plat, use_container_width=True)
            
            with c2:
                if 'Aggregate' in df.columns:
                    agg_counts = df['Aggregate'].value_counts()
                    fig_agg = go.Figure(data=[go.Pie(labels=agg_counts.index, values=agg_counts.values, hole=.4)])
                    fig_agg.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                                          marker=dict(colors=px.colors.qualitative.Prism))
                    fig_agg.update_layout(title="Aggregate Distribution", 
                                          plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font=dict(family='Poppins'))
                    st.plotly_chart(fig_agg, use_container_width=True)
            
            # Interactive Timeline
            st.markdown("#### ⏳ Recent Project Timeline")
            if 'Start of Project' in df.columns:
                try:
                    df_time = df.copy()
                    df_time['Start of Project'] = pd.to_datetime(df_time['Start of Project'], errors='coerce')
                    timeline_df = df_time.dropna(subset=['Start of Project']).sort_values('Start of Project', ascending=False).head(10)
                    if not timeline_df.empty:
                        fig_time = px.scatter(timeline_df, x='Start of Project', y='Project Code', color='Platform',
                                              title="Project Kickoff Timeline (Last 10)",
                                              size_max=20, hover_data=['Model', 'Aggregate'])
                        fig_time.update_layout(plot_bgcolor='#f1f5f9', paper_bgcolor='white', xaxis_title="Date")
                        st.plotly_chart(fig_time, use_container_width=True)
                except Exception as e:
                    pass

    # --- TAB 3: DATA MANAGEMENT ---
    with tab_data:
        st.markdown("### 🗃️ Database Records")
        
        # Action Bar
        col_search, col_export = st.columns([3, 1])
        with col_search:
            search_query = st.text_input("🔍 Search Database", placeholder="Type any keyword...")
        with col_export:
            st.write("") 
            st.write("") 
            if not df.empty:
                csv = df.to_csv(index=False)
                st.download_button("📥 Export CSV", csv, "tws_export_db.csv", "text/csv", use_container_width=True)

        # Filtered View
        if not df.empty:
            display_df = df.copy()
            if search_query:
                mask = display_df.astype(str).apply(lambda x: x.str.contains(search_query, case=False)).any(axis=1)
                display_df = display_df[mask]
            
            # Explicitly showing all formatting clean columns
            st.dataframe(
                display_df,
                use_container_width=True,
                height=500
            )
            
            st.caption(f"Showing {len(display_df)} records.")
            
            # Bulk Actions
            with st.expander("⚠️ Danger Zone: Bulk Delete"):
                del_code = st.selectbox("Select Project to Delete", [""] + list(df['Project Code'].unique()))
                if st.button("🗑️ Delete Selected Project"):
                    if del_code:
                        df = df[df['Project Code'] != del_code]
                        save_data(df)
                        st.success(f"Deleted {del_code}")
                        time.sleep(1)
                        st.rerun()

    # Sidebar Content
    with st.sidebar:
        st.markdown("### ⚙️ Tools")
        if st.checkbox("Show Raw Configuration"):
            st.json({"Theme": "Premium 3D Blue", "Version": "3.0.0", "Author": "TWS Team"})
        
        sidebar_stats(df)
        
        st.markdown("---")
        st.info("Need Help? Contact IT Dept.")

if __name__ == "__main__":
    main()