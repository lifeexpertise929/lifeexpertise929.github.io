@echo off
echo 🚀 啟動自動化更新流程...

:: 1. 清除舊的網頁檔案
echo 🧹 正在清理舊的 _posts 資料夾...
if exist _posts (
    del /q _posts\*
) else (
    mkdir _posts
)

:: 2. 執行 Python 腳本補全數據並產生網頁
echo ⚙️ 正在產生最新網頁內容...
python fill_excel.py
python generator.py

:: 3. 推送到 GitHub (如果你有使用 Git)
echo 📤 正在同步至 GitHub...
git add .
git commit -m "Auto-update site content %date% %time%"
git push origin main

echo ✨ 所有更新已完成！請重新整理您的網頁。
pause