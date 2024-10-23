import requests
import streamlit as st
from streamlit_lottie import st_lottie

# st.set_page_config(page_title="Jenrick.com")
st.set_page_config(
    page_title="Home Page",
    page_icon="🏚️",  # You can also use a string (emoji) or the path to an image file
)


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


with st.container():
    dog_column, pussy_column = st.columns(2)
    with dog_column:
        st.page_link("pages/SOCIAL MEDIA.py", label="Social Media💬")
        font_url = "https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400&display=swap"

        # Custom CSS with the correct font name and italic style
        custom_css = f"""
                <style>
                @import url('{font_url}');
                .custom-font {{
                    font-family: 'Dancing Script', cursive;  /* Use the Dancing Script font */
                    font-size: 40px;  
                    font-style: italic; 
                    color: #00000;      
                }}
                </style>
            """

        # Display the custom CSS
        st.markdown(custom_css, unsafe_allow_html=True)

        # Use HTML for the subheader
        st.markdown('<h2 class="custom-font">I am John Jenrick👋</h2>', unsafe_allow_html=True)
        st.caption("𝓦𝓮𝓵𝓬𝓸𝓶𝓮 𝓽𝓸 𝓶𝔂 𝓹𝓮𝓻𝓼𝓸𝓷𝓪𝓵 𝔀𝓮𝓫𝓼𝓲𝓽𝓮!🙈")

st.write("###")
st.write(
    """

        Hello and welcome to my corner of the internet! My name is John Jenrick, and I’m an 11th-grade student currently pursuing the TVL ICT strand. This website is a project born out of my curiosity, creativity, and a little bit of boredom. It’s a space where I can share my thoughts, showcase my skills, and connect with others who share similar interests.

        As a student, I am passionate about technology and its role in our daily lives. I enjoy learning about different aspects of information and communication technology, from programming and web development to graphic design and digital media. This website serves as a reflection of my journey as I explore these areas and develop my skills. When I’m not studying or working on projects, you can find me indulging in my hobbies. I love gaming, experimenting with new tech gadgets, and watching movies. I also enjoy hanging out with friends and discovering new music. Each of these interests adds a unique flavor to my life.

        Education is a lifelong journey, and I believe in the importance of continuous learning. This website is a platform for me to document my learning experiences, share tips and resources, and connect with other students and enthusiasts in the ICT field. Whether you’re a fellow student, a teacher, or just someone curious about technology, I hope you find something valuable here.

    """
)
# st.write("###")
# st.write(
#    """
#
#        Hello and welcome to my corner of the internet! My name is John Jenrick, and I’m an 11th-grade student currently pursuing the TVL ICT strand. This website is a project born out of my curiosity, creativity, and a little bit of boredom. It’s a space where I can share my thoughts, showcase my skills, and connect with others who share similar interests.
#
#        As a student, I am passionate about technology and its role in our daily lives. I enjoy learning about different aspects of information and communication technology, from programming and web development to graphic design and digital media. This website serves as a reflection of my journey as I explore these areas and develop my skills. When I’m not studying or working on projects, you can find me indulging in my hobbies. I love gaming, experimenting with new tech gadgets, and watching movies. I also enjoy hanging out with friends and discovering new music. Each of these interests adds a unique flavor to my life.
#
#        Education is a lifelong journey, and I believe in the importance of continuous learning. This website is a platform for me to document my learning experiences, share tips and resources, and connect with other students and enthusiasts in the ICT field. Whether you’re a fellow student, a teacher, or just someone curious about technology, I hope you find something valuable here.
#
#    """
# )


# load asset
lottie_coding = load_lottieurl("https://lottie.host/19a174cf-ed62-4d05-a7c2-dd188a8dfce6/H22QT9wjWK.json")

# what i do
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write(
            """
            Thank you for taking the time to visit my website. I appreciate your support and interest in my work. I hope you enjoy exploring my projects and insights as much as I enjoy creating them. Here’s to creativity, learning, and all the exciting possibilities that lie ahead!
    
            I encourage you to engage with my content! Feel free to leave comments, ask questions, or share your thoughts. I’m always open to feedback and eager to learn from others. You can also follow me on social media to keep up with my latest updates and projects.
            """
        )

        ##   st.write("[𝓕𝓐𝓒𝓔𝓑𝓞𝓞𝓚 𝓐𝓒𝓒𝓞𝓤𝓝𝓣⇝](https://www.facebook.com/profile.php?id=100086128746020)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")
st.write("---")

with st.container():
    input_placeholder = st.empty()
    name = input_placeholder.text_input("Please enter your name:")

    output_container = st.container()

    if name:
        capitalized_name = name.title()

        with (output_container):
            st.subheader(f":rainbow[Hi {capitalized_name}, Feel free to send me an email </3]")
            input_placeholder.empty()
            unsafe_allow_html = True
            contact_form = """
                <form action="https://formsubmit.co/jenrick212@gmail.com" method="POST">
                    <input type="hidden" name="_captcha" value="false">
                    <input type="text" name="name" placeholder="Your Name" required>
                    <input type="email" name="email" placeholder="Your Email" required>
                    <textarea name="message" placeholder="Your Message Here"></textarea>
                    <button type="submit">Send</button >
                </form>
                """

            st.markdown(contact_form, unsafe_allow_html=True)


            # style sa css sana gumana hahahahaha
            def local_css(file_name):
                with open(file_name) as f:
                    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


            local_css("style.css")