@ECHO ON
TITLE AUTOCRAW
:loop
	
	cd "C:\VSCODE PROJECTS\nohryang0.1\server"
	
	
	
	::Add all files in the directory
	python imagecr.py
	
	cmd.exe

	TIMEOUT 300
	
::Restart from the top.	
goto loop