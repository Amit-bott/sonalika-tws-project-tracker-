# import streamlit as st
# import pandas as pd
# from datetime import date
# import plotly.express as px
# import plotly.graph_objects as go
# from io import StringIO

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

# # ================= ENHANCED 3D STYLE =================
# st.markdown("""
# <style>
#     /* Main background */
#     .stApp {
#         background: linear-gradient(135deg, #0b3c5d 0%, #1d2b64 25%, #0b3c5d 50%, #1d2b64 75%, #0b3c5d 100%);
#         background-size: 400% 400%;
#         animation: gradientBG 15s ease infinite;
#     }
    
#     @keyframes gradientBG {
#         0% { background-position: 0% 50% }
#         50% { background-position: 100% 50% }
#         100% { background-position: 0% 50% }
#     }
    
#     /* Headers */
#     h1, h2, h3, h4 {
#         color: #ffffff !important;
#         font-weight: 700 !important;
#         text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
#         font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
#     }
    
#     /* Cards and Containers */
#     .stTabs [data-baseweb="tab-list"] {
#         gap: 24px;
#     }
    
#     .stTabs [data-baseweb="tab"] {
#         height: 60px;
#         padding: 0 24px;
#         background: rgba(255, 255, 255, 0.1) !important;
#         border-radius: 12px !important;
#         border: 2px solid rgba(255, 255, 255, 0.2) !important;
#         backdrop-filter: blur(10px);
#         transition: all 0.3s ease !important;
#         font-weight: 600 !important;
#     }
    
#     .stTabs [data-baseweb="tab"]:hover {
#         transform: translateY(-3px) scale(1.05);
#         box-shadow: 0 10px 20px rgba(0,0,0,0.3) !important;
#         border-color: #4dabf7 !important;
#         background: rgba(77, 171, 247, 0.2) !important;
#     }
    
#     /* 3D Animated Buttons */
#     .stButton > button {
#         width: 100%;
#         height: 50px;
#         border-radius: 12px !important;
#         background: linear-gradient(145deg, #1d2b64, #0b3c5d) !important;
#         border: 2px solid rgba(77, 171, 247, 0.5) !important;
#         color: white !important;
#         font-weight: 600 !important;
#         font-size: 16px !important;
#         transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
#         position: relative !important;
#         overflow: hidden !important;
#         transform-style: preserve-3d !important;
#         perspective: 1000px !important;
#     }
    
#     .stButton > button:hover {
#         transform: translateY(-5px) rotateX(10deg) !important;
#         box-shadow: 0 15px 30px rgba(0, 0, 0, 0.4), 0 5px 15px rgba(77, 171, 247, 0.4) !important;
#         background: linear-gradient(145deg, #4dabf7, #1d2b64) !important;
#         border-color: #4dabf7 !important;
#     }
    
#     .stButton > button:active {
#         transform: translateY(-2px) rotateX(5deg) !important;
#         transition: all 0.1s !important;
#     }
    
#     .stButton > button::after {
#         content: '';
#         position: absolute;
#         top: 0;
#         left: -100%;
#         width: 100%;
#         height: 100%;
#         background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
#         transition: 0.5s;
#     }
    
#     .stButton > button:hover::after {
#         left: 100%;
#     }
    
#     /* Form inputs with 3D effect */
#     .stTextInput > div > div, .stTextArea > div > div, .stSelectbox > div > div, .stDateInput > div > div {
#         background: rgba(0, 0, 0, 0.7) !important;
#         border-radius: 10px !important;
#         border: 2px solid rgba(77, 171, 247, 0.3) !important;
#         transition: all 0.3s ease !important;
#         backdrop-filter: blur(5px);
#     }
    
#     .stTextInput > div > div:hover, .stTextArea > div > div:hover, .stSelectbox > div > div:hover {
#         transform: translateY(-2px);
#         box-shadow: 0 5px 15px rgba(77, 171, 247, 0.3) !important;
#         border-color: #4dabf7 !important;
#     }
    
#     input, textarea, select {
#         color: #ffffff !important;
#         font-weight: 500 !important;
#     }
    
#     /* Metrics styling */
#     [data-testid="stMetric"] {
#         background: rgba(255, 255, 255, 0.1) !important;
#         padding: 20px !important;
#         border-radius: 16px !important;
#         border: 1px solid rgba(255, 255, 255, 0.2) !important;
#         backdrop-filter: blur(10px);
#         transition: all 0.3s ease !important;
#     }
    
#     [data-testid="stMetric"]:hover {
#         transform: translateY(-5px) scale(1.02);
#         box-shadow: 0 10px 25px rgba(0,0,0,0.3) !important;
#         border-color: #4dabf7 !important;
#     }
    
#     /* Radio buttons styling */
#     .stRadio > div {
#         background: rgba(0, 0, 0, 0.7) !important;
#         padding: 15px !important;
#         border-radius: 12px !important;
#         border: 2px solid rgba(77, 171, 247, 0.2) !important;
#     }
    
#     /* File uploader styling */
#     .stFileUploader > div {
#         background: rgba(0, 0, 0, 0.7) !important;
#         border: 2px dashed rgba(77, 171, 247, 0.3) !important;
#         border-radius: 12px !important;
#         padding: 20px !important;
#         transition: all 0.3s ease !important;
#     }
    
#     .stFileUploader > div:hover {
#         border-color: #4dabf7 !important;
#         background: rgba(0, 0, 0, 0.8) !important;
#         transform: translateY(-3px);
#     }
    
