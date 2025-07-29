import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
sns.set_palette("pastel")

# Load the dataset
df = pd.read_csv("group1.csv")

# Title and project overview
st.title("Global AI Index Dashboard")
st.markdown("""
This interactive dashboard analyzes AI readiness across 62 countries.  
It includes indicators like Talent, Infrastructure, Research, Development, Government Strategy, and Commercial Use.  
Use the filters on the sidebar to explore by region and income group.
""")

# Sidebar filters
st.sidebar.header("Filter the Data")
region = st.sidebar.selectbox("Select Region", df['Region'].dropna().unique())
income_group = st.sidebar.radio("Select Income Group", df['Income group'].dropna().unique())
filtered_df = df[(df['Region'] == region) & (df['Income group'] == income_group)]

# Summary metrics
st.subheader("Summary Metrics")
top_country = filtered_df.loc[filtered_df['Total score'].idxmax(), 'Country']
top_score = filtered_df['Total score'].max()
avg_score = filtered_df['Total score'].mean()
col1, col2, col3 = st.columns(3)
col1.metric("Top Country", top_country)
col2.metric("Highest Score", f"{top_score:.2f}")
col3.metric("Average Score", f"{avg_score:.2f}")

# Chart 1: Distribution
st.subheader("1. Distribution of AI Readiness Scores")
fig1, ax1 = plt.subplots()
sns.histplot(filtered_df['Total score'], kde=True, ax=ax1)
ax1.set_title("Total AI Score Distribution")
st.pyplot(fig1)
st.markdown("**Insight:** Most countries score below 60. This shows that only a few countries are highly advanced in AI readiness, while the rest still have significant gaps.")

# Chart 2: Government Strategy vs Score
st.subheader("2. Government Strategy vs Total Score")
fig2, ax2 = plt.subplots()
sns.scatterplot(data=filtered_df, x='Government Strategy', y='Total score', hue='Country', ax=ax2)
ax2.set_title("Government Strategy vs AI Readiness")
st.pyplot(fig2)
st.markdown("**Insight:** Stronger government strategies are often linked to higher readiness. But having a good strategy doesn’t always mean high performance—it must be backed by real implementation.")

# Chart 3: Commercial Use by Income
st.subheader("3. Commercial AI Use by Income Group")
fig3, ax3 = plt.subplots()
sns.barplot(data=df, x='Income group', y='Commercial', estimator='mean', ci=None, ax=ax3)
ax3.set_title("Commercial Use vs Income Level")
st.pyplot(fig3)
st.markdown("**Insight:** High-income countries lead in commercial AI adoption, but some upper-middle-income countries are catching up fast.")

# Chart 4: Total Score by Region
st.subheader("4. Total AI Readiness by Region")
fig4, ax4 = plt.subplots()
sns.boxplot(data=df, x='Region', y='Total score', ax=ax4)
ax4.set_title("AI Readiness by Region")
st.pyplot(fig4)
st.markdown("**Insight:** Europe and Asia-Pacific have both higher and more consistent scores. Other regions show more variation and often lower readiness.")

# Chart 5: Infrastructure vs Score
st.subheader("5. Infrastructure vs Total Score")
fig5, ax5 = plt.subplots()
sns.scatterplot(data=df, x='Infrastructure', y='Total score', hue='Region', ax=ax5)
ax5.set_title("Infrastructure vs Readiness")
st.pyplot(fig5)
st.markdown("**Insight:** Countries with stronger infrastructure tend to score higher. However, infrastructure alone isn't enough without talent and policy.")

# Chart 6: Score by Income Group
st.subheader("6. AI Readiness by Income Group")
fig6, ax6 = plt.subplots()
sns.boxplot(data=df, x='Income group', y='Total score', ax=ax6)
ax6.set_title("AI Readiness by Income Group")
st.pyplot(fig6)
st.markdown("**Insight:** High-income countries usually lead, but upper-middle-income countries are showing rapid progress and closing the gap.")

# Chart 7: Research Score by Region
st.subheader("7. Research Score by Region")
fig7, ax7 = plt.subplots()
sns.barplot(data=df, x='Region', y='Research', estimator='mean', ci=None, ax=ax7)
ax7.set_title("Average Research Score by Region")
st.pyplot(fig7)
st.markdown("**Insight:** Europe and Asia-Pacific dominate in AI research, reflecting strong academic and institutional investment in innovation.")

# Final filtered table
st.subheader("Filtered Data Table")
st.dataframe(filtered_df)
