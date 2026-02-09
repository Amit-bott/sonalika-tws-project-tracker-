# import streamlit as st
# import pandas as pd
# import os

# FILE_NAME = "tws_project_data.csv"

# st.set_page_config(
#     page_title="TWS Project Tracking System",
#     layout="wide"
# )

# st.title("📊 TWS Project Tracking System")
# st.caption("Enterprise Google Form Alternative | Add • Update • Delete")

# COLUMNS = [
#     "Email",
#     "Project Code",
#     "Project Description",
#     "Start of Project",
#     "Platform (HP)",
#     "Continent",
#     "Country",
#     "Model",
#     "Aggregate",
#     "Implementation Month",
#     "BCR No",
#     "Cut-off No",
#     "Milestone G1",
#     "Milestone G2",
#     "PRR",
#     "BOM",
#     "SPC",
#     "Status",
#     "Remarks"
# ]

# # Load / Create Data
# if os.path.exists(FILE_NAME):
#     df = pd.read_csv(FILE_NAME)
# else:
#     df = pd.DataFrame(columns=COLUMNS)

# menu = st.sidebar.radio(
#     "Navigation",
#     ["➕ Add Project", "📋 View / Update / Delete"]
# )

# # ---------------- ADD PROJECT ----------------
# if menu == "➕ Add Project":
#     with st.form("add_form"):
#         col1, col2, col3 = st.columns(3)

#         with col1:
#             email = st.text_input("Email")
#             project_code = st.text_input("Project Code")
#             start_project = st.date_input("Start of Project")
#             platform = st.selectbox(
#                 "Platform (HP)",
#                 ["Below 30 HP", "30–60 HP", "60–101 HP", "Above 101 HP"]
#             )

#         with col2:
#             project_desc = st.text_area("Project Description")
#             continent = st.text_input("Continent")
#             country = st.text_input("Country")
#             model = st.text_input("Model")

#         with col3:
#             aggregate = st.selectbox(
#                 "Aggregate",
#                 ["Electrical", "Hydraulic", "Transmission", "Engine", "Vehicle", "Cabin"]
#             )
#             impl_month = st.selectbox(
#                 "Implementation Month",
#                 ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
#             )
#             bcr = st.text_input("BCR No")
#             cutoff = st.text_input("Cut-off No")

#         col4, col5, col6 = st.columns(3)

#         with col4:
#             g1 = st.text_input("Milestone G1")
#             g2 = st.text_input("Milestone G2")

#         with col5:
#             prr = st.text_input("PRR")
#             bom = st.text_input("BOM")

#         with col6:
#             spc = st.text_input("SPC")
#             status = st.selectbox(
#                 "Status",
#                 ["Planned", "In Progress", "Completed", "Hold"]
#             )

#         remarks = st.text_area("Remarks")

#         submit = st.form_submit_button("✅ Submit Project")

#         if submit:
#             new_row = {
#                 "Email": email,
#                 "Project Code": project_code,
#                 "Project Description": project_desc,
#                 "Start of Project": start_project,
#                 "Platform (HP)": platform,
#                 "Continent": continent,
#                 "Country": country,
#                 "Model": model,
#                 "Aggregate": aggregate,
#                 "Implementation Month": impl_month,
#                 "BCR No": bcr,
#                 "Cut-off No": cutoff,
#                 "Milestone G1": g1,
#                 "Milestone G2": g2,
#                 "PRR": prr,
#                 "BOM": bom,
#                 "SPC": spc,
#                 "Status": status,
#                 "Remarks": remarks
#             }

#             df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
#             df.to_csv(FILE_NAME, index=False)
#             st.success("✅ Project added successfully")

# # ---------------- VIEW / UPDATE / DELETE ----------------
# if menu == "📋 View / Update / Delete":
#     st.subheader("📋 Project Records")
#     st.dataframe(df, use_container_width=True)

#     if not df.empty:
#         index = st.selectbox("Select Project Row", df.index)

#         st.markdown("### ✏ Edit Project")

#         for col in COLUMNS:
#             if col in ["Project Description", "Remarks"]:
#                 df.at[index, col] = st.text_area(col, df.at[index, col])
#             else:
#                 df.at[index, col] = st.text_input(col, str(df.at[index, col]))

#         colA, colB = st.columns(2)

#         if colA.button("💾 Update Project"):
#             df.to_csv(FILE_NAME, index=False)
#             st.success("✅ Project updated")

