Create table If Not Exists Logs
(
    Id  int,
    Num int
);
Truncate table Logs;
insert into Logs (Id, Num)
values ('1', '1');
insert into Logs (Id, Num)
values ('2', '1');
insert into Logs (Id, Num)
values ('3', '1');
insert into Logs (Id, Num)
values ('4', '2');
insert into Logs (Id, Num)
values ('5', '1');
insert into Logs (Id, Num)
values ('6', '2');
insert into Logs (Id, Num)
values ('7', '2');

SELECT DISTINCT Num AS ConsecutiveNums
FROM (SELECT Num, @preValue AS p, @prePreValue AS pp, @prePreValue := @preValue, @preValue := Num
      FROM Logs,
           (SELECT @preValue := NULL, @prePreValue := NULL) as pVpPV) AS TempTable
WHERE Num = p
  AND p = pp;
