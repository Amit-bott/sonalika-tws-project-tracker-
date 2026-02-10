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













# import streamlit as st
# import pandas as pd
# from datetime import date
# import plotly.express as px
# import plotly.graph_objects as go
# import base64
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

# # ================= PREMIUM CURSOR REVEAL EFFECT =================
# def create_cursor_reveal_effect():
#     cursor_html = """
#     <!DOCTYPE html>
#     <html lang="en">
#     <head>
#     <meta charset="UTF-8">
#     <title>Premium 3D Cursor Reveal</title>
    
#     <style>
#       :root {
#         --circle-size: 400px;
#         --gradient-color-1: rgba(29, 78, 216, 0.95);
#         --gradient-color-2: rgba(37, 99, 235, 0.85);
#         --gradient-color-3: rgba(59, 130, 246, 0.75);
#         --shadow-color: rgba(29, 78, 216, 0.4);
#       }
      
#       * {
#         margin: 0;
#         padding: 0;
#         box-sizing: border-box;
#       }
      
#       body {
#         margin: 0;
#         height: 100vh;
#         display: flex;
#         justify-content: center;
#         align-items: center;
#         background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
#         overflow: hidden;
#         font-family: 'Segoe UI', system-ui, sans-serif;
#       }

#       .container {
#         position: relative;
#         width: 900px;
#         height: 500px;
#         background-image: url("https://images.unsplash.com/photo-1451187580459-43490279c0fa?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2072&q=80");
#         background-size: cover;
#         background-position: center;
#         overflow: hidden;
#         border-radius: 20px;
#         box-shadow: 
#           0 25px 50px -12px rgba(0, 0, 0, 0.5),
#           0 0 0 1px rgba(255, 255, 255, 0.1);
#         transform-style: preserve-3d;
#         perspective: 1000px;
#       }

#       .container::before {
#         content: '';
#         position: absolute;
#         inset: 0;
#         background: linear-gradient(135deg, 
#           rgba(29, 78, 216, 0.1) 0%, 
#           rgba(37, 99, 235, 0.05) 100%);
#         z-index: 1;
#         pointer-events: none;
#       }

#       .overlay {
#         position: absolute;
#         inset: 0;
#         background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
#         pointer-events: none;
#         transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
#         border-radius: 20px;
#         box-shadow: 
#           inset 0 0 60px rgba(255, 255, 255, 0.05),
#           0 8px 32px rgba(0, 0, 0, 0.4);
#       }

#       .cursor-tracer {
#         position: absolute;
#         width: 40px;
#         height: 40px;
#         border: 2px solid rgba(59, 130, 246, 0.8);
#         border-radius: 50%;
#         pointer-events: none;
#         z-index: 100;
#         opacity: 0;
#         transition: transform 0.2s, opacity 0.2s;
#         mix-blend-mode: screen;
#         filter: blur(1px);
#       }

#       .cursor-dot {
#         position: absolute;
#         width: 8px;
#         height: 8px;
#         background: #3b82f6;
#         border-radius: 50%;
#         pointer-events: none;
#         z-index: 101;
#         box-shadow: 0 0 20px #3b82f6;
#         opacity: 0;
#       }

#       .title {
#         position: absolute;
#         top: 50%;
#         left: 50%;
#         transform: translate(-50%, -50%);
#         color: white;
#         font-size: 3rem;
#         font-weight: 700;
#         text-align: center;
#         z-index: 10;
#         opacity: 0.9;
#         text-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
#         letter-spacing: 2px;
#         pointer-events: none;
#         background: linear-gradient(135deg, #60a5fa 0%, #3b82f6 100%);
#         -webkit-background-clip: text;
#         -webkit-text-fill-color: transparent;
#         background-clip: text;
#       }

#       .subtitle {
#         position: absolute;
#         top: 60%;
#         left: 50%;
#         transform: translate(-50%, -50%);
#         color: #cbd5e1;
#         font-size: 1.2rem;
#         text-align: center;
#         z-index: 10;
#         opacity: 0.8;
#         font-weight: 300;
#         letter-spacing: 1px;
#         pointer-events: none;
#       }

#       .particles {
#         position: absolute;
#         inset: 0;
#         pointer-events: none;
#         z-index: 5;
#       }

#       .particle {
#         position: absolute;
#         width: 4px;
#         height: 4px;
#         background: rgba(59, 130, 246, 0.6);
#         border-radius: 50%;
#         pointer-events: none;
#         animation: float 3s infinite ease-in-out;
#       }

#       @keyframes float {
#         0%, 100% { transform: translateY(0) rotate(0deg); opacity: 0; }
#         50% { opacity: 1; }
#       }

#       @keyframes pulse {
#         0%, 100% { transform: scale(1); opacity: 0.7; }
#         50% { transform: scale(1.1); opacity: 1; }
#       }

#       .glow {
#         position: absolute;
#         width: var(--circle-size);
#         height: var(--circle-size);
#         border-radius: 50%;
#         background: radial-gradient(
#           circle at center,
#           var(--gradient-color-1) 0%,
#           var(--gradient-color-2) 30%,
#           var(--gradient-color-3) 50%,
#           transparent 70%
#         );
#         filter: blur(40px);
#         opacity: 0;
#         pointer-events: none;
#         transition: opacity 0.3s;
#         mix-blend-mode: screen;
#         animation: pulse 4s infinite ease-in-out;
#       }

#       .ripple {
#         position: absolute;
#         border: 2px solid rgba(59, 130, 246, 0.3);
#         border-radius: 50%;
#         pointer-events: none;
#         animation: ripple 1.5s infinite;
#       }

#       @keyframes ripple {
#         0% { transform: scale(0.8); opacity: 1; }
#         100% { transform: scale(2); opacity: 0; }
#       }
#     </style>
#     </head>

#     <body>
#     <div class="container" id="box">
#       <div class="overlay" id="overlay"></div>
#       <div class="title">TWS PROJECTS</div>
#       <div class="subtitle">Move cursor to reveal content</div>
#       <div class="particles" id="particles"></div>
#       <div class="cursor-tracer" id="cursorTracer"></div>
#       <div class="cursor-dot" id="cursorDot"></div>
#       <div class="glow" id="glow"></div>
#     </div>

#     <script>
#       const box = document.getElementById("box");
#       const overlay = document.getElementById("overlay");
#       const cursorTracer = document.getElementById("cursorTracer");
#       const cursorDot = document.getElementById("cursorDot");
#       const glow = document.getElementById("glow");
#       const particles = document.getElementById("particles");

#       // Create particles
#       function createParticles() {
#         for (let i = 0; i < 50; i++) {
#           const particle = document.createElement("div");
#           particle.className = "particle";
#           particle.style.left = `${Math.random() * 100}%`;
#           particle.style.top = `${Math.random() * 100}%`;
#           particle.style.animationDelay = `${Math.random() * 3}s`;
#           particle.style.animationDuration = `${2 + Math.random() * 3}s`;
#           particles.appendChild(particle);
#         }
#       }

#       function setMask(x, y) {
#         // Create 3D gradient mask with multiple layers
#         const mask = `
#           radial-gradient(
#             circle at ${x}px ${y}px,
#             transparent 0%,
#             rgba(0,0,0,0.95) 30%,
#             rgba(0,0,0,0.85) 45%,
#             rgba(255,255,255,0.1) 60%,
#             rgba(255,255,255,0.3) 70%,
#             white 85%
#           )
#         `;

#         overlay.style.maskImage = mask;
#         overlay.style.webkitMaskImage = mask;
        
#         // Add CSS filter for depth
#         overlay.style.filter = `
#           drop-shadow(0 0 30px rgba(59, 130, 246, 0.3))
#           brightness(1.1)
#         `;
#       }

#       function updateCursorElements(x, y) {
#         cursorTracer.style.left = `${x - 20}px`;
#         cursorTracer.style.top = `${y - 20}px`;
#         cursorTracer.style.opacity = '1';
#         cursorTracer.style.transform = `scale(${1 + Math.sin(Date.now() * 0.01) * 0.1})`;
        
#         cursorDot.style.left = `${x - 4}px`;
#         cursorDot.style.top = `${y - 4}px`;
#         cursorDot.style.opacity = '1';
        
