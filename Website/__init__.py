from flask import Flask, render_template_string

app = Flask(__name__)

# Your romantic HTML page content
romantic_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Romantic Home</title>
    <style>
        body {
            background-color: #FFE4E1; /* Misty Rose */
            font-family: 'Times New Roman', Times, serif;
            color: #8B0000; /* Dark Red */
            text-align: center;
            padding: 50px;
        }
        .title {
            border: 3px solid #8B0000;
            padding: 20px;
            margin: 20px auto;
            width: fit-content;
            background-color: #FFF0F5; /* Lavender Blush */
            border-radius: 10px;
            font-size: 3em;
        }
        p {
            font-size: 1.5em;
        }
        .heart {
            color: #FF1493; /* Deep Pink */
            font-size: 5em;
        }
        .message-box {
            border: 2px solid #8B0000;
            padding: 20px;
            margin: 20px auto;
            width: 70%;
            background-color: #FFF0F5; /* Lavender Blush */
            border-radius: 10px;
        }
        a {
            color: #8B0000;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="title">Bowser's Valentine's Day Project</div>
    <p>I thought i'd put my new skills to use with this new soppy code. Hopefully it passes the fact I forgot the card in Manchester.</p>
    <p class="heart">❤️</p>
    <h2>Happy Valentine's Day!</h2>
    <div class="message-box">
        <h3>Reason 1: Your Kindness</h3>
        <p>You always go out of your way to help others.</p>
        <p>You have a heart of gold and a smile that brightens the day.</p>
        <p>Your kindness knows no bounds, making everyone feel special.</p>
    </div>
    <div class="message-box">
        <h3>Reason 2: Your Humor</h3>
        <p>You make me laugh even on my darkest days.</p>
        <p>I love your crazy antics - especially the way you wobble like a cute penguin.</p>
        <p>I especially love your crazy borderline racist comments - is there someting wong with that.</p>
    </div>
    <div class="message-box">
        <h3>Reason 3: Your Strength</h3>
        <p>I love the way you power through everything - despite everything that is affecting you.</p>
        <p>I love how even when you're down - you are my support and pillar.</p>
        <p>You are the strongest / most determined person I know.</p>
    </div>
<h1>Our Love Story</h1>
    <p><a href="https://drive.google.com/your-google-drive-link-here" target="_blank">View Our Photos on Google Drive</a></p>
    <p><a href="/">Back to Home</a></p>
</body>
</html>

@app.route('/')
def home():
    return render_template_string(romantic_html)

if __name__ == '__main__':
    app.run()
