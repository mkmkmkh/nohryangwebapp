@ECHO OFF
TITLE AUTOPUSH

	
	
cd C:\pythonvscode\nohryang0.1\server
	
::  git init
	
	
	
git add -A
git commit -m "auto push"
git push

cmd.exe

echo Complete. Relaunching...
