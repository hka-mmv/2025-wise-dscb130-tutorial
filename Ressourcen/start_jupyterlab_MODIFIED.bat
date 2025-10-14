@echo off
chcp 65001
:: sub local path to user and location of miniconda3 folder
cd "C:\Users\USER\DSCB130_Info-1"
call C:\ProgramData\miniconda3\Scripts\activate.bat dscb130
call jupyter lab
