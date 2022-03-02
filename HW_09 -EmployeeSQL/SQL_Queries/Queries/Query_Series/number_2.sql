--2 List first name, last name, and hire date for employees who were hired in 1986.
SELECT 
	e.first_name, 
	e.last_name, 
	e.hire_date 
FROM 
	employees e
WHERE 
	extract(year from e.hire_date) = 1986