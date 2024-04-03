# Python_Challenge
Homework for Module 3.
## Resources
### Albert Lee assisted me in the following code that I did apply into my assignment:
  My code is below. Lots of comments below so I could follow the logic. The average change calculation was the toughest for me. The variable total_months is set to 0. The IF conditional is nested inside the FOR loop. The average change calc has to be outside the IF conditional.<br>
'initiate IF on second run<br>
    if total_months > 1:<br>
      # calculate change from month to month<br>
      # previous month variable has not been overwritten<br>
      change = current_month_profit_loss - previous_month_profit_loss<br>
      # add change calc from above to changes list<br>
      changes.append(change)<br>
      # sum all changes and stores in total change<br>
      total_change += change<br>
      # first run will skip IF and will store Cell B2 to previous month<br>
      # second run will overwrite and store Cell B3 to previous month<br>
      previous_month_profit_loss = current_month_profit_loss<br>
'calc avg change, len(changes) will provide a count of all values stored in changes list<br>
average_change = total_change / len(changes)<br>

Co-Pilot: used to learn how to line break in readme.md to read the above code appropriately.
Youtube: I watched various YouTube videos on loops and calculations but no code was used in my assignment.

Self-Assessment: Albert Lees assistance allowed me to determine what I was doing wrong.  I didn't understand the concept of loops fully and pushing values to new values and holding new values.  Once I reviewed the code and made my assignment work, I was able to determine how to finish the assignment with writing the code to put the date for the greatest and lowest months, and calculate the total.  I think I made some progress on looking at code differently.


