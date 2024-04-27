import streamlit as st

def main():
    st.set_page_config(
        page_title="What is this website about?",
        page_icon="❔"
    )
    st.title("HELLO THERE!!, You can call me LongLastBot.")
    st.markdown("=-=-=")
    st.subheader("Answer some of these questions.")
    # Question 1
    name = st.text_input("What is your full name?")

    # Only display next question if name is provided
    if name:
        # Question 2
        st.write("Oh, Hello", name)
        st.write("How old are you?")
        a = st.number_input("Wait let me guess, which year were you born in (AD)?")
        age = 2024 - a
        if a :
            st.write("So your", age,"years old.")
            x = st.text_input("Oh thats cool, wait let me compare my age, when's your birthday?[MONTH(xx)/DAY(xx(]")
            if x == "04/27":
                st.write("Wait whatt, Isn't that today???")
                i = ["I dont want to say", "Yeah, it is", "Nope"]
                c = st.radio("Is it?",
                         i)
                if c == "Yeah, it is" :
                    st.title("🎈🎂🎉🎊HAPPY BIRTHDAY ❗ ❗🎉🎊 🎈, May all your wishes come true.")
                    st.balloons()
                    st.subheader("Anyways, Here is a message I got from your favourite person(Hopefully).")
                    st.image("Screenshot 2024-04-27 073656.png", use_column_width= True)
                               
                if c == "Nope" :
                    st.title("Your lying😹, It is today, anyways 🎈🎂🎉🎊HAPPY BIRTHDAY ❗ ❗🎉🎊 🎈!")
                    st.balloons()
                    st.subheader("You are such a liar, anyways I have a message for you from someone who calls themselves 'Your admirer'.")
                    st.image =("Lies.png",use_column_width=True
                              )
                if c == "I dont want to say":
                    st.write("OK then")
            else: st.write("Okay, maybe it isn't today or did you somehow make a mistake?")



if __name__ == "__main__":
    main()

