# OpenP

Hey, I'm Harley.  
This is a personal tool I built to open my projects faster — no more typing repetitive `cd` and `code .` commands every time I work on something.

---

## 💡 Why I Made This

Every time I wanted to open a project, I'd do this:

- Open the folder in File Explorer
- Click the address bar, type `cmd`
- Then type `code .` to open it in VS Code
- Or type `cd` to specific directory project then type `code .`.

Now that might sound fine... until you have multiple folders like:

- `/backend`
- `/frontend`
- `/mobile-frontend`

And I do this multiple times. Every. Single. Day.

Yeah, sure — I could just open them from VS Code directly or group them all into one folder…  
But that's not how I've worked for the past 4 years, That's gay as fuck. That setup doesn’t fit **how I like to move**. I want **control**, **speed**, and **workflow comfort** — not someone else's ideal.

So this CLI tool, `openp`, lets me:

- Save project configurations 
  -- add config path(s)
  -- edit config path(s)
- Automatically open multiple folders at once in VS Code
- Avoid `cd` and `code .` over and over

It's part lazy, part genius. Mostly genius. 😏



## 🛠️ How to Set This Up

This is how I set it up on my own machine:

1. In my user directory (`C:\Users\sampleuser\`), I created a folder named `DevTools`
2. I moved or for you clone this project into that folder, so the path looks like this: (`C:\Users\sampleuser\DevTools\openp`)
3. 3. I opened **Environment Variables** from System Settings, selected the **"Path"** under User Variables, and added the full path to the `openp` folder.
4. You'll also need to have **Python** installed to run this tool.

## 🚀 How to Use It

After adding the folder to your environment path, you can:

- Run `openp` in your terminal to launch the CLI tool  
This lets you:
- Add new config paths
- Edit existing ones

- Once you’ve created a config, you can run: openp -configname 

This will instantly open all folders in that config using VS Code.
No more typing `cd` and `code .` over and over. Set it once — and launch full-stack projects like a boss.


## ⚠️ Disclaimer

This is a personal project. Some words or expressions used here reflect my personality and humor — not intended to offend. If you're cool with that, you're welcome here.
