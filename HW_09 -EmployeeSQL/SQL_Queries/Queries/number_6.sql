-- #6 List all employees in the Sales department, including their employee number, last name, first name, and department name.


Select 
	d.dept_no,
	d.dept_name,
	e.emp_no,
	e.first_name,
	e.last_name
From
	employees e
	join dept_emp de on e.emp_no = de.emp_no
	join departments d on d.dept_no = de.dept_no
where 
	dept_name = 'Sales'
order by
	e.last_name asc
limit 15 
