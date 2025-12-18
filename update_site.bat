@echo off
echo 🤖 [1/3] 正在自動補完 Excel 資料...
python fill_excel.py
if %errorlevel% neq 0 pause

echo.
echo 📝 [2/3] 正在產生網頁檔案...
python generator.py
if %errorlevel% neq 0 pause

echo.
echo ☁️ [3/3] 正在同步到 GitHub...
git add .
git commit -m "Site updated: %date% %time%"
git push

echo.
echo ✅ 全部大功告成！請等待 1-2 分鐘後查看網頁。
pause