import gradio as gr
import subprocess
import sys
import os

# --- Debugging Step: Print the Python executable running this script ---
print(f"--- Gradio App started with Python: {sys.executable} ---")
print(f"--- Current Working Directory: {os.getcwd()} ---")

# python -m venv venv
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
# .\venv\Scripts\Activate.ps1
# pip install -r requirements.txt
# python gradio_app.py
# deactivate

def run_evaluation(model_to_load, stock_name, initial_balance, window_size):
    command = [
        "python", "evaluate.py",
        "--model_to_load", model_to_load,
        "--stock_name", stock_name,
        "--initial_balance", str(int(initial_balance)),
        "--window_size", str(int(window_size))
    ]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout + "\n" + result.stderr

gr.Interface(
    fn=run_evaluation,
    inputs=[
        gr.Textbox(label="Model to Load", value="DQN_ep10"),
        gr.Textbox(label="Stock Name", value="^GSPC_2018"),
        gr.Number(label="Initial Balance", value=50000),
        gr.Number(label="Window Size", value=10)
    ],
    outputs="text"
).launch()