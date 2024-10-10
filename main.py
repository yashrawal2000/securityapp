import tkinter as tk
from tkinter import ttk
from scanner.dashboard import Dashboard
from scanner.proxy import Proxy
from scanner.repeater import Repeater
from scanner.encoder_decoder import EncoderDecoder

class WebScannerApp:
    def __init__(self, root):
        self.root = root
        root.title("YMR Web Scanner")

        # Create a notebook (tabbed layout)
        notebook = ttk.Notebook(root)
        notebook.pack(fill="both", expand=True)

        # Add Dashboard Tab
        self.dashboard_frame = ttk.Frame(notebook)
        notebook.add(self.dashboard_frame, text="Dashboard")
        self.dashboard = Dashboard(self.dashboard_frame)
        self.dashboard.pack(fill="both", expand=True)

        # Add Proxy Tab
        self.proxy_frame = ttk.Frame(notebook)
        notebook.add(self.proxy_frame, text="Proxy")
        self.proxy = Proxy(self.proxy_frame)
        self.proxy.pack(fill="both", expand=True)

        # Add Repeater Tab
        self.repeater_frame = ttk.Frame(notebook)
        notebook.add(self.repeater_frame, text="Repeater")
        self.repeater = Repeater(self.repeater_frame)
        self.repeater.pack(fill="both", expand=True)

        # Add Encoder/Decoder Tab
        self.encoder_decoder_frame = ttk.Frame(notebook)
        notebook.add(self.encoder_decoder_frame, text="Encode/Decode")
        self.encode_decode = EncoderDecoder(self.encoder_decoder_frame)
        self.encode_decode.pack(fill="both", expand=True)

# Running the main application
if __name__ == "__main__":
    root = tk.Tk()
    app = WebScannerApp(root)
    root.mainloop()
