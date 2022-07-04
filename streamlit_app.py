import streamlit
import pandas

streamlit.title('My parents new healthy diner')
streamlit.header('Breakfast Favourites')
streamlit.text('🥣 omega 3 & blueberry oatmeal')
streamlit.text('🥗 kale, spinach & rocket smoothie')
streamlit.text(' 🐔 Hard-boiled Free-Range egg')
streamlit.text('🥑🍞 Avacado toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
