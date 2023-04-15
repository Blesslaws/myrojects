import streamlit as st

# Define the pages
def home():
    st.title("Home Page")
    st.write("Welcome to my home page!")
    st.write("Paragraph 1: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce id nisl sit amet libero consequat ornare non vitae tellus. Duis ac dui at quam scelerisque finibus et ut dolor. Mauris nibh lorem, mattis et nisi nec, finibus tincidunt sem. Pellentesque gravida congue placerat. Sed sit amet semper risus. In lacinia nulla vel cursus sodales. Quisque iaculis eu lectus ac laoreet. Curabitur auctor consectetur rhoncus. Maecenas consequat hendrerit convallis. Vivamus egestas tellus justo, a semper ex elementum eget. Donec tempor dui at dolor facilisis vehicula. Quisque congue egestas fermentum. Aliquam fermentum, velit quis ullamcorper luctus, justo erat ultrices ex, non dapibus tellus tortor eu mauris. Donec massa mi, ullamcorper in tempor in, maximus lacinia neque.")
    st.write("Paragraph 2: Donec vel lobortis sem, a ultricies mauris. Etiam eget dolor nibh. Morbi tincidunt sapien ut semper volutpat. Donec mauris quam, posuere ac est egestas, lobortis sodales ex. Proin commodo accumsan pellentesque. Curabitur quis placerat mauris. Donec placerat placerat felis eu commodo. Integer quis ex purus. Nunc a massa condimentum, consequat enim eu, bibendum lacus. Pellentesque suscipit libero sit amet sodales lacinia. Aliquam iaculis tellus id dignissim mollis. Mauris vel nunc rutrum, rhoncus orci id, malesuada nulla. Donec molestie malesuada magna, eget fringilla orci tincidunt id.")
    st.write("Paragraph 3: Nullam tempus risus vitae odio molestie iaculis. Mauris fermentum dolor quis elit porta, vitae lacinia sem auctor. Pellentesque congue sit amet quam non tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Mauris in erat elementum, suscipit erat vulputate, feugiat nibh. Proin facilisis ipsum id libero ultricies rhoncus. In porttitor lacus nec nulla facilisis commodo. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Pellentesque in pellentesque urna. Donec eget ligula ac dui ornare rutrum ut ac turpis. Sed gravida nisl id mollis dapibus. Suspendisse pharetra, arcu ut lobortis rhoncus, orci quam tincidunt mauris, in commodo ligula mi ac augue. Fusce eu euismod velit, ac tempus dui. Nulla ut lorem mauris.")
    st.write("Paragraph 4: Vivamus iaculis turpis a efficitur vestibulum. Fusce ullamcorper, ipsum quis dictum malesuada, tortor erat venenatis felis, id consectetur ipsum justo id lectus. Aliquam fermentum, neque sit amet scelerisque pretium, velit lectus vehicula erat, non euismod tellus mi in ante. Vivamus molestie non nulla eget euismod. Morbi sit amet nisl ipsum. Nam in ligula ut ante aliquet tempus. Morbi velit mi, tempus quis nisl a, tincidunt porta felis. Etiam vel felis ut urna dignissim commodo. Vivamus id mollis mauris. Nam vitae lorem dignissim, condimentum nisl ut, vehicula sem.")
    st.write("Paragraph 5: Nunc odio massa, vulputate et tortor sit amet, ultricies venenatis magna. Proin tortor sapien, hendrerit a bibendum sed, vestibulum sit amet massa. Sed malesuada tincidunt purus rutrum maximus. In auctor, quam nec ullamcorper laoreet, nunc massa fermentum sem, et rutrum orci tellus ac orci. Vivamus pretium turpis neque, vel laoreet enim pellentesque eu. Vestibulum aliquam interdum quam. Vestibulum non sem egestas eros cursus porttitor id et nisl. Duis non ex ut odio gravida vestibulum. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Etiam nec molestie lectus, non suscipit nibh. Cras finibus feugiat sem in gravida. Nulla in fermentum lorem. Aliquam volutpat facilisis dolor nec molestie. Donec quis dolor ut ex vestibulum cursus in sit amet nisi. Sed venenatis risus in libero ultricies, sed porta massa consequat.")
    

def contact():
    st.title("Contact Me")
    st.write("You can contact me using the form below.")
    with st.form(key="contact_form"):
        name = st.text_input(label="Name")
        email = st.text_input(label="Email")
        message = st.text_area(label="Message")
        submit_button = st.form_submit_button(label="Submit")
        if submit_button:
            st.success("Thank you for your message! I will get back to you soon.")

def portfolio():
    st.title("Portfolio")
    st.write("Here are some examples of my work.")
    st.image("https://picsum.photos/400/300?random=1", caption="Project 1")
    st.image("https://picsum.photos/400/300?random=2", caption="Project 2")
    st.image("https://picsum.photos/400/300?random=3", caption="Project 3")
    st.image("https://picsum.photos/400/300?random=4", caption="Project 4")
    st.image("https://picsum.photos/400/300?random=5", caption="Project 5")

# Define the footer
def footer():
    st.write("")
    st.write("")
    st.write("Connect with me on social media:")
    st.write("<a href='https://twitter.com/your_twitter_username'><img src='https://i.imgur.com/h7JZOgg.png' width='30'></a>", unsafe_allow_html=True)
    st.write("<a href='https://www.linkedin.com/in/your_linkedin_username'><img src='https://i.imgur.com/6TfUg0h.png' width='30'></a>", unsafe_allow_html=True)

# Set page config
st.set_page_config(
    page_title="My Streamlit Web Blog",
    page_icon=":pencil:",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Set CSS style
st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(90deg, #66c2ff, #b3ecff);
            color: white;
        }

        .stHeader {
            font-size: 30px;
            font-weight: bold;
            text-align: center;
        }

        .stButton>button {
            background-color: white;
            color: #66c2ff;
            border-color: #66c2ff;
        }

        .stTextInput>div>div>input {
            background-color: blue;
        }

        .stTextArea>div>div>textarea {
            background-color: white;
        }

        .stSelectbox>div>div>div {
            background-color: blue;
        }

        .stCheckbox>div>div>div>div {
            background-color: white;
        }

        .stNumberInput>div>div>input {
            background-color: blue;
        }

        .stMultiselect>div>div>div>div>div {
            background-color: blue;
        }

        .stAlert {
            background-color: white;
        }

        .social-links img {
            margin: 0 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Create the navigation bar
menu = ["Home", "Contact Me", "Portfolio"]
choice = st.sidebar.selectbox("Select a page", menu)

# Display the appropriate page based on the user's choice
if choice == "Home":
    home()
elif choice == "Contact Me":
    contact()
else:
    portfolio()

# Display the footer
footer()
