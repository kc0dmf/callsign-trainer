# Callsign Trainer

Ths _Callsign Trainer_ is an application that speaks random Amateur Radio callsigns
for you to guess. The purpose of this is to give you practice at hearing callsigns.
Ideally, it helps you to pick up the callsign correctly on the first try.

Guessing the callsign correctly gives you a "correct" message. Otherwise, the same 
callsign is repeated back to you until you guess it correctly. Then a new callsign
is generated. 

When you finish, you will be given some statistics to show how well you did.

For now, the _Callsign Trainer_ only does US and Canadian call signs.

<a id="return-to-top"></a>
# Table of Contents

- [Current Status](#current-status)
- [How To Install](#how-to-install)
- [How To Run](#how-to-run)
- [Introduction](#introduction)
  - [Why Did I Build This](#why-did-i-build-this)
  - [Inflection Makes This Special](#inflection-makes-this-special)
- [License](#license)
- [Addendum](#addendum)
  - [Note on Contributing](#note)
  - [The Confession](#the-confession)
  - [How To Customize The Audios](#how-to-customize-the-audios)
  - [History of Changes](#history-of-changes)


<a id="current-status"></a>
# Current Status
[Return to top](#return-to-top)

* In the current version (0.9.x), this application will play all Fast letters (Fast Mode) and Slow Letters (Slow Mode).
  This fixes Issue #11.
* You can change the code to stick to only one format of callsign (1x3, 2x3, etc.).
  * Find "UNCOMMENT ME:" in the code discussing callsign formats.
  * Uncomment the variables that will force the callsign to be of a particular format.
  * See Issue #9.


<a id="how-to-install"></a>
# How To Install
[Return to top](#return-to-top)

## Requirements

* Python 3.x
* simpleaudio

## Installation Steps

### 1. Download the Project
Clone or download this repository to your local machine.

### 2. Create a Python Virtual Environment

Navigate to the project directory and create a virtual environment:

```bash
python3 -m venv .venv
```

### 3. Activate the Virtual Environment

**On Mac/Linux:**
```bash
source .venv/bin/activate
```

**On Windows (Command Prompt):**
```bash
.venv\Scripts\activate
```

**On Windows (PowerShell):**
```bash
.venv\Scripts\Activate.ps1
```

You should see `(.venv)` appear at the beginning of your terminal prompt when the environment is activated.

### 4. Install Dependencies

With the virtual environment activated, install the required package:

```bash
pip3 install simpleaudio
```

### 5. Deactivate the Virtual Environment (when done)

```bash
deactivate
```

## Tested Platforms

This application has been tested and works on:
* macOS (Macbook Pro with IntelliJ)
* Raspberry Pi

It should work in any Python 3 environment, including Windows, though it hasn't been fully tested on Windows yet.


<a id="how-to-run"></a>
# How To Run
[Return to top](#return-to-top)

### 1. Activate the Virtual Environment

Make sure you're in the project directory, then activate the virtual environment:

**On Mac/Linux:**
```bash
source .venv/bin/activate
```

**On Windows (Command Prompt):**
```bash
.venv\Scripts\activate
```

**On Windows (PowerShell):**
```bash
.venv\Scripts\Activate.ps1
```

Look for `(.venv)` at the beginning of your terminal prompt to confirm it's activated.

### 2. Navigate to the Source Directory

```bash
cd src/main/python
```

### 3. Run the Application

```bash
python3 callsign.py
```

### Using IntelliJ IDE

1. Open the project in IntelliJ
2. Open the IntelliJ terminal (View → Tool Windows → Terminal)
3. If you don't see `(.venv)` in the prompt, activate the environment:
   ```bash
   source .venv/bin/activate
   ```
4. Navigate to the source directory:
   ```bash
   cd src/main/python
   ```
5. Run the application:
   ```bash
   python3 callsign.py
   ```

Alternatively, you can right-click on `callsign.py` in IntelliJ and select "Run".


<a id="introduction"></a>
# Introduction
[Return to top](#return-to-top)

<a id="why-did-i-build-this"></a>
## Why Did I Build This
[Return to top](#return-to-top)

Hint: it wasn't only just for fun. :-)

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


<a id="inflection-makes-this-special"></a>
## Inflection Makes This Special
[Return to top](#return-to-top)

I use tone or inflection in each letter that is spoken to make the callsign sound 
more realistic. I didn't want some robotic-sounding application.

While I was writing the program, I quickly learned that a robotic speech would not be 
good enough. So I added inflection to each letter and digit in a way a person would
naturally do it. As you give a callsign on the air, you raise or lower
the tone in your voice slightly to convey the callsign to someone. You can hear this if
you say the following callsign out loud:  
`^al^pha^ -ze-ro- -yank-ee- -zu-lu_`  
In the above, I used ^ to mean a higher tone, a - to mean a middle tone, and _ to mean a
lower tone.

This application uses 3 recordings of each letter (one for a high tone, one for a 
mid tone, and one for a low). Each digit uses just 1 recording (for a mid tone).

This feature was included in the original program!


<a id="license"></a>
# License
[Return to top](#return-to-top)

This project is licensed under the MIT License—see the [LICENSE](LICENSE) file for details.

**Note on Audio Files:** The Python source code is licensed under the MIT License. The voice recordings (audio files) are © kc0dmf and are included for use with this software.


<a id="addendum"></a>
# Addendum
[Return to top](#return-to-top)

<a id="note"></a>
## Note on Contributing
[Return to top](#return-to-top)

This is my first public repository. I may not check for comments or issues regularly, 
but I appreciate any feedback or contributions!

<a id="the-confession"></a>
## The Confession
[Return to top](#return-to-top)

I'm a software developer by trade. I'm good at what I do. However, for the Creative
Engineering class I was taking I decided
to use a language I wasn't very familiar with: Python. And, I only had 7 days to get this
working! I want you to know that I feel absolutely terrible with the myriads of poor
decisions I chose for this application. There are some pretty crappy areas in this program
(including naming things, using non-standard Python conventions, etc.). You should NOT
use this program as a template of good Python programming practice.

That being said, I got it to work. And that's all that mattered. : )


<a id="how-to-customize-the-audios"></a>
## How To Customize The Audios
[Return to top](#return-to-top)

This could be customized to use your own voice by replacing each audio file with your
own voice. Be warned though: this is a fair bit of work! You need a good quiet area
and a good microphone.
What I ended up doing is making one audio recording for the fast letters and one
for the slow letter. In each audio recording I would first do digits, then the letters:  
"These are the fast digits ...  
alpha zero alpha ... alpha zero alpha  
alpha one alpha ... alpha one alpha  
...  
These are the fast letters ...  
alpha two alpha alpha ... alpha two alpha alpha  
bravo two bravo bravo ...  
..."  
(Note: I began using Two instead of One for the letters because I was accidentally
blending the letter to the www sound in the word One.)
After this, I used audio software like Audacity to break up each letter into its
own file.

It took about 10 hours to do the whole thing (maybe longer).


### Personal Notes - Creating Audios
[Return to top](#return-to-top)

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


<a id="history-of-changes"></a>
## History of Changes
[Return to top](#return-to-top)

* In version (0.9.x), this application will play all Fast letters (Fast Mode) and Slow Letters (Slow Mode).
  This fixes Issue #11.
* In version (0.8.x), this application will play all Fast letters (Fast
  Mode) and **will crash** if you attempt to play this in Slow Mode. To make
  slow mode work:
  * Find "UNCOMMENT ME:" in the code talking about the Slow audio files.
  * Uncomment the dictionary below this comment to restrict to audio files that can be
    used for slow letters. Note: you can still play the fast letters.
  * See Issue #11.
