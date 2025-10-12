@echo off
chcp 65001
:: activate environment and launch Jupyter Lab
cd "C:\Users\linca\DSCB130_Info-1"
call C:\ProgramData\miniconda3\Scripts\activate.bat dscb130
call jupyter lab
