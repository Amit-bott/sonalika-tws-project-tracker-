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






















import streamlit as st
import pandas as pd
from datetime import date
import plotly.express as px
import plotly.graph_objects as go
from io import StringIO
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

# ================= LOTTIE ANIMATION (for dashboard & sidebar) =================
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
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        total_projects = len(df)
        st.metric("Total Projects", total_projects,
                  delta=f"+{len(df[df['Start of Project'] == pd.Timestamp(date.today()).strftime('%Y-%m-%d')])} today" if total_projects > 0 else None)
    with col2:
        g1_completed = df["G1 Drg Release"].notna().sum()
        completion_rate = (g1_completed / total_projects * 100) if total_projects > 0 else 0
        st.metric("G1 Completed", g1_completed, delta=f"{completion_rate:.1f}%")
    with col3:
        g2_completed = df["G2 Go Ahead"].notna().sum()
        g2_rate = (g2_completed / total_projects * 100) if total_projects > 0 else 0
        st.metric("G2 Completed", g2_completed, delta=f"{g2_rate:.1f}%")
    with col4:
        active_projects = len(df[df['Implementation Month'].str.strip().str.lower() == pd.Timestamp.now().strftime('%b').lower()]) if 'Implementation Month' in df.columns else 0
        st.metric("Active This Month", active_projects)
    
    st.markdown("---")
    
    if not df.empty:
        col1, col2 = st.columns(2)
        with col1:
            if 'Platform' in df.columns:
                platform_counts = df['Platform'].value_counts()
                fig = go.Figure(data=[go.Bar(x=platform_counts.index, y=platform_counts.values,
                                              marker_color='#2563eb', text=platform_counts.values, textposition='auto')])
                fig.update_layout(title='Projects by Platform', paper_bgcolor='white', plot_bgcolor='white',
                                  font=dict(color='#1e40af'), height=400)
                st.plotly_chart(fig, use_container_width=True)
        with col2:
            if 'Aggregate' in df.columns:
                aggregate_counts = df['Aggregate'].value_counts()
                fig = go.Figure(data=[go.Pie(labels=aggregate_counts.index, values=aggregate_counts.values, hole=.3,
                                             marker=dict(colors=['#2563eb', '#1d4ed8', '#1e40af', '#3730a3', '#312e81']))])
                fig.update_layout(title='Projects by Aggregate Type', paper_bgcolor='white', plot_bgcolor='white',
                                  font=dict(color='#1e40af'), height=400)
                st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("### 📋 Recent Projects")
    if not df.empty:
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
        st.dataframe(recent_df[display_cols], width='stretch')
    else:
        st.info("No projects available. Add your first project in the Data Entry tab.")

# ================= MAIN =================
# ========= HEADER WITH 300px LOTTIE + CENTERED TITLE (NO SCROLL) =========
col1, col2 = st.columns([1, 3])

with col1:
    components.html("""
    <script src="https://unpkg.com/@lottiefiles/dotlottie-wc@0.8.11/dist/dotlottie-wc.js" type="module"></script>
    <dotlottie-wc
      src="https://lottie.host/8dd2e6af-9e9a-4464-ad99-41e7c2a723e2/AzY19wIzNy.lottie"
      style="width: 200px; height: 200px"
      autoplay
      loop
    ></dotlottie-wc>
    """, height=320)

with col2:
    # Centered title – marquee removed
    # st.markdown('<h2 style="text-align: center;">TWS Project – Exports Management</h2>', unsafe_allow_html=True)
    st.markdown('<h1 style="text-align: center; font-size: 48px; font-weight: 800; background: linear-gradient(135deg, #2563eb, #1d4ed8); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 5px;">TWS Project – Exports Management</h1>', unsafe_allow_html=True)
    # st.markdown("**Professional Project Tracking System**")

tab1, tab2, tab3 = st.tabs(["📝 Data Entry Form", "📊 Dashboard", "📁 Data Management"])

