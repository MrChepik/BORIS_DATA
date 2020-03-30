#!/usr/bin/env python3
#-*-decode='utf-8'-*-



%load_ext sql
# type in your query to retrieve list of all tables in the database for your db2 schema (username)
import pandas as pd

chicago_public_schools = pd.read_csv('https://ibm.box.com/shared/static/f9gjvj1gjmxxzycdhplzt01qtz0s7ew7.csv')
%sql PERSIST chicago_public_schools

# type in your query to retrieve the number of columns in the SCHOOLS table
%sql select * from chicago_public_schools limit 5

# type in your query to retrieve all column names in the SCHOOLS table along with their datatypes and length
%sql select COLNAME, TYPENAME, LENGTH from SYSCAT.COLUMNS where TABNAME = 'SCHOOLS'

#How many Elementary Schools are in the dataset?
%sql select NAME_OF_SCHOOL  from SCHOOLS where "Elementary, Middle, or High School" = 'ES'

#What is the highest Safety Score?¶
%sql select max(SAFETY_SCORE) from SCHOOLS

#Which schools have highest Safety Score?¶
%sql select NAME_OF_SCHOOL from SCHOOLS where SAFETY_SCORE = (select max(SAFETY_SCORE)from SCHOOLS)

#What are the top 10 schools with the highest "Average Student Attendance"?
%sql select NAME_OF_SCHOOL, Average_Student_Attendance from SCHOOLS \
    order by Average_Student_Attendance desc nulls last limit 10

#Retrieve the list of 5 Schools with the lowest Average Student Attendance sorted in ascending order based on attendance
%sql select NAME_OF_SCHOOL, Average_Student_Attendance from SCHOOLS \
    order by Average_Student_Attendance fetch first 5 rows only

#Now remove the '%' sign from the above result set for Average Student Attendance column
%sql select NAME_OF_SCHOOL, replace(Average_Student_Attendance, '%', ' ') from SCHOOLS\
    order by Average_Student_Attendance fetch first 5 rows only

#Which Schools have Average Student Attendance lower than 70%?
%sql select Name_of_School, Average_Student_Attendance from SCHOOLS \
    where cast(replace(Average_Student_Attendance, '%', ' ') as double) < 70\
    order by Average_Student_Attendance

#Get the total College Enrollment for each Community Area
%sql select COMMUNITY_AREA_NAME, sum(College_Enrollment) as TOTAL_ENROLLMENT from SCHOOLS \
group by COMMUNITY_AREA_NAME

#Get the 5 Community Areas with the least total College Enrollment sorted in ascending order
%sql select COMMUNITY_AREA_NAME, College_Enrollment from SCHOOLS \
    order by College_enrollment asc 

#Get the hardship index for the community area which has College Enrollment of 4638
%sql select Hardship_index from CHICAGO_SOCIOECONOMIC_DATA CD, SCHOOLS CPS \
    where CD.ca = CPS.Community_Area_Number and College_Enrollment = 4368

#Get the hardship index for the community area which has the highest value for College Enrollment
%sql select ca, Community_Area_Name, Hardship_Index from CHICAGO_SOCIOECONOMIC_DATA  \
    where ca in (select Community_Area_Number from SCHOOLS order by College_Enrollment desc limit 1)
