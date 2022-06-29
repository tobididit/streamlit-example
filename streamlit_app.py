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



	

	
	# TAKE WEIGHT INPUT in kgs
number of nodes = st.number_input("how many nodes are needed?")	
	
pphinstance = st.number_input("how many pph/instance?")

maxuser = st.number_input("how many maxuser?")

minuser = st.number_input("how many minuser?")

guessmax = st.number_input("guess how many max users?")
	
	
	
	

	# slider

# first argument takes the title of the slider
# second argument takes the starting of the slider
# last argument takes the end number
level = st.slider("Select the level", 1, 5)

# print the level
# format() is used to print value
# of a variable at a specific position
st.text('Selected: {}'.format(level))