#         glow.style.left = `${x - 200}px`;
#         glow.style.top = `${y - 200}px`;
#         glow.style.opacity = '0.7';
        
#         // Create ripple effect
#         if (Math.random() > 0.7) {
#           const ripple = document.createElement("div");
#           ripple.className = "ripple";
#           ripple.style.left = `${x}px`;
#           ripple.style.top = `${y}px`;
#           box.appendChild(ripple);
#           setTimeout(() => ripple.remove(), 1500);
#         }
#       }

#       function handleMouseMove(e) {
#         const rect = box.getBoundingClientRect();
#         const x = e.clientX - rect.left;
#         const y = e.clientY - rect.top;
        
#         setMask(x, y);
#         updateCursorElements(x, y);
        
#         // Parallax effect
#         box.style.transform = `
#           perspective(1000px)
#           rotateY(${(x - rect.width / 2) / 50}deg)
#           rotateX(${-(y - rect.height / 2) / 50}deg)
#         `;
#       }

#       function handleMouseLeave() {
#         overlay.style.maskImage = "none";
#         overlay.style.webkitMaskImage = "none";
#         overlay.style.filter = "none";
#         cursorTracer.style.opacity = '0';
#         cursorDot.style.opacity = '0';
#         glow.style.opacity = '0';
#         box.style.transform = "perspective(1000px) rotateY(0deg) rotateX(0deg)";
#       }

#       // Initialize
#       createParticles();
      
#       box.addEventListener("mousemove", handleMouseMove);
#       box.addEventListener("mouseleave", handleMouseLeave);
      
#       // Touch support
#       box.addEventListener("touchmove", (e) => {
#         e.preventDefault();
#         const touch = e.touches[0];
#         const rect = box.getBoundingClientRect();
#         const x = touch.clientX - rect.left;
#         const y = touch.clientY - rect.top;
        
#         setMask(x, y);
#         updateCursorElements(x, y);
#       });
      
#       box.addEventListener("touchend", handleMouseLeave);
#     </script>
#     </body>
#     </html>
#     """
#     return cursor_html

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
    
#     /* Premium Cursor Reveal Container */
#     .cursor-container {
#         border-radius: 20px;
#         overflow: hidden;
#         margin: 20px 0;
#         box-shadow: 0 20px 60px rgba(29, 78, 216, 0.15);
#         border: 1px solid rgba(59, 130, 246, 0.1);
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
# col1, col2 = st.columns([1, 4])
# with col1:
#     display_lottie_animation()
# with col2:
#     st.title("TWS Project – Exports Management")
#     st.markdown("**Professional Project Tracking System**")

# tab1, tab2, tab3, tab4 = st.tabs(["🎯 Cursor Reveal Effect", "📝 Data Entry Form", "📊 Dashboard", "📁 Data Management"])

# # ================= CURSOR REVEAL EFFECT TAB =================
# with tab1:
#     st.markdown("### 🎨 Premium 3D Cursor Reveal Effect")
#     st.markdown("""
#     <div style='background: linear-gradient(135deg, #2563eb, #1d4ed8); padding: 20px; border-radius: 15px; color: white; margin-bottom: 20px;'>
#         <h3 style='color: white; margin: 0;'>✨ Interactive Experience</h3>
#         <p style='margin: 10px 0 0 0;'>Move your cursor over the image below to reveal the hidden content with a 3D circle effect.</p>
#     </div>
#     """, unsafe_allow_html=True)
    
#     # Display the premium cursor reveal effect
#     cursor_html = create_cursor_reveal_effect()
#     components.html(cursor_html, height=550, scrolling=False)
    
#     st.markdown("---")
    
#     col1, col2 = st.columns(2)
#     with col1:
#         st.markdown("""
#         ### 🎯 Features
#         - **3D Parallax Effect**: Container responds to cursor movement
#         - **Dynamic Particles**: Floating particles for depth
#         - **Ripple Animations**: Smooth ripple effects on cursor
#         - **Gradient Glow**: Professional blue gradient glow
#         - **Smooth Transitions**: Fluid animations and transitions
#         """)
    
#     with col2:
#         st.markdown("""
#         ### 💡 Technology
#         - **CSS 3D Transforms**: Advanced 3D perspective
#         - **Radial Gradients**: Multiple gradient layers
#         - **Custom Masks**: Dynamic mask generation
#         - **JavaScript Animation**: Real-time cursor tracking
#         - **Particle System**: Dynamic particle generation
#         """)

# # ================= FORM TAB =================
# with tab2:
#     # Display cursor effect as background with lower opacity
#     st.markdown("""
#     <style>
#     .form-container {
#         background: rgba(255, 255, 255, 0.95);
#         padding: 30px;
#         border-radius: 20px;
#         box-shadow: 0 20px 60px rgba(29, 78, 216, 0.1);
#         border: 1px solid rgba(59, 130, 246, 0.2);
#         margin: 20px 0;
#         position: relative;
#         z-index: 10;
#     }
    
#     .form-header {
#         background: linear-gradient(135deg, #2563eb, #1d4ed8);
#         color: white;
#         padding: 20px;
#         border-radius: 15px;
#         margin-bottom: 30px;
#         text-align: center;
#     }
#     </style>
    
#     <div class="form-header">
#         <h2 style="color: white; margin: 0;">✨ New Project Entry</h2>
#         <p style="margin: 10px 0 0 0; opacity: 0.9;">Fill in the details below to create a new project</p>
#     </div>
#     """, unsafe_allow_html=True)
    
#     st.markdown('<div class="form-container">', unsafe_allow_html=True)
    
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
# with tab3:
#     create_dashboard()

# # ================= DATA MANAGEMENT TAB =================
# with tab4:
#     st.markdown("### 📁 Data Management Center")
    
#     col1, col2, col3 = st.columns([1, 2, 1])
#     with col2:
#         display_lottie_animation()
    
#     mgmt_tab1, mgmt_tab2, mgmt_tab3 = st.tabs(["📊 View & Edit All Data", "📤 Import from Google Sheets", "⚙️ Bulk Operations"])
    
#     with mgmt_tab1:
#         st.markdown("#### 📋 Complete Project Database")
        
#         if not df.empty and len(df) > 0:
#             col1, col2 = st.columns([3, 1])
#             with col1:
#                 search_term = st.text_input("🔍 Search across all columns:", placeholder="Type to search...", key="search_all")
            
#             show_cols = st.multiselect(
#                 "Filter Columns:",
#                 options=df.columns.tolist(),
#                 default=df.columns.tolist()[:min(8, len(df.columns))] if len(df.columns) > 8 else df.columns.tolist(),
#                 key="filter_cols"
#             )
            
#             if search_term:
#                 mask = df.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)
#                 display_df = df[mask]
#             else:
#                 display_df = df
            
#             if not show_cols:
#                 show_cols = df.columns.tolist()
            
#             st.markdown(f"**Showing {len(display_df)} of {len(df)} records**")
            
#             st.dataframe(
#                 display_df[show_cols],
#                 width='stretch'
#             )
            
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
#                 new_data = pd.read_csv(uploaded_file)
                
#                 st.markdown("##### 📄 File Preview (First 5 rows):")
#                 st.dataframe(new_data.head(), width='stretch')
                
#                 st.markdown(f"**File contains {len(new_data)} rows and {len(new_data.columns)} columns**")
                
#                 if 'Project Code' not in new_data.columns:
#                     st.error("❌ CSV must contain 'Project Code' column!")
#                 else:
#                     st.markdown("##### 🔄 Column Mapping")
#                     mapping_df = pd.DataFrame({
#                         'CSV Columns': new_data.columns,
#                         'Database Columns': [col if col in COLUMNS else '❌ No match' for col in new_data.columns]
#                     })
#                     st.dataframe(mapping_df, width='stretch')
                    
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
                                
#                                 new_data['Project Code'] = new_data['Project Code'].astype(str)
#                                 if not df.empty:
#                                     df['Project Code'] = df['Project Code'].astype(str)
                                
#                                 for idx, row in new_data.iterrows():
#                                     project_code = str(row.get('Project Code', ''))
                                    
