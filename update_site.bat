@echo off
echo [Step 1] Cleaning old posts...
if exist _posts (
    del /q _posts\*
) else (
    mkdir _posts
)

echo [Step 2] Calibrating data and Generating pages...
:: 執行你的兩個 Python 腳本
python fill_excel.py
python generator.py

echo [Step 3] Syncing to GitHub...
git add .
git commit -m "Site auto-update: %date% %time%"
git push origin main

echo Done! Please refresh your website in 3 minutes.
pause