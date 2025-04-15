# 📤 Company Image Uploader

A cute and professional Flask web app for uploading image files (JPG, PNG, AI, PSD, etc.) to Dropbox — themed per company. No login, just a simple passphrase for access.

---

## ✨ Features

- Select from 3 companies: Simple Move, Page Relocation, Baxter Moving
- Upload graphic files categorized as: Graphic, Template, or Photo
- Cute, color-coded themes per company (pastel aesthetic 🌸)
- Frontend + backend file type validation
- Error handling with friendly feedback
- No history stored — perfect for team use
- Optional Dropbox integration (just plug in your token)

---

## 🛠 Setup

1. **Clone the repo**
   ```bash
   git clone https://github.com/YOUR_USERNAME/company-image-uploader.git
   cd company-image-uploader
   ```

2. **Create virtual environment and install dependencies**
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Create a `.env` file**

   Example:
   ```env
   SECRET_KEY=your-super-secret-key
   UPLOAD_PASSPHRASE=your-passphrase
   ALLOWED_FILE_EXTENSIONS=.png,.jpg,.jpeg,.ai,.psd,.heic
   # DROPBOX_TOKEN=your-dropbox-token (optional)
   ```

4. **Run the app**
   ```bash
   flask run
   ```

---

## 📁 Folder Structure

```
project-root/
│
├── app.py
├── .env
├── requirements.txt
├── README.md
│
├── static/
│   ├── style.css
│   └── script.js
│
└── templates/
    ├── home.html
    ├── upload.html
    ├── result.html
    └── passphrase.html
```

---

## 🔐 Security Notes

- Passphrase is stored only in `.env`
- No login required — intended for internal use
- Optional: add IP restrictions, access logging, or browser-persisted keys for extra protection

---

## 🧁 Future Ideas

- Drag & drop file support
- Progress bar while uploading
- Company logos or mascots per theme
- Optional login (if ever needed)

---

Made with 💖 and pastel vibes.