#     /* Dataframe styling */
#     .dataframe {
#         background: rgba(0, 0, 0, 0.8) !important;
#         border-radius: 12px !important;
#         overflow: hidden !important;
#     }
    
#     /* Custom scrollbar */
#     ::-webkit-scrollbar {
#         width: 10px;
#     }
    
#     ::-webkit-scrollbar-track {
#         background: rgba(255, 255, 255, 0.1);
#         border-radius: 5px;
#     }
    
#     ::-webkit-scrollbar-thumb {
#         background: linear-gradient(45deg, #4dabf7, #1d2b64);
#         border-radius: 5px;
#     }
    
#     ::-webkit-scrollbar-thumb:hover {
#         background: linear-gradient(45deg, #1d2b64, #4dabf7);
#     }
    
#     /* Success message animation */
#     .stAlert {
#         border-radius: 12px !important;
#         animation: slideIn 0.5s ease-out !important;
#     }
    
#     @keyframes slideIn {
#         from {
#             transform: translateX(-100%);
#             opacity: 0;
#         }
#         to {
#             transform: translateX(0);
#             opacity: 1;
#         }
#     }
    
#     /* Status indicators */
#     .status-indicator {
#         display: inline-block;
#         width: 12px;
#         height: 12px;
#         border-radius: 50%;
#         margin-right: 8px;
#         animation: pulse 2s infinite;
#     }
    
#     @keyframes pulse {
#         0% { opacity: 1; }
#         50% { opacity: 0.5; }
#         100% { opacity: 1; }
#     }
    
#     .status-complete { background-color: #00ff88; box-shadow: 0 0 10px #00ff88; }
#     .status-progress { background-color: #ffcc00; box-shadow: 0 0 10px #ffcc00; }
#     .status-pending { background-color: #ff4444; box-shadow: 0 0 10px #ff4444; }
# </style>
# """, unsafe_allow_html=True)

# # ================= LOAD / SAVE =================
# def load_data():
#     try:
#         return pd.read_csv(DATA_FILE)
#     except:
#         return pd.DataFrame(columns=COLUMNS)

# def save_data(df):
#     df.to_csv(DATA_FILE, index=False)

# df = load_data()

# # ================= PROFESSIONAL DASHBOARD COMPONENTS =================
# def create_dashboard():
#     col1, col2, col3, col4 = st.columns(4)
    
#     with col1:
#         total_projects = len(df)
#         st.metric(
#             "📊 Total Projects", 
#             total_projects,
#             delta=f"{len(df[df['G1 Drg Release'].notna()])} Active",
#             help="Total number of projects with active G1 designs"
#         )
    
#     with col2:
#         g1_completed = df["G1 Drg Release"].notna().sum()
#         completion_rate = (g1_completed / total_projects * 100) if total_projects > 0 else 0
#         st.metric(
#             "✅ G1 Completed", 
#             g1_completed,
#             delta=f"{completion_rate:.1f}%",
#             delta_color="normal",
#             help="Projects with G1 design release completed"
#         )
    
#     with col3:
#         g2_completed = df["G2 Go Ahead"].notna().sum()
#         g2_rate = (g2_completed / total_projects * 100) if total_projects > 0 else 0
#         st.metric(
#             "🚀 G2 Completed", 
#             g2_completed,
#             delta=f"{g2_rate:.1f}%",
#             help="Projects with G2 go-ahead approved"
#         )
    
#     with col4:
#         active_projects = len(df[df['Implementation Month'].notna()])
#         st.metric(
#             "📅 Active This Month", 
#             active_projects,
#             delta=f"{len(df[df['PRR Sign-off'].notna()])} Signed-off",
#             help="Projects active in current month with PRR sign-offs"
#         )
    
#     # Visualization Section
#     st.markdown("---")
#     col1, col2 = st.columns(2)
    
#     with col1:
#         if not df.empty and 'Platform' in df.columns:
#             platform_counts = df['Platform'].value_counts()
#             fig = go.Figure(data=[
#                 go.Pie(
#                     labels=platform_counts.index,
#                     values=platform_counts.values,
#                     hole=.3,
#                     marker=dict(colors=['#4dabf7', '#1d2b64', '#00ff88', '#ffcc00']),
#                     textinfo='label+percent'
#                 )
#             ])
#             fig.update_layout(
#                 title='📈 Projects by Platform',
#                 title_font=dict(size=20, color='white'),
#                 paper_bgcolor='rgba(0,0,0,0)',
#                 plot_bgcolor='rgba(0,0,0,0)',
#                 font=dict(color='white'),
#                 height=400
#             )
#             st.plotly_chart(fig, use_container_width=True)
    
#     with col2:
#         if not df.empty and 'Aggregate' in df.columns:
#             aggregate_counts = df['Aggregate'].value_counts()
#             fig = go.Figure(data=[
#                 go.Bar(
#                     x=aggregate_counts.index,
#                     y=aggregate_counts.values,
#                     marker_color='#4dabf7',
#                     text=aggregate_counts.values,
#                     textposition='auto',
#                 )
#             ])
#             fig.update_layout(
#                 title='🔧 Projects by Aggregate',
#                 title_font=dict(size=20, color='white'),
#                 paper_bgcolor='rgba(0,0,0,0)',
#                 plot_bgcolor='rgba(0,0,0,0)',
#                 font=dict(color='white'),
#                 xaxis=dict(tickangle=45),
#                 height=400
#             )
#             st.plotly_chart(fig, use_container_width=True)
    
