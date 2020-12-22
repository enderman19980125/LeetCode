Create table If Not Exists Employee
(
    Id           int,
    Name         varchar(255),
    Salary       int,
    DepartmentId int
);
Create table If Not Exists Department
(
    Id   int,
    Name varchar(255)
);
Truncate table Employee;
insert into Employee (Id, Name, Salary, DepartmentId)
values ('1', 'Joe', '85000', '1');
insert into Employee (Id, Name, Salary, DepartmentId)
values ('2', 'Henry', '80000', '2');
insert into Employee (Id, Name, Salary, DepartmentId)
values ('3', 'Sam', '60000', '2');
insert into Employee (Id, Name, Salary, DepartmentId)
values ('4', 'Max', '90000', '1');
insert into Employee (Id, Name, Salary, DepartmentId)
values ('5', 'Janet', '69000', '1');
insert into Employee (Id, Name, Salary, DepartmentId)
values ('6', 'Randy', '85000', '1');
insert into Employee (Id, Name, Salary, DepartmentId)
values ('7', 'Will', '70000', '1');
Truncate table Department;
insert into Department (Id, Name)
values ('1', 'IT');
insert into Department (Id, Name)
values ('2', 'Sales');

SELECT Department.Name AS Department, Employee.Name AS Employee, Employee.Salary AS Salary
FROM Employee,
     Department,
     (SELECT DepartmentId, MIN(Salary) AS MinSalary
      FROM (SELECT DepartmentId,
                   Salary,
                   IF(@preDepartment = DepartmentId, IF(@preSalary = Salary, @r, @r := @r + 1), @r := 1) AS Ranking,
                   @preSalary := Salary,
                   @preDepartment := DepartmentId
            FROM Employee,
                 (SELECT @r := 0, @preSalary := NULL, @preDepartment := NULL) AS T
            ORDER BY DepartmentId, Salary DESC)
               AS DepartmantRankingTable
      WHERE Ranking <= 3
      GROUP BY DepartmentId) AS DepartmentMinTable
WHERE Employee.DepartmentId = DepartmentMinTable.DepartmentId
  AND Employee.DepartmentId = Department.Id
  AND Employee.Salary >= DepartmentMinTable.MinSalary;
