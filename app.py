import os
from flask import Flask, request, render_template, redirect
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Get PDF Links from environment variables
PDF_LINKS = {
    "hindi": os.getenv("HINDI_PDF_LINK"),
    "english": os.getenv("ENGLISH_PDF_LINK"),
}

@app.route('/download', methods=["GET", "POST"])
def download_page():
    order_id = request.args.get("order_id")  # Get order ID from Cashfree redirect

    # Check if order_id exists
    if not order_id:
        return "Invalid Access! You must come through payment gateway.", 403
    
    if request.method == "POST":
        selected_lang = request.form.get("language")
        
        # Redirect to the selected PDF
        return redirect(PDF_LINKS[selected_lang])

    return render_template("download.html", order_id=order_id)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
