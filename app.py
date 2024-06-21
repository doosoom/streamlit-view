import streamlit as st
import pandas as pd

view = [100,150,30]

st.write('# Youtube view') # 1개면 가장 큰 제목으로 표시됨
st.write('## raw')
view
st.write('## bar chart')
st.bar_chart(view)

sview = pd.Series(view)
sview