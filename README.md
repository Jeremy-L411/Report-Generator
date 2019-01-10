# Report-Generator

These programs were designed to be executed on a server one at a time

Starting with either make_fakefiles or structured_random_files to generate a set of fake data to test the code. Adjust 
the values in the for loops to get desired number of files to run

Next execution is moveFiles, this organizes the files into Name> Year> Month files. If the organized folder does not
exist it creates one. 

monthly_report creates a monthly mulitsheet xlsx file in each month for each name

yearly_report creates a sum of all the bonus and expense files for each name

