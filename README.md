# TextMimic Setup Guide

This project requires API keys and configuration for **Chutes.ai** and **Firebase** to function correctly. These keys are currently hardcoded in the HTML files and should be replaced with your own credentials.

## Required API Keys

### 1. Chutes.ai API Key (`SYSTEM_API_KEY`)

*   **Purpose:** Used for AI text generation via the Chutes.ai API.
*   **Variable Name:** `SYSTEM_API_KEY`
*   **Where to find:** [https://chutes.ai/](https://chutes.ai/) - Sign up and generate an API key.
*   **Files to Update:**
    *   `index.html`
    *   `creator.html`

### 2. Firebase Configuration (`firebaseConfig`)

*   **Purpose:** Used for backend services (database, hosting, etc.).
*   **Variable Name:** `firebaseConfig` object
*   **Where to find:** [https://console.firebase.google.com/](https://console.firebase.google.com/)
    *   Create a new project.
    *   Add a web app to your project.
    *   Copy the `firebaseConfig` object provided in the setup instructions.
*   **Required Fields:**
    *   `apiKey`
    *   `authDomain`
    *   `projectId`
    *   `storageBucket`
    *   `messagingSenderId`
    *   `appId`
    *   `measurementId`
*   **Files to Update:**
    *   `index.html`
    *   `creator.html`
    *   `admin.html`

## Setup Instructions

1.  Open each of the files listed above.
2.  Locate the `SYSTEM_API_KEY` variable and replace the existing string with your Chutes.ai API key.
3.  Locate the `firebaseConfig` object and replace the values with your Firebase project configuration.
