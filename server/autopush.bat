@ECHO ON
TITLE AUTOPUSH
:loop
	
	
	cd "C:\VSCODE PROJECTS\nohryang0.1"
	
	::  git init
	
	
	
	git add -A
	git commit -m "auto push"
	git push

	cmd.exe

	echo Complete. Relaunching...
	
	TIMEOUT /t 300
	
::Restart from the top.	
goto loop