#     # Timeline visualization
#     st.markdown("### 📅 Project Timeline Overview")
#     if not df.empty and 'Start of Project' in df.columns:
#         df['Start of Project'] = pd.to_datetime(df['Start of Project'])
#         monthly_counts = df.groupby(df['Start of Project'].dt.to_period('M')).size()
        
#         col1, col2 = st.columns([3, 1])
#         with col1:
#             timeline_df = pd.DataFrame({
#                 'Month': monthly_counts.index.astype(str),
#                 'Projects': monthly_counts.values
#             })
#             fig = px.line(timeline_df, x='Month', y='Projects', markers=True)
#             fig.update_traces(line_color='#4dabf7', marker_color='#ffcc00')
#             fig.update_layout(
#                 paper_bgcolor='rgba(0,0,0,0)',
#                 plot_bgcolor='rgba(0,0,0,0)',
#                 font=dict(color='white'),
#                 height=300
#             )
#             st.plotly_chart(fig, use_container_width=True)
        
#         with col2:
#             st.markdown("#### 🎯 Status Overview")
#             status_data = {
#                 "G1 Pending": len(df[df['G1 Drg Release'].isna()]),
#                 "G1 Complete": len(df[df['G1 Drg Release'].notna()]),
#                 "G2 Pending": len(df[df['G2 Go Ahead'].isna()]),
#                 "G2 Complete": len(df[df['G2 Go Ahead'].notna()]),
#                 "Testing": len(df[df['Testing Start'].notna()]),
#                 "PRR Signed": len(df[df['PRR Sign-off'].notna()])
#             }
            
#             for status, count in status_data.items():
#                 if count > 0:
#                     status_color = "status-complete" if "Complete" in status or "Signed" in status else "status-progress"
#                     st.markdown(f'<span class="status-indicator {status_color}"></span> {status}: **{count}**', unsafe_allow_html=True)

# # ================= MAIN =================
# st.title("🚜 TWS Project – Exports Management")
# st.markdown("### *Professional Project Tracking System*")

# tab1, tab2, tab3 = st.tabs(["📝 Data Entry Form", "📊 Analytics Dashboard", "📁 Data Management"])

# # ================= FORM TAB =================
# with tab1:
#     st.markdown("### ✨ New Project Entry")
    
#     with st.form("tws_form"):
#         # Section 1: Basic Information
#         st.markdown("#### 📋 Basic Information")
#         col1, col2 = st.columns(2)
#         with col1:
#             email = st.text_input("📧 Email *", placeholder="Enter your email")
#             project_code = st.text_input("🔢 Project Code *", placeholder="PRJ-XXXX-YY")
#         with col2:
#             project_desc = st.text_area("📝 Project Description *", placeholder="Detailed description of the project")
        
#         start_project = st.date_input("📅 Start of Project", date.today(), help="Project commencement date")
        
#         # Section 2: Technical Details
#         st.markdown("#### ⚙️ Technical Specifications")
#         col1, col2 = st.columns(2)
#         with col1:
#             platform = st.radio(
#                 "Platform Category",
#                 ["Below 30 HP", "30–60 HP", "60–101 HP", "Above 101 HP"],
#                 horizontal=True
#             )
#             continent = st.text_input("🌍 Continent / Country", placeholder="e.g., North America / USA")
#             scr_no = st.text_input("📄 SCR Number", placeholder="SCR-XXXX")
#             scr_issue = st.text_input("🔧 SCR Issue in CFT", placeholder="Issue discussed in cross-functional team")
#         with col2:
#             model = st.text_input("🚜 Model", placeholder="Model name/number")
#             aggregate = st.selectbox(
#                 "🔩 Aggregate Type",
#                 ["Electrical", "Hydraulic", "Transmission", "Engine", "Vehicle", "Cabin"]
#             )
#             agg_lead = st.text_input("👨‍💼 Aggregate Lead / Project Owner", placeholder="Lead person name")
#             impl_month = st.selectbox(
#                 "📆 Implementation Month",
#                 ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
#             )
        
#         r_and_d = st.radio(
#             "🔬 R&D PMO",
#             ["Mohit Rana", "Arashdeep Parmar"],
#             horizontal=True
#         )
        
#         # Section 3: Documents & Uploads
#         st.markdown("#### 📎 Documents & Uploads")
#         feasibility = st.file_uploader(
#             "📎 Upload Feasibility Study (PDF/DOCX)",
#             type=['pdf', 'docx', 'doc'],
#             help="Upload feasibility study document"
#         )
        
#         # Section 4: Timeline
#         st.markdown("#### ⏳ Project Timeline")
#         col1, col2 = st.columns(2)
#         with col1:
#             g1 = st.date_input("📐 G1 Drg Release")
#             material = st.date_input("📦 Material Availability")
#             proto = st.date_input("🔧 Proto Fitment")
#             testing = st.date_input("🧪 Testing Start")
#             interim = st.date_input("✅ Interim Testing Go Ahead")
#         with col2:
#             g1_orc_drg = st.date_input("🔄 G1 ORC Drg Release")
#             g1_orc_mat = st.date_input("📦 G1 ORC Material Avl")
#             g1_orc_proto = st.date_input("🔧 G1 ORC Proto Fitment")
#             g2_go = st.date_input("🚀 G2 Go Ahead")
#             g2_mat = st.date_input("📦 G2 Material Avl")
        
