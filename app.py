import streamlit as st
import streamlit.components.v1 as stc
import statsmodels
import sklearn
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA # Import the PCA class function from sklearn
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity,linear_kernel
pd.set_option('display.max_columns', None)
pd.set_option("display.precision", 2)

def search_term_if_not_found(term,df):
    result_df=df[df['name'].str.contains(term)]
    return result_df


def get_recommendation(name,df,num_or_rec=5):
    course_indices= pd.Series(df.index,index=df['name'])
    idx=course_indices[name]
    final_result=df[['name','track_name','track_uri']]
    return final_result


def main():
    st.title("Recommendation app")
    st.caption("This site is designed to get recommendation of Spotify Songs")
    menu = ['Home', 'Recommend', 'About']
    choice = st.sidebar.selectbox('Menu', menu)
    df = pd.read_csv('C:/Users/LENOVO/Downloads/feature_engineering_dataset (1).csv')

    if choice == "Home":
        st.subheader("Home")
        st.dataframe(df.head(10))
    elif choice == "Recommend":
        st.subheader("Recommend Music")
        search_term=st.text_input("Search")
        num_of_rec=st.sidebar.number_input("Number",4,30,7)
        if st.button("Recommend"):
            if search_term is not None:
                try:
                    results = get_recommendation(search_term, df, num_of_rec)
                    for row in results.itterrows():
                        rec_name = row[1][0]
                        rec_track = row[1][1]
                        rec_url = row[1][2]
                        # st.write('Name',rec_name,)
                        stc.html(RESULT_TEMP.format(rec_name, rec_track, rec_url))
                except Exception as e:
                    results = 'Not Found'
                    st.warning(results)
                    st.info("Suggesting includes")
                    result_df=search_term_if_not_found(search_term,df)
                    st.dataframe(result_df)



    else:
        st.subheader("About")
        st.text("Built with streamlit by Mahmoud Salama")

if __name__=="__main__":
    main()

