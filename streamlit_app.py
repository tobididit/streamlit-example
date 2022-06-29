# import module
import streamlit as st

# Title
st.title("Thanks for choosing to use Odin's Cloud Cost Calculator !!!")


# Selection box

# first argument takes the titleof the selectionbox
# second argument takes options
Nodename = st.selectbox("Nodename: ",
					['gpu-eu-w2a', 'gpu-eu-w2b', 'pool-infra', 'pol-micro-services-cpu', 'pool-pulsar'])

# print the selected hobby
st.write("Your selected Nodename is: ", Nodename)

MT = st.selectbox("MachineType: ",
					 ['n1-standard-4', 'n2-standard-4', 'n2-standard-16'])

# print the selected MT
st.write("Your selected MachineType is: ", MT)



# Text Input

# save the input text in the variable 'name'
# first argument shows the title of the text input box
# second argument displays a default text inside the text input area
numberofnodes = st.text_input("how many nodes are needed?", "Type Here ...")

# display the name when the submit button is clicked
# .title() is used to get the input text string
if(st.button('Submit')):
	result = numberofnodes.title()
	st.success(result)
	
	pph = st.text_input("how many pph/instance?", "Type Here ...")

# display the name when the submit button is clicked
# .title() is used to get the input text string
if(st.button('Submit')):
	result = pph.title()
	
	
	
	

	# slider

# first argument takes the title of the slider
# second argument takes the starting of the slider
# last argument takes the end number
level = st.slider("Select the level", 1, 5)

# print the level
# format() is used to print value
# of a variable at a specific position
st.text('Selected: {}'.format(level))

