# 🧠 File Recovery System

A Python-based file recovery tool that helps scan storage devices, preview recoverable files, and recover lost or deleted data. This project is built with a modular structure and a simple GUI to ease user interaction.

## 🚀 Features

- 🔍 Scans for deleted or lost files from partitions  
- 🧾 Previews recoverable files  
- 💾 Recovers files to a specified location  
- 🖼️ GUI interface for easy usage  
- 🛠️ Logging system for debugging and auditing

## 📁 Project Structure

| File                    | Description                            |
|-------------------------|----------------------------------------|
| `main.py`               | Entry point of the application         |
| `gui.py`                | GUI components and layout              |
| `scanner.py`            | Scanning logic for files and partitions|
| `recovery_utils.py`     | Utilities for file recovery operations |
| `preview.py`            | Preview functionality for files        |
| `partition_recovery.py` | Handles partition-based recovery       |
| `logger.py`             | Handles logging of application events  |
| `.history/`             | Version history of development files   |

## 🛠️ Requirements

- Python 3.x  
- Tkinter or PyQt5 (depending on GUI implementation)  
- Admin privileges (for low-level disk access)

## 📦 Installation

```bash
git clone https://github.com/whitewolfkhan/file-recovery-system.git
cd file-recovery-system
pip install -r requirements.txt
python main.py
