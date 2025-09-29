import streamlit as st
from datetime import datetime

st.title("GauntletAI ⚔️")
st.subheader("Run epic battles across all universes")

combatant1 = st.text_input("Combatant A")
combatant2 = st.text_input("Combatant B")
format = st.selectbox("Choose Format", [
    "DB-Style Arc",
    "Format 3",
    "Rematch",
    "Full Death Battle Episode",
    "Add-On – No Bias Program"
])
lore1 = st.text_area("Lore for Combatant A (optional)")
lore2 = st.text_area("Lore for Combatant B (optional)")

if st.button("Run Match"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.markdown(f"### [{format}] {combatant1} vs {combatant2}")
    st.markdown(f"**Timestamp:** {timestamp}")
    st.markdown(f"**Lore A:** {lore1}")
    st.markdown(f"**Lore B:** {lore2}")
    st.markdown("**Verdict:** Pending... (AI integration coming soon)")
    st.markdown("**VERDICT SEALED**")
