import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Display Title
st.title("This is a title.") 


# Display Message
st.write("Output characters here")


# Create Table
df = pd.DataFrame([[0,1,2],[3,4,5],[6,7,8]],columns=["Column1","Column2","Column3"])
st.table(df)


# Create Dataframe
df = pd.DataFrame([[0,1,2],[3,4,5],[6,7,8]],columns=["Column1","Column2","Column3"])
st.dataframe(df)


# Show Mathematical Formula
st.latex(
    r"""
    S = \sum^{N}_{i=0}a_{n}
    """
)


# Create Graph
df = pd.DataFrame()
df["x"] = np.arange(0,10)
df["y"] = np.power(np.arange(0,10),2)
st.write("Line Chart")
st.line_chart(data=df)
st.write("Area Chart")
st.area_chart(data = df)
st.write("Bar Chart")
st.bar_chart(data=df)

fig,ax = plt.subplots(figsize=(5,3))
ax.scatter(x=df["x"],y=df["y"])
plt.xlabel("x")
plt.ylabel("y")
st.pyplot(fig)


# Checkbox
if(st.checkbox("Check here")):
    st.write("Checked !")
    

# Selectbox
select_list = ["Apple","Orange","Grape"]
ret = st.selectbox("Select a fruit : ",select_list)
st.write(ret)


# Multiselect
select_list = ["Apple","Orange","Grape","Peach"]
ret = st.multiselect("Choose as many fruits as you like",select_list)
st.write(ret)


# Radio
select_list = ["Apple","Orange","Grape","Peach"]
ret = st.radio("Select one fruit",select_list)
st.write(ret)


# Input Number
ret = st.number_input("Enter a number here",min_value=0,max_value=10,step=1)
st.write("Your number is : ",ret)


# Sidebar
ret = st.sidebar.number_input("Enter a number here",min_value=0,max_value=10,step=1)
st.write(ret)