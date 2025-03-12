import streamlit as st

# Title
st.markdown("### Text Analyzer")

# Separator
st.markdown("---")

# User input for paragraph
paragraph = st.text_area("Enter your paragraph here:")

# Analyze button and validation
if st.button("Analyze"):
    if not paragraph.strip():
        st.error("Please enter some text to analyze!")
    else:
        # 1. Display Original Paragraph
        st.markdown("**Original Paragraph:**")
        st.write(paragraph)

        # 2. Word and Character Count
        words = paragraph.split()
        word_count = len(words)
        char_count = len(paragraph)

        # 3. Vowel Count
        vowels = "aeiouAEIOU"
        vowel_count = sum(1 for char in paragraph if char in vowels)

        # 4. Check if "Python" is in the paragraph
        python_present = "Yes" if "Python" in paragraph else "No"

        # 5. Display Counts
        st.markdown("**Total Words:** " + str(word_count))
        st.markdown("**Total Characters:** " + str(char_count))
        st.markdown("**Number of Vowels:** " + str(vowel_count))
        st.markdown("**Does the paragraph contain the word \"Python\"?** " + python_present)

        # 6. Search and Replace
        st.markdown("**Enter a word to search for:**")
        search_word = st.text_input("Search word", value="Python")
        st.markdown("**Enter a word to replace it with:**")
        replace_word = st.text_input("Replace word", value="Java")
        if search_word and replace_word:
            modified_paragraph = paragraph.replace(search_word, replace_word)
            st.markdown("**Modified Paragraph:**")
            st.write(modified_paragraph)

        # 7. Uppercase and Lowercase
        st.markdown("**Paragraph in Uppercase:**")
        st.write(paragraph.upper())
        st.markdown("**Paragraph in Lowercase:**")
        st.write(paragraph.lower())

        # 8. Average Word Length
        if word_count > 0:
            avg_word_length = char_count / word_count
            st.markdown("**Average Word Length:** " + f"{avg_word_length:.2f}")
        else:
            st.markdown("**Average Word Length:** Cannot calculate (no words).")