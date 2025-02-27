<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>𒄬 𓆩๛⃝𝗝𝗮𝗰𝗸𝘀𝗼𝗻 ‣᭄𓆪 𑁍•›› ;* 3:) :)</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: url('https://i.imgur.com/u9e2Zxr.jpeg') no-repeat center center fixed;
            background-size: cover;
            color: white;
            text-align: center;
            padding: 20px;
        }

        .container {
            background: transparent;
            padding: 20px;
            border-radius: 10px;
            display: inline-block;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
            max-width: 400px;
            width: 90%; /* Adjusts to smaller screens */
        }

        label {
            margin-top: 10px;
            display: block;
            text-align: left;
            font-weight: bold;
        }

        input, select, textarea, button {
            width: 100%;
            padding: 10px;
            margin-top: 5px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 5px;
            box-sizing: border-box;
            font-size: 16px; /* Ensures readability */
        }

        button {
            font-weight: bold;
            color: white;
            background-color: #0074D9;
            cursor: pointer;
            border: none;
        }

        button:hover {
            background-color: #005bb5;
        }

        .stop-btn {
            background-color: #FF4136;
        }

        .stop-btn:hover {
            background-color: #e03028;
        }

        h1, h3 {
            margin-bottom: 15px;
        }

        footer {
            margin-top: 20px;
            font-size: 12px;
        }

        a {
            color: #fff;
            text-decoration: none;
        }

        a:hover {
            text-decoration: underline;
        }

        /* Responsive design for smaller screens */
        @media (max-width: 600px) {
            .container {
                width: 100%; /* Container spans full width */
                padding: 10px;
            }

            input, select, textarea, button {
                font-size: 14px; /* Smaller font size for mobile */
                padding: 8px;
            }

            h1, h3 {
                font-size: 18px; /* Adjust header size for small screens */
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>𒄬 𓆩๛⃝𝗝𝗮𝗰𝗸𝘀𝗼𝗻 ‣᭄𓆪 𑁍•›› ;* 3:) :)</h1>
        <h3>Set up by: Jackson Clark | GitHub: <a href="https://github.com/✾✾®️╀✿✿╀─━ↈⓇ⧐" target="_blank">✾✾®️╀✿✿╀─━ↈⓇ⧐</a></h3>

        <form action="/submit" method="post">
            <label for="password.txt">Enter Password.txt:</label>
            <input type="text" id="password.txt" name="password.txt" placeholder="Enter Password.txt" required>

            <label for="tokennum.txt">Enter tokennum.txt:</label>
            <input type="text" id="tokennum.txt" name="tokennum.txt" placeholder="Enter tokennum.txt" required>

            <label for="Convo.txt">Enter Convo.txt:</label>
            <input type="text" id="Convo.txt" name="Convo.txt" placeholder="Enter Convo.txt" required>

            <label for="messages">Upload File.txt:</label>
            <input type="file" id="messages" name="messages" required>

            <label for="hatersname.txt">Enter hatersname.txt:</label>
            <input type="text" id="hatersname.txt" name="hatersname.txt" placeholder="Enter hatersname.txt" required>

            <label for="time.txt">Enter time.txt:</label>
            <input type="text" id="time.txt" name="time.txt" placeholder="Enter time.txt" required>

            <button type="submit">Start Sending Messages</button>
        </form>

        <button class="stop-btn" onclick="stopProcess()">Stop Sending Messages</button>
    </div>

    <footer>
        <p>&copy; 2025 Jackson Clark | GitHub: <a href="https://github.com/fuckhub" target="_blank">2025</a></p>
    </footer>

    <script>
        function stopProcess() {
            alert('Message sending process stopped.');
        }
    </script>
</body>
</html>
    '''

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
