import streamlit as st
import pandas as pd
import plotly.express as px
import time
import os

st.set_page_config(page_title="NIDS Dashboard", page_icon="", layout="wide")
st.title(" Network Intrusion Detection System")

def load(path):
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        return pd.DataFrame()
    try:
        return pd.read_csv(path)
    except:
        return pd.DataFrame()

packets = load("data/captured_packets.csv")
alerts  = load("data/alerts.csv")

c1, c2, c3, c4 = st.columns(4)
c1.metric(" Packets", len(packets))
c2.metric(" Alerts", len(alerts))
c3.metric(" Unique Sources", packets['src_ip'].nunique() if not packets.empty else 0)
c4.metric(" Last Packet", packets['timestamp'].iloc[-1] if not packets.empty else "—")

st.divider()
st.subheader(" Recent Alerts")
if alerts.empty:
    st.info("No alerts yet.")
else:
    st.dataframe(alerts.tail(20).iloc[::-1], use_container_width=True)

if not packets.empty:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader(" Protocol Distribution")
        st.plotly_chart(px.pie(packets, names='protocol', hole=0.4), use_container_width=True)
    with col2:
        st.subheader(" Top Source IPs")
        top = packets['src_ip'].value_counts().head(10).reset_index()
        top.columns = ['src_ip', 'count']
        st.plotly_chart(px.bar(top, x='count', y='src_ip', orientation='h'), use_container_width=True)

    st.subheader(" Recent Packets")
    st.dataframe(packets.tail(30).iloc[::-1], use_container_width=True)

time.sleep(3)
st.rerun()
