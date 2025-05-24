# 🖍️ Blackboard - Python Virtual Drawing Board with Webcam

**Blackboard** is a Python-based virtual drawing board that allows users to draw on a full-screen canvas in real time. It includes drawing tools like **pen**, **pencil**, **eraser**, **color picker**, and **webcam integration**, making it perfect for sketching, teaching, or quick notes.

---

## 🚀 Features

- ✅ Fullscreen virtual canvas
- 🖌️ Drawing tools: Pen, Pencil, Eraser
- 🎨 Custom color picker
- 📷 Real-time webcam feed integration
- 💾 Save drawings as PNG images
- 🧰 Minimalistic, movable tool panel
- 🎯 Hotkey support for quick access to tools
- 🖥️ Supports all screen sizes

---

## 🖼️ Interface Overview

- **Canvas:** Fullscreen blackboard to draw on.
- **Tool Panel:** Choose between tools like Pen, Pencil, Eraser, Color, Save, and Camera.
- **Webcam Feed:** Small real-time camera window in the corner.

---

## 🎮 Controls & Hotkeys

| Action              | Key/Mouse            |
|---------------------|----------------------|
| Start Drawing       | Left Mouse Button    |
| Toggle Fullscreen   | `F11`                |
| Toggle Camera       | `F12`                |
| Choose Color        | `Ctrl + C`           |
| Save Canvas         | `Ctrl + S`           |
| Use Eraser          | `Ctrl + E`           |
| Use Pen             | `Ctrl + P`           |
| Use Pencil          | `Ctrl + X`           |
| Use Rectangle Tool  | `Ctrl + R` *(coming soon)* |
| Use Oval Tool       | `Ctrl + O` *(coming soon)* |
| Exit Application    | `Esc` or window close |

---

## 💾 Save Drawings

Drawings are saved as **EPS (vector image)** by default. You can easily convert it to PNG using PIL or an image converter.

To save:

Ctrl + S

blackboard-python/
├── blackboard.py         # Main application file
├── drawing.eps           # Saved drawing (after first save)
├── README.md             # Project documentation