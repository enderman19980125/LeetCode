Create table If Not Exists Employee
(
    Id        int,
    Name      varchar(255),
    Salary    int,
    ManagerId int
);
Truncate table Employee;
insert into Employee (Id, Name, Salary, ManagerId)
values ('1', 'Joe', '70000', '3');
insert into Employee (Id, Name, Salary, ManagerId)
values ('2', 'Henry', '80000', '4');
insert into Employee (Id, Name, Salary, ManagerId)
values ('3', 'Sam', '60000', NULL);
insert into Employee (Id, Name, Salary, ManagerId)
values ('4', 'Max', '90000', NULL);

SELECT E1.Name AS Employee
FROM Employee E1,
     Employee E2
WHERE E1.ManagerId = E2.Id
  AND E1.Salary > E2.Salary;
