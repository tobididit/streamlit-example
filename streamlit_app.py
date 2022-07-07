# import module
import streamlit as st
import math

@st.cache(allow_output_mutation=True)
def persistdata():
    return {}

# Title
st.title("Thanks for choosing to use Odin's Cloud Cost Calculator !!!")



# Selection box
totalcost = persistdata()
with st.form("costinmonth"):
	
	gpueuw2a = {
  "nofnodes": 3,
  "pphinstance": 0.52,
  "minuser": 4,
  "guessmax": 5,
  "nodeneeded": 75,
  "minuserpernode": 1.333333333
}
# print(gpueuw2a["year"])

	gpueuw2b = {
  "nofnodes": 2,
  "pphinstance": 0.52,
  "minuser": 4,
  "guessmax": 4,
  "nodeneeded": 50,
  "minuserpernode": 2
}
# print(thisdict["year"])

	poolinfra = {
  "nofnodes": 1,
  "pphinstance": 0.2,
  "minuser": 6,
  "guessmax": 10,
  "nodeneeded": 17,
  "minuserpernode": 6
}

	poolmicroservicescpu = {
  "nofnodes": 1,
  "pphinstance": 0.2,
  "minuser": 10,
  "guessmax": 100,
  "nodeneeded": 10,
  "minuserpernode": 10
}

	poolpulsar = {
  "nofnodes": 1,
  "pphinstance": 0.79,
  "minuser": 5,
  "guessmax": 10,
  "nodeneeded": 20,
  "minuserpernode": 5
}


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

	submitted = st.form_submit_button("Submit")

	if submitted:
		cma = math.ceil((gpueuw2a["nodeneeded"] * hours * days * 4.345 * gpueuw2a["pphinstance"]))
		cmb = math.ceil((gpueuw2b["nodeneeded"] * hours * days * 4.345 * gpueuw2b["pphinstance"]))
		cmc = math.ceil((poolinfra["nodeneeded"] * hours * days * 4.345 * poolinfra["pphinstance"]))
		cmd = math.ceil((poolmicroservicescpu["nodeneeded"] * hours * days * 4.345 * poolmicroservicescpu["pphinstance"]))
		cme = math.ceil((poolpulsar["nodeneeded"] * hours * days * 4.345 * poolpulsar["pphinstance"]))

		st.text("Cost in a month is {}.".format(cma + cmb + cmc + cmd + cme))
		totalcost[cma + cmb + cmc + cmd + cme] = cma + cmb + cmc + cmd + cme
		st.text("Procedures is {}.".format(users * hours * days * 4.345 / 0.5))
		procedures[users * hours * days * 4.345 / 0.5] = users * hours * days * 4.345 / 0.5
		st.text("Price per Procedure is {}.".format(totalcost / procedures))
		#st.text("Cost in a month is {}.".format(totalcost))


	# first argument takes the titleof the selectionbox
	# second argument takes options
# 	Nodename = st.selectbox("Nodename: ",
# 						['gpu-eu-w2a', 'gpu-eu-w2b', 'pool-infra', 'pol-micro-services-cpu', 'pool-pulsar'])

	# print the selected hobby
# 	st.write("Your selected Nodename is: ", Nodename)
	
# 	minuser = st.number_input("how many minuser?")
# 	users = st.number_input("guess how many users?")
# 	submitted = st.form_submit_button("Submit")
# 	if submitted:
# 		nodeneeded = math.ceil(users / minuser)
# 		st.text("Your Node needed is {}.".format(nodeneeded))
# 		nodeholder[Nodename] = nodeneeded
# 		st.text("Your Node needed is {}.".format(nodeholder))
		
		
# with st.form("TotalCost"):
	

# 	MT = st.selectbox("MachineType: ",
# 						 ['n1-standard-4', 'n2-standard-4', 'n2-standard-16'])


	# print the selected MT
# 	st.write("Your selected MachineType is: ", MT)


	# TAKE INPUT in figures needed

# 	pphinstance = st.number_input("how many pph/instance?")


# 	Services = st.selectbox("Services: ",
# 						 ['polyp-det', 'ms-all', 'websocket/webserver', 'freeze/image/storage', 'prediction storage', 'pulsar'])


	# print the selected MT
# 	st.write("The service you are using is: ", Services)


# 	users = st.number_input("guess how many users?")


		# slider

	# first argument takes the title of the slider
	# second argument takes the starting of the slider
	# last argument takes the end number
# 	hours = st.slider("How many hours in a day", 1, 24)

	# print the level
	# format() is used to print value
	# of a variable at a specific position
# 	st.text('Selected: {}'.format(hours))

# 	days = st.slider("How many days in a week", 1, 7)
# 	st.text('Selected: {}'.format(days))


# 	procedurelength = st.number_input("What is the proocedure length in hours?")

# 	submitted = st.form_submit_button("Submit")
# 	if submitted:
# 		costpermonth = 0
# 		for key, value in nodeholder.items():
# 			costpermonth += (value * hours * days * 4.345 * pphinstance)
# 		st.text("Your cost per month is {}.".format(costpermonth))
		
# 		procedures = (users * hours * days * 4.345 / procedurelength)
# 		st.text ("Procedures is {}.".format(procedures))
# 		priceperprocedure = (costpermonth / procedures)
# 		st.text ("Price per Procedures is {}.".format(priceperprocedure))