#                                     if not df.empty and project_code in df['Project Code'].values:
#                                         if import_mode == "Update Existing & Add New":
#                                             if conflict_resolution == "Update with new data":
#                                                 db_idx = df[df['Project Code'] == project_code].index[0]
#                                                 for col in new_data.columns:
#                                                     if col in df.columns and pd.notna(row[col]):
#                                                         df.at[db_idx, col] = row[col]
#                                                 updated_count += 1
#                                             elif conflict_resolution == "Skip record":
#                                                 skipped_count += 1
#                                             else:
#                                                 skipped_count += 1
#                                     else:
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





















import streamlit as st
import pandas as pd
from datetime import date
import plotly.express as px
import plotly.graph_objects as go
import base64
import streamlit.components.v1 as components

# ================= CONFIG =================
st.set_page_config(
    page_title="TWS Project – Exports",
    layout="wide",
    initial_sidebar_state="expanded"
)

DATA_FILE = "tws_exports.csv"
COLUMNS = [
    "Email","Project Code","Project Description","Start of Project","Platform",
    "Continent/Country","SCR No","SCR Issue in CFT","Model","Aggregate",
    "Aggregate Lead","Implementation Month","R&D PMO","Feasibility Uploaded",
    "G1 Drg Release","Material Avl","Proto Fitment","Testing Start",
    "Interim Testing Go Ahead","G1 ORC Drg","G1 ORC Material","G1 ORC Proto",
    "G2 Go Ahead","G2 Material","5 Tractors Online","PRR Sign-off",
    "Pre ERN","Go Ahead ERN","BOM Change","BCR Number","BCR Date","Cut-off Number"
]

