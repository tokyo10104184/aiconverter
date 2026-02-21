// ▼▼▼ Config ▼▼▼
// 環境変数からAPIキーを取得 (ローカル/Vercel環境)
export const OPENROUTER_API_KEY = (window.ENV && window.ENV.OPENROUTER_API_KEY) || '';

export const firebaseConfig = {
    apiKey: "AIzaSyCgSNCKuPIdi-7P7hJDv3NcCKp_cjPRlB4",
    authDomain: "aihenkan-7f101.firebaseapp.com",
    projectId: "aihenkan-7f101",
    storageBucket: "aihenkan-7f101.firebasestorage.app",
    messagingSenderId: "695320170916",
    appId: "1:695320170916:web:a1317704b02970b1c07131",
    measurementId: "G-G4DW26MH4L"
};

export const CATEGORIES = [
    { id: 'business', label: 'ビジネス' },
    { id: 'entertainment', label: 'エンタメ・ネタ' },
    { id: 'life', label: '生活・便利' },
    { id: 'study', label: '学習・知識' },
    { id: 'creative', label: '創作・なりきり' },
    { id: 'other', label: 'その他' }
];
// ▲▲▲
