# README for Steve Bryan Yoshinari Bryan
## Visualization 1
Demographics of female tech-related major students changed over time. || vis1.html in the root folder

Racial demographic change over a five year period. We chose institutions that had complete data over the years displayed. The interaction allows selection between races to reduce visual clutter, or a "spaghetti" plot. The y-axis is not fixed because the trend is more important than the specific number values.

Prototypes of this visualization originally included more races but some numbers were too small too meaningfully visualize (very small integers) so the smallest groups were removed. The visualization had the remaining races graphed at the same time but some groups were large enough to cause the smaller groups to disappear into being nearly straight lines without interesting features that were present.

The motivation for this vis was to see how enrollment over time was changing within a race category but by separating races to see if there were effects on once gender but not the other. We dealt with holes in the data by looking for a time period that was long enough to see meaningful trends, but short enough to make sure we still had several institutions’ data to find widespread effects. 

## Visualization 2
Which institution is doing well on retaining female tech-related students? || vis2.html in the root folder

We picked the year 2015 and then summed all values within the institution regarding students staying in their major, switching majors, or leaving the institution. The interaction quickly compares genders to see if there is a gender-based difference in retention and allows for ensemble statistics of negative retention measures to be perceived by the viewer. After initial extraction, data was sorted within Excel to order the institutions from highest rate of women leaving the institution to the lowest. Without giving explicit statistics, it is clear to see that the two negative measures of retention are higher for women over all the institutions, although within-institution values varied widely.

The original idea for this vis had the two sets of information plotted in order, like in a science journal. A later version had one of the bottom of the two plots flipped vertically to move the negative retention measures for each gender next to each other, diverging up and down from a common midline running left and right. This may still be the most affective static display, but we chose to make this the feature of our interaction to aid the ensemble statistics process. 

## Visualization 3
Is admission ratio biased by gender revealed through GPA/ACT score? || vis3.html in the root folder

It seems clear that the admission process is a potential source of bias in the majors within the data from NCWIT. To highlight potential biases, we created a modified scatter plot to highlight how standardized test scores (ACT) or high school GPA could show a disparity between the men and women being admitted to college. We suspected that we might find a trend between disparities related to the percentage of enrolled students that were women. 

At first glance it may seem difficult to pull much information from the visualization, especially because this is a unique implementation of a scatter plot. One thing that we can see right away is that some institutions have imperceptibly small differences in one of these measures or the other, while some institutions have startlingly large differences between the average scores of the incoming women compared to men. Through some more observation (especially with a secondary prototype, discussed later), we can see that women are being admitted with higher GPAs than men in most cases (in all but 11 of the 52 pairs). We recognize that the pool of applicants may add nuance to interpreting the visualization.

ACT scores show perhaps an even more interesting features (also aided by the secondary prototype). Most ACT score spreads (between men and women) seem much closer than the high school GPAs showed, however, some of the institutions showed wider spreads than seen at all for GPA. There is a trend showing that institutions with higher ACT scores of admitted students are ranked higher for women admission rates but their spread of ACT scores do not seem notably different. Also, women nearly always had higher GPAs (noted above) but men usually had higher ACT scores of the admitted students. 

After creating the vis that we submitted, we continued to prototype other ideas, which have been submitted as PDFs created with Excel and Preview. In the re-interpretation of the graphics described above, the institutions were ranked by percent of women enrollment (i.e. rank instead of actual percentage as y-value, to allow separation of institutions). The new graphics also had lines added that were color coded to match the “leading” or “highest scoring” gender for that institution to all for quick visual summary of bar lengths and colors (genders).

# Design Process
* Initial sketching by a pen and a sheet of paper.
* Prototype visualization by Tableau and finding out the problem of the imbalance between races (i.e., more Asian female students than White female students)
* Do we have the clean data for our visualization purpose
* Different restrictions by years (to see if we have enough data to plot)
* Whether the visualization is clean enough to interpret or not.
* Validity of the resulting visualization or not (confusing or not).
* After making the initial versions of 3 visualizations are made, we came up with checklists to make the visualizations easy to understand (e.g., adding legends, improved prototypes suggested by Bryan). 

# Team Roles
All team members contributed to what visualization we want.
* Adam: Data cleanup and extraction, vis iteration, vis coding
* Steve: vis coding, prototyping, vis iteration, suggesting refinements
* Bryan: Prototyping, vis iteration, documentation, cosmetic coding, suggesting refinements
* Yoshinari: Prototyping, vis coding, initial documentation

# How to Run
Assuming you are running a local python server (i.e., `python -m http.server` for Python 3),
1. Run your local server in this directory
1. Open your browser
1. Visualization 1 is at `http://localhost:8000/vis1.html`
1. Visualization 2 is at `http://localhost:8000/vis2.html`
1. Visualization 3 is at `http://localhost:8000/vis3.html`


# References
* [Changing the size of a button](https://www.w3schools.com/bootstrap/bootstrap_buttons.asp)

#CU/INFO5602
