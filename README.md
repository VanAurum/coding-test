<h2>Coding Test</h2>
<h3>By: Kevin Vecmanis, P.Eng</h3>
<h3>Author Preface & Comments:</h3>
For this soluton I opted to use a string format for the time range inputs. For example, an acceptable input for either A or B will be in the form:
<br>

```
['8:00-10:00'] or
['8:00-10:00', '11:15-12:00', '14:25-15:00']
```

The solution can also handle whitespace and other undesirable user input formats like: 
<br>

```
[' 9:00am - 10:00am '] will be converted to ['9:00-10:00']
```

<br>
All inputs are assumed to be in 24 hour time.  I programmed a simple command line interface tool for running the program and editing the time range lists.  Jump to <b>Getting Started</b> for information on how to download and run the CLI.

<h3>Coding problem</h3>

Write a program that will subtract one list of time ranges from another. Formally: for two lists of time ranges A and B, a time is in (A-B) if and only if it is part of A and not part of B.
<br>
<br>
A time range has a start time and an end time. You can define times and time ranges however you want (Unix timestamps, date/time objects in your preferred language, the actual string “start-end”, etc).
<br>
<br>
Your solution shouldn’t rely on the granularity of the timestamps (so don’t, for example, iterate over all the times in all the ranges and check to see if that time is “in”).
<br>
<br>
Examples:<br>
```
(9:00-10:00) “minus” (9:00-9:30) = (9:30-10:00)
(9:00-10:00) “minus” (9:00-10:00) = ()
(9:00-9:30) “minus” (9:30-15:00) = (9:00-9:30)
(9:00-9:30, 10:00-10:30) “minus” (9:15-10:15) = (9:00-9:15, 10:15-10:30)
(9:00-11:00, 13:00-15:00) “minus” (9:00-9:15, 10:00-10:15, 12:30-16:00) = (9:15-10:00, 10:15-11:00)
```
<h3>Getting Started</h3>
To run the CLI, you will need to clone the repository.  First, create a directory anywhere on your computer and navigate to it using the command line. 

<h4>Prerequisites</h4>
To run the CLI, you will need Python 3.7 installed.  It's possible earlier versions will work but they haven't been tested. There is only one third party package required, <b>Click</b>, used for running the CLI. 

```
Step 1. cd <mydir>
Step 2. git clone https://github.com/VanAurum/coding-test.git
Step 3. pip install click (to install only 3rd party package dependency)
```
Alternatively, if you have pipenv installed on your machine you can run:
```
pipenv install --dev
```
This will install all dependencies within the project. To install pipenv on MacOS:
```
brew install pipenv
```
<h3>Using the CLI</h3>
To run the CLI, navigate to the solution folder within your terminal and run

```
python cli.py
```

You should see the default CLI menu that looks like this

```
------------------------------
   M A I N - M E N U✨
  By: Kevin Vecmanis
------------------------------
Hello League. This is my submission 
for the coding test. Enjoy!

Default choices for lists A and B are shown below:

List A:
9:00-10:00
10:25-15:25

List B:
9:15-9:45
10:15-14:00

------------------------------
Enter the list you would like to 
change, or enter "run" to use default lists (A, B, run, quit):
```

If you encounter errors regarding packages or click, install pipenv and run the following within the root directory of the project

```
$ pipenv shell
$ cd solution
$ python cli.py
```


There are four commands: A, B, run and quit. 

```
'A' to change time ranges for list A
'B' to change time ranges for list B
'run' to subtract B from A 
'quit' to exit the CLI
```

List input to the CLI is robust, but not perfectly robust. To enter new lists in CLI, you can enter the following time range variations:

```
9:00-10:00 (without leading 0)
09:00am-10:00am (with leading 0)
9:00 - 10:00 (whitespace)
9:00-10:00,22:00-22:05 (multiple entries)
00:01-00:04, 00:08-00:10 
```

If the time range does not include a dash "-", or colons are missing, you will be asked to re-enter input.  