#         if colB.button("🗑 Delete Project"):
#             df = df.drop(index)
#             df.to_csv(FILE_NAME, index=False)
#             st.warning("❌ Project deleted")












# import streamlit as st
# import pandas as pd
# import os

# FILE = "tws_responses.csv"

# st.set_page_config(
#     page_title="TWS Project Tracking System",
#     layout="centered"
# )

# # ---------- CSS (Google Form Look) ----------
# st.markdown("""
# <style>
# body {
#     background-color: #f1f3f4;
# }
# .form-card {
#     background: white;
#     padding: 30px;
#     border-radius: 8px;
#     margin-bottom: 20px;
#     box-shadow: 0 1px 3px rgba(0,0,0,0.15);
# }
# .title {
#     font-size: 28px;
#     font-weight: 600;
# }
# .desc {
#     color: #5f6368;
#     margin-bottom: 20px;
# }
# </style>
# """, unsafe_allow_html=True)

# # ---------- Load Data ----------
# if os.path.exists(FILE):
#     df = pd.read_csv(FILE)
# else:
#     df = pd.DataFrame(columns=[
#         "Email","Project Code","Project Description","Start of Project",
#         "Platform","Continent","Country","Model","Aggregate",
#         "Implementation Month","BCR No","Cut-off No",
#         "G1","G2","PRR","BOM","SPC","Status","Remarks"
#     ])

# # ---------- Tabs (Questions / Responses) ----------
# tab1, tab2 = st.tabs(["📝 Questions", "📊 Responses"])

# # ================= QUESTIONS =================
# with tab1:
#     st.markdown('<div class="form-card">', unsafe_allow_html=True)
#     st.markdown('<div class="title">TWS Project Tracking System</div>', unsafe_allow_html=True)
#     st.markdown(
#         '<div class="desc">Please fill project & export details. All fields are important.</div>',
#         unsafe_allow_html=True
#     )

#     with st.form("project_form"):
#         email = st.text_input("Email *")
#         project_code = st.text_input("Project Code *")
#         project_desc = st.text_area("Project Description *")
#         start_date = st.date_input("Start of Project *")

#         platform = st.selectbox(
#             "Platform (HP) *",
#             ["Below 30 HP","30–60 HP","60–101 HP","Above 101 HP"]
#         )

#         continent = st.text_input("Continent *")
#         country = st.text_input("Country *")
#         model = st.text_input("Model *")

#         aggregate = st.selectbox(
#             "Aggregate *",
#             ["Electrical","Hydraulic","Transmission","Engine","Vehicle","Cabin"]
#         )

#         impl_month = st.selectbox(
#             "Implementation Month *",
#             ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
#         )

#         bcr = st.text_input("BCR No")
#         cutoff = st.text_input("Cut-off No")

#         g1 = st.text_input("G1 Milestone")
#         g2 = st.text_input("G2 Milestone")
#         prr = st.text_input("PRR")
#         bom = st.text_input("BOM")
#         spc = st.text_input("SPC")

#         status = st.selectbox(
#             "Status *",
#             ["Planned","In Progress","Completed","Hold"]
#         )

#         remarks = st.text_area("Remarks")

#         submit = st.form_submit_button("Submit")

#     if submit:
#         new = {
#             "Email": email,
#             "Project Code": project_code,
#             "Project Description": project_desc,
#             "Start of Project": start_date,
#             "Platform": platform,
#             "Continent": continent,
#             "Country": country,
#             "Model": model,
#             "Aggregate": aggregate,
#             "Implementation Month": impl_month,
#             "BCR No": bcr,
#             "Cut-off No": cutoff,
#             "G1": g1,
#             "G2": g2,
#             "PRR": prr,
#             "BOM": bom,
#             "SPC": spc,
#             "Status": status,
#             "Remarks": remarks
#         }

#         df = pd.concat([df, pd.DataFrame([new])], ignore_index=True)
#         df.to_csv(FILE, index=False)
#         st.success("Response recorded successfully ✔")

#     st.markdown('</div>', unsafe_allow_html=True)

# # ================= RESPONSES =================
# with tab2:
#     st.subheader("All Responses")

#     if df.empty:
#         st.info("No responses yet.")
#     else:
#         st.dataframe(df, use_container_width=True)

#         row = st.selectbox("Select response to edit/delete", df.index)

#         for col in df.columns:
#             df.at[row, col] = st.text_input(col, str(df.at[row, col]))

#         c1, c2 = st.columns(2)

#         if c1.button("Update"):
#             df.to_csv(FILE, index=False)
#             st.success("Updated successfully")

