FOR %%a IN (*.bmp) DO Magick convert "%%~a" "%%~dpna.jpg"
PAUSE