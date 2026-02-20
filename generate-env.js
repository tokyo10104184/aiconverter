import fs from 'fs';
import dotenv from 'dotenv';
dotenv.config();

const envContent = `window.ENV = {
    OPENROUTER_API_KEY: ${JSON.stringify(process.env.OPENROUTER_API_KEY || '')}
};`;

fs.writeFileSync('env.js', envContent);
console.log('env.js generated successfully.');