#         if c2.button("Delete"):
#             df = df.drop(row)
#             df.to_csv(FILE, index=False)
#             st.warning("Deleted successfully")



















# import streamlit as st
# import pandas as pd
# from datetime import date

# # ================= CONFIG =================
# st.set_page_config(page_title="TWS Project – Exports", layout="wide")

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

# # ================= STYLE =================
# st.markdown("""
# <style>
# .stApp {
#     background-color: #0b3c5d;
# }

# /* Text color */
# h1,h2,h3,label,span,p {
#     color: white !important;
# }

# /* Input boxes */
# input, textarea, select {
#     background-color: #000000 !important;
#     color: white !important;
# }

# /* Date picker & file uploader */
# div[data-baseweb="input"] input {
#     background-color: #000000 !important;
#     color: white !important;
# }

# /* Selectbox */
# div[data-baseweb="select"] > div {
#     background-color: #000000 !important;
#     color: white !important;
# }

# /* Buttons */
# button {
#     background-color: #111111 !important;
#     color: white !important;
#     border: 1px solid #444 !important;
# }

# /* Dataframe */
# [data-testid="stDataFrame"] {
#     background-color: black !important;
# }

# /* Container padding */
# .block-container {
#     padding: 2rem;
# }
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

# # ================= MAIN =================
# st.title("📘 TWS Project – Exports")

# tab1, tab2, tab3 = st.tabs(["📝 Form", "📊 Dashboard", "📁 Data"])

# # ================= FORM =================
# with tab1:
#     with st.form("tws_form"):
#         c1, c2 = st.columns(2)
#         email = c1.text_input("Email *")
#         project_code = c2.text_input("Project Code *")
#         project_desc = st.text_area("Project Description *")
#         start_project = st.date_input("Start of Project", date.today())

#         platform = st.radio("Platform",["Below 30 HP","30–60 HP","60–101 HP","Above 101 HP"])
#         continent = st.text_input("Continent / Country")
#         scr_no = st.text_input("SCR No")
#         scr_issue = st.text_input("SCR – Issue discussed in CFT")
#         model = st.text_input("Model")

#         aggregate = st.selectbox(
#             "Aggregate",
#             ["Electrical","Hydraulic","Transmission","Engine","Vehicle","Cabin"]
#         )

#         agg_lead = st.text_input("Aggregate Lead / Project Owner")

#         impl_month = st.selectbox(
#             "Implementation Month",
#             ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
#         )

#         r_and_d = st.radio("R&D – PMO",["Mohit Rana","Arashdeep Parmar"])

#         feasibility = st.file_uploader("Feasibility Study Upload")

#         g1 = st.date_input("G1 Drg Release")
#         material = st.date_input("Material Avl")
#         proto = st.date_input("Proto Fitment")
#         testing = st.date_input("Testing Start")
#         interim = st.date_input("Interim Testing Go Ahead")

#         g1_orc_drg = st.date_input("G1 ORC Drg Release")
#         g1_orc_mat = st.date_input("G1 ORC Material Avl")
#         g1_orc_proto = st.date_input("G1 ORC Proto Fitment")

#         g2_go = st.date_input("G2 Go Ahead")
#         g2_mat = st.date_input("G2 Material Avl")

#         tractors = st.text_input("5 Tractors Making Online")
#         prr = st.text_input("PRR Sign-off 5 nos")

#         pre_ern = st.text_input("Pre ERN")
#         go_ern = st.text_input("Go Ahead ERN")
#         bom = st.text_input("BOM Change")

#         bcr_no = st.text_input("BCR Number")
#         bcr_date = st.date_input("BCR Date")
#         cutoff = st.text_input("Cut-off Number")

#         submit = st.form_submit_button("Submit")

#     if submit:
#         df.loc[len(df)] = [
#             email,project_code,project_desc,start_project,platform,
#             continent,scr_no,scr_issue,model,aggregate,agg_lead,
#             impl_month,r_and_d,feasibility.name if feasibility else "",
#             g1,material,proto,testing,interim,g1_orc_drg,
#             g1_orc_mat,g1_orc_proto,g2_go,g2_mat,tractors,prr,
#             pre_ern,go_ern,bom,bcr_no,bcr_date,cutoff
#         ]
#         save_data(df)
#         st.success("✅ Data saved successfully")

