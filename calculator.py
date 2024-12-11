import streamlit as st

def calculator():
    st.title("Simple Calculator")

    #Get the input values
    num1=st.number_input("Enter the first number: ")
    num2=st.number_input("Enter the second number: ")

    #Selection Operation
    operation = st.selectbox("Select Operation ", ["+","-","*","/"])


    #perform calculations
    if st.button("Calculate"):
        if operation == "+":
            result =num1+num2
        elif operation == "-":
            result=num1-num2
        elif operation == "*":
            result=num1*num2
        elif operation == "/":
            if num2 == 0:
                result = "Division by zero is error"
            else:
                result=num1/num2

        st.success(f"Result : {result}")

if __name__=="__main__":
    calculator()