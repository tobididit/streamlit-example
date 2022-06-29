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
numberofnodes = st.number_input("how many nodes are needed?")	
	
pphinstance = st.number_input("how many pph/instance?")

maxuser = st.number_input("how many maxuser?")

minuser = st.number_input("how many minuser?")

guessmax = st.number_input("guess how many max users?")

Services = st.selectbox("Services: ",
					 ['polyp-det', 'ms-all', 'websocket/webserver', 'freeze/image/storage', 'prediction storage', 'pulsar'])


# print the selected MT
st.write("The service you are using is: ", Services)
	
	
users = st.number_input("guess how many users?")
	

	# slider

# first argument takes the title of the slider
# second argument takes the starting of the slider
# last argument takes the end number
hours = st.slider("How many hours in a day", 1, 24)

# print the level
# format() is used to print value
# of a variable at a specific position
st.text('Selected: {}'.format(hours))

days = st.slider("How many days in a week", 1, 7)
st.text('Selected: {}'.format(days))


procedurelength = st.number_input("What is the proocedure length in hours?")




nodeneeded = (users + minuser)

st.text("Your Node needed is {}.".format(nodeneeded))
