# league-coding-test
<h3>By: Kevin Vecmanis, P.Eng</h3>
<br>
This is the submission repository for League's take-home coding test.
<br>
<h3>Author comments:</h3>
For this soluton I opted to use a string format for the time range inputs. For example, an acceptable input for either A or B will be in the form:
<br>
<br>
['8:00-10:00'] or<br>
['8:00-10:00', '11:15-12:00', '14:25-15:00',]
<br>
<br>
The solution can also handle whitespace and other undesirable user input formats like: 
<br>
<br>
[' 9:00am - 10:00am '] will be converted to ['9:00-10:00']
<br>
<br>
All inputs are assumed to be in 24 hour time.

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
(9:00-10:00) “minus” (9:00-9:30) = (9:30-10:00)<br>
(9:00-10:00) “minus” (9:00-10:00) = ()<br>
(9:00-9:30) “minus” (9:30-15:00) = (9:00-9:30)<br>
(9:00-9:30, 10:00-10:30) “minus” (9:15-10:15) = (9:00-9:15, 10:15-10:30)<br>
(9:00-11:00, 13:00-15:00) “minus” (9:00-9:15, 10:00-10:15, 12:30-16:00) = (9:15-10:00, 10:15-11:00)

<br>
<h3>Command Line Interface</h3>
I programmed a simple command line interface for League code reviewers so they can try varations of time ranges.  

