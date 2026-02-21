import fs from 'fs';
import path from 'path';
import dotenv from 'dotenv';
dotenv.config();

const OUTPUT_DIR = 'public';

// 1. Create output directory
if (!fs.existsSync(OUTPUT_DIR)){
    fs.mkdirSync(OUTPUT_DIR);
}

// 2. Generate env.js in output directory
const envContent = `window.ENV = {
    OPENROUTER_API_KEY: ${JSON.stringify(process.env.OPENROUTER_API_KEY || '')}
};`;
fs.writeFileSync(path.join(OUTPUT_DIR, 'env.js'), envContent);
console.log('env.js generated successfully in public/');

// 3. Copy files to output directory
// Only copy the essential source files.
const filesToCopy = [
    'index.html',
    'creator.html',
    'admin.html',
    'config.js',
    'firestore.rules'
];

filesToCopy.forEach(file => {
    if (fs.existsSync(file)) {
        const dest = path.join(OUTPUT_DIR, file);
        fs.copyFileSync(file, dest);
        console.log(`Copied ${file} to public/`);
    } else {
        console.warn(`Warning: ${file} not found, skipping copy.`);
    }
});

console.log('Build completed successfully.');