#         # Section 5: Production & Approval
#         st.markdown("#### 🏭 Production & Approvals")
#         col1, col2 = st.columns(2)
#         with col1:
#             tractors = st.text_input("🚜 5 Tractors Making Online", placeholder="Status/Date")
#             prr = st.text_input("✅ PRR Sign-off 5 nos", placeholder="PRR status")
#             pre_ern = st.text_input("📋 Pre ERN", placeholder="Pre-ERN details")
#         with col2:
#             go_ern = st.text_input("✅ Go Ahead ERN", placeholder="Go-ahead ERN details")
#             bom = st.text_input("📊 BOM Change", placeholder="Bill of Materials changes")
#             bcr_no = st.text_input("🔢 BCR Number", placeholder="BCR reference")
        
#         bcr_date = st.date_input("📅 BCR Date")
#         cutoff = st.text_input("✂️ Cut-off Number", placeholder="Cut-off reference")
        
#         # Submit button with enhanced styling
#         submit_col1, submit_col2, submit_col3 = st.columns([1, 2, 1])
#         with submit_col2:
#             submit = st.form_submit_button(
#                 "🚀 Submit Project Data",
#                 use_container_width=True
#             )
    
#     if submit:
#         if not email or not project_code or not project_desc:
#             st.error("❌ Please fill all required fields (marked with *)")
#         else:
#             new_row = {
#                 "Email": email,
#                 "Project Code": project_code,
#                 "Project Description": project_desc,
#                 "Start of Project": start_project,
#                 "Platform": platform,
#                 "Continent/Country": continent,
#                 "SCR No": scr_no,
#                 "SCR Issue in CFT": scr_issue,
#                 "Model": model,
#                 "Aggregate": aggregate,
#                 "Aggregate Lead": agg_lead,
#                 "Implementation Month": impl_month,
#                 "R&D PMO": r_and_d,
#                 "Feasibility Uploaded": feasibility.name if feasibility else "",
#                 "G1 Drg Release": g1,
#                 "Material Avl": material,
#                 "Proto Fitment": proto,
#                 "Testing Start": testing,
#                 "Interim Testing Go Ahead": interim,
#                 "G1 ORC Drg": g1_orc_drg,
#                 "G1 ORC Material": g1_orc_mat,
#                 "G1 ORC Proto": g1_orc_proto,
#                 "G2 Go Ahead": g2_go,
#                 "G2 Material": g2_mat,
#                 "5 Tractors Online": tractors,
#                 "PRR Sign-off": prr,
#                 "Pre ERN": pre_ern,
#                 "Go Ahead ERN": go_ern,
#                 "BOM Change": bom,
#                 "BCR Number": bcr_no,
#                 "BCR Date": bcr_date,
#                 "Cut-off Number": cutoff
#             }
            
#             df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
#             save_data(df)
            
#             # Success animation and message
#             st.balloons()
#             success_msg = st.success("""
#             ✅ **Project Data Saved Successfully!**
            
#             **Details:**
#             - Project Code: **{}**
#             - Platform: **{}**
#             - Aggregate: **{}**
#             - Lead: **{}**
            
#             Data has been securely stored and is now available in the dashboard.
#             """.format(project_code, platform, aggregate, agg_lead))
            
#             # Refresh data
#             df = load_data()

# # ================= DASHBOARD TAB =================
# with tab2:
#     st.markdown("## 📊 Advanced Analytics Dashboard")
#     create_dashboard()

# # ================= DATA MANAGEMENT TAB =================
# with tab3:
#     col1, col2 = st.columns([2, 1])
    
#     with col1:
#         st.markdown("### 📋 All Project Records")
#         if not df.empty:
#             # Add search functionality
#             search_term = st.text_input("🔍 Search projects...", placeholder="Search by Project Code, Model, or Aggregate")
            
#             if search_term:
#                 filtered_df = df[df.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)]
#             else:
#                 filtered_df = df
            
#             # Display dataframe with enhanced styling
#             st.dataframe(
#                 filtered_df,
#                 use_container_width=True,
#                 height=600,
#                 hide_index=True,
#                 column_config={
#                     "Project Code": st.column_config.TextColumn("Project Code", width="medium"),
#                     "Platform": st.column_config.TextColumn("Platform", width="small"),
#                     "Aggregate": st.column_config.TextColumn("Aggregate", width="small"),
#                     "Status": st.column_config.ProgressColumn(
#                         "Progress",
#                         help="Project progress based on milestones",
#                         width="small",
#                         min_value=0,
#                         max_value=100,
#                     )
#                 }
#             )
#         else:
#             st.info("📭 No project data available. Start by adding a project in the Data Entry tab.")
    
#     with col2:
#         st.markdown("### 🔄 Data Operations")
        
#         # Download button with enhanced styling
#         st.markdown("#### 📥 Export Data")
#         if not df.empty:
#             csv_data = df.to_csv(index=False)
#             st.download_button(
#                 label="💾 Download CSV",
#                 data=csv_data,
#                 file_name="tws_exports_data.csv",
#                 mime="text/csv",
#                 help="Download all project data as CSV file",
#                 use_container_width=True
#             )
            
#             excel_data = df.to_excel(index=False)
#             st.download_button(
#                 label="📊 Download Excel",
#                 data=csv_data,  # Using CSV data for Excel conversion
#                 file_name="tws_exports_data.xlsx",
#                 mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
#                 help="Download all project data as Excel file",
#                 use_container_width=True
#             )
        
