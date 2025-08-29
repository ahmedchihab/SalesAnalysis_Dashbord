import pandas as pd
import streamlit as st
import plotly.express as px

# ================================
# 🔹 Charger les données
file_path = "data/cleaned_sales_data_final.csv"
df = pd.read_csv(file_path)

# Assurer que la date est en datetime
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')

# ================================
# 🔹 Sidebar - Filtres
# ================================
st.sidebar.header("📌 Filtres")

year_filter = st.sidebar.multiselect(
    "Sélectionner l'année :",
    options=df['Year'].unique(),
    default=df['Year'].unique()
)

city_filter = st.sidebar.multiselect(
    "Sélectionner la ville :",
    options=df['City'].unique(),
    default=df['City'].unique()
)

# Appliquer filtres
df_filtered = df[(df['Year'].isin(year_filter)) & (df['City'].isin(city_filter))]

# ================================
# 🔹 KPIs
# ================================
st.title("📊 Sales Analysis Dashboard")

total_revenue = df_filtered['Revenue'].sum()
total_orders = df_filtered['Order ID'].nunique()
best_product = df_filtered.groupby("Product")['Quantity Ordered'].sum().idxmax()

col1, col2, col3 = st.columns(3)
col1.metric("💰 Total Revenue", f"${total_revenue:,.0f}")
col2.metric("📦 Total Orders", f"{total_orders:,}")
col3.metric("🏆 Best Product", best_product)

st.markdown("---")

# ================================
# 🔹 Graphiques
# ================================

# Ventes par mois
sales_by_month = df_filtered.groupby("Month")['Revenue'].sum().reset_index()
fig_month = px.bar(sales_by_month, x="Month", y="Revenue",
                   title="📈 Ventes par Mois", text_auto=True)
st.plotly_chart(fig_month, use_container_width=True)

# Répartition par ville
sales_by_city = df_filtered.groupby("City")['Revenue'].sum().reset_index()
fig_city = px.pie(sales_by_city, names="City", values="Revenue",
                  title="🏙️ Répartition des Ventes par Ville")
st.plotly_chart(fig_city, use_container_width=True)

# Top produits
top_products = (df_filtered.groupby("Product")['Quantity Ordered']
                .sum().sort_values(ascending=False).head(10).reset_index())

fig_products = px.bar(top_products, x="Quantity Ordered", y="Product",
                      orientation="h", title="🔥 Top 10 Produits Vendus", text_auto=True)
st.plotly_chart(fig_products, use_container_width=True)


