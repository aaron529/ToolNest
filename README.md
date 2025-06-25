# ToolNest - Multi-Utility Desktop Assistant 🧰🖥️

**ToolNest** is a modern, sleek Python desktop application built using **CustomTkinter**, combining a rich UI with practical tools like **QR Code generation**, **Text-to-Speech**, and an **Internet Speed Test** — all wrapped in a light/dark theme-aware interface.

---

## ✨ Features

- 🔐 **User Authentication System**  
  Beautiful login/register interface with smooth transitions and user-friendly layout.

- 🧑‍💼 **Personalized Dashboard**  
  A warm greeting with three main functional areas:
  - QR Code Generator
  - Text-to-Speech Engine
  - Internet Speed Tester

- 🎨 **Modern UI Design**  
  - CustomTkinter-powered theming with **light and dark mode**
  - Large, gradient-labeled buttons with icon support
  - Responsive layout that adapts to screen size changes

- 📷 **QR Code Generator**  
  - Customize version, error correction, fill and background color
  - Real-time preview with blurred-to-clear animation
  - Export QR as PNG

- 🔊 **Text-to-Speech (TTS)**  
  - Adjustable rate and volume
  - Male/Female voice toggle
  - **Animated visualizer** and lyrics output
  - Save as MP3

- 🚀 **Internet Speed Test**  
  - Download, upload, and ping metrics
  - Auto-categorized status via color-coded icons (Green, Yellow, Red)

---

## 🛠️ Technologies Used

- **Python 3**
- **CustomTkinter**
- **Pillow (PIL)**
- **pyttsx3** – TTS Engine
- **qrcode** – QR Code generator
- **speedtest-cli** – Speed test API

---

## 🗂 Project Structure (simplified)

ToolNest/  
├── forms/          (Contains Login and Registration form)  
├── images/         (Contains required and theme-aware images)  
│   ├── dark/  
│   └── light/  
├── pages/          (Contains the 4 main app pages: Home, QR, TTS, Speed Test)  
└── main.py         (Main file and app entry point)


## 🚧 Notes

- User authentication is simple and **dictionary-based** for demo purposes.
- Voice files, QR codes, and speed test results are processed locally.
- Saved audio output defaults to `audio.mp3`.

---

## 📸 Screenshots
![image](https://github.com/user-attachments/assets/a8cde37f-c1c8-4bed-bdc1-db0ddeb39e8f)

![image](https://github.com/user-attachments/assets/14741774-549f-4549-aa64-4ca589411031)

![image](https://github.com/user-attachments/assets/04106a1d-16a0-4ec4-b1df-ddfbc9f1c75c)

![image](https://github.com/user-attachments/assets/b706f2e1-02e7-42ae-8df4-ee862fd8e41d)

![image](https://github.com/user-attachments/assets/77db1de8-2555-49cc-bfa9-f22a47d6e12d)


---

## 📦 How to Run

```bash
pip install customtkinter pillow pyttsx3 qrcode speedtest-cli
python main.py
```
