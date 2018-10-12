# league-coding-test
<h5>By: Kevin Vecmanis, P.Eng<h5>
<br>
This is the submission repository for League's take-home coding test.
<br>
<br>
<h3>Coding problem<h3>

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
