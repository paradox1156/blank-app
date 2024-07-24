import streamlit as st
import random

# List of romantasy tropes
tropes = [
    "Enemies to Lovers", "Forbidden Love", "Fated Mates", "Love Triangle", 
    "Hidden Royalty", "Hero's Journey", "Rescue Romance", "Opposites Attract", 
    "Slow Burn", "Secret Identity", "Magical Bond", "Second Chances", 
    "Fake Relationship", "Reincarnated Lovers", "Tragic Love"
]

# List of character types
character_types = [
    "The Chosen One", "The Warrior", "The Healer", "The Mage/Sorcerer",
    "The Rogue/Thief", "The Noble/Prince/Princess", "The Outsider", "The Mentor",
    "The Villain", "The Seer/Prophet", "The Shape-shifter", "The Rebel",
    "The Guardian/Protector", "The Love Interest", "The Tragic Hero/Heroine"
]

# List of words for generating a plot
plot_words = [
    "destiny", "battle", "love", "betrayal", "kingdom", "magic", "adventure", 
    "journey", "mystery", "quest", "power", "sacrifice", "truth", "hidden", 
    "danger", "enemy", "alliance", "secret", "ancient", "future", "hope", 
    "despair", "legend", "myth", "curse", "freedom"
]

def generate_plot(words, length=10):
    return ' '.join(random.choices(words, k=length))

# Streamlit app
st.title("Romantasy Plot Generator")

if st.button("Generate Romantasy Plot"):
    selected_trope = random.choice(tropes)
    character1 = random.choice(character_types)
    character2 = random.choice(character_types)
    while character1 == character2:
        character2 = random.choice(character_types)
    plot = generate_plot(plot_words)
    
    st.write("### Selected Trope:")
    st.write(selected_trope)
    
    st.write("### Main Characters:")
    st.write(f"1. {character1}")
    st.write(f"2. {character2}")
    
    st.write("### Plot:")
    st.write(plot)