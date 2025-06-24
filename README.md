# Callsign Trainer

Ham radio callsign trainer.

# Table of Contents
> [!TODO]  
> TODO: Need to do.  
> TODO: Need to test links.  

<a id="return-to-top"></a>
- [Current Status](#current-status)
- [Introduction](#introduction)
- [How To Install](#how-to-install)
- [How To Run](#how-to-run)
- [Addendum](#addendum)


<a id="current-status"></a>
# Current Status
[Return to top](#return-to-top)  
* In the current version (0.8.x), this application will play all Fast letters (Fast 
  Mode) and **will crash** if you attempt to play this in Slow Mode. To make
  slow mode work:
  * Find "UNCOMMENT ME:" in the code talking about the Slow audio files.
  * Uncomment the dictionary below this comment to restrict to audio files that can be
  used for slow letters. Note: you can still play the fast letters.
  * See Issue #11.
* You can change the code to stick to only one format of callsign (1x3, 2x3, etc.).
  * Find "UNCOMMENT ME:" in the code discussing callsign formats.
  * Uncomment the variables that will force the callsign to be of a particular format.
  * See Issue #9.


<a id="introduction"></a>
# Introduction
[Return to top](#return-to-top)  
Ths _Callsign Trainer_ is an application that speaks random Amateur Radio callsigns
for you to guess. The purpose of this is to give you practice at hearing callsigns.
Ideally, it helps you to pick up the callsign correctly on the first try.

Guessing the callsign correctly gives you a "correct" message. Otherwise, the same 
callsign is repeated back to you until you guess it correctly. Then a new callsign
is generated. 

When you finish, you will be given some statistics to show how well you did.


## Why Did I Build This
Hint: it wasn't just because I wanted to.

There's a couple of events that came together that caused me to build this application.

First, I was in a creative engineering class (from Mark Rober). One of the challenges
was to build something that would help you develop a good habit or break a
bad habit. And, we only had about 7 days to build it!

Second, it was because of passion.
Two of my passions are ham radio and software development. As a ham radio guy involved in
contesting, I wanted something to help me build the habit of hearing a callsign correctly
on the first try. If I can do this, it will give me an edge in the ham radio contests that
I participate in.

So for my project, I decided to write a program that would generate random callsigns for
me to guess. And so, the Callsign Trainer was born.


## One Of The Things That Makes This So Special
I use tone or inflection in each letter that is spoken to make the callsign sound 
more realistic.

While I was writing the program, I quickly learned that a robotic speech would not be 
good enough. So I added inflection to each letter and digit in a way a person would
naturally do it. As you give a callsign on the air, you raise or lower
the tone in your voice slightly to convey the callsign to someone. You can hear this if
you say the following callsign out loud:  
`^al^pha^ -ze-ro- -yank-ee- -zu_lu_`  
In the above, I used ^ to mean a higher tone, a - to mean a middle tone, and _ to mean a
lower tone.

This application uses 3 recordings of each letter (one for a high tone, one for a 
mid tone, and one for a low). Each digit uses just 1 recording (for a mid tone).

Note: This feature was included in the original program!


<a id="how-to-install"></a>
# How To Install
[Return to top](#return-to-top)  
You will need to download this application and put it in some directory.
Then, install Python and a Python environment that you will use to run the program.

> [!TODO]  
> TODO: How to install python environment?
> TODO: Specify requirements (minimal requirements, only Python and SimpleAudio)

`$ pip3 install simpleaudio`

Personal notes: I got this to work running on:  
* IntelliJ on a Macbook Pro
* a Raspberry Pi

It's untested in Windows but this program should work in any Python environment.


<a id="how-to-run"></a>
# How To Run:
[Return to top](#return-to-top)  
> [!TODO]  
> TODO: Need to verify the following instructions are correct.


## Command Line:
`$ (do something to activate the python environment)`  
`$ cd ./src/main/python`  
`$ python3 callsign.py`  


## IntelliJ
`$ (activate the environment)`  
`Open the IntelliJ terminal`  
`If you don't see "(.venv)" on the prompt, do:`  
`$ cd ./.venv/bin && ./activate`  
`$ pip3 install <my-package>` (like simpleaudio)

To create a python environment:  
`$ python -m venv [directory]`  
--> NOTE: I think the env is in the project's directory: callsign-trainer/env 
or callsign-trainer/.env or callsign-trainer/.venv

To activate the python environment:  
`$ source [directory]/.venv/bin/activate`  

To deactivate the python environment:  
`$ deactivate`

To remove the python environment (almost never need to do this):  
`$ deactivate`  
`$ rm [directory]`  


<a id="addendum"></a>
# Addendum
[Return to top](#return-to-top)  


## The Confession

I'm a software developer by trade. I'm good at what I do. However, for the Creative
Engineering class I was taking I decided
to use a language I wasn't very familiar with: Python. And, I only had 7 days to get this
working! I want you to know that I feel absolutely terrible with the myriads of poor
decisions I chose for this application. There are some pretty crappy areas in this program
(including naming things, using non-standard Python conventions, etc.). You should NOT
use this program as a template of good Python programming practice.

That being said, I got it to work. And that's all that mattered. : )


# Personal Notes
## Creating Audios
Master of all sounds at:  
~/Documents/hobby/ham radio/speech/2023 recordings/full-fast.aup3

Storing individual files in:  
~/Documents/hobby/dev/ham-radio/callsign-trainer/src/main/resource/fast

After each audio is created:
Effect -> Volume and Compression -> Normalize (Peak Amplitude to -5.0 or -4.0)  
or  
Effect -> Volume and Compression -> Amplify (New Peak Value = -5.0 or -4.0 db)

If audio sounds like it ends awkwardly, try adding a fade to the end:
Effect -> Fading -> Fade out
