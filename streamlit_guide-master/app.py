


import streamlit as st
import pandas as pd

import plotly.express as px
import os



def main():
    DATA_URL = (
        os.path.join(os.path.dirname(os.path.abspath(__file__)) , "result.xlsx")
    )

    st.title("Business Infromation System")
    st.sidebar.title("All Functionality")

    st.markdown("### Ahmed Maher Fouzy Mohamed Salam")
    st.markdown("#### Aanalyze student result")
    st.sidebar.markdown("let's get statred 🐦")

    @st.cache(persist=True)
    def load_data():
        data = pd.read_excel(DATA_URL)
        
        return data

    data = load_data()
    header =  data.columns.ravel()







    student_id = st.text_input("Enter your Number")
    st.write(data.query("ID == @student_id "))

    select = st.sidebar.selectbox('Visualization type', ['Bar plot', 'Pie chart'], key='1')
    select_subject = st.sidebar.selectbox("For what?" , header[2:] , key ="1")

    subject_count = data[select_subject].value_counts()
    subject_count = pd.DataFrame({'Sentiment':subject_count.index, 'Mark':subject_count.values})

    if select == 'Bar plot':
        fig = px.bar(subject_count, x='Sentiment', y='Mark', color='Mark', height=500)
        st.plotly_chart(fig)
    else:
        fig = px.pie(subject_count, values='Mark', names='Sentiment')
        st.plotly_chart(fig)





    # st.sidebar.subheader("Compare between result")
    # choice = st.sidebar.multiselect('Pick', header[2:], key=0)


    # if len(choice) > 0:
    #     choice_data = data[(choice)]

    #     st.write(choice_data)
        # fig_0 = px.histogram(
        #                     choice_data, 
        
        #                       height=600, width=800)
        # st.plotly_chart(fig_0)
    # if  st.sidebar.checkbox("Show raw data", False):
    #     st.write(data)



if __name__ == "__main__":
    main()

