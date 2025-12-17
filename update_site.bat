@echo off
echo 🤖 正在啟動 AI 生成文章與固定頁面...
python generator.py

echo.
echo ☁️ 正在同步到 GitHub 伺服器...
git add .
git commit -m "AI 自動更新: %date% %time%"
git push

echo.
echo ✅ 全部大功告成！請等待 1-2 分鐘後查看網頁。
pause