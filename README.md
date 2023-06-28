# university
Consider a UNIVERSITY database that has different requirements from the UNIVERSITY
database presented in Section 3.10. This database keeps track of students and their 
majors, transcripts, and registration as well as of the university’s course offerings. 
The database also keeps track of the sponsored research projects of faculty and 
graduate students. This schema is shown in Figure 4.9. A discussion of the requirements that led to this schema follows.
For each person, the database maintains information on the person’s Name [Name], 
Social Security number [Ssn], address [Address], sex [Sex], and birth date [Bdate]. 
Two subclasses of the PERSON entity type are identified: FACULTY and STUDENT. 
Specific attributes of FACULTY are rank [Rank] (assistant, associate, adjunct, research,
visiting, and so on), office [Foffice], office phone [Fphone], and salary [Salary]. All faculty members are related to the academic department(s) with which they are affiliated 
[BELONGS] (a faculty member can be associated with several departments, so the 
relationship is M:N). A specific attribute of STUDENT is [Class] (freshman = 1, sophomore = 2, … , MS student = 5, PhD student = 6). Each STUDENT is also related to his 
or her major and minor departments (if known) [MAJOR] and [MINOR], to the course 
sections he or she is currently attending [REGISTERED], and to the courses completed 
[TRANSCRIPT]. Each TRANSCRIPT instance includes the grade the student received 
[Grade] in a section of a course.
GRAD_STUDENT is a subclass of STUDENT, with the defining predicate (Class = 5 OR 
Class = 6). For each graduate student, we keep a list of previous degrees in a composite, multivalued attribute [Degrees]. We also relate the graduate student to a faculty 
advisor [ADVISOR] and to a thesis committee [COMMITTEE], if one exists.
An academic department has the attributes name [Dname], telephone [Dphone], and 
office number [Office] and is related to the faculty member who is its chairperson 
[CHAIRS] and to the college to which it belongs [CD]. Each college has attributes college name [Cname], office number [Coffice], and the name of its dean [Dean].
A course has attributes course number [C#], course name [Cname], and course 
description [Cdesc]. Several sections of each course are offered, with each section 
having the attributes section number [Sec#] and the year and quarter in which the 
section was offered ([Year] and [Qtr]).10 Section numbers uniquely identify each 
section. The sections being offered during the current quarter are in a subclass 
CURRENT_SECTION of SECTION, with the defining predicate Qtr = Current_qtr and 
Year = Current_year. Each section is related to the instructor who taught or is teaching it ([TEACH]), if that instructor is in the database.
The category INSTRUCTOR_RESEARCHER is a subset of the union of FACULTY and 
GRAD_STUDENT and includes all faculty, as well as graduate students who are supported by teaching or research. Finally, the entity type GRANT keeps track of research 
grants and contracts awarded to the university. Each grant has attributes grant title 
[Title], grant number [No], the awarding agency [Agency], and the starting date 
[St_date]. A grant is related to one principal investigator [PI] and to all researchers it 
supports [SUPPORT]. Each instance of support has as attributes the starting date of 
support [Start], the ending date of the support (if known) [End], and the percentage of 
time being spent on the project [Time] by the researcher being supported.
![EER University 2](https://github.com/hazemAzzam/university/assets/61450444/41368ef2-c6b7-4ee4-81a6-407874f0c038)
