# import module
import streamlit as st

# Title
st.title("Thanks for choosing to use Odin's Cloud Cost Calculator !!!")


# Selection box

# first argument takes the titleof the selectionbox
# second argument takes options
Nodename = st.selectbox("Nodename: ",
					['n1-standard-4', 'n2-standard-4', 'pool-pulsar'])

# print the selected hobby
st.write("Your selected Nodename is: ", Nodename)

Node = st.selectbox("MachineType: ",
					['gpu-u-w2a', 'gpu-u-w2b', 'poo-infra', 'pol-micro-services-cpu', 'poo-pulsar'])

# print the selected hobby
st.write("Your selected MachineType is: ", Node)



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
	
	
	

	# slider

# first argument takes the title of the slider
# second argument takes the starting of the slider
# last argument takes the end number
level = st.slider("Select the level", 1, 5)

# print the level
# format() is used to print value
# of a variable at a specific position
st.text('Selected: {}'.format(level))

