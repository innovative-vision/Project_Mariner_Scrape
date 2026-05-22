# Project Mariner Scrape

Project Mariner (aka Gemini Spark) is open source.

## Other systems that can leverage this code

The setup commands below are also suitable for:

- **WSL2 (Windows Subsystem for Linux):** Use the Mac/Linux command block.
- **Cloud VPS (Vultr, AWS, DigitalOcean):** Run headless for long-term scraping/research tasks.
- **Raspberry Pi 5:** Suitable for Python backend + headless Selenium automation.
- **Apple Silicon (M1/M2/M3):** Runs natively in Terminal/Zsh with no command changes.

## Clean Reddit copy-paste block

**TL;DR:** Imagine you found a secret backdoor to borrow a super-smart robot brain that usually costs big companies $250/month. This one-stop setup takes about 3 minutes and gives you the same browsing/task-running agent power for free.

Before you begin, install:

- Python
- Git
- **Google Chrome**

You also need a free API key from [Google AI Studio](https://aistudio.google.com/).

Choose the correct commands for your operating system.

### Windows (Command Prompt)

```bat
git clone https://github.com/Fandry96/k3-mariner.git
cd k3-mariner
pip install -r requirements.txt
set GEMINI_API_KEY=YOUR_API_KEY_HERE
python -m streamlit run app.py
```

### Mac / Linux

```bash
git clone https://github.com/Fandry96/k3-mariner.git
cd k3-mariner
pip3 install -r requirements.txt --break-system-packages
export GEMINI_API_KEY="YOUR_API_KEY_HERE"
python3 -m streamlit run app.py
```

### Important key safety note

**Do NOT:**

1. Share your API key with anyone (including AI tools).
2. Save it permanently in project files.

**Do this instead:**

- Paste the key into terminal only when needed.
- Store it in a password manager.

Your terminal will print a local URL (usually `http://localhost:8501`). Open it in Chrome, then paste your API key into the app settings and choose your preferred model.

You now have a free, open-source version of Gemini's agent (Project Mariner), and can run it locally for long tasks (including overnight automation).

## Validation notes

This repository only contains documentation. There is no application/test harness here to directly execute or verify the upstream `k3-mariner` runtime commands in CI.
