# 🎧 Spotify Saved Tracks Exporter

This repository lets you export your **Spotify saved tracks** into a `saved_tracks.json` file by using GitHub Actions — no coding needed.

When you **fork this repository** and follow a few setup steps, you’ll be able to run a workflow that connects to your Spotify account and downloads your saved tracks into a structured JSON file.

---

> 📝 **Why this exists:**  
> Sometimes Spotify removes or loses saved tracks from user libraries.  
> By running this workflow regularly, you can create a history of your saved tracks over time.  
> If tracks go missing, you can detect the changes using Git and recover the track info from past JSON versions.

---

## ✨ What It Does

- Authenticates with your Spotify account using Spotipy (via stored GitHub secrets)
- Uses a GitHub Actions workflow to run a script that pulls your saved tracks
- Generates a file named `saved_tracks.json` in the root of your forked repository

---

## ⚙️ Setup Guide

### 📌 0. Fork This Repository

To get started, first **fork this repository** to your own GitHub account:

1. Click the **"Fork"** button in the top-right corner of this page.
2. This will create a copy of the repository under your account, where you can add secrets and run workflows.

> 🛠 All the following setup steps should be done in your **forked repository**, not this original one.

---

### 1. 🎵 Create a Spotify Developer App

1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications)
2. Create a new app and note:
   - **Client ID**
   - **Client Secret**
3. Set a **Redirect URI** (e.g., `http://localhost:8888/callback`)

---

### 2. 🔐 Add Repository Secrets

Go to your forked repo: **Settings → Secrets and variables → Actions**, and add the following secrets:

| Secret Name              | Description                            |
|--------------------------|----------------------------------------|
| `SPOTIPY_CLIENT_ID`      | Your Spotify Client ID                 |
| `SPOTIPY_CLIENT_SECRET`  | Your Spotify Client Secret             |
| `SPOTIPY_REDIRECT_URI`   | The same redirect URI from Step 1      |
| `SPOTIPY_SCOPE`          | e.g., `user-library-read`              |

---

### 3. 🛠️ Generate Your Refresh Token

1. Download the file **`get_refresh_token.exe`** from this repository.
2. Run the `get_refresh_token.exe` locally on your machine. It will ask for:
   - Your **Client ID**
   - Your **Client Secret**
   - Your **Redirect URI**
3. After authentication, a **refresh token** will be shown in your terminal.

✅ Copy the refresh token.

---

### 4. 🔐 Add the Refresh Token to Secrets

Add one more repository secret:

| Secret Name       | Description                      |
|-------------------|----------------------------------|
| `SPOTIPY_REFRESH_TOKEN`   | The refresh token from Step 3    |

---

## 🚀 Run the Workflow

1. In your forked repository, go to the **Actions** tab.
2. Select the **`update_save_tracks.yml`** workflow.
3. Click **“Run workflow”** in the top-right corner.

The workflow will:
- Authenticate using your Spotify credentials
- Clone the secondary script repository
- Fetch your saved tracks
- Generate `saved_tracks.json` in your repository

---

## 📄 Output

After the workflow completes, you’ll find:

- **`saved_tracks.json`** – contains all your saved Spotify tracks in JSON format in your fork repository.

You can re-run the workflow any time to keep your saved tracks up-to-date.

---
