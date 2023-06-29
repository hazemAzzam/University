# University Database

The UNIVERSITY database keeps track of students and their majors, transcripts, and registration, as well as the university's course offerings. It also tracks the sponsored research projects of faculty and graduate students.

## Entity Types and Attributes

### PERSON
- Name [Name]
- Social Security number [Ssn]
- Address [Address]
- Sex [Sex]
- Birth date [Bdate]

### FACULTY (subclass of PERSON)
- Rank [Rank] (assistant, associate, adjunct, research, visiting, etc.)
- Office [Foffice]
- Office phone [Fphone]
- Salary [Salary]
- Affiliated department(s) [BELONGS] (M:N relationship)

### STUDENT (subclass of PERSON)
- Class [Class] (freshman = 1, sophomore = 2, MS student = 5, PhD student = 6)
- Major department(s) [MAJOR]
- Minor department(s) [MINOR]
- Course sections currently attending [REGISTERED]
- Completed courses [TRANSCRIPT]
- Grade [Grade] in each course section

### GRAD_STUDENT (subclass of STUDENT)
- Degrees [Degrees] (composite, multivalued attribute)
- Faculty advisor [ADVISOR]
- Thesis committee [COMMITTEE] (if exists)

### ACADEMIC DEPARTMENT
- Name [Dname]
- Telephone [Dphone]
- Office number [Office]
- Chairperson [CHAIRS]
- Belongs to college [CD]

### COLLEGE
- College name [Cname]
- Office number [Coffice]
- Dean's name [Dean]

### COURSE
- Course number [C#]
- Course name [Cname]
- Course description [Cdesc]

### SECTION
- Section number [Sec#]
- Year [Year] and quarter [Qtr] offered

### CURRENT_SECTION (subclass of SECTION)
- Sections offered in the current quarter (defined by Qtr = Current_qtr and Year = Current_year)

### INSTRUCTOR_RESEARCHER (subset of FACULTY and GRAD_STUDENT)
- Includes faculty and supported graduate students (teaching or research)

### GRANT
- Grant title [Title]
- Grant number [No]
- Awarding agency [Agency]
- Starting date [St_date]
- Principal investigator [PI]
- Researchers supported [SUPPORT]
- Support attributes: starting date [Start], ending date [End], percentage of time [Time]

## Entity-Relationship Diagram (ERD)
![EER University 2](https://github.com/hazemAzzam/university/assets/61450444/41368ef2-c6b7-4ee4-81a6-407874f0c038)
