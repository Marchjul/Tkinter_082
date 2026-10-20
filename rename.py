import tkinter as tk
from tkinter import ttk

MAPEL = [f"Nilai Mata Pelajaran {i}" for i in range(1, 11)]

JURUSAN = [
    "Teknologi Informasi",
    "Teknik Sipil",
    "Teknik Mesin",
    "Teknik Elektro",
    "Teknik Industri",
    "Teknik Kimia",
    "Teknik Arsitektur",
]


def hasil_prediksi():
    label_hasil.config(text="Teknologi Informasi")

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.resizable(False, False)

label_judul = ttk.Label(
    root, text="Aplikasi Prediksi Prodi Pilihan", font=("Segoe UI", 16, "bold")
)
label_judul.pack(pady=(20, 10))
