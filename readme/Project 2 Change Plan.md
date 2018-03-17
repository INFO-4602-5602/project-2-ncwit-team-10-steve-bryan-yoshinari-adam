# Project 2 Change Plan
## Vis1
- [ ] Up/Down arrow keys bound to menu selection
- [ ] Male/ Female instead of M/ F in legend (to be very politically correct we could even use Men/ Women
- [ ] State in the README how many institutions were included in the final set.

## Vis2
- [ ] Axis labels need to be rotated and translated. Rotation has been working but it  doesn’t seem to be about the tick connection so it shifts them to not be lined up with their institution. I have found how to rotate _or_ translate but not both since only one `transform` seems to be allowed at a time. I found [d3.js - Combining translate and rotate with D3 - Stack Overflow](https://stackoverflow.com/questions/20030473/combining-translate-and-rotate-with-d3) with some method for doing both but everything broke when I tried to do that. And alternative might be to move institution number to a tooltip/ mousover. 
- [ ] Legend added with the red color being percent that left the institution and yellow is the percent that switched majors. I suggest “Left Institution” and “Switched Major” as the labels.
- [ ] Move button to a more intuitive and obvious location. Perhaps centered over the top, below the bottom, or prominently (larger) on the left or right side. Add a color to it?
- [ ] First bar and the y-axis are not abutting but I feel that they should be.
- [ ] Y-axis labeled as “Percent of Student Body”
- [ ] X-axis labeled as “Institution Number”
- [ ] Describe sorting method in README
- [ ] We used [Stacked Bar Chart - bl.ocks.org](https://bl.ocks.org/mbostock/3886208) as inspiration.

## Vis3
- [ ] Y-axis values should be converted to integers 0-100 instead of decimal representation.
- [ ] I prototyped another version with Excel and Preview that Steve thinks ours should probably be like, but we might not have the time to do it. 
<!--- - [ ] Make the button more obvious, as discussed for Vis2 --->
<!--- - [ ] “ACT” should be “ACT Score” --->
- [ ] Legend

## Other
- [ ] Clean up the submission folder
- [ ] Make sure we expand on the “Why did you choose the representation?” in the README
- [ ] Expand on the “Design Process” in the README


#CU/INFO5602
