import streamlit as st
import subprocess


def main():
    st.title("Snake Game")
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(
        "<h4> <br> Click the button to start the game:</h4>",
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Launch The App"):
        st.spinner("Launching...")

        process = subprocess.Popen(
            ["python", "snakegame.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )

        # Read the output from the subprocess
        output, error = process.communicate()

        if process.returncode == 0:
            st.success("Finished Successfully!")
        else:
            st.error(f"Error launching the script: {error.decode()}")

    st.markdown("<br>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()