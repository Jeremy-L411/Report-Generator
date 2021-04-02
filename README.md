# Report-Generator

This was a personal project I worked on to generate monthly 
and yearly reports for a job I worked at. I started off just wanting to do 
my own expenses and later decided to expand it to multiple people with multiple 
months and years. 

There are two ways to generate fake data in the specific format for this program. 
One is make_fakefiles.py, this will generate a random number of people, months and years. 
It works well, however, you may only have one employee with one expense
and another employee with 20. 

structured_random_files.py is as it states, structured. You can specify how many employees, 
how many expenses in a month and how many bonuses. 

The format for organizing the employees is Name > Year > Month for each name 
in the sort folder.

After using one of the report generators monthly_report.py and year_report.py can be ran 
to perform a monthly report for each month for each employee or a yearly report for each employee.

It is configured so that there is a main sorting folder where you put all the randomly generated 
expense and bonus forms, then in moveFiles.py select the folder where they are located,
a temporary folder that will generate its own folders and delete once it has accomplished sorting
and then a destination folder for the sorted reports. If a name, year, or month has already been 
created it will not rewrite. 