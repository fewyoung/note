@echo off
set /p choice=1:veny^

2:pytyon^


if %choice%==1 goto 1
if %choice%==2 goto 2
:1
start cmd /k "cd C:\inetpub\wwwroot\venv\Scripts&&activate&&cd C:\Users\Administrator\Desktop\python\note"
exit
:2
start cmd /k "cd C:\Users\Administrator\Desktop\python\note"
exit