# ================= FORM TAB =================
with tab1:
    st.markdown("### ✨ New Project Entry")
    
    with st.form("tws_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            email = st.text_input("📧 Email *", placeholder="user@company.com")
            project_code = st.text_input("🔢 Project Code *", placeholder="PRJ-XXXX-YY")
            project_desc = st.text_area("📝 Project Description *", height=100)
            start_project = st.date_input("📅 Start of Project", date.today())
            
            # ----- Platform selection with key for dynamic default -----
            platform = st.selectbox(
                "🖥️ Platform",
                ["Below 30 HP", "30–60 HP", "60–101 HP", "Above 101 HP"],
                key="platform_select"
            )
            
            continent = st.text_input("🌍 Continent / Country", placeholder="North America / USA")
            scr_no = st.text_input("📄 SCR Number", placeholder="SCR-XXXX")
            
        with col2:
            scr_issue = st.text_input("🔧 SCR Issue in CFT", placeholder="Issue discussed in cross-functional team")
            model = st.text_input("🚜 Model", placeholder="Model name/number")
            aggregate = st.selectbox(
                "🔩 Aggregate",
                ["Electrical", "Hydraulic", "Transmission", "Engine", "Vehicle", "Cabin"]
            )
            agg_lead = st.text_input("👨‍💼 Aggregate Lead", placeholder="Lead person name")

            imp_month = st.date_input("📅 Implementation Month", date.today())
            
            # ----- R&D PMO with dynamic default based on platform -----
            r_and_d_options = ["Mohit Rana", "Arashdeep Parmar"]
            # Read current platform from session state
            current_platform = st.session_state.get("platform_select", "Below 30 HP")
            if "30–60 HP" in current_platform:
                default_rnd = "Mohit Rana"
            elif "60–101 HP" in current_platform:
                default_rnd = "Arashdeep Parmar"
            else:
                default_rnd = "Mohit Rana"   # fallback
            rnd_index = r_and_d_options.index(default_rnd) if default_rnd in r_and_d_options else 0
            
            r_and_d = st.selectbox(
                "🔬 R&D PMO",
                r_and_d_options,
                index=rnd_index
            )
#         current_platform = st.selectbox(
#     "🖥️ Platform",
#     ["Below 30 HP", "30–60 HP", "60–110 HP", "Above 110 HP"],
#     key="platform"
# )
#         PLATFORM_TO_PMO = {
#     "30–60 HP": "Mohit Rana",
#     "60–110 HP": "Arashdeep Parmar"
# }
# # Initialize PMO only once
#         if "rnd_pmo" not in st.session_state:
#          st.session_state.rnd_pmo = PLATFORM_TO_PMO.get(platform, "Mohit Rana")

# # Update PMO whenever platform changes
#         if platform in PLATFORM_TO_PMO:
#          st.session_state.rnd_pmo = PLATFORM_TO_PMO[platform]

#          r_and_d = st.selectbox(
#     "🔬 R&D PMO",
#     ["Mohit Rana", "Arashdeep Parmar"],
#     key="rnd_pmo"
# )



        st.markdown("---")
        st.markdown("#### 📎 Documents & Timeline")
        
        col1, col2 = st.columns(2)
        with col1:
            feasibility = st.file_uploader("📎 Feasibility Study", type=['pdf', 'docx', 'doc'])
            g1 = st.date_input("📐 G1 Drg Release")
            material = st.date_input("📦 Material Avl")
            proto = st.date_input("🔧 Proto Fitment")
            testing = st.date_input("🧪 Testing Start")
            interim = st.date_input("✅ Interim Testing Go Ahead")
        with col2:
            g1_orc_drg = st.date_input("🔄 G1 ORC Drg")
            g1_orc_mat = st.date_input("📦 G1 ORC Material")
            g1_orc_proto = st.date_input("🔧 G1 ORC Proto")
            g2_go = st.date_input("🚀 G2 Go Ahead")
            g2_mat = st.date_input("📦 G2 Material")
        
        st.markdown("---")
        st.markdown("#### 🏭 Production & Approvals")
        col1, col2, col3 = st.columns(3)
        with col1:
            bcr_no = st.text_input("🔢 BCR Number", placeholder="Reference")
            bcr_date = st.date_input("📅 BCR Date")
            cutoff = st.text_input("✂️ Cut-off Number", placeholder="Reference")
        
        submit = st.form_submit_button("🚀 Submit Project", use_container_width=True)
    
    if submit:
        if not email or not project_code or not project_desc:
            st.error("❌ Please fill all required fields (*)")
        else:
            project_code_str = str(project_code)
            if not df.empty and 'Project Code' in df.columns:
                df['Project Code'] = df['Project Code'].astype(str)
                if project_code_str in df['Project Code'].values:
                    st.warning("⚠️ Project Code already exists! Updating existing record...")
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
                "Implementation Month": format_date(imp_month),
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
                "BCR Number": str(bcr_no),
                "BCR Date": format_date(bcr_date),
                "Cut-off Number": str(cutoff)
            }
            
            if update_record:
                for key, value in new_data.items():
                    if key in df.columns:
                        df.at[idx, key] = value
                st.success(f"✅ Project {project_code} updated successfully!")
            else:
                for col in COLUMNS:
                    if col not in new_data:
                        new_data[col] = ""
                df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
                st.success(f"✅ New project {project_code} added successfully!")
            
            save_data(df)
            df = load_data()

