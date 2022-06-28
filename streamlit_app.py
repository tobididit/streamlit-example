# import module
import streamlit as st

# Title
st.title("Thanks for choosing to use Odin's Cloud Cost Calculator !!!")


# Selection box

# first argument takes the titleof the selectionbox
# second argument takes options
Nodename = st.selectbox("Nodename: ",
					['gpu-eu-w2a', 'gpu-eu-w2b', 'pool-infra', 'pool-micro-services-cpu', 'pool-pulsar'])

# print the selected hobby
st.write("Your hobby is: ", Nodename)

