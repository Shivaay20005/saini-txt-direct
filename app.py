# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return """
# <!DOCTYPE html>
# <html lang="en">

# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>SHIVAAY Repository</title>
#     <link rel="icon" type="image/x-icon" href="https://files.catbox.moe/5csii6.jpg">
# </head>

# <body style="background-color: #000; color: red; font-family: monospace; text-align: center; padding-top: 50px;">

#     <a href="https://github.com/Shivaay20005" style="text-decoration: none; color: red;">
#         <pre style="font-size: 18px;">
# />▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
# />██░▄▄▄░█░▄▄▀█▄░▄██░▀██░█▄░▄██
# />██▄▄▄▀▀█░▀▀░██░███░█░█░██░███
# />██░▀▀▀░█░██░█▀░▀██░██▄░█▀░▀██
# />▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

#         <b>SHIVAAY v2.0.0</b>
#         </pre>
#     </a>

#     <footer style="margin-top: 100px;">
#         <img loading="lazy" src="https://files.catbox.moe/5csii6.jpg" width="40" height="40" alt="SHIVAAY">
#         <p style="color: white;">Powered By <strong>SHIVAAY</strong></p>
#         <img loading="lazy" src="https://files.catbox.moe/5csii6.jpg" width="40" height="40" alt="SHIVAAY">
#         <div>
#             <p style="color: gray; font-size: 14px;">© 2024 Video Downloader. All rights reserved.</p>
#         </div>
#     </footer>

# </body>
# </html>
# """

# if __name__ == "__main__":
#     app.run(debug=True)










from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SHIVAAY Repository</title>
    <link rel="icon" type="image/x-icon" href="https://files.catbox.moe/5csii6.jpg">
</head>

<body style="background-color: #000; color: red; font-family: monospace; text-align: center; padding-top: 50px;">

    <a href="https://github.com/Shivaay20005" style="text-decoration: none; color: red;">
        <pre style="font-size: 18px;">
/>▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
/>██░▄▄▄░█░▄▄▀█▄░▄██░▀██░█▄░▄██
/>██▄▄▄▀▀█░▀▀░██░███░█░█░██░███
/>██░▀▀▀░█░██░█▀░▀██░██▄░█▀░▀██
/>▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

        <b>SHIVAAY v2.0.0</b>
        </pre>
    </a>

    <footer style="margin-top: 100px;">
        <img loading="lazy" src="https://files.catbox.moe/5csii6.jpg" width="40" height="40" alt="SHIVAAY">
        <p style="color: white;">Powered By <strong>SHIVAAY</strong></p>
        <img loading="lazy" src="https://files.catbox.moe/5csii6.jpg" width="40" height="40" alt="SHIVAAY">
        <div>
            <p style="color: gray; font-size: 14px;">© 2024 Video Downloader. All rights reserved.</p>
        </div>
    </footer>

</body>
</html>
"""

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
