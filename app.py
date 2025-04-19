# app.py
from flask import Flask, render_template, request, redirect, url_for, session, flash
import os

# import dropbox  # Keep this commented until Dropbox is ready TODO
# from werkzeug.utils import secure_filename # Keep this commented until Dropbox is ready TODO
from dotenv import load_dotenv

# Load secret key and passphrase from .env file
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

# Set your passphrase in .env
EXPECTED_PASSPHRASE = os.getenv("UPLOAD_PASSPHRASE")

# Pastel theme colors per company
COMPANY_THEMES = {
    "Page Relocation": "#ffdee9",  # light pink
    "Simple Move": "#d0f4de",  # light mint
    "Baxter Moving": "#d0e0f4",  # light blue
}

ALLOWED_EXTENSIONS = [
    ext.strip() for ext in os.getenv("ALLOWED_FILE_EXTENSIONS", "").split(",")
]


def is_allowed_file(filename):
    return os.path.splitext(filename.lower())[1] in ALLOWED_EXTENSIONS


# --- Routes ---


@app.route("/", methods=["GET", "POST"])
def passphrase():
    if request.method == "POST":
        entered = request.form.get("passphrase", "")
        if entered == EXPECTED_PASSPHRASE:
            session["authenticated"] = True
            return redirect(url_for("home"))
        else:
            return render_template("passphrase.html", error="Wrong passphrase!")
    return render_template("passphrase.html")


@app.route("/home")
def home():
	if not session.get("authenticated"):
		return redirect(url_for("passphrase"))

	company_themes = {
		company: COMPANY_THEMES.get(company, "#ffffff")
		for company in COMPANY_THEMES
	}

	return render_template("home.html", company_themes=company_themes)


@app.route("/upload", methods=["GET", "POST"])
def upload():
    if not session.get("authenticated"):
        return redirect(url_for("passphrase"))

    if request.method == "POST":
        company = request.form.get("company")
        image_type = request.form.get("image_type")
        files = request.files.getlist("files")

        theme_color = COMPANY_THEMES.get(company, "#ffffff")

        if not company or not image_type or not files:
            flash("Missing information.")
            return render_template(
                "result.html",
                success=False,
                error="Missing information.",
                company=company,
                theme_color=theme_color,
            )

        invalid_files = [f.filename for f in files if not is_allowed_file(f.filename)]

        if invalid_files:
            return render_template(
                "result.html",
                success=False,
                error=f"The following file(s) are not allowed: {', '.join(invalid_files)}",
                company=company,
                theme_color=theme_color,
            )

        try:
            # raise Exception("Simulated error for testing!") # FOR TESTING PURPOSES ONLY TODO
            # Placeholder for future Dropbox integration
            # dbx = dropbox.Dropbox(os.getenv("DROPBOX_TOKEN"))
            # for file in files:
            #     filename = secure_filename(file.filename)
            #     dropbox_path = f"/{company}/{image_type}/{filename}"
            #     dbx.files_upload(file.read(), dropbox_path, mode=dropbox.files.WriteMode.overwrite)
            pass

        except Exception as e:
            return render_template(
                "result.html",
                success=False,
                error=str(e),
                company=company,
                theme_color=theme_color,
            )

        return render_template(
            "result.html",
            success=True,
            company=company,
            image_type=image_type,
            theme_color=theme_color,
        )

    # GET request — show upload form
    company = request.args.get("company", "Unknown")
    theme_color = COMPANY_THEMES.get(company, "#ffffff")
    allowed_exts_str = ",".join(ALLOWED_EXTENSIONS)
    return render_template(
        "upload.html",
        company=company,
        theme_color=theme_color,
        allowed_extensions=allowed_exts_str,
    )


if __name__ == "__main__":
    app.run(debug=True)
