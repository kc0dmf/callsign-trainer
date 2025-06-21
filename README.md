# Callsign Trainer

Ham radio callsign trainer.

## How To Install
`$ pip3 install simpleaudio`  
TODO: How to install python environment?  

## How To Run:
### Command Line:
`$ (activate the python environment; this might have been erased)`  
`$ cd ./src/main/python`  
`$ python3 callsign.py`  

### IntelliJ
`$ (activate the environment)`  
`Open the IntelliJ terminal`  
`(if you don't see "(.venv)" on the prompt ... $ cd ./.venv/bin && ./activate`  
` pip3 install <my-package>` (like simpleaudio)

To create a python environment:  
`$ python -m venv [directory]`  
--> NOTE: I think the env is in the project's directory: callsign_training/env

To activate the python environment:  
`$ source [directory]/bin/activate`  

To deactivate the python environment:  
`$ deactivate`

To remove the python environment:  
`$ deactivate`  
`$ rm [directory]`  


# Creating Audios
Master of all sounds at:  
/Users/craiglarsen/Documents/hobby/ham radio/speech/2023 recordings/full-fast.aup3

Storing individual files in:  
/Users/craiglarsen/Documents/hobby/dev/ham-radio/callsign-trainer/src/main/resource/fast

After each audio is created:
Effect -> Volume and Compression -> Normalize (Peak Amplitude to -5.0 or -4.0)  
or  
Effect -> Volume and Compression -> Amplify (New Peak Value = -5.0 or -4.0 db)

If audio sounds like it ends awkwardly, try adding a fade to the end:
Effect -> Fading -> Fade out
