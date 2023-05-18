# import module
import streamlit as st

# Title
st.title("Hello World")

# Header
st.header("This is a header")

# Subheader
st.subheader("This is a subheader")

# Text
st.text("Hello this is an introductory text")

# Markdown
st.markdown("### This is a markdown")
st.markdown("> This is a markdown quote")

# Success
st.success("Success")

# Information
st.info("Information")

# Warning
st.warning("Warning")

# Error
st.error("Error")

# Exception - this has to be added later
exp = ZeroDivisionError("Trying to Divide by Zero")
st.exception(exp)

# write text 
st.write("Text with write")

# writing python inbuild function range
st.write(range(10))

# Display Images

# import Image form pillow to open images
from PIL import Image
img = Image.open("C:\\Users\\Jacob\\Pictures\\github-icon-4.jpg")

# display image using streamlit
# width is used to set the width of the image
st.image(img, width=200)

# checkbox
# check if checkbox is checked
# title of the checkbox is show/hide
if st.checkbox("Show/Hide"):
    # display the text if the checkbox returns true value
    st.text("Showing the widget")

# Radio buttom
# first argument is the title of the radio button
# second argument is the options of the radio buttomn
status = st.radio("Select Gender: ", ('Male', 'Female'))

# conditional statement to print
# Male if male is selected else print female
# show the result using the success function
if (status == 'Male'):
    st.success('Male')
else:
    st.success("Female")

# selection box
# first argument takes the titleof the selection
# second argument takes optios
hobby = st.selectbox("Hobbies:", ['Dancing', 'Reading', 'Sports'])

# print the selected hobby
st.write("Your hobby is: ", hobby)

# multi-select box
# first argument takes the box title
# second argument takes the options to show
hobbies = st.multiselect("Hobbies: ", ["Dancing", "Reading", "Sports"])

# write the selected options
st.write("You Selected", len(hobbies), 'hobbies')

# create a simple button that does nothing
st.button("Click for not reason")

# create a button, that when clicked, shows a text
if(st.button("About")):
    st.text("Welcome to the site")

# text input
# save the input text in the variable 'name'
# first argument shows the title of the text input box
# the second arggument displays a default text inside the text input area
name = st.text_input('Enter your name: ')

# display the name when the submit button is clicked
# .title() is used to get the imput text string
if(st.button('Submit')):
    result=name.title()
    st.success(result)

# slider
# first argument takes the title of the slider
# second argument takes the starting of the slider
# last argument takes the end number
level = st.sleder("Select the level", 1,10)

# print the level
# .format() is used to print value
# of a variable at a specific position
st.text('Selected: {}'.format(level))

