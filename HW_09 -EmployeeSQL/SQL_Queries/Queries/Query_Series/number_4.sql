--List the department of each employee with the following information: employee number, last name, first name, and department name.
Select
	e.emp_no,
	e.last_name,
	e.first_name,
	d.dept_name
From
	departments as d
	join employees as e on d.dept_name = d.dept_name;