# ================= DASHBOARD TAB =================
with tab2:
    create_dashboard()

# ================= DATA MANAGEMENT TAB =================
with tab3:
    st.markdown("### 📁 Data Management Center")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        display_lottie_animation()
    
    mgmt_tab1, mgmt_tab2, mgmt_tab3 = st.tabs(["📊 View & Edit All Data", "📤 Import from Google Sheets", "⚙️ Bulk Operations"])
    
    with mgmt_tab1:
        st.markdown("#### 📋 Complete Project Database")
        if not df.empty:
            col1, col2 = st.columns([3, 1])
            with col1:
                search_term = st.text_input("🔍 Search across all columns:", placeholder="Type to search...", key="search_all")
            show_cols = st.multiselect(
                "Filter Columns:",
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
            st.markdown(f"**Showing {len(display_df)} of {len(df)} records**")
            st.dataframe(display_df[show_cols], width='stretch')
            
            col1, col2, col3 = st.columns(3)
            with col1:
                if st.button("🔄 Refresh Data", use_container_width=True, key="refresh_all"):
                    df = load_data()
                    st.rerun()
            with col2:
                if st.button("📥 Export to CSV", use_container_width=True, key="export_csv"):
                    csv = df.to_csv(index=False)
                    st.download_button(label="⬇️ Download CSV", data=csv,
                                       file_name=f"tws_exports_{date.today()}.csv", mime="text/csv", use_container_width=True)
            with col3:
                if not df.empty:
                    project_to_delete = st.selectbox("Select project to delete:", options=df['Project Code'].astype(str).tolist(), key="delete_select")
                    if st.button("🗑️ Delete Selected", use_container_width=True, key="delete_btn"):
                        df = df[df['Project Code'].astype(str) != project_to_delete]
                        save_data(df)
                        st.success(f"✅ Project {project_to_delete} deleted successfully!")
                        st.rerun()
        else:
            st.info("📭 No data available. Add your first project or import data.")
    
    with mgmt_tab2:
        st.markdown("#### 📤 Import from Google Sheets/CSV")
        st.info("Upload a CSV file exported from Google Sheets to update your database.")
        uploaded_file = st.file_uploader("Choose a CSV file", type=['csv'], help="Upload CSV file with matching column names", key="csv_uploader")
        if uploaded_file is not None:
            try:
                new_data = pd.read_csv(uploaded_file)
                st.markdown("##### 📄 File Preview (First 5 rows):")
                st.dataframe(new_data.head(), width='stretch')
                st.markdown(f"**File contains {len(new_data)} rows and {len(new_data.columns)} columns**")
                if 'Project Code' not in new_data.columns:
                    st.error("❌ CSV must contain 'Project Code' column!")
                else:
                    st.markdown("##### 🔄 Column Mapping")
                    mapping_df = pd.DataFrame({
                        'CSV Columns': new_data.columns,
                        'Database Columns': [col if col in COLUMNS else '❌ No match' for col in new_data.columns]
                    })
                    st.dataframe(mapping_df, width='stretch')
                    st.markdown("##### ⚙️ Import Options")
                    import_mode = st.radio("Select import mode:", ["Update Existing & Add New", "Replace Entire Database", "Add New Only"], key="import_mode")
                    conflict_resolution = st.radio("If project exists:", ["Update with new data", "Keep existing data", "Skip record"], key="conflict_res")
                    if st.button("🚀 Process Import", use_container_width=True, key="process_import"):
                        with st.spinner("Processing import..."):
                            if import_mode == "Replace Entire Database":
                                df = new_data
                                save_data(df)
                                st.success("✅ Database replaced successfully!")
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
                                        if import_mode == "Update Existing & Add New":
                                            if conflict_resolution == "Update with new data":
                                                db_idx = df[df['Project Code'] == project_code].index[0]
                                                for col in new_data.columns:
                                                    if col in df.columns and pd.notna(row[col]):
                                                        df.at[db_idx, col] = row[col]
                                                updated_count += 1
                                            elif conflict_resolution == "Skip record":
                                                skipped_count += 1
                                            else:
                                                skipped_count += 1
                                    else:
                                        if import_mode in ["Update Existing & Add New", "Add New Only"]:
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
                                ✅ **Import Completed!**
                                **Summary:**
                                - 📝 Records updated: **{updated_count}**
                                - ➕ New records added: **{added_count}**
                                - ⏭️ Records skipped: **{skipped_count}**
                                - 📊 Total records now: **{len(df)}**
                                """)
                        st.rerun()
            except Exception as e:
                st.error(f"❌ Error reading file: {str(e)}")
    
    with mgmt_tab3:
        st.markdown("#### ⚙️ Bulk Operations")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("##### 🗑️ Delete Operations")
            if not df.empty:
                st.markdown("**Delete by Project Code:**")
                projects_to_delete = st.multiselect("Select projects to delete:", options=df['Project Code'].astype(str).tolist(), help="Select projects to delete", key="bulk_delete")
                if projects_to_delete and st.button("🗑️ Delete Selected Projects", use_container_width=True, key="bulk_delete_btn"):
                    df = df[~df['Project Code'].astype(str).isin(projects_to_delete)]
                    save_data(df)
                    st.success(f"✅ Deleted {len(projects_to_delete)} projects!")
                    st.rerun()
                st.markdown("**Clean Duplicates:**")
                if st.button("🔍 Find & Remove Duplicates", use_container_width=True, key="remove_dups"):
                    if not df.empty and 'Project Code' in df.columns:
                        duplicates = df.duplicated(subset=['Project Code'], keep='first')
                        if duplicates.any():
                            st.warning(f"Found {duplicates.sum()} duplicate project codes!")
                            df = df.drop_duplicates(subset=['Project Code'], keep='first')
                            save_data(df)
                            st.success("✅ Duplicates removed!")
                        else:
                            st.info("✅ No duplicates found!")
        with col2:
            st.markdown("##### 🔄 Batch Update")
            if not df.empty:
                st.markdown("**Update Field for Multiple Projects:**")
                update_field = st.selectbox("Select field to update:", options=[col for col in df.columns if col not in ['Project Code', 'Email']], key="batch_field")
                update_value = st.text_input(f"New value for {update_field}:", placeholder="Enter new value...", key="batch_value")
                projects_to_update = st.multiselect("Select projects to update:", options=df['Project Code'].astype(str).tolist(), key="batch_projects")
                if update_value and projects_to_update and st.button("🔄 Apply Batch Update", use_container_width=True, key="batch_update_btn"):
                    df.loc[df['Project Code'].astype(str).isin(projects_to_update), update_field] = update_value
                    save_data(df)
                    st.success(f"✅ Updated {len(projects_to_update)} projects!")
                    st.rerun()
        
        st.markdown("---")
        st.markdown("##### 🚨 Database Management")
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("📊 Backup Database", use_container_width=True, key="backup_btn"):
                backup_file = f"tws_backup_{date.today()}.csv"
                df.to_csv(backup_file, index=False)
                st.success(f"✅ Backup saved as {backup_file}")
        with col2:
            if st.button("🧹 Clear All Data", use_container_width=True, key="clear_all"):
                confirm = st.checkbox("⚠️ I understand this will delete ALL data permanently", key="confirm_clear")
                if confirm:
                    df = pd.DataFrame(columns=COLUMNS)
                    save_data(df)
                    st.error("🗑️ All data cleared!")
                    st.rerun()
        with col3:
            if st.button("🔍 Validate Data", use_container_width=True, key="validate_btn"):
                if not df.empty:
                    missing_email = df['Email'].isna().sum() if 'Email' in df.columns else 0
                    missing_code = df['Project Code'].isna().sum() if 'Project Code' in df.columns else 0
                    if missing_email + missing_code == 0:
                        st.success("✅ All data is valid!")
                    else:
                        st.warning(f"""
                        ⚠️ **Data Issues Found:**
                        - Missing Email: {missing_email}
                        - Missing Project Code: {missing_code}
                        """)

# ================= SIDEBAR =================
with st.sidebar:
    lottie_sidebar = """
    <script src="https://unpkg.com/@lottiefiles/dotlottie-wc@0.8.11/dist/dotlottie-wc.js" type="module"></script>
    <dotlottie-wc src="https://lottie.host/8dd2e6af-9e9a-4464-ad99-41e7c2a723e2/AzY19wIzNy.lottie" style="width: 80px; height: 80px" autoplay loop></dotlottie-wc>
    """
    components.html(lottie_sidebar, height=100)
    
    st.markdown("### TWS Exports")
    st.markdown("**Project Management**")
    st.markdown("---")
    st.markdown("### 📈 Quick Stats")
    if not df.empty:
        total_projects = len(df)
        active_this_month = len(df[df['Implementation Month'].str.strip().str.lower() == pd.Timestamp.now().strftime('%b').lower()]) if 'Implementation Month' in df.columns else 0
        g1_complete = df['G1 Drg Release'].notna().sum() if 'G1 Drg Release' in df.columns else 0
        st.metric("Total Projects", total_projects)
        st.metric("Active This Month", active_this_month)
        st.metric("G1 Complete", g1_complete)
    else:
        st.info("No data yet")
    st.markdown("---")
    st.markdown("### ⚡ Quick Actions")
    if st.button("➕ Add New Project", use_container_width=True, key="sidebar_new"):
        st.session_state.current_tab = "📝 Data Entry Form"
        st.rerun()
    if not df.empty:
        csv = df.to_csv(index=False)
        st.download_button(label="📥 Export Data", data=csv, file_name="tws_exports.csv", mime="text/csv", use_container_width=True, key="sidebar_export")
    st.markdown("---")
    st.markdown("### 📅 Recent Activity")
    if not df.empty:
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
            st.info("Could not load recent activity")
    st.markdown("---")
    st.markdown("#### 📊 Database Info")
    if not df.empty:
        st.markdown(f"""
        - **Size:** {len(df)} records
        - **Last Updated:** {date.today()}
        - **Columns:** {len(df.columns)}
        """)
