# # ================= DASHBOARD =================
# with tab2:
#     st.subheader("📊 Project Dashboard")
#     st.metric("Total Projects", len(df))
#     st.metric("G1 Completed", df["G1 Drg Release"].notna().sum())
#     st.metric("G2 Completed", df["G2 Go Ahead"].notna().sum())

# # ================= DATA =================
# with tab3:
#     st.subheader("📁 All Records")
#     st.dataframe(df, use_container_width=True)

#     st.download_button(
#         "⬇️ Download Excel",
#         data=df.to_csv(index=False),
#         file_name="tws_exports.xlsx",
#         mime="application/vnd.ms-excel"
#     )

#     st.subheader("✏️ Update / Delete")

#     idx = st.number_input("Row index", min_value=0, step=1)
#     if idx < len(df):
#         df.at[idx,"Project Code"] = st.text_input(
#             "Project Code", df.at[idx,"Project Code"])
#         if st.button("Update"):
#             save_data(df)
#             st.success("Updated")

#     if st.button("Delete Row"):
#         df.drop(idx, inplace=True)
#         df.reset_index(drop=True, inplace=True)
#         save_data(df)
#         st.warning("Deleted")


# # ================= DATA =================
# with tab3:
#     st.subheader("📁 All Records")
#     st.dataframe(df, use_container_width=True)

#     st.download_button(
#         "⬇️ Download Excel",
#         data=df.to_csv(index=False),
#         file_name="tws_exports.xlsx",
#         mime="application/vnd.ms-excel"
#     )

#     st.subheader("✏️ Update / Delete")

#     idx = st.number_input("Row index", min_value=0, step=1)

#     if idx < len(df):
#         df.at[idx, "Project Code"] = st.text_input(
#             "Project Code", df.at[idx, "Project Code"]
#         )

#         if st.button("Update"):
#             save_data(df)
#             st.success("Updated")

#     if st.button("Delete Row"):
#         df.drop(idx, inplace=True)
#         df.reset_index(drop=True, inplace=True)
#         save_data(df)
#         st.warning("Deleted")



#     # ================= CSV / GOOGLE SHEET UPDATE =================
#     st.subheader("🔄 Upload Google Sheet / CSV & Update")

#     col1, col2 = st.columns([3, 1])

#     with col1:
#         uploaded_csv = st.file_uploader(
#             "Upload CSV (Exported from Google Sheets)",
#             type=["csv"]
#         )

#     with col2:
#         sync_btn = st.button("🔁 Update Data", use_container_width=True)

#     if sync_btn:
#         if uploaded_csv is None:
#             st.error("❌ Please upload a CSV file first")
#         else:
#             new_df = pd.read_csv(uploaded_csv)

#             if "Project Code" not in new_df.columns:
#                 st.error("❌ CSV must contain 'Project Code' column")
#             else:
#                 updated = 0
#                 added = 0

#                 for _, row in new_df.iterrows():
#                     pcode = row["Project Code"]

#                     if pcode in df["Project Code"].values:
#                         row_idx = df[df["Project Code"] == pcode].index[0]
#                         for col in new_df.columns:
#                             if col in df.columns and pd.notna(row[col]):
#                                 df.at[row_idx, col] = row[col]
#                         updated += 1
#                     else:
#                         new_row = {col: row[col] if col in new_df.columns else "" for col in df.columns}
#                         df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
#                         added += 1

#                 save_data(df)
#                 st.success(f"✅ Update Complete | Updated: {updated} | Added: {added}")
















import streamlit as st
import pandas as pd
from datetime import date

# ================= CONFIG =================
st.set_page_config(page_title="TWS Project – Exports", layout="wide")

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

# ================= STYLE =================
st.markdown("""
<style>
.stApp { background-color:#0b3c5d; }
h1,h2,h3,label,span,p { color:white !important; }

input, textarea, select {
    background-color: #000 !important;
    color: white !important;
}

div[data-baseweb="select"] > div {
    background-color: #000 !important;
    color: white !important;
}

button {
    background-color:#111 !important;
    color:white !important;
    border:1px solid #444 !important;
}

.block-container { padding:2rem; }
</style>
""", unsafe_allow_html=True)

# ================= LOAD / SAVE =================
def load_data():
    try:
        return pd.read_csv(DATA_FILE)
    except:
        return pd.DataFrame(columns=COLUMNS)

def save_data(df):
    df.to_csv(DATA_FILE, index=False)

df = load_data()

# ================= MAIN =================
st.title("📘 TWS Project – Exports")

tab1, tab2, tab3 = st.tabs(["📝 Form", "📊 Dashboard", "📁 Data"])

