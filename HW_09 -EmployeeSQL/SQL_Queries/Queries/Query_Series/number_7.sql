--7. List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.
Select
	d.dept_no,
	d.dept_name,
	e.emp_no,
	e.last_name,
	e.first_name
From
	employees e
	join dept_emp de on e.emp_no = de.emp_no
	join departments d on d.dept_no = de.dept_no
Where
	d.dept_name = 'Development' 
	or d.dept_name = 'Sales'
order by 
	dept_name desc;