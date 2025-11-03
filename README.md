# 🟩 Simple Wordle (Python + Tkinter)

A **lightweight 4-letter Wordle game** built using **Python** and **Tkinter**.  
This project provides a fun, minimal version of the popular Wordle game — perfect for beginners learning GUI development in Python.

---

## 🎮 Features

- 🎯 Guess the **4-letter secret word** in **8 attempts**
- 🟩 **Green** → Correct letter in the correct position  
- 🟨 **Yellow** → Correct letter in the wrong position  
- ⬜ **Gray** → Letter not in the word
- 🧠 Randomly chosen secret word each game
- 💬 Popup messages for win/loss
- 🪶 Clean GUI layout (350×500 window)
- 🔤 Case-insensitive input

---

## 🧩 How to Run

### 1️⃣ Install Python  
Make sure you have **Python 3.8+** installed.  
Check using:
```bash
python --version
```

### 2️⃣ Save the Script  
Save the following Python file as:
```
wordle_lite.py
```

### 3️⃣ Run the Game  
Open a terminal in the folder where the file is saved and run:
```bash
python wordle_lite.py
```

---

## 📂 File Structure

```
wordle_lite/
│
├── wordle_lite.py       # Main game file
└── README.md             # Documentation
```

---

## 🧠 Game Logic Summary

- A secret word (like `APPLE`, `CRANE`, `HELLO`, etc.) is selected randomly.  
- You enter a **4-letter guess** in the input box.  
- The app checks each letter:
  - ✅ **Green:** Letter is correct and in the right position  
  - ⚠️ **Yellow:** Letter exists in the word but in the wrong position  
  - ❌ **Gray:** Letter doesn’t exist in the word  
- You have **8 chances** to guess it right.
- Game ends when:
  - 🎉 You guess correctly → “You Win!” popup  
  - 😔 You run out of guesses → “Game Over!” popup  

---

## 🖼️ Screenshot / Gameplay Video

🎥 **Add your gameplay demo here!**

You can record the screen using OBS, Xbox Game Bar, or any recorder and add:

### ▶️ YouTube Link
```markdown
https://youtu.be/your-demo-link
```

### 🖼️ Optional Screenshot
![Gameplay Screenshot](screenshots/demo.png)

If you host your video on YouTube, you can also embed a clickable thumbnail like this:
```markdown
[![Watch the video](https://img.youtube.com/vi/your-video-id/maxresdefault.jpg)](https://youtu.be/your-video-id)
```

---

## 💡 Customization

You can easily modify:
- `WORD_LIST` → Add your own secret words  
- `WORD_LENGTH` → Change number of letters  
- `MAX_GUESSES` → Adjust the number of tries  
- Colors → Change `COLOR_GREEN`, `COLOR_YELLOW`, etc.  
- Fonts and layout → Adjust in `create_widgets()`  

---

## 📜 License

This project is **open-source** and free to use for learning or personal use.  
Feel free to modify and improve it!

---

**👨‍💻 Author:** Daksh Jain  
**🧠 Built with:** Python + Tkinter  
**📦 Version:** 1.0
