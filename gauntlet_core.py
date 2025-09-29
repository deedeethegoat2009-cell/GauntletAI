import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

class GauntletAI:
    def run_match(self, combatant1, combatant2, format, lore1="", lore2=""):
        prompt = f"""
You are GauntletAI, a mythic battle narrator. Simulate a cinematic battle between {combatant1} and {combatant2} in the format: {format}.
Include lore, stat scaling, emotional stakes, and a final verdict.
Combatant A Lore: {lore1}
Combatant B Lore: {lore2}
Respond with a dramatic narration and seal the verdict.
"""
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.9
        )
        return response['choices'][0]['message']['content']

