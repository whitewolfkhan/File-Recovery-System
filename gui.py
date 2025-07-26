import customtkinter as ctk
import threading
import subprocess
from scanner import unified_scan  # Our new unified scanning function
from logger import log_recovery  # (Assuming you have a simple logger)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class RecoveryApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("File System Recovery Tool")
        self.geometry("600x600")

        # Partition selection label and dropdown.
        self.label = ctk.CTkLabel(self, text="Select Partition:")
        self.label.pack(pady=10)

        self.drive_var = ctk.StringVar()
        self.drive_dropdown = ctk.CTkComboBox(self, variable=self.drive_var, values=self.get_drives())
        self.drive_dropdown.pack(pady=10)

        # Single scan button that performs unified scanning.
        self.scan_button = ctk.CTkButton(self, text="Scan for Deleted Files", command=self.start_unified_scan)
        self.scan_button.pack(pady=10)

        # Label and textbox for showing recovered/deleted file names.
        self.deleted_files_label = ctk.CTkLabel(self, text="Recovered/Deleted Files:")
        self.deleted_files_label.pack(pady=10)

        self.deleted_files_textbox = ctk.CTkTextbox(self, height=100, width=200)
        self.deleted_files_textbox.pack(pady=10)
        
        # Progress bar and percentage label.
        self.progress_bar = ctk.CTkProgressBar(self)
        self.progress_bar.pack(pady=10)
        self.progress_bar.set(0)
        self.progress_bar.configure(fg_color="blue")

        self.progress_percentage_label = ctk.CTkLabel(self, text="0%")
        self.progress_percentage_label.pack(pady=5)

        # Label for current file being scanned (for debugging).
        self.current_file_label = ctk.CTkLabel(self, text="Currently scanning: None")
        self.current_file_label.pack(pady=5)

        self.result_label = ctk.CTkLabel(self, text="")
        self.result_label.pack(pady=10)
