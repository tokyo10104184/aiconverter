# TextMimic セットアップガイド

このプロジェクトを正しく動作させるためには、**OpenRouter** と **Firebase** のAPIキーおよび設定が必要です。これらのキーは現在HTMLファイル内にハードコードする形式となっており、ご自身の認証情報に置き換える必要があります。

## 必要なAPIキー

### 1. OpenRouter API Key (`OPENROUTER_API_KEY`)

*   **用途:** OpenRouter API経由でのAIテキスト生成に使用します。
*   **変数名:** `OPENROUTER_API_KEY`
*   **入手先:** [https://openrouter.ai/](https://openrouter.ai/) - サインアップしてAPIキーを生成してください。
*   **更新するファイル:**
    *   `index.html`
    *   `creator.html`

### 2. Firebase Configuration (`firebaseConfig`)

*   **用途:** バックエンドサービス（データベース、ホスティングなど）に使用します。
*   **変数名:** `firebaseConfig` オブジェクト
*   **入手先:** [https://console.firebase.google.com/](https://console.firebase.google.com/)
    *   新しいプロジェクトを作成します。
    *   プロジェクトにウェブアプリを追加します。
    *   セットアップ手順で提供される `firebaseConfig` オブジェクトをコピーします。
*   **必要なフィールド:**
    *   `apiKey`
    *   `authDomain`
    *   `projectId`
    *   `storageBucket`
    *   `messagingSenderId`
    *   `appId`
    *   `measurementId`
*   **更新するファイル:**
    *   `index.html`
    *   `creator.html`
    *   `admin.html`

## 設定手順

1.  上記の各ファイルを開きます。
2.  `OPENROUTER_API_KEY` 変数を見つけ、空の文字列をご自身のOpenRouter APIキーに置き換えてください。
3.  `firebaseConfig` オブジェクトを見つけ、値をFirebaseプロジェクトの設定内容に置き換えてください。
