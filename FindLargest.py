import streamlit as st

st.title("Largest Among Three Number")

def find_largest(num1,num2,num3):
    if(num2<num1>num3):
        return num1
    elif(num1<num2>num3):
        return num2
    else:
        return num3

def user_input_feature():
    first_number = st.number_input("First Number")
    second_number = st.number_input("Second Number")
    third_number = st.number_input("Third Number")
    
    if(st.button("Find Largest")):
        largest = find_largest(first_number,second_number,third_number)
        st.success(f"The largest number is {largest}")
        
if __name__=="__main__":
    user_input_feature()