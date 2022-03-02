-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/fFZSAo
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

drop table if exists titles cascade;
drop table if exists departments cascade;
drop table if exists dept_emp cascade;
drop table if exists dept_manager cascade;
drop table if exists employees cascade;
drop table if exists salaries cascade;


CREATE TABLE "titles" (
    "ID" serial   NOT NULL,
    "title_id" VARCHAR(10) NOT NULL UNIQUE,
    "title" VARCHAR(50),
    "last_udpated" timestamp default localtimestamp NOT NULL,
    CONSTRAINT "pk_titles" PRIMARY KEY (
        "ID"
     )
);

CREATE TABLE "departments" (
    "ID" serial NOT NULL,
    "dept_no" VARCHAR(10) NOT NULL UNIQUE,
    "dept_name" VARCHAR(50),
    "last_udpated" timestamp default localtimestamp NOT NULL,
    CONSTRAINT "pk_departments" PRIMARY KEY (
        "ID"
     )
);

CREATE TABLE "employees" (
    "ID" serial NOT NULL,
    "emp_no" int NOT NULL UNIQUE,
    "emp_title_id" VARCHAR(10),
    "birth_date" date,
    "first_name" VARCHAR(100),
    "last_name" VARCHAR(100),
	"gender" VARCHAR(1)
    "hite_date" date,
    "last_udpated" timestamp default localtimestamp NOT NULL,
    CONSTRAINT "pk_employees" PRIMARY KEY (
        "ID"
     )
);

CREATE TABLE "dept_manager" (
    "ID" serial NOT NULL,
	"emp_no" int NOT NULL UNIQUE,
    "dept_no" VARCHAR(10) NOT NULL,
    "last_udpated" timestamp default localtimestamp NOT NULL,
    CONSTRAINT "pk_dept_manager" PRIMARY KEY (
        "ID"
     )
);

CREATE TABLE "salaries" (
    "ID" serial NOT NULL,
    "emp_no" int NOT NULL,
    "salary" int NOT NULL,
    "last_udpated" timestamp default localtimestamp NOT NULL,
    CONSTRAINT "pk_salaries" PRIMARY KEY (
        "ID"
     )
);

CREATE TABLE "dept_emp" (
    "ID" serial   NOT NULL,
	"emp_no" int NOT NULL,
    "dept_no" VARCHAR(10) NOT NULL,
    "last_udpated" timestamp default localtimestamp NOT NULL,
    CONSTRAINT "pk_dept_emp" PRIMARY KEY (
        "ID"
     )
);

ALTER TABLE "employees" ADD CONSTRAINT "fk_employees_emp_title_id" FOREIGN KEY("emp_title_id")
REFERENCES "titles" ("title_id");

ALTER TABLE "dept_manager" ADD CONSTRAINT "fk_dept_manager_dept_no" FOREIGN KEY("dept_no")
REFERENCES "departments" ("dept_no");

ALTER TABLE "dept_manager" ADD CONSTRAINT "fk_dept_manager_emp_no" FOREIGN KEY("emp_no")
REFERENCES "employees" ("emp_no");

ALTER TABLE "salaries" ADD CONSTRAINT "fk_salaries_emp_no" FOREIGN KEY("emp_no")
REFERENCES "employees" ("emp_no");

ALTER TABLE "dept_emp" ADD CONSTRAINT "fk_dept_emp_emp_no" FOREIGN KEY("emp_no")
REFERENCES "employees" ("emp_no");

ALTER TABLE "dept_emp" ADD CONSTRAINT "fk_dept_emp_dept_no" FOREIGN KEY("dept_no")
REFERENCES "departments" ("dept_no");



