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













# import streamlit as st
# import pandas as pd
# from datetime import date
# import plotly.express as px
# import streamlit.components.v1 as components
# import time

# # ================= CONFIG =================
# st.set_page_config(
#     page_title="TWS Project – Exports",
#     layout="wide",
#     page_icon="🚜"
# )

# DATA_FILE = "tws_exports.csv"

# COLUMNS = [
#     "Email","Project Code","Project Description","Start of Project","Platform",
#     "Continent/Country","SCR No","SCR Issue in CFT","Model","Aggregate",
#     "Aggregate Lead","Implementation Month","R&D PMO",
#     "Feasibility Study","G1 Drg Release","Material Avl","Proto Fitment",
#     "Testing Start","Interim Testing Go Ahead","G1 ORC Drg Release",
#     "G1 ORC Material Avl","G1 ORC Proto Fitment","G2 Go Ahead",
#     "G2 Material Avl","5 Tractors Making on line","PRR Sing-Off 5 nos",
#     "Pre ERN","Go Ahead ERN","BOM Change",
#     "BCR Number","BCR Date","Cut-off Number",
#     "Status","Due Date"
# ]

# # ================= STYLE =================
# st.markdown("""
# <style>
# .stApp { background:#f8fafc; font-family:Poppins,sans-serif; }
# h1,h2,h3 { font-weight:700 }
# .fired-alert{
#     background:#fee2e2;
#     color:#991b1b;
#     padding:12px;
#     border-left:5px solid #dc2626;
#     border-radius:6px;
#     margin-bottom:12px;
# }
# </style>
# """, unsafe_allow_html=True)

# # ================= HELPERS =================
# def load_data():
#     try:
#         df = pd.read_csv(DATA_FILE)
#     except:
#         df = pd.DataFrame(columns=COLUMNS)

#     for c in COLUMNS:
#         if c not in df.columns:
#             df[c] = ""

#     df = df.fillna("")

#     def fired(row):
#         if row["Status"].lower() != "completed" and row["Due Date"]:
#             try:
#                 return pd.to_datetime(row["Due Date"]).date() < date.today()
#             except:
#                 return False
#         return False

#     df["is_fired"] = df.apply(fired, axis=1)
#     return df

# def save_data(df):
#     out = df.copy()
#     if "is_fired" in out.columns:
#         out.drop(columns=["is_fired"], inplace=True)
#     out.to_csv(DATA_FILE, index=False)

# # ================= MAIN =================
# def main():
#     st.title("TWS Project Exports")

#     df = load_data()
#     fired_count = int(df["is_fired"].sum()) if not df.empty else 0

#     if fired_count:
#         st.markdown(
#             f'<div class="fired-alert">🔥 {fired_count} FIRED PROJECTS (Overdue)</div>',
#             unsafe_allow_html=True
#         )

#     tab1, tab2, tab3 = st.tabs(["📝 Form","📊 Dashboard","🗃️ Database"])

#     # ================= FORM =================
#     with tab1:
#         with st.form("project_form"):
#             st.markdown("## 📋 Basic Details")
#             c1,c2,c3 = st.columns(3)
#             email = c1.text_input("Email")
#             code = c1.text_input("Project Code")
#             desc = c1.text_area("Description")
#             start = c1.date_input("Start Date", value=None)

#             platform = c2.selectbox("Platform",["Below 30 HP","30–60 HP","60–101 HP","Above 101 HP"])
#             country = c2.text_input("Country")
#             status = c2.selectbox("Status",["Pending","In Progress","Completed"])

#             model = c3.text_input("Model")
#             owner = c3.text_input("Owner")
#             due = c3.date_input("Due Date", value=None)

#             st.markdown("## 🏗️ Milestones")
#             m1,m2,m3 = st.columns(3)
#             g1 = m1.date_input("G1 Drg Release", value=None)
#             mat = m1.date_input("Material Avl", value=None)
#             proto = m1.date_input("Proto Fitment", value=None)

#             g2 = m2.date_input("G2 Go Ahead", value=None)
#             trac = m2.date_input("5 Tractors Online", value=None)

#             prr = m3.date_input("PRR Signoff", value=None)

#             st.markdown("## 📈 Implementation")
#             i1,i2,i3 = st.columns(3)
#             bcr = i1.text_input("BCR Number")
#             bcrd = i2.date_input("BCR Date", value=None)
#             cut = i3.text_input("Cut-off Number")

#             submit = st.form_submit_button("Save Project")

#             if submit:
#                 if not email or not code:
#                     st.error("Email & Project Code required")
#                     st.stop()

#                 def f(d): return d.strftime("%Y-%m-%d") if d else ""

#                 row = {
#                     "Email":email,
#                     "Project Code":code,
#                     "Project Description":desc,
#                     "Start of Project":f(start),
#                     "Platform":platform,
#                     "Continent/Country":country,
#                     "Model":model,
#                     "Aggregate Lead":owner,
#                     "Status":status,
#                     "Due Date":f(due),
#                     "G1 Drg Release":f(g1),
#                     "Material Avl":f(mat),
#                     "Proto Fitment":f(proto),
#                     "G2 Go Ahead":f(g2),
#                     "5 Tractors Making on line":f(trac),
#                     "PRR Sing-Off 5 nos":f(prr),
#                     "BCR Number":bcr,
#                     "BCR Date":f(bcrd),
#                     "Cut-off Number":cut
#                 }

#                 if code in df["Project Code"].values:
#                     df.loc[df["Project Code"]==code, row.keys()] = row.values()
#                 else:
#                     df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)

#                 save_data(df)
#                 st.success("Saved Successfully")
#                 time.sleep(1)
#                 st.rerun()

#     # ================= DASHBOARD =================
#     with tab2:
#         if not df.empty:
#             c1,c2,c3 = st.columns(3)
#             c1.metric("Total",len(df))
#             c2.metric("Fired",fired_count)
#             c3.metric("Completed",len(df[df["Status"]=="Completed"]))

#             fig = px.bar(df["Platform"].value_counts(), title="Projects by Platform")
#             st.plotly_chart(fig, use_container_width=True)

#     # ================= DATABASE =================
#     with tab3:
#         st.subheader("Professional Database")

#         search = st.text_input("Search")
#         view = df.copy()

#         if search:
#             view = view[view.astype(str).apply(
#                 lambda x: x.str.contains(search,case=False)
#             ).any(axis=1)]

#         rows = ""
#         for _,r in view.iterrows():
#             fired = r["is_fired"]
#             stat = "FIRED" if fired else r["Status"]
#             badge = "#fee2e2" if fired else "#e2e8f0"
#             rows += f"""
#             <tr style="{'text-decoration:line-through;' if fired else ''}">
#               <td><span style="background:{badge};padding:4px 8px;border-radius:4px">{stat}</span></td>
#               <td>{r['Project Code']}</td>
#               <td>{r['Email']}</td>
#               <td>{r['Platform']}</td>
#               <td>{r['Model']}</td>
#               <td>{r['Aggregate Lead']}</td>
#               <td>{r['Due Date'] or '—'}</td>
#             </tr>
#             """

#         st.markdown(f"""
#         <table border="1" style="width:100%;border-collapse:collapse">
#         <tr><th>Status</th><th>Code</th><th>Email</th><th>Platform</th>
#             <th>Model</th><th>Owner</th><th>Due</th></tr>
#         {rows}
#         </table>
#         """, unsafe_allow_html=True)

#         st.download_button("Download CSV", view.to_csv(index=False), "tws_data.csv")

# # ================= RUN =================
# if __name__ == "__main__":
#     main()
