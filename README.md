# TextMimic Setup Guide

This project requires API keys and configuration for **OpenRouter** and **Firebase** to function correctly.

## Required API Keys

### 1. OpenRouter API Key (`OPENROUTER_API_KEY`)

*   **Purpose:** Used for AI text generation via the OpenRouter API.
*   **Variable Name:** `OPENROUTER_API_KEY`
*   **Where to find:** [https://openrouter.ai/](https://openrouter.ai/) - Sign up and generate an API key.

### 2. Firebase Configuration (`firebaseConfig`)

*   **Purpose:** Used for backend services (database, hosting, etc.).
*   **Variable Name:** `firebaseConfig` object
*   **Where to find:** [https://console.firebase.google.com/](https://console.firebase.google.com/)
    *   Create a new project.
    *   Add a web app to your project.
    *   Copy the `firebaseConfig` object provided in the setup instructions.

## Setup Instructions

1.  Open the file `config.js` in the root directory.
2.  Locate the `OPENROUTER_API_KEY` variable and replace the empty string with your OpenRouter API key.
3.  Locate the `firebaseConfig` object and replace the values with your Firebase project configuration.
