# Praying App 🕌

A desktop app for Windows that tracks your five daily prayers and keeps your progress saved automatically.

## Features

- ✅ Check off each of the 5 daily prayers (Fajr, Dhuhr, Asr, Maghrib, Isha)
- 📊 Daily progress ring and completion message
- 🔥 Day streak, total prayers, and perfect-days counters
- 📅 Last-7-days history heatmap
- 🌙 Hijri + Gregorian date display
- 💾 Progress is saved automatically on your device — close the app anytime, nothing is lost
- 🕛 Resets automatically at midnight for the new day

## Download (Windows .exe)

Go to the [Releases page](../../releases) and download either:

- **PrayingApp-Portable-1.0.0.exe** — just double-click and run, no install needed
- **PrayingApp-Setup-1.0.0.exe** — one-click installer with Start Menu shortcut

The `.exe` files are built automatically by GitHub Actions on every push (see the *Build Windows EXE* workflow).

## Run from source

```bash
npm install
npm start        # run the app
npm run dist     # build Windows .exe (on Windows)
```

Built with Electron. Prayer data is stored locally via `localStorage` in the app's user-data folder.
