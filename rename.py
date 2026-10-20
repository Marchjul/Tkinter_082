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

frame_input = ttk.LabelFrame(root, text=" Masukkan Nilai Mata Pelajaran ")
frame_input.pack(padx=30, pady=5, fill="x")
frame_input.columnconfigure(0, weight=1)
frame_input.columnconfigure(1, weight=1)

entries = []
for i, mapel in enumerate(MAPEL):
    ttk.Label(frame_input, text=mapel + " :").grid(
        row=i, column=0, padx=(20, 8), pady=4, sticky="e"
    )
    entry = ttk.Entry(frame_input, width=14, justify="center")
    entry.grid(row=i, column=1, padx=(8, 20), pady=4, sticky="w")
    entries.append(entry)

frame_jurusan = ttk.LabelFrame(root, text=" Pilihan Jurusan ")
frame_jurusan.pack(padx=30, pady=10, fill="x")

combo_jurusan = ttk.Combobox(
    frame_jurusan, values=JURUSAN, state="readonly", justify="center"
)
combo_jurusan.current(0)
combo_jurusan.pack(padx=20, pady=10, fill="x")
