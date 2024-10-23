import requests
import streamlit as st
from streamlit_lottie import st_lottie



#st.set_page_config(page_title="SocialMedias💬", )
st.set_page_config(
    page_title="Social Media",
    page_icon="💬",  # You can also use a string (emoji) or the path to an image file
)



def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
#load asset
lottie_mail = load_lottieurl("https://lottie.host/93843105-b3a2-48b0-840f-239a8e0679a2/krkfJ0TMje.json")

with st.container():
    button_box, add_box = st.columns(2)
    with button_box:
        st.page_link("HOME.py", label="🏚️‎ Back To Main")


        ##st.page_link("HOME.py", label="🏚️‎ Back To Main")
    with add_box:
        ad_code = """
        <!-- Replace this with your Google AdSense code -->
        <div style="text-align: center;">
            <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3993397003342112"></script>
            <ins class="adsbygoogle"
                 style="display:block"
                 data-ad-client="ca-pub-3993397003342112"
                 data-ad-slot="2355431176"
                 data-ad-format="auto"></ins>
            <script>
                 (adsbygoogle = window.adsbygoogle || []).push({});
            </script>
        </div>
        """

        # Display the ad
        st.markdown(ad_code, unsafe_allow_html=True)

st.write("---")
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.link_button(":red[FACEBOOOK]", "https://www.facebook.com/Jj.cornejo29/", type='secondary')

        st.link_button(":red[‎ INSTAGRAM]", "https://www.instagram.com/jinrikk/?hl=en", type='secondary')
        st.write("---")
        st.subheader(":rainbow[DISCORD SERVER]")

        st.link_button(":orange[COMMING SOON]", "https://discord.com", type='secondary')

    with right_column:

#        adsense_script = """
#        <div style="text-align: center;">
#            <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3993397003342112"></script>
#           <ins class="adsbygoogle"
#                 data-ad-client="ca-pub-XXXXXXXXXXXXXXXX"
#                 data-ad-slot="XXXXXXXXXX"
#                 data-ad-format="auto"></ins>
#            <script>
#                 (adsbygoogle = window.adsbygoogle || []).push({});
#            </script>
#        </div>
#        """

#        st.components.v1.html(adsense_script, height=100)

        st_lottie(lottie_mail, height=300, key="mail")

with st.container():
    st.write("---")

