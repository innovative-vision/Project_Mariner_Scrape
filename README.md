# Project Mariner Scrape

Project Mariner (aka Gemini Spark) is open source.

This repository now includes a tiny Python bootstrap scaffold plus tests so you can track the setup work here while you gather the API keys.

## Other systems that can leverage this code

The setup commands below are also suitable for:

- **WSL2 (Windows Subsystem for Linux):** Use the Mac/Linux command block.
- **Cloud VPS (Vultr, AWS, DigitalOcean):** Run headless for long-term scraping/research tasks.
- **Raspberry Pi 5:** Suitable for Python backend + headless Selenium automation.
- **Apple Silicon (M1/M2/M3):** Runs natively in Terminal/Zsh with no command changes.

## Before you begin

- Python 3.11+
- pip
- Git
- **Google Chrome** on the laptop/host machine
- Chrome on your Android phone

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

## Laptop Chrome tabs

To run this comfortably from laptop browser tabs, you will also want:

- A laptop that can keep Chrome open during long sessions
- Enough free RAM/CPU to leave Chrome and Python running together
- Power connected or sleep disabled during long jobs
- The ability to open the local Streamlit URL in Chrome

## Android phone access

To use the same app from your Android phone, you will need:

- Chrome installed on Android
- The phone and laptop on the same Wi-Fi network **or** a secure tunnel / hosted deployment
- The laptop firewall configured to allow access to the app if you expose it on the network
- The app hosted on a machine that stays awake while you use it from the phone

If you are only running locally on your laptop, your Android phone usually cannot reach `localhost` directly. You will need either:

1. a local network IP plus the correct port exposure, or
2. a hosted VPS / cloud deployment, or
3. a secure tunneling solution.

## What else you'll need

Beyond the API key itself, these are the other things you will likely need to get this repo off the ground:

- The actual upstream application code referenced here (`k3-mariner`)
- A place to run it continuously (laptop, desktop, mini PC, or VPS)
- A password manager or secure secret storage for the API key
- A stable internet connection
- Optional: an always-on host if you want the phone to reach it anytime
- Optional: a domain or tunnel if you want remote access outside your home network

## Bootstrap helper

This repository now includes a small checklist helper you can run while you prepare the rest of the stack:

```bash
python3 -m project_mariner_scrape.setup_requirements
```

## Validation

### Important key safety note

**Do NOT:**

1. Share your API key with anyone (including AI tools).
2. Save it permanently in project files.

**Do this instead:**

- Paste the key into terminal only when needed.
- Store it in a password manager.

Your terminal will print a local URL (usually `http://localhost:8501`). Open it in Chrome, then paste your API key into the app settings and choose your preferred model.

You now have a free, open-source version of Gemini's agent (Project Mariner), and can run it locally for long tasks (including overnight automation).

Run the lightweight checks in this repository with:

```bash
python3 -m unittest discover
python3 scripts/check_readme.py
```

## Validation notes

This repository still does **not** vendor the upstream `k3-mariner` application, so it cannot directly execute the full runtime here yet. The scaffold added in this repo only validates documentation and setup readiness until you bring in the API keys and the upstream runtime.