#         # Google Sheets/CSV Upload with FIXED functionality
#         st.markdown("---")
#         st.markdown("#### ☁️ Sync from Google Sheets")
        
#         uploaded_csv = st.file_uploader(
#             "📤 Upload CSV/Excel from Google Sheets",
#             type=["csv", "xlsx", "xls"],
#             help="Upload data exported from Google Sheets"
#         )
        
#         if uploaded_csv is not None:
#             try:
#                 if uploaded_csv.name.endswith('.csv'):
#                     new_df = pd.read_csv(uploaded_csv)
#                 else:
#                     new_df = pd.read_excel(uploaded_csv)
                
#                 # Show preview
#                 st.markdown("**Preview of uploaded data:**")
#                 st.dataframe(new_df.head(3), use_container_width=True)
                
#                 # Clean column names
#                 new_df.columns = [col.strip() for col in new_df.columns]
                
#                 if "Project Code" not in new_df.columns:
#                     st.error("❌ Uploaded file must contain 'Project Code' column")
#                 else:
#                     sync_btn = st.button(
#                         "🔄 Sync with Existing Data",
#                         use_container_width=True,
#                         help="Merge uploaded data with existing records"
#                     )
                    
#                     if sync_btn:
#                         # Update existing records and add new ones
#                         updated_count = 0
#                         new_count = 0
                        
#                         for _, new_row in new_df.iterrows():
#                             project_code_val = new_row.get("Project Code")
                            
#                             if project_code_val in df["Project Code"].values:
#                                 # Update existing row
#                                 idx = df[df["Project Code"] == project_code_val].index[0]
#                                 for col in new_df.columns:
#                                     if col in df.columns and pd.notna(new_row[col]):
#                                         df.at[idx, col] = new_row[col]
#                                 updated_count += 1
#                             else:
#                                 # Add new row
#                                 new_record = {col: new_row.get(col, "") for col in df.columns}
#                                 df = pd.concat([df, pd.DataFrame([new_record])], ignore_index=True)
#                                 new_count += 1
                        
#                         save_data(df)
                        
#                         # Show success message
#                         st.success(f"""
#                         ✅ **Data Sync Completed Successfully!**
                        
#                         **Summary:**
#                         - 📝 Records updated: **{updated_count}**
#                         - ➕ New records added: **{new_count}**
#                         - 📊 Total records: **{len(df)}**
                        
#                         Data has been synchronized with the database.
#                         """)
                        
#                         # Refresh the data display
#                         st.rerun()
            
#             except Exception as e:
#                 st.error(f"❌ Error processing file: {str(e)}")
#                 st.info("💡 Tip: Ensure your file has the correct format and column names match the system requirements.")
        
#         # Data management actions
#         st.markdown("---")
#         st.markdown("#### ⚙️ Database Actions")
        
#         col_act1, col_act2 = st.columns(2)
        
#         with col_act1:
#             if st.button("🔄 Refresh Data", use_container_width=True):
#                 df = load_data()
#                 st.rerun()
        
#         with col_act2:
#             if st.button("🗑️ Clear All Data", use_container_width=True):
#                 if st.checkbox("⚠️ Confirm permanent deletion of ALL data"):
#                     df = pd.DataFrame(columns=COLUMNS)
#                     save_data(df)
#                     st.error("🗑️ All data has been cleared!")
#                     st.rerun()

# # ================= SIDEBAR INFO =================
# with st.sidebar:
#     st.markdown("""
#     <div style='text-align: center; padding: 20px;'>
#         <h2 style='color: #4dabf7;'>🚜 TWS Exports</h2>
#         <p style='color: #ccc;'>Project Management System</p>
#     </div>
#     """, unsafe_allow_html=True)
    
#     st.markdown("---")
    
#     st.markdown("### 📈 Quick Stats")
#     if not df.empty:
#         st.metric("Active Projects", len(df))
#         st.metric("G1 Completion", f"{df['G1 Drg Release'].notna().sum()}/{len(df)}")
#         st.metric("G2 Completion", f"{df['G2 Go Ahead'].notna().sum()}/{len(df)}")
    
#     st.markdown("---")
    
#     st.markdown("### 🔔 Recent Activity")
#     if not df.empty:
#         recent = df.sort_values('Start of Project', ascending=False).head(3)
#         for _, row in recent.iterrows():
#             st.info(f"**{row['Project Code']}** - {row['Platform']}")
    
#     st.markdown("---")
    
#     st.markdown("### 📞 Support")
#     st.markdown("""
#     **Need help?**
#     - 📧 Email: support@tws.com
#     - 📞 Phone: +1-234-567-8900
#     - 🕐 Hours: 9 AM - 6 PM EST
#     """)
























# import streamlit as st
# import pandas as pd
# from datetime import date
# import plotly.express as px
# import plotly.graph_objects as go
# from io import StringIO
# import numpy as np

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

# #CLEAN WHITE STYLE WITH BLUE THEME 
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
#     .css-1d391kg {
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

# # LOAD / SAVE
# def load_data():
#     try:
#         return pd.read_csv(DATA_FILE)
#     except:
#         return pd.DataFrame(columns=COLUMNS)

# def save_data(df):
#     df.to_csv(DATA_FILE, index=False)

# df = load_data()

