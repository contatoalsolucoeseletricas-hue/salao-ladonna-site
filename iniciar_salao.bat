@echo off
title La Donna Studio - Hair & Nails (Servidor Local 8085)
cd /d C:\SALAO_LA_DONNA
echo =======================================================
echo    INICIANDO LA DONNA STUDIO - HAIR & NAILS
echo =======================================================
echo.
start http://localhost:8085/index.html
python server_salao.py
pause
