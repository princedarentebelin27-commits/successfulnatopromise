import cv2 
import streamlit as st 
import numpy as np 



cap = cv2.VideoCapture(0)
st.header("image: ")
image_placeholder = st.empty()
st.header("select filter: ")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
     normal_b = st.button("Normal")
with col2:
     hsv_b = st.button("HSV")
with col3:
     grey_b = st.button("Grey")
with col4:
     binary_b = st.button("Binary")
with col5:
     edges_b = st.button("Edges")



while True:
    ret, frame = cap.read()
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    th, binary = cv2.threshold(grey, 155,255, cv2.THRESH_BINARY)
    edges = cv2.Canny (grey,100,100)
    
    
    
    if normal_b:
        image_placeholder.image(frame, channels= "BGR")
        hsv_b = False
        grey_b = False
        binary_b = False
        edges_b = False
    elif hsv_b:
         image_placeholder.image(hsv, channels= "RGB")
         normal_b = False
         grey_b = False
         binary_b = False
         edges_b = False
         
    elif grey_b:
         image_placeholder.image(grey, channels= "GRAY")
         normal_b = False
         hsv_b = False
         binary_b = False
         edges_b = False
         
    elif binary_b:
         image_placeholder.image(binary, channels= "GRAY")
         normal_b = False
         hsv_b = False
         grey_b = False
         edges_b = False
         
    elif edges_b:
         image_placeholder.image(edges, channels= "GRAY")
         normal_b = False
         hsv_b = False
         grey_b = False
         binary_b = False
         

    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
