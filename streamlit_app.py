import streamlit as st
from datetime import datetime
from gauntlet_core import GauntletAI  # This connects to your backend

gauntlet = GauntletAI()

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
    result = gauntlet.run_match(combatant1, combatant2, format, lore1, lore2)
    st.markdown(f"**Timestamp:** {timestamp}")
    st.markdown(result)
