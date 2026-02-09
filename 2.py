st.subheader("🔄 Google Sheet / CSV Auto Sync")

c1, c2 = st.columns([3,1])

with c1:
    uploaded_file = st.file_uploader(
        "Upload CSV exported from Google Sheets",
        type=["diabetes.csv"]
    )

with c2:
    sync_btn = st.button("🔁 Sync Data", use_container_width=True)

if sync_btn:
    if uploaded_file is None:
        st.error("❌ Please upload a CSV file first")
    else:
        new_df = pd.read_csv(uploaded_file)

        if "Project Code" not in new_df.columns:
            st.error("❌ 'Project Code' column is mandatory")
        else:
            updated = 0
            added = 0

            for _, row in new_df.iterrows():
                proj_code = row["Project Code"]

                if proj_code in df["Project Code"].values:
                    # UPDATE
                    idx = df[df["Project Code"] == proj_code].index[0]
                    for col in new_df.columns:
                        if col in df.columns and pd.notna(row[col]):
                            df.at[idx, col] = row[col]
                    updated += 1
                else:
                    # ADD
                    new_row = {}
                    for col in df.columns:
                        new_row[col] = row[col] if col in new_df.columns else ""
                    df = pd.concat(
                        [df, pd.DataFrame([new_row])],
                        ignore_index=True
                    )
                    added += 1

            save_data(df)

            st.success(f"✅ Sync Completed | Updated: {updated} | Added: {added}")