# #PROFESSIONAL DASHBOARD
# def create_dashboard():
#     st.markdown("### 📊 Project Analytics Dashboard")
    
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
#         active_projects = len(df[df['Implementation Month'] == pd.Timestamp.now().strftime('%b')])
#         st.metric(
#             "Active This Month", 
#             active_projects
#         )
    
#     st.markdown("---")
    
#     # Charts Row
#     col1, col2 = st.columns(2)
    
#     with col1:
#         if not df.empty and 'Platform' in df.columns:
#             platform_counts = df['Platform'].value_counts()
#             fig = go.Figure(data=[
#                 go.Bar(
#                     x=platform_counts.index,
#                     y=platform_counts.values,
#                     marker_color='#2563eb',
#                     text=platform_counts.values,
#                     textposition='auto',
#                 )
#             ])
#             fig.update_layout(
#                 title='Projects by Platform',
#                 paper_bgcolor='white',
#                 plot_bgcolor='white',
#                 font=dict(color='#1e40af'),
#                 height=400
#             )
#             st.plotly_chart(fig, use_container_width=True)
    
#     with col2:
#         if not df.empty and 'Aggregate' in df.columns:
#             aggregate_counts = df['Aggregate'].value_counts()
#             fig = go.Figure(data=[
#                 go.Pie(
#                     labels=aggregate_counts.index,
#                     values=aggregate_counts.values,
#                     hole=.3,
#                     marker=dict(colors=['#2563eb', '#1d4ed8', '#1e40af', '#3730a3', '#312e81']),
#                 )
#             ])
#             fig.update_layout(
#                 title='Projects by Aggregate Type',
#                 paper_bgcolor='white',
#                 plot_bgcolor='white',
#                 font=dict(color='#1e40af'),
#                 height=400
#             )
#             st.plotly_chart(fig, use_container_width=True)
    
#     # Recent Projects Table
#     st.markdown("### 📋 Recent Projects")
#     if not df.empty:
#         recent_df = df.sort_values('Start of Project', ascending=False).head(10)
#         st.dataframe(
#             recent_df[['Project Code', 'Project Description', 'Platform', 'Aggregate', 'Aggregate Lead', 'Implementation Month']],
#             use_container_width=True
#         )

# # b MAIN 
# st.title("🚜 TWS Project – Exports Management")
# st.markdown("**Professional Project Tracking System**")

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
#             tractors = st.text_input("🚜 5 Tractors Online", placeholder="Status")
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
    
#     if submit:
#         if not email or not project_code or not project_desc:
#             st.error("❌ Please fill all required fields (*)")
#         else:
#             # Check if project code already exists
#             if project_code in df['Project Code'].values:
#                 st.warning("⚠️ Project Code already exists! Updating existing record...")
#                 idx = df[df['Project Code'] == project_code].index[0]
#                 update_record = True
#             else:
#                 idx = len(df)
#                 update_record = False
            
#             new_data = {
#                 "Email": email,
#                 "Project Code": project_code,
#                 "Project Description": project_desc,
#                 "Start of Project": start_project,
#                 "Platform": platform,
#                 "Continent/Country": continent,
#                 "SCR No": scr_no,
#                 "SCR Issue in CFT": scr_issue,
#                 "Model": model,
#                 "Aggregate": aggregate,
#                 "Aggregate Lead": agg_lead,
#                 "Implementation Month": impl_month,
#                 "R&D PMO": r_and_d,
#                 "Feasibility Uploaded": feasibility.name if feasibility else "",
#                 "G1 Drg Release": g1,
#                 "Material Avl": material,
#                 "Proto Fitment": proto,
#                 "Testing Start": testing,
#                 "Interim Testing Go Ahead": interim,
#                 "G1 ORC Drg": g1_orc_drg,
#                 "G1 ORC Material": g1_orc_mat,
#                 "G1 ORC Proto": g1_orc_proto,
#                 "G2 Go Ahead": g2_go,
#                 "G2 Material": g2_mat,
#                 "5 Tractors Online": tractors,
#                 "PRR Sign-off": prr,
#                 "Pre ERN": pre_ern,
#                 "Go Ahead ERN": go_ern,
#                 "BOM Change": bom,
#                 "BCR Number": bcr_no,
#                 "BCR Date": bcr_date,
#                 "Cut-off Number": cutoff
#             }
            
#             if update_record:
#                 for key, value in new_data.items():
#                     df.at[idx, key] = value
#                 st.success(f"✅ Project {project_code} updated successfully!")
#             else:
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
    
#     # Tabs for different data management operations
#     mgmt_tab1, mgmt_tab2, mgmt_tab3 = st.tabs(["📊 View & Edit All Data", "📤 Import from Google Sheets", "⚙️ Bulk Operations"])
    
#     with mgmt_tab1:
#         st.markdown("#### 📋 Complete Project Database")
        
#         if not df.empty:
#             # Search and Filter
#             col1, col2 = st.columns([3, 1])
#             with col1:
#                 search_term = st.text_input("🔍 Search across all columns:", placeholder="Type to search...")
#             with col2:
#                 show_cols = st.multiselect(
#                     "Filter Columns:",
#                     options=df.columns.tolist(),
#                     default=df.columns.tolist()[:10]
#                 )
            
#             # Display editable dataframe
#             if search_term:
#                 mask = df.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)
#                 display_df = df[mask]
#             else:
#                 display_df = df
            
#             if not show_cols:
#                 show_cols = df.columns.tolist()
            
#             st.markdown(f"**Showing {len(display_df)} of {len(df)} records**")
            
