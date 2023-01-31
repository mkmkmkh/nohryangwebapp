:loop
	
	:: Navigate to the directory you wish to push to GitHub
	::Change <path> as needed. Eg. C:\Users\rich\Desktop\Writings
	cd C:\VSCODE PROJECTS\nohryang0.1\server
	
	::Initialize GitHub
	::  git init
	
	
	::Add all files in the directory
	imagecr.py
	
	::Commit all changes with the message "auto push". 
	::Change as needed.
	
	
	::Wait 300 seconds until going to the start of the loop.
	::Change as needed.
	TIMEOUT 300
	
::Restart from the top.	
goto loop