# ================= TWO-PAGE CURSOR REVEAL EFFECT =================
def create_two_page_cursor_reveal():
    cursor_html = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Two-Page Cursor Reveal</title>
    
    <style>
      :root {
        --circle-size: 400px;
        --gradient-color-1: rgba(29, 78, 216, 0.95);
        --gradient-color-2: rgba(37, 99, 235, 0.85);
        --gradient-color-3: rgba(59, 130, 246, 0.75);
      }
      
      * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }
      
      body {
        margin: 0;
        height: 100vh;
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        overflow: hidden;
        font-family: 'Segoe UI', system-ui, sans-serif;
        display: flex;
        justify-content: center;
        align-items: center;
      }

      .pages-container {
        position: relative;
        width: 100vw;
        height: 100vh;
        overflow: hidden;
      }

      .page {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
        opacity: 0;
        pointer-events: none;
        transition: opacity 0.8s cubic-bezier(0.4, 0, 0.2, 1);
      }

      .page.active {
        opacity: 1;
        pointer-events: all;
      }

      .container {
        position: relative;
        width: 900px;
        height: 500px;
        background-size: cover;
        background-position: center;
        overflow: hidden;
        border-radius: 20px;
        box-shadow: 
          0 25px 50px -12px rgba(0, 0, 0, 0.5),
          0 0 0 1px rgba(255, 255, 255, 0.1);
        transform-style: preserve-3d;
        perspective: 1000px;
      }

      .overlay {
        position: absolute;
        inset: 0;
        background: white;
        pointer-events: none;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        border-radius: 20px;
        box-shadow: 
          inset 0 0 60px rgba(255, 255, 255, 0.1),
          0 8px 32px rgba(0, 0, 0, 0.3);
        opacity: 0.98;
      }

      /* Page 1 Background */
      .page1 .container {
        background-image: url("https://images.unsplash.com/photo-1490474418585-ba9bad8fd0ea?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80");
      }

      /* Page 2 Background */
      .page2 .container {
        background-image: url("https://images.unsplash.com/photo-1500382017468-9049fed747ef?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80");
      }

      .content {
        position: absolute;
        inset: 0;
        z-index: 20;
        padding: 40px;
        color: white;
        display: flex;
        flex-direction: column;
        justify-content: center;
        pointer-events: none;
      }

      .page1 .content {
        background: linear-gradient(135deg, 
          rgba(107, 33, 168, 0.7) 0%, 
          rgba(168, 85, 247, 0.5) 100%);
      }

      .page2 .content {
        background: linear-gradient(135deg, 
          rgba(21, 94, 117, 0.7) 0%, 
          rgba(56, 189, 248, 0.5) 100%);
      }

      .years-badge {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 10px;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
      }

      .main-heading {
        font-size: 3.5rem;
        font-weight: 800;
        margin-bottom: 20px;
        text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.7);
        line-height: 1.2;
      }

      .sub-heading {
        font-size: 1.5rem;
        font-weight: 300;
        margin-bottom: 30px;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
        opacity: 0.9;
        line-height: 1.6;
      }

      .highlight-text {
        font-size: 1.8rem;
        font-weight: 600;
        color: #ffd700;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
        border-left: 4px solid #ffd700;
        padding-left: 15px;
        margin-top: 20px;
      }

      .timeline-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-top: 30px;
        padding: 0 20px;
      }

      .timeline-item {
        text-align: center;
        flex: 1;
      }

      .year {
        font-size: 3rem;
        font-weight: 700;
        color: #ffd700;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
      }

      .year-label {
        font-size: 1.2rem;
        font-weight: 300;
        margin-top: 5px;
        opacity: 0.9;
      }

      .timeline-line {
        flex: 2;
        height: 2px;
        background: linear-gradient(90deg, 
          rgba(255, 215, 0, 0.3) 0%, 
          rgba(255, 215, 0, 0.7) 50%, 
          rgba(255, 215, 0, 0.3) 100%);
        margin: 0 20px;
      }

      .commitment-text {
        font-size: 1.4rem;
        font-weight: 400;
        text-align: center;
        margin-top: 20px;
        color: #ffd700;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
      }

      .cursor-tracer {
        position: absolute;
        width: 40px;
        height: 40px;
        border: 2px solid rgba(255, 215, 0, 0.8);
        border-radius: 50%;
        pointer-events: none;
        z-index: 100;
        opacity: 0;
        transition: transform 0.2s, opacity 0.2s;
        mix-blend-mode: screen;
        filter: blur(1px);
      }

      .cursor-dot {
        position: absolute;
        width: 8px;
        height: 8px;
        background: #ffd700;
        border-radius: 50%;
        pointer-events: none;
        z-index: 101;
        box-shadow: 0 0 20px #ffd700;
        opacity: 0;
      }

      .glow {
        position: absolute;
        width: var(--circle-size);
        height: var(--circle-size);
        border-radius: 50%;
        background: radial-gradient(
          circle at center,
          rgba(255, 215, 0, 0.6) 0%,
          rgba(255, 215, 0, 0.4) 30%,
          rgba(255, 215, 0, 0.2) 50%,
          transparent 70%
        );
        filter: blur(40px);
        opacity: 0;
        pointer-events: none;
        transition: opacity 0.3s;
        mix-blend-mode: screen;
      }

      .navigation {
        position: absolute;
        bottom: 30px;
        left: 50%;
        transform: translateX(-50%);
        display: flex;
        gap: 20px;
        z-index: 1000;
      }

      .nav-btn {
        background: rgba(255, 255, 255, 0.1);
        border: 2px solid rgba(255, 215, 0, 0.5);
        color: white;
        padding: 12px 24px;
        border-radius: 50px;
        font-size: 1rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        backdrop-filter: blur(10px);
        min-width: 120px;
        text-align: center;
      }

      .nav-btn:hover {
        background: rgba(255, 215, 0, 0.2);
        border-color: #ffd700;
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(255, 215, 0, 0.3);
      }

      .page-indicator {
        position: absolute;
        top: 30px;
        right: 30px;
        display: flex;
        gap: 10px;
        z-index: 1000;
      }

      .indicator-dot {
        width: 12px;
        height: 12px;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.3);
        cursor: pointer;
        transition: all 0.3s ease;
      }

      .indicator-dot.active {
        background: #ffd700;
        transform: scale(1.2);
        box-shadow: 0 0 10px rgba(255, 215, 0, 0.5);
      }

      .ripple {
        position: absolute;
        border: 2px solid rgba(255, 215, 0, 0.3);
        border-radius: 50%;
        pointer-events: none;
        animation: ripple 1.5s infinite;
      }

      @keyframes ripple {
        0% { transform: scale(0.8); opacity: 1; }
        100% { transform: scale(2); opacity: 0; }
      }

      .instruction {
        position: absolute;
        bottom: 80px;
        left: 50%;
        transform: translateX(-50%);
        color: rgba(255, 255, 255, 0.7);
        font-size: 0.9rem;
        text-align: center;
        z-index: 1000;
        background: rgba(0, 0, 0, 0.3);
        padding: 8px 16px;
        border-radius: 20px;
        backdrop-filter: blur(5px);
      }
    </style>
    </head>

    <body>
    <div class="pages-container">
      <!-- Page 1 -->
      <div class="page page1 active">
        <div class="container" id="box1">
          <div class="overlay" id="overlay1"></div>
          <div class="content">
            <div class="years-badge">30 YEARS OF TRUST</div>
            <div class="main-heading">जिव्ही ऐसे...</div>
            <div class="sub-heading">
              मिट्टी को सोना बनाते हैं हम<br>
              किसान को वक्त की ताकत आज थमाते हैं हम...
            </div>
            <div class="highlight-text">
              युवियां ऐसी - जो मिट्टी से सोना बनायें
            </div>
          </div>
          <div class="cursor-tracer" id="cursorTracer1"></div>
          <div class="cursor-dot" id="cursorDot1"></div>
          <div class="glow" id="glow1"></div>
        </div>
      </div>

      <!-- Page 2 -->
      <div class="page page2">
        <div class="container" id="box2">
          <div class="overlay" id="overlay2"></div>
          <div class="content">
            <div class="years-badge">30 YEARS OF TRUST</div>
            <div class="timeline-container">
              <div class="timeline-item">
                <div class="year">1996</div>
                <div class="year-label">DUM KA<br>PEHLA<br>KADAM</div>
              </div>
              <div class="timeline-line"></div>
              <div class="timeline-item">
                <div class="year">2026</div>
                <div class="year-label">DUM<br>SABSE AAGE<br>REHNE KA</div>
              </div>
            </div>
            <div class="commitment-text">THREE DECADES<br>ONE COMMITMENT</div>
          </div>
          <div class="cursor-tracer" id="cursorTracer2"></div>
          <div class="cursor-dot" id="cursorDot2"></div>
          <div class="glow" id="glow2"></div>
        </div>
      </div>

      <!-- Navigation -->
      <div class="navigation">
        <button class="nav-btn" onclick="showPage(1)">पेज 1</button>
        <button class="nav-btn" onclick="showPage(2)">पेज 2</button>
      </div>

      <!-- Page Indicator -->
      <div class="page-indicator">
        <div class="indicator-dot active" onclick="showPage(1)"></div>
        <div class="indicator-dot" onclick="showPage(2)"></div>
      </div>

      <!-- Instruction -->
      <div class="instruction">Move cursor over the image to reveal background</div>
    </div>

    <script>
      let currentPage = 1;
      const pages = document.querySelectorAll('.page');
      const indicators = document.querySelectorAll('.indicator-dot');

      // Initialize all pages with cursor effects
      initializePage(1);
      initializePage(2);

      function showPage(pageNumber) {
        // Hide all pages
        pages.forEach(page => {
          page.classList.remove('active');
        });
        
        // Show selected page
        document.querySelector(`.page${pageNumber}`).classList.add('active');
        
        // Update indicators
        indicators.forEach((indicator, index) => {
          indicator.classList.toggle('active', index === pageNumber - 1);
        });
        
        currentPage = pageNumber;
      }

      function initializePage(pageNumber) {
        const box = document.getElementById(`box${pageNumber}`);
        const overlay = document.getElementById(`overlay${pageNumber}`);
        const cursorTracer = document.getElementById(`cursorTracer${pageNumber}`);
        const cursorDot = document.getElementById(`cursorDot${pageNumber}`);
        const glow = document.getElementById(`glow${pageNumber}`);

        function setMask(x, y) {
          const mask = `
            radial-gradient(
              circle at ${x}px ${y}px,
              transparent 0%,
              rgba(0,0,0,0.95) 30%,
              rgba(0,0,0,0.85) 45%,
              rgba(255,255,255,0.1) 60%,
              rgba(255,255,255,0.3) 70%,
              white 85%
            )
          `;

          overlay.style.maskImage = mask;
          overlay.style.webkitMaskImage = mask;
          
          // Add CSS filter for depth
          overlay.style.filter = `
            drop-shadow(0 0 30px rgba(255, 215, 0, 0.3))
            brightness(1.1)
          `;
        }

        function updateCursorElements(x, y) {
          if (!cursorTracer || !cursorDot || !glow) return;
          
          cursorTracer.style.left = `${x - 20}px`;
          cursorTracer.style.top = `${y - 20}px`;
          cursorTracer.style.opacity = '1';
          cursorTracer.style.transform = `scale(${1 + Math.sin(Date.now() * 0.01) * 0.1})`;
          
          cursorDot.style.left = `${x - 4}px`;
          cursorDot.style.top = `${y - 4}px`;
          cursorDot.style.opacity = '1';
          
          glow.style.left = `${x - 200}px`;
          glow.style.top = `${y - 200}px`;
          glow.style.opacity = '0.7';
          
          // Create ripple effect occasionally
          if (Math.random() > 0.8) {
            const ripple = document.createElement("div");
            ripple.className = "ripple";
            ripple.style.left = `${x}px`;
            ripple.style.top = `${y}px`;
            box.appendChild(ripple);
            setTimeout(() => ripple.remove(), 1500);
          }
        }

        function handleMouseMove(e) {
          const rect = box.getBoundingClientRect();
          const x = e.clientX - rect.left;
          const y = e.clientY - rect.top;
          
          setMask(x, y);
          updateCursorElements(x, y);
          
          // Parallax effect
          box.style.transform = `
            perspective(1000px)
            rotateY(${(x - rect.width / 2) / 50}deg)
            rotateX(${-(y - rect.height / 2) / 50}deg)
          `;
        }

        function handleMouseLeave() {
          overlay.style.maskImage = "none";
          overlay.style.webkitMaskImage = "none";
          overlay.style.filter = "none";
          if (cursorTracer) cursorTracer.style.opacity = '0';
          if (cursorDot) cursorDot.style.opacity = '0';
          if (glow) glow.style.opacity = '0';
          box.style.transform = "perspective(1000px) rotateY(0deg) rotateX(0deg)";
        }

        // Add event listeners
        box.addEventListener("mousemove", handleMouseMove);
        box.addEventListener("mouseleave", handleMouseLeave);
        
        // Touch support
        box.addEventListener("touchmove", (e) => {
          e.preventDefault();
          const touch = e.touches[0];
          const rect = box.getBoundingClientRect();
          const x = touch.clientX - rect.left;
          const y = touch.clientY - rect.top;
          
          setMask(x, y);
          updateCursorElements(x, y);
        });
        
        box.addEventListener("touchend", handleMouseLeave);
      }

      // Auto-switch pages every 10 seconds
      setInterval(() => {
        currentPage = currentPage === 1 ? 2 : 1;
        showPage(currentPage);
      }, 10000);
    </script>
    </body>
    </html>
    '''
    return cursor_html

# ================= CLEAN WHITE STYLE WITH BLUE THEME =================
st.markdown("""
<style>
    /* White Background Theme */
    .stApp {
        background-color: #ffffff !important;
    }
    
    /* Blue Headers */
    h1, h2, h3, h4, h5, h6 {
        color: #1a56db !important;
        font-weight: 700 !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Blue Labels and Text */
    label, span, p, div {
        color: #1e40af !important;
    }
    
    /* Dataframe Styling */
    .stDataFrame {
        border: 2px solid #1d4ed8 !important;
        border-radius: 10px !important;
    }
    
    /* Blue Input Fields */
    input, textarea, select {
        background-color: #ffffff !important;
        color: #1e40af !important;
        border: 1px solid #3b82f6 !important;
        border-radius: 8px !important;
    }
    
    /* Blue Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #2563eb, #1d4ed8) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        padding: 10px 24px !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #1d4ed8, #1e40af) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 12px rgba(29, 78, 216, 0.3) !important;
    }
    
    /* Tab Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: #ffffff !important;
        color: #1e40af !important;
        border: 1px solid #dbeafe !important;
        border-radius: 8px 8px 0 0 !important;
        padding: 12px 24px !important;
    }
    
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background-color: #dbeafe !important;
        color: #1d4ed8 !important;
        border-bottom: 3px solid #2563eb !important;
    }
    
    /* Metrics Styling */
    [data-testid="stMetric"] {
        background-color: #f0f9ff !important;
        padding: 20px !important;
        border-radius: 12px !important;
        border: 1px solid #bae6fd !important;
    }
    
    [data-testid="stMetricLabel"], [data-testid="stMetricValue"], [data-testid="stMetricDelta"] {
        color: #1e40af !important;
    }
    
    /* Radio Buttons */
    .stRadio > div {
        background-color: #f8fafc !important;
        padding: 15px !important;
        border-radius: 10px !important;
        border: 1px solid #e2e8f0 !important;
    }
    
    /* File Uploader */
    .stFileUploader > div {
        background-color: #f8fafc !important;
        border: 2px dashed #93c5fd !important;
        border-radius: 10px !important;
        padding: 20px !important;
    }
    
    /* Success/Error Messages */
    .stAlert {
        border-radius: 8px !important;
        border: 1px solid !important;
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #f8fafc !important;
    }
    
    /* Table Styling */
    .dataframe {
        background-color: #ffffff !important;
        color: #1e40af !important;
    }
    
    /* Select Box */
    div[data-baseweb="select"] > div {
        background-color: #ffffff !important;
        color: #1e40af !important;
        border: 1px solid #3b82f6 !important;
    }
    
    /* Checkbox */
    .stCheckbox > label {
        color: #1e40af !important;
    }
    
    /* Divider */
    hr {
        border-color: #dbeafe !important;
    }
    
    /* Card-like containers */
    .st-expander {
        background-color: #f8fafc !important;
        border: 1px solid #dbeafe !important;
        border-radius: 10px !important;
    }
    
    /* Blue Scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #f1f5f9;
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #3b82f6, #1d4ed8);
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #1d4ed8;
    }
    
    /* Status Badges */
    .status-badge {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 600;
    }
    
    .status-complete {
        background-color: #dcfce7;
        color: #166534;
    }
    
    .status-pending {
        background-color: #fef3c7;
        color: #92400e;
    }
    
    .status-progress {
        background-color: #dbeafe;
        color: #1e40af;
    }
    
    /* Premium Cursor Reveal Container */
    .cursor-container {
        border-radius: 20px;
        overflow: hidden;
        margin: 20px 0;
        box-shadow: 0 20px 60px rgba(29, 78, 216, 0.15);
        border: 1px solid rgba(59, 130, 246, 0.1);
    }
    
    /* Two Page Styles */
    .two-page-header {
        background: linear-gradient(135deg, #2563eb, #1d4ed8);
        color: white;
        padding: 25px;
        border-radius: 15px;
        margin-bottom: 25px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(29, 78, 216, 0.2);
    }
    
    .page-description {
        background: #f0f9ff;
        padding: 20px;
        border-radius: 12px;
        border-left: 5px solid #3b82f6;
        margin: 20px 0;
    }
</style>
""", unsafe_allow_html=True)

# ================= LOAD / SAVE =================
def load_data():
    try:
        df = pd.read_csv(DATA_FILE)
        if 'Project Code' in df.columns:
            df['Project Code'] = df['Project Code'].astype(str)
        return df
    except:
        return pd.DataFrame(columns=COLUMNS)

def save_data(df):
    if 'Project Code' in df.columns:
        df['Project Code'] = df['Project Code'].astype(str)
    df.to_csv(DATA_FILE, index=False)

df = load_data()

# ================= LOTTIE ANIMATION =================
def display_lottie_animation():
    lottie_html = """
    <script src="https://unpkg.com/@lottiefiles/dotlottie-wc@0.8.11/dist/dotlottie-wc.js" type="module"></script>
    <dotlottie-wc src="https://lottie.host/8dd2e6af-9e9a-4464-ad99-41e7c2a723e2/AzY19wIzNy.lottie" style="width: 100px; height: 100px" autoplay loop></dotlottie-wc>
    """
    components.html(lottie_html, height=120)

# ================= PROFESSIONAL DASHBOARD =================
def create_dashboard():
    st.markdown("### 📊 Project Analytics Dashboard")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        display_lottie_animation()
    
    # Metrics Row
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_projects = len(df)
        st.metric(
            "Total Projects", 
            total_projects,
            delta=f"+{len(df[df['Start of Project'] == pd.Timestamp(date.today()).strftime('%Y-%m-%d')])} today" if total_projects > 0 else None
        )
    
    with col2:
        g1_completed = df["G1 Drg Release"].notna().sum()
        completion_rate = (g1_completed / total_projects * 100) if total_projects > 0 else 0
        st.metric(
            "G1 Completed", 
            g1_completed,
            delta=f"{completion_rate:.1f}%",
            delta_color="normal"
        )
    
    with col3:
        g2_completed = df["G2 Go Ahead"].notna().sum()
        g2_rate = (g2_completed / total_projects * 100) if total_projects > 0 else 0
        st.metric(
            "G2 Completed", 
            g2_completed,
            delta=f"{g2_rate:.1f}%"
        )
    
    with col4:
        active_projects = len(df[df['Implementation Month'].str.strip().str.lower() == pd.Timestamp.now().strftime('%b').lower()]) if 'Implementation Month' in df.columns else 0
        st.metric(
            "Active This Month", 
            active_projects
        )
    
    st.markdown("---")
    
    # Charts Row
    if not df.empty:
        col1, col2 = st.columns(2)
        
        with col1:
            if 'Platform' in df.columns:
                platform_counts = df['Platform'].value_counts()
                fig = go.Figure(data=[
                    go.Bar(
                        x=platform_counts.index,
                        y=platform_counts.values,
                        marker_color='#2563eb',
                        text=platform_counts.values,
                        textposition='auto',
                    )
                ])
                fig.update_layout(
                    title='Projects by Platform',
                    paper_bgcolor='white',
                    plot_bgcolor='white',
                    font=dict(color='#1e40af'),
                    height=400
                )
                st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            if 'Aggregate' in df.columns:
                aggregate_counts = df['Aggregate'].value_counts()
                fig = go.Figure(data=[
                    go.Pie(
                        labels=aggregate_counts.index,
                        values=aggregate_counts.values,
                        hole=.3,
                        marker=dict(colors=['#2563eb', '#1d4ed8', '#1e40af', '#3730a3', '#312e81']),
                    )
                ])
                fig.update_layout(
                    title='Projects by Aggregate Type',
                    paper_bgcolor='white',
                    plot_bgcolor='white',
                    font=dict(color='#1e40af'),
                    height=400
                )
                st.plotly_chart(fig, use_container_width=True)
    
    # Recent Projects Table
    st.markdown("### 📋 Recent Projects")
    if not df.empty and len(df) > 0:
        if 'Start of Project' in df.columns:
            try:
                df_display = df.copy()
                df_display['Start of Project'] = pd.to_datetime(df_display['Start of Project'], errors='coerce')
                recent_df = df_display.sort_values('Start of Project', ascending=False).head(10)
            except:
                recent_df = df.head(10)
        else:
            recent_df = df.head(10)
        
        display_cols = ['Project Code', 'Project Description', 'Platform', 'Aggregate', 'Aggregate Lead', 'Implementation Month']
        display_cols = [col for col in display_cols if col in recent_df.columns]
        
        st.dataframe(
            recent_df[display_cols],
            width='stretch'
        )
    else:
        st.info("No projects available. Add your first project in the Data Entry tab.")

# ================= MAIN =================
col1, col2 = st.columns([1, 4])
with col1:
    display_lottie_animation()
with col2:
    st.title("TWS Project – Exports Management")
    st.markdown("**Professional Project Tracking System with Interactive Display**")

tab1, tab2, tab3, tab4 = st.tabs(["🎯 Two-Page Display", "📝 Data Entry Form", "📊 Dashboard", "📁 Data Management"])

# ================= TWO-PAGE DISPLAY TAB =================
with tab1:
    st.markdown("""
    <div class="two-page-header">
        <h2 style="color: white; margin: 0;">✨ 30 Years Celebration - Interactive Display</h2>
        <p style="margin: 10px 0 0 0; opacity: 0.9;">Move cursor over images to reveal background content</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="page-description">
            <h4 style="color: #1d4ed8; margin-top: 0;">पेज 1: 30 वर्षों की विरासत</h4>
            <p><strong>30 YEARS OF TRUST</strong> - तीन दशकों का विश्वास</p>
            <p>"मिट्टी को सोना बनाते हैं हम" - हमारी प्रतिबद्धता किसानों के साथ</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="page-description">
            <h4 style="color: #1d4ed8; margin-top: 0;">पेज 2: यात्रा का सफर</h4>
            <p><strong>1996 से 2026 तक</strong> - 30 वर्षों की यात्रा</p>
            <p>"THREE DECADES ONE COMMITMENT" - एक ही प्रतिबद्धता, तीन दशक</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Instructions
    st.markdown("""
    ### 🎮 कैसे इस्तेमाल करें:
    1. **पेज स्विच करें**: नीचे दिए गए बटन से पेज 1 और पेज 2 के बीच स्विच करें
    2. **कर्सर घुमाएं**: इमेज पर कर्सर घुमाएं ताकि पृष्ठभूमि दिखाई दे
    3. **ऑटो प्ले**: पेज स्वचालित रूप से हर 10 सेकंड में बदलते रहेंगे
    """)
    
    # Display the two-page cursor reveal effect
    cursor_html = create_two_page_cursor_reveal()
    components.html(cursor_html, height=650, scrolling=False)
    
    st.markdown("---")
    
    # Feature highlights
    st.markdown("### ✨ विशेषताएं:")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **🎯 इंटरएक्टिव डिज़ाइन**
        - कर्सर ट्रैकिंग
        - रियल-टाइम रिवील
        - 3D पैरलैक्स इफेक्ट
        """)
    
    with col2:
        st.markdown("""
        **🔄 मल्टी-पेज नेविगेशन**
        - दो अलग-अलग पेज
        - आसान स्विचिंग
        - ऑटो प्ले मोड
        """)
    
    with col3:
        st.markdown("""
        **🎨 प्रीमियम विज़ुअल्स**
        - गोल्डन थीम
        - स्मूथ ट्रांजिशन
        - प्रोफेशनल टाइपोग्राफी
        """)

# ================= FORM TAB =================
with tab2:
    st.markdown("""
    <div class="two-page-header">
        <h2 style="color: white; margin: 0;">📝 नया प्रोजेक्ट जोड़ें</h2>
        <p style="margin: 10px 0 0 0; opacity: 0.9;">नीचे दिए गए विवरण भरकर एक नया प्रोजेक्ट बनाएं</p>
    </div>
    """, unsafe_allow_html=True)
    
    with st.form("tws_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            email = st.text_input("📧 ईमेल *", placeholder="user@company.com")
            project_code = st.text_input("🔢 प्रोजेक्ट कोड *", placeholder="PRJ-XXXX-YY")
            project_desc = st.text_area("📝 प्रोजेक्ट विवरण *", height=100)
            start_project = st.date_input("📅 प्रोजेक्ट की शुरुआत", date.today())
            platform = st.selectbox(
                "🖥️ प्लेटफॉर्म",
                ["Below 30 HP", "30–60 HP", "60–101 HP", "Above 101 HP"]
            )
            continent = st.text_input("🌍 महाद्वीप / देश", placeholder="उत्तर अमेरिका / USA")
            scr_no = st.text_input("📄 SCR नंबर", placeholder="SCR-XXXX")
            
        with col2:
            scr_issue = st.text_input("🔧 CFT में SCR समस्या", placeholder="क्रॉस-फंक्शनल टीम में चर्चा")
            model = st.text_input("🚜 मॉडल", placeholder="मॉडल नाम/नंबर")
            aggregate = st.selectbox(
                "🔩 एग्रीगेट",
                ["Electrical", "Hydraulic", "Transmission", "Engine", "Vehicle", "Cabin"]
            )
            agg_lead = st.text_input("👨‍💼 एग्रीगेट लीड", placeholder="लीड व्यक्ति का नाम")
            impl_month = st.selectbox(
                "📆 कार्यान्वयन माह",
                ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
            )
            r_and_d = st.selectbox(
                "🔬 R&D PMO",
                ["Mohit Rana", "Arashdeep Parmar"]
            )
        
        st.markdown("---")
        st.markdown("#### 📎 दस्तावेज़ और समयसीमा")
        
        col1, col2 = st.columns(2)
        
        with col1:
            feasibility = st.file_uploader("📎 फ़ीज़िबिलिटी स्टडी", type=['pdf', 'docx', 'doc'])
            g1 = st.date_input("📐 G1 ड्राइंग रिलीज़")
            material = st.date_input("📦 मटेरियल उपलब्धता")
            proto = st.date_input("🔧 प्रोटो फिटमेंट")
            testing = st.date_input("🧪 टेस्टिंग शुरू")
            interim = st.date_input("✅ इंटरिम टेस्टिंग गो अहेड")
            
        with col2:
            g1_orc_drg = st.date_input("🔄 G1 ORC ड्राइंग")
            g1_orc_mat = st.date_input("📦 G1 ORC मटेरियल")
            g1_orc_proto = st.date_input("🔧 G1 ORC प्रोटो")
            g2_go = st.date_input("🚀 G2 गो अहेड")
            g2_mat = st.date_input("📦 G2 मटेरियल")
        
        st.markdown("---")
        st.markdown("#### 🏭 उत्पादन और अनुमोदन")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            tractors = st.text_input("5 ट्रैक्टर ऑनलाइन", placeholder="स्थिति")
            prr = st.text_input("✅ PRR साइन-ऑफ", placeholder="स्थिति")
            pre_ern = st.text_input("📋 प्री ERN", placeholder="विवरण")
            
        with col2:
            go_ern = st.text_input("✅ गो अहेड ERN", placeholder="विवरण")
            bom = st.text_input("📊 BOM परिवर्तन", placeholder="परिवर्तन")
            bcr_no = st.text_input("🔢 BCR नंबर", placeholder="संदर्भ")
            
        with col3:
            bcr_date = st.date_input("📅 BCR तिथि")
            cutoff = st.text_input("✂️ कट-ऑफ नंबर", placeholder="संदर्भ")
        
        submit = st.form_submit_button("🚀 प्रोजेक्ट सबमिट करें", use_container_width=True)
    
    if submit:
        if not email or not project_code or not project_desc:
            st.error("❌ कृपया सभी आवश्यक फ़ील्ड भरें (*)")
        else:
            project_code_str = str(project_code)
            if not df.empty and 'Project Code' in df.columns:
                df['Project Code'] = df['Project Code'].astype(str)
                if project_code_str in df['Project Code'].values:
                    st.warning("⚠️ प्रोजेक्ट कोड पहले से मौजूद है! मौजूदा रिकॉर्ड अपडेट किया जा रहा है...")
                    idx = df[df['Project Code'] == project_code_str].index[0]
                    update_record = True
                else:
                    idx = len(df)
                    update_record = False
            else:
                update_record = False
            
            def format_date(date_val):
                if pd.isna(date_val) or date_val is None:
                    return ""
                return date_val.strftime('%Y-%m-%d') if hasattr(date_val, 'strftime') else str(date_val)
            
            new_data = {
                "Email": str(email),
                "Project Code": project_code_str,
                "Project Description": str(project_desc),
                "Start of Project": format_date(start_project),
                "Platform": str(platform),
                "Continent/Country": str(continent),
                "SCR No": str(scr_no),
                "SCR Issue in CFT": str(scr_issue),
                "Model": str(model),
                "Aggregate": str(aggregate),
                "Aggregate Lead": str(agg_lead),
                "Implementation Month": str(impl_month),
                "R&D PMO": str(r_and_d),
                "Feasibility Uploaded": feasibility.name if feasibility else "",
                "G1 Drg Release": format_date(g1),
                "Material Avl": format_date(material),
                "Proto Fitment": format_date(proto),
                "Testing Start": format_date(testing),
                "Interim Testing Go Ahead": format_date(interim),
                "G1 ORC Drg": format_date(g1_orc_drg),
                "G1 ORC Material": format_date(g1_orc_mat),
                "G1 ORC Proto": format_date(g1_orc_proto),
                "G2 Go Ahead": format_date(g2_go),
                "G2 Material": format_date(g2_mat),
                "5 Tractors Online": str(tractors),
                "PRR Sign-off": str(prr),
                "Pre ERN": str(pre_ern),
                "Go Ahead ERN": str(go_ern),
                "BOM Change": str(bom),
                "BCR Number": str(bcr_no),
                "BCR Date": format_date(bcr_date),
                "Cut-off Number": str(cutoff)
            }
            
            if update_record:
                for key, value in new_data.items():
                    if key in df.columns:
                        df.at[idx, key] = value
                st.success(f"✅ प्रोजेक्ट {project_code} सफलतापूर्वक अपडेट किया गया!")
            else:
                for col in COLUMNS:
                    if col not in new_data:
                        new_data[col] = ""
                
                df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
                st.success(f"✅ नया प्रोजेक्ट {project_code} सफलतापूर्वक जोड़ा गया!")
            
            save_data(df)
            df = load_data()

# ================= DASHBOARD TAB =================
with tab3:
    create_dashboard()

# ================= DATA MANAGEMENT TAB =================
with tab4:
    st.markdown("### 📁 डेटा प्रबंधन केंद्र")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        display_lottie_animation()
    
    mgmt_tab1, mgmt_tab2, mgmt_tab3 = st.tabs(["📊 सभी डेटा देखें और संपादित करें", "📤 Google Sheets से आयात करें", "⚙️ बल्क ऑपरेशन"])
    
    with mgmt_tab1:
        st.markdown("#### 📋 पूर्ण प्रोजेक्ट डेटाबेस")
        
        if not df.empty and len(df) > 0:
            col1, col2 = st.columns([3, 1])
            with col1:
                search_term = st.text_input("🔍 सभी कॉलम में खोजें:", placeholder="खोजने के लिए टाइप करें...", key="search_all")
            
            show_cols = st.multiselect(
                "कॉलम फ़िल्टर करें:",
                options=df.columns.tolist(),
                default=df.columns.tolist()[:min(8, len(df.columns))] if len(df.columns) > 8 else df.columns.tolist(),
                key="filter_cols"
            )
            
            if search_term:
                mask = df.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)
                display_df = df[mask]
            else:
                display_df = df
            
            if not show_cols:
                show_cols = df.columns.tolist()
            
            st.markdown(f"**{len(display_df)} में से {len(df)} रिकॉर्ड दिखा रहा हूं**")
            
            st.dataframe(
                display_df[show_cols],
                width='stretch'
            )
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                if st.button("🔄 डेटा ताज़ा करें", use_container_width=True, key="refresh_all"):
                    df = load_data()
                    st.rerun()
            
            with col2:
                if st.button("📥 CSV में निर्यात करें", use_container_width=True, key="export_csv"):
                    csv = df.to_csv(index=False)
                    st.download_button(
                        label="⬇️ CSV डाउनलोड करें",
                        data=csv,
                        file_name=f"tws_exports_{date.today()}.csv",
                        mime="text/csv",
                        use_container_width=True
                    )
            
            with col3:
                if not df.empty:
                    project_to_delete = st.selectbox(
                        "हटाने के लिए प्रोजेक्ट चुनें:",
                        options=df['Project Code'].astype(str).tolist(),
                        key="delete_select"
                    )
                    
                    if st.button("🗑️ चयनित हटाएं", use_container_width=True, key="delete_btn"):
                        df = df[df['Project Code'].astype(str) != project_to_delete]
                        save_data(df)
                        st.success(f"✅ प्रोजेक्ट {project_to_delete} सफलतापूर्वक हटाया गया!")
                        st.rerun()
        else:
            st.info("📭 कोई डेटा उपलब्ध नहीं है। अपना पहला प्रोजेक्ट जोड़ें या डेटा आयात करें।")
    
    with mgmt_tab2:
        st.markdown("#### 📤 Google Sheets/CSV से आयात करें")
        st.info("अपने डेटाबेस को अपडेट करने के लिए Google Sheets से निर्यात की गई CSV फ़ाइल अपलोड करें।")
        
        uploaded_file = st.file_uploader(
            "CSV फ़ाइल चुनें",
            type=['csv'],
            help="मिलान कॉलम नामों के साथ CSV फ़ाइल अपलोड करें",
            key="csv_uploader"
        )
        
        if uploaded_file is not None:
            try:
                new_data = pd.read_csv(uploaded_file)
                
                st.markdown("##### 📄 फ़ाइल पूर्वावलोकन (पहली 5 पंक्तियाँ):")
                st.dataframe(new_data.head(), width='stretch')
                
                st.markdown(f"**फ़ाइल में {len(new_data)} पंक्तियाँ और {len(new_data.columns)} कॉलम हैं**")
                
                if 'Project Code' not in new_data.columns:
                    st.error("❌ CSV में 'Project Code' कॉलम होना चाहिए!")
                else:
                    st.markdown("##### 🔄 कॉलम मैपिंग")
                    mapping_df = pd.DataFrame({
                        'CSV कॉलम': new_data.columns,
                        'डेटाबेस कॉलम': [col if col in COLUMNS else '❌ कोई मेल नहीं' for col in new_data.columns]
                    })
                    st.dataframe(mapping_df, width='stretch')
                    
                    st.markdown("##### ⚙️ आयात विकल्प")
                    
                    import_mode = st.radio(
                        "आयात मोड चुनें:",
                        ["मौजूदा अपडेट करें और नया जोड़ें", "पूरा डेटाबेस बदलें", "केवल नया जोड़ें"],
                        key="import_mode"
                    )
                    
                    conflict_resolution = st.radio(
                        "यदि प्रोजेक्ट मौजूद है:",
                        ["नए डेटा से अपडेट करें", "मौजूदा डेटा रखें", "रिकॉर्ड छोड़ें"],
                        key="conflict_res"
                    )
                    
                    if st.button("🚀 आयात प्रोसेस करें", use_container_width=True, key="process_import"):
                        with st.spinner("आयात प्रोसेस किया जा रहा है..."):
                            if import_mode == "पूरा डेटाबेस बदलें":
                                df = new_data
                                save_data(df)
                                st.success("✅ डेटाबेस सफलतापूर्वक बदल दिया गया!")
                            
                            else:
                                updated_count = 0
                                added_count = 0
                                skipped_count = 0
                                
                                new_data['Project Code'] = new_data['Project Code'].astype(str)
                                if not df.empty:
                                    df['Project Code'] = df['Project Code'].astype(str)
                                
                                for idx, row in new_data.iterrows():
                                    project_code = str(row.get('Project Code', ''))
                                    
                                    if not df.empty and project_code in df['Project Code'].values:
                                        if import_mode == "मौजूदा अपडेट करें और नया जोड़ें":
                                            if conflict_resolution == "नए डेटा से अपडेट करें":
                                                db_idx = df[df['Project Code'] == project_code].index[0]
                                                for col in new_data.columns:
                                                    if col in df.columns and pd.notna(row[col]):
                                                        df.at[db_idx, col] = row[col]
                                                updated_count += 1
                                            elif conflict_resolution == "रिकॉर्ड छोड़ें":
                                                skipped_count += 1
                                            else:
                                                skipped_count += 1
                                    else:
                                        if import_mode in ["मौजूदा अपडेट करें और नया जोड़ें", "केवल नया जोड़ें"]:
                                            new_row = {}
                                            for col in COLUMNS:
                                                if col in new_data.columns:
                                                    new_row[col] = row[col] if pd.notna(row.get(col)) else ""
                                                else:
                                                    new_row[col] = ""
                                            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
                                            added_count += 1
                                
                                save_data(df)
                                
                                st.success(f"""
                                ✅ **आयात पूरा हुआ!**
                                
                                **सारांश:**
                                - 📝 अपडेट किए गए रिकॉर्ड: **{updated_count}**
                                - ➕ नए रिकॉर्ड जोड़े गए: **{added_count}**
                                - ⏭️ छोड़े गए रिकॉर्ड: **{skipped_count}**
                                - 📊 अब कुल रिकॉर्ड: **{len(df)}**
                                """)
                        
                        st.rerun()
            
            except Exception as e:
                st.error(f"❌ फ़ाइल पढ़ने में त्रुटि: {str(e)}")
    
    with mgmt_tab3:
        st.markdown("#### ⚙️ बल्क ऑपरेशन")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### 🗑️ हटाने के ऑपरेशन")
            
            if not df.empty:
                st.markdown("**प्रोजेक्ट कोड से हटाएं:**")
                projects_to_delete = st.multiselect(
                    "हटाने के लिए प्रोजेक्ट चुनें:",
                    options=df['Project Code'].astype(str).tolist(),
                    help="हटाने के लिए प्रोजेक्ट चुनें",
                    key="bulk_delete"
                )
                
                if projects_to_delete and st.button("🗑️ चयनित प्रोजेक्ट हटाएं", use_container_width=True, key="bulk_delete_btn"):
                    df = df[~df['Project Code'].astype(str).isin(projects_to_delete)]
                    save_data(df)
                    st.success(f"✅ {len(projects_to_delete)} प्रोजेक्ट हटाए गए!")
                    st.rerun()
                
                st.markdown("**डुप्लिकेट साफ़ करें:**")
                if st.button("🔍 डुप्लिकेट ढूंढें और हटाएं", use_container_width=True, key="remove_dups"):
                    if not df.empty and 'Project Code' in df.columns:
                        duplicates = df.duplicated(subset=['Project Code'], keep='first')
                        if duplicates.any():
                            st.warning(f"{duplicates.sum()} डुप्लिकेट प्रोजेक्ट कोड मिले!")
                            df = df.drop_duplicates(subset=['Project Code'], keep='first')
                            save_data(df)
                            st.success("✅ डुप्लिकेट हटाए गए!")
                        else:
                            st.info("✅ कोई डुप्लिकेट नहीं मिला!")
        
        with col2:
            st.markdown("##### 🔄 बल्क अपडेट")
            
            if not df.empty:
                st.markdown("**कई प्रोजेक्ट के लिए फ़ील्ड अपडेट करें:**")
                update_field = st.selectbox(
                    "अपडेट करने के लिए फ़ील्ड चुनें:",
                    options=[col for col in df.columns if col not in ['Project Code', 'Email']],
                    key="batch_field"
                )
                
                update_value = st.text_input(f"{update_field} के लिए नया मान:", placeholder="नया मान दर्ज करें...", key="batch_value")
                
                projects_to_update = st.multiselect(
                    "अपडेट करने के लिए प्रोजेक्ट चुनें:",
                    options=df['Project Code'].astype(str).tolist(),
                    key="batch_projects"
                )
                
                if update_value and projects_to_update and st.button("🔄 बल्क अपडेट लागू करें", use_container_width=True, key="batch_update_btn"):
                    df.loc[df['Project Code'].astype(str).isin(projects_to_update), update_field] = update_value
                    save_data(df)
                    st.success(f"✅ {len(projects_to_update)} प्रोजेक्ट अपडेट किए गए!")
                    st.rerun()
        
        st.markdown("---")
        st.markdown("##### 🚨 डेटाबेस प्रबंधन")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("📊 डेटाबेस बैकअप", use_container_width=True, key="backup_btn"):
                backup_file = f"tws_backup_{date.today()}.csv"
                df.to_csv(backup_file, index=False)
                st.success(f"✅ बैकअप {backup_file} के रूप में सहेजा गया")
        
        with col2:
            if st.button("🧹 सभी डेटा साफ़ करें", use_container_width=True, key="clear_all"):
                confirm = st.checkbox("⚠️ मैं समझता हूं कि यह स्थायी रूप से सभी डेटा हटा देगा", key="confirm_clear")
                if confirm:
                    df = pd.DataFrame(columns=COLUMNS)
                    save_data(df)
                    st.error("🗑️ सभी डेटा साफ़ किया गया!")
                    st.rerun()
        
        with col3:
            if st.button("🔍 डेटा मान्य करें", use_container_width=True, key="validate_btn"):
                if not df.empty:
                    missing_email = df['Email'].isna().sum() if 'Email' in df.columns else 0
                    missing_code = df['Project Code'].isna().sum() if 'Project Code' in df.columns else 0
                    
                    if missing_email + missing_code == 0:
                        st.success("✅ सभी डेटा वैध है!")
                    else:
                        st.warning(f"""
                        ⚠️ **डेटा समस्याएं मिलीं:**
                        - लापता ईमेल: {missing_email}
                        - लापता प्रोजेक्ट कोड: {missing_code}
                        """)

# ================= SIDEBAR =================
with st.sidebar:
    lottie_sidebar = """
    <script src="https://unpkg.com/@lottiefiles/dotlottie-wc@0.8.11/dist/dotlottie-wc.js" type="module"></script>
    <dotlottie-wc src="https://lottie.host/8dd2e6af-9e9a-4464-ad99-41e7c2a723e2/AzY19wIzNy.lottie" style="width: 80px; height: 80px" autoplay loop></dotlottie-wc>
    """
    components.html(lottie_sidebar, height=100)
    
    st.markdown("### TWS एक्सपोर्ट्स")
    st.markdown("**प्रोजेक्ट प्रबंधन**")
    
    st.markdown("---")
    
    st.markdown("### 📈 त्वरित आंकड़े")
    if not df.empty and len(df) > 0:
        total_projects = len(df)
        active_this_month = len(df[df['Implementation Month'].str.strip().str.lower() == pd.Timestamp.now().strftime('%b').lower()]) if 'Implementation Month' in df.columns else 0
        g1_complete = df['G1 Drg Release'].notna().sum() if 'G1 Drg Release' in df.columns else 0
        
        st.metric("कुल प्रोजेक्ट", total_projects)
        st.metric("इस माह सक्रिय", active_this_month)
        st.metric("G1 पूर्ण", g1_complete)
    else:
        st.info("अभी तक कोई डेटा नहीं")
    
    st.markdown("---")
    
    st.markdown("### ⚡ त्वरित क्रियाएं")
    if st.button("➕ नया प्रोजेक्ट जोड़ें", use_container_width=True, key="sidebar_new"):
        st.session_state.current_tab = "📝 Data Entry Form"
        st.rerun()
    
    if not df.empty:
        csv = df.to_csv(index=False)
        st.download_button(
            label="📥 डेटा निर्यात करें",
            data=csv,
            file_name="tws_exports.csv",
            mime="text/csv",
            use_container_width=True,
            key="sidebar_export"
        )
    
    st.markdown("---")
    
    st.markdown("### 📅 हाल की गतिविधि")
    if not df.empty and len(df) > 0:
        try:
            if 'Start of Project' in df.columns:
                df_recent = df.copy()
                df_recent['Start of Project'] = pd.to_datetime(df_recent['Start of Project'], errors='coerce')
                recent = df_recent.sort_values('Start of Project', ascending=False).head(3)
            else:
                recent = df.head(3)
            
            for _, row in recent.iterrows():
                project_code = str(row.get('Project Code', 'N/A'))
                platform = str(row.get('Platform', 'N/A'))
                aggregate = str(row.get('Aggregate', 'N/A'))
                st.markdown(f"**{project_code}**")
                st.markdown(f"*{platform} - {aggregate}*")
                st.markdown("---")
        except:
            st.info("हाल की गतिविधि लोड नहीं की जा सकी")
    
    st.markdown("---")
    
    st.markdown("#### 📊 डेटाबेस जानकारी")
    if not df.empty:
        st.markdown(f"""
        - **आकार:** {len(df)} रिकॉर्ड
        - **अंतिम अपडेट:** {date.today()}
        - **कॉलम:** {len(df.columns)}
        """)