#             # Editable dataframe
#             edited_df = st.data_editor(
#                 display_df[show_cols],
#                 use_container_width=True,
#                 num_rows="dynamic",
#                 column_config={
#                     "Project Code": st.column_config.TextColumn(
#                         "Project Code",
#                         width="medium",
#                         required=True
#                     ),
#                     "Platform": st.column_config.SelectboxColumn(
#                         "Platform",
#                         options=["Below 30 HP", "30–60 HP", "60–101 HP", "Above 101 HP"],
#                         width="small"
#                     ),
#                     "Aggregate": st.column_config.SelectboxColumn(
#                         "Aggregate",
#                         options=["Electrical", "Hydraulic", "Transmission", "Engine", "Vehicle", "Cabin"],
#                         width="small"
#                     )
#                 }
#             )
            
#             # Action buttons
#             col1, col2, col3 = st.columns(3)
            
#             with col1:
#                 if st.button("💾 Save All Changes", use_container_width=True):
#                     if not search_term:
#                         df = edited_df
#                     else:
#                         # Update only searched rows
#                         for idx in display_df.index:
#                             for col in show_cols:
#                                 if col in edited_df.columns:
#                                     df.at[idx, col] = edited_df.at[idx, col]
#                     save_data(df)
#                     st.success("✅ All changes saved successfully!")
#                     st.rerun()
            
#             with col2:
#                 if st.button("🔄 Refresh Data", use_container_width=True):
#                     df = load_data()
#                     st.rerun()
            
#             with col3:
#                 if st.button("📥 Export to CSV", use_container_width=True):
#                     csv = df.to_csv(index=False)
#                     st.download_button(
#                         label="⬇️ Download CSV",
#                         data=csv,
#                         file_name="tws_exports_full.csv",
#                         mime="text/csv",
#                         use_container_width=True
#                     )
#         else:
#             st.info("📭 No data available. Add your first project or import data.")
    
#     with mgmt_tab2:
#         st.markdown("#### 📤 Import from Google Sheets/CSV")
#         st.info("Upload a CSV file exported from Google Sheets to update your database.")
        
#         uploaded_file = st.file_uploader(
#             "Choose a CSV file",
#             type=['csv'],
#             help="Upload CSV file with matching column names"
#         )
        
#         if uploaded_file is not None:
#             try:
#                 # Read uploaded file
#                 new_data = pd.read_csv(uploaded_file)
                
#                 # Show preview
#                 st.markdown("##### 📄 File Preview (First 5 rows):")
#                 st.dataframe(new_data.head(), use_container_width=True)
                
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
#                     st.dataframe(mapping_df, use_container_width=True)
                    
#                     # Import options
#                     st.markdown("##### ⚙️ Import Options")
                    
#                     col1, col2 = st.columns(2)
                    
#                     with col1:
#                         import_mode = st.radio(
#                             "Select import mode:",
#                             ["Update Existing & Add New", "Replace Entire Database", "Add New Only"]
#                         )
                    
#                     with col2:
#                         conflict_resolution = st.radio(
#                             "If project exists:",
#                             ["Update with new data", "Keep existing data", "Skip record"]
#                         )
                    
#                     if st.button("🚀 Process Import", use_container_width=True):
#                         progress_bar = st.progress(0)
#                         status_text = st.empty()
                        
#                         if import_mode == "Replace Entire Database":
#                             df = new_data
#                             save_data(df)
#                             status_text.success("✅ Database replaced successfully!")
                        
#                         else:
#                             updated_count = 0
#                             added_count = 0
#                             skipped_count = 0
                            
#                             for idx, row in new_data.iterrows():
#                                 progress = (idx + 1) / len(new_data)
#                                 progress_bar.progress(progress)
                                
#                                 project_code = row.get('Project Code')
                                
#                                 if project_code in df['Project Code'].values:
#                                     # Update existing
#                                     if import_mode == "Update Existing & Add New":
#                                         if conflict_resolution == "Update with new data":
#                                             db_idx = df[df['Project Code'] == project_code].index[0]
#                                             for col in new_data.columns:
#                                                 if col in df.columns and pd.notna(row[col]):
#                                                     df.at[db_idx, col] = row[col]
#                                             updated_count += 1
#                                         else:
#                                             skipped_count += 1
#                                 else:
#                                     # Add new
#                                     if import_mode in ["Update Existing & Add New", "Add New Only"]:
#                                         new_row = {}
#                                         for col in COLUMNS:
#                                             if col in new_data.columns:
#                                                 new_row[col] = row[col] if pd.notna(row.get(col)) else ""
#                                             else:
#                                                 new_row[col] = ""
#                                         df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
#                                         added_count += 1
                            
#                             save_data(df)
#                             progress_bar.empty()
                            
#                             st.success(f"""
#                             ✅ **Import Completed!**
                            
#                             **Summary:**
#                             - 📝 Records updated: **{updated_count}**
#                             - ➕ New records added: **{added_count}**
#                             - ⏭️ Records skipped: **{skipped_count}**
#                             - 📊 Total records now: **{len(df)}**
#                             """)
                        
#                         st.rerun()
            
#             except Exception as e:
#                 st.error(f"❌ Error reading file: {str(e)}")
    
#     with mgmt_tab3:
#         st.markdown("#### ⚙️ Bulk Operations")
        
#         col1, col2 = st.columns(2)
        
#         with col1:
#             st.markdown("##### 🗑️ Delete Operations")
            
