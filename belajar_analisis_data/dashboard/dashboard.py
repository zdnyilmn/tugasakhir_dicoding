import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from func import DataAnalyzer
from babel.numbers import format_currency
sns.set_theme(style='dark')
st.set_option('deprecation.showPyplotGlobalUse', False)

# Dataset
datetime_cols = ["order_approved_at", "order_delivered_carrier_date", "order_delivered_customer_date", "order_estimated_delivery_date", "order_purchase_timestamp", "shipping_limit_date"]
all_df = pd.read_csv("./data/all_data.csv")
all_df.sort_values(by="order_approved_at", inplace=True)
all_df.reset_index(inplace=True)

for col in datetime_cols:
    all_df[col] = pd.to_datetime(all_df[col])

min_date = all_df["order_approved_at"].min()
max_date = all_df["order_approved_at"].max()

# Sidebar
with st.sidebar:
    # Title
    st.title("Muhammad Zidny Ilman")

    # Logo Image
    st.image("data:image/jpeg;base64,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")

    # Date Range
    start_date, end_date = st.date_input(
        label="Select Date Range",
        value=[min_date, max_date],
        min_value=min_date,
        max_value=max_date
    )

# Main
    main_df = all_df[(all_df["order_approved_at"] >= str(start_date)) & 
                 (all_df["order_approved_at"] <= str(end_date))]
    
    function = DataAnalyzer(main_df)

daily_orders_df = function.create_daily_orders_df()
sum_order_items_df = function.create_sum_order_items_df()
state, most_common_state = function.create_bystate_df()
order_status, common_status = function.create_order_status()

# Title
st.header("E-Commerce Dashboard :convenience_store:")

# Daily Orders
st.subheader("Penjualan")

col1, col2 = st.columns(2)

with col1:
    total_order = daily_orders_df["order_count"].sum()
    st.markdown(f"Total Order: **{total_order}**")

with col2:
    total_revenue = format_currency(daily_orders_df["revenue"].sum(), "IDR", locale="id_ID")
    st.markdown(f"Total Revenue: **{total_revenue}**")

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(
    daily_orders_df["order_approved_at"],
    daily_orders_df["order_count"],
    marker="o",
    linewidth=2,
    color="#90CAF9"
)
ax.tick_params(axis="x", rotation=45)
ax.tick_params(axis="y", labelsize=15)
st.pyplot(fig)

# Order Items
st.subheader("Produk Penjualan")
col1, col2 = st.columns(2)

with col1:
    total_items = sum_order_items_df["product_count"].sum()
    st.markdown(f"Total Items: **{total_items}**")

with col2:
    avg_items = sum_order_items_df["product_count"].mean()
    st.markdown(f"Average Items: **{avg_items}**")

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(45, 25))

colors = ["#068DA9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

sns.barplot(x="product_count", y="product_category_name", data=sum_order_items_df.head(5), palette=colors, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel("Number of Sales", fontsize=30)
ax[0].set_title("Produk paling banyak terjual", loc="center", fontsize=50)
ax[0].tick_params(axis ='y', labelsize=35)
ax[0].tick_params(axis ='x', labelsize=30)

sns.barplot(x="product_count", y="product_category_name", data=sum_order_items_df.sort_values(by="product_count", ascending=True).head(5), palette=colors, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel("Number of Sales", fontsize=30)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title("Produk paling sedikit terjual", loc="center", fontsize=50)
ax[1].tick_params(axis='y', labelsize=35)
ax[1].tick_params(axis='x', labelsize=30)

st.pyplot(fig)

# Customer Demographic
st.subheader("Customer Demographic")
tab1, tab2 = st.tabs(["State", "Order Status"])

with tab1:
    most_common_state = state.customer_state.value_counts().index[0]
    st.markdown(f"Most Common State: **{most_common_state}**")

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x=state.customer_state.value_counts().index,
                y=state.customer_count.values, 
                data=state,
                palette=["#068DA9" if score == most_common_state else "#D3D3D3" for score in state.customer_state.value_counts().index]
                    )

    plt.title("Number customers from State", fontsize=15)
    plt.xlabel("State")
    plt.ylabel("Number of Customers")
    plt.xticks(fontsize=12)
    st.pyplot(fig)

with tab2:
    common_status_ = order_status.value_counts().index[0]
    st.markdown(f"Most Common Order Status: **{common_status_}**")

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x=order_status.index,
                y=order_status.values,
                order=order_status.index,
                palette=["#068DA9" if score == common_status else "#D3D3D3" for score in order_status.index]
                )
    
    plt.title("Order Status", fontsize=15)
    plt.xlabel("Status")
    plt.ylabel("Count")
    plt.xticks(fontsize=12)
    st.pyplot(fig)

    st.caption('Copyright (C) Muhammad Zidny Ilman 2024')