# ================= FORM =================
with tab1:
    with st.form("tws_form"):
        c1, c2 = st.columns(2)
        email = c1.text_input("Email *")
        project_code = c2.text_input("Project Code *")
        project_desc = st.text_area("Project Description *")
        start_project = st.date_input("Start of Project", date.today())

        platform = st.radio("Platform",["Below 30 HP","30–60 HP","60–101 HP","Above 101 HP"])
        continent = st.text_input("Continent / Country")
        scr_no = st.text_input("SCR No")
        scr_issue = st.text_input("SCR – Issue discussed in CFT")
        model = st.text_input("Model")

        aggregate = st.selectbox(
            "Aggregate",
            ["Electrical","Hydraulic","Transmission","Engine","Vehicle","Cabin"]
        )

        agg_lead = st.text_input("Aggregate Lead / Project Owner")

        impl_month = st.selectbox(
            "Implementation Month",
            ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
        )

        r_and_d = st.radio("R&D – PMO",["Mohit Rana","Arashdeep Parmar"])

        feasibility = st.file_uploader("Feasibility Study Upload")

        g1 = st.date_input("G1 Drg Release")
        material = st.date_input("Material Avl")
        proto = st.date_input("Proto Fitment")
        testing = st.date_input("Testing Start")
        interim = st.date_input("Interim Testing Go Ahead")

        g1_orc_drg = st.date_input("G1 ORC Drg Release")
        g1_orc_mat = st.date_input("G1 ORC Material Avl")
        g1_orc_proto = st.date_input("G1 ORC Proto Fitment")

        g2_go = st.date_input("G2 Go Ahead")
        g2_mat = st.date_input("G2 Material Avl")

        tractors = st.text_input("5 Tractors Making Online")
        prr = st.text_input("PRR Sign-off 5 nos")

        pre_ern = st.text_input("Pre ERN")
        go_ern = st.text_input("Go Ahead ERN")
        bom = st.text_input("BOM Change")

        bcr_no = st.text_input("BCR Number")
        bcr_date = st.date_input("BCR Date")
        cutoff = st.text_input("Cut-off Number")

        submit = st.form_submit_button("Submit")

    if submit:
        df.loc[len(df)] = [
            email,project_code,project_desc,start_project,platform,
            continent,scr_no,scr_issue,model,aggregate,agg_lead,
            impl_month,r_and_d,feasibility.name if feasibility else "",
            g1,material,proto,testing,interim,g1_orc_drg,
            g1_orc_mat,g1_orc_proto,g2_go,g2_mat,tractors,prr,
            pre_ern,go_ern,bom,bcr_no,bcr_date,cutoff
        ]
        save_data(df)
        st.success("✅ Data saved successfully")

# ================= DASHBOARD =================
with tab2:
    st.subheader("📊 Project Dashboard")
    st.metric("Total Projects", len(df))
    st.metric("G1 Completed", df["G1 Drg Release"].notna().sum())
    st.metric("G2 Completed", df["G2 Go Ahead"].notna().sum())

# ================= DATA =================
with tab3:
    st.subheader("📁 All Records")
    st.dataframe(df, use_container_width=True)

    st.download_button(
        "⬇️ Download Excel",
        data=df.to_csv(index=False),
        file_name="tws_exports.xlsx",
        mime="application/vnd.ms-excel",
        key="download_excel_main"
    )

    st.subheader("🔄 Upload Google Sheet / CSV & Update")

    c1, c2 = st.columns([3,1])

    with c1:
        uploaded_csv = st.file_uploader(
            "Upload CSV (Exported from Google Sheets)",
            type=["csv"],
            key="csv_upload"
        )

    with c2:
        sync_btn = st.button("🔁 Update Data", key="sync_button")

    if sync_btn and uploaded_csv is not None:
        new_df = pd.read_csv(uploaded_csv)

        if "Project Code" not in new_df.columns:
            st.error("❌ CSV must contain 'Project Code'")
        else:
            for _, row in new_df.iterrows():
                code = row["Project Code"]

                if code in df["Project Code"].values:
                    idx = df[df["Project Code"] == code].index[0]
                    for col in new_df.columns:
                        if col in df.columns and pd.notna(row[col]):
                            df.at[idx, col] = row[col]
                else:
                    new_row = {col: row[col] if col in new_df.columns else "" for col in df.columns}
                    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

            save_data(df)
            st.success("✅ CSV Sync Completed Successfully")