#             # Delete by project code
#             st.markdown("**Delete by Project Code:**")
#             projects_to_delete = st.multiselect(
#                 "Select projects to delete:",
#                 options=df['Project Code'].tolist() if not df.empty else [],
#                 help="Select projects to delete"
#             )
            
#             if projects_to_delete and st.button("🗑️ Delete Selected Projects", use_container_width=True):
#                 df = df[~df['Project Code'].isin(projects_to_delete)]
#                 save_data(df)
#                 st.success(f"✅ Deleted {len(projects_to_delete)} projects!")
#                 st.rerun()
            
#             # Delete duplicates
#             st.markdown("**Clean Duplicates:**")
#             if st.button("🔍 Find & Remove Duplicates", use_container_width=True):
#                 duplicates = df.duplicated(subset=['Project Code'], keep='first')
#                 if duplicates.any():
#                     st.warning(f"Found {duplicates.sum()} duplicate project codes!")
#                     df = df.drop_duplicates(subset=['Project Code'], keep='first')
#                     save_data(df)
#                     st.success("✅ Duplicates removed!")
#                 else:
#                     st.info("✅ No duplicates found!")
        
#         with col2:
#             st.markdown("##### 🔄 Batch Update")
            
#             st.markdown("**Update Field for Multiple Projects:**")
#             update_field = st.selectbox(
#                 "Select field to update:",
#                 options=[col for col in df.columns if col not in ['Project Code', 'Email']]
#             )
            
#             update_value = st.text_input(f"New value for {update_field}:", placeholder="Enter new value...")
            
#             projects_to_update = st.multiselect(
#                 "Select projects to update:",
#                 options=df['Project Code'].tolist() if not df.empty else []
#             )
            
#             if update_value and projects_to_update and st.button("🔄 Apply Batch Update", use_container_width=True):
#                 df.loc[df['Project Code'].isin(projects_to_update), update_field] = update_value
#                 save_data(df)
#                 st.success(f"✅ Updated {len(projects_to_update)} projects!")
#                 st.rerun()
        
#         st.markdown("---")
#         st.markdown("##### 🚨 Database Management")
        
#         col1, col2, col3 = st.columns(3)
        
#         with col1:
#             if st.button("📊 Backup Database", use_container_width=True):
#                 backup_file = f"backup_{date.today()}.csv"
#                 df.to_csv(backup_file, index=False)
#                 st.success(f"✅ Backup saved as {backup_file}")
        
#         with col2:
#             if st.button("🧹 Clear All Data", use_container_width=True):
#                 if st.checkbox("⚠️ I understand this will delete ALL data permanently"):
#                     df = pd.DataFrame(columns=COLUMNS)
#                     save_data(df)
#                     st.error("🗑️ All data cleared!")
#                     st.rerun()
        
#         with col3:
#             if st.button("🔍 Validate Data", use_container_width=True):
#                 # Check for missing required fields
#                 missing_email = df['Email'].isna().sum()
#                 missing_code = df['Project Code'].isna().sum()
                
#                 if missing_email + missing_code == 0:
#                     st.success("✅ All data is valid!")
#                 else:
#                     st.warning(f"""
#                     ⚠️ **Data Issues Found:**
#                     - Missing Email: {missing_email}
#                     - Missing Project Code: {missing_code}
#                     """)

# # ================= SIDEBAR =================
# with st.sidebar:
#     st.markdown("""
#     <div style='text-align: center; padding: 20px;'>
#         <h2 style='color: #1d4ed8;'>🚜 TWS Exports</h2>
#         <p style='color: #1e40af;'>Project Management</p>
#     </div>
#     """, unsafe_allow_html=True)
    
#     st.markdown("---")
    
#     st.markdown("### 📈 Quick Stats")
#     if not df.empty:
#         st.metric("Total Projects", len(df))
#         st.metric("Active This Month", len(df[df['Implementation Month'] == pd.Timestamp.now().strftime('%b')]))
#         st.metric("G1 Complete", df['G1 Drg Release'].notna().sum())
#     else:
#         st.info("No data yet")
    
#     st.markdown("---")
    
#     st.markdown("### ⚡ Quick Actions")
#     if st.button("➕ Add New Project", use_container_width=True):
#         st.switch_page("streamlit_app.py")
    
#     if st.button("📥 Export Data", use_container_width=True):
#         csv = df.to_csv(index=False)
#         st.download_button(
#             label="Download CSV",
#             data=csv,
#             file_name="tws_exports.csv",
#             mime="text/csv",
#             use_container_width=True
#         )
    
#     st.markdown("---")
    
#     st.markdown("### 📅 Recent Activity")
#     if not df.empty:
#         recent = df.sort_values('Start of Project', ascending=False).head(3)
#         for _, row in recent.iterrows():
#             st.markdown(f"""
#             **{row['Project Code']}**
#             *{row['Platform']} - {row['Aggregate']}*
#             """)
    
#     st.markdown("---")
    
#     st.markdown("#### 📊 Database Info")
#     if not df.empty:
#         st.markdown(f"""
#         - **Size:** {len(df)} records
#         - **Last Updated:** {date.today()}
#         - **Storage:** {(len(df) * len(COLUMNS) * 50) / 1024:.1f} KB
#         """)

# # Auto-refresh data every 30 seconds
# st.markdown("""
# <script>
#     setTimeout(function() {
#         window.location.reload();
#     }, 30000); // 30 seconds
# </script>
# """, unsafe_allow_html=True)





