# gradio display leaderboard

import gradio as gr
import pandas as pd

def leaderboard():
    df = pd.read_csv('leaderboard/wired_network.csv')
    return df

iface = gr.Interface(fn=leaderboard, title="Leaderboard", description="Display leaderboard", allow_flagging=False)
iface.launch()