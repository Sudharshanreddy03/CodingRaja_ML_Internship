import streamlit as st
from textblob import TextBlob
  
  
from streamlit_extras.let_it_rain import rain
  
st.title("Sentiment Analysis")
  
message = st.text_area("Please Enter your text")
  
if st.button("Analyze the Sentiment"):
  blob = TextBlob(message)
  result = blob.sentiment
  polarity = result.polarity
  subjectivity = result.subjectivity
  if polarity < 0:
    st.warning("The entered text has negative sentiments associated with it"+str(polarity))
    
  if polarity >= 0:
    st.success("The entered text has positive sentiments associated with it."+str(polarity))
  st.success(result)
