Create table If Not Exists Weather
(
    Id          int,
    RecordDate  date,
    Temperature int
);
Truncate table Weather;
insert into Weather (Id, RecordDate, Temperature)
values ('1', '2015-01-01', '10');
insert into Weather (Id, RecordDate, Temperature)
values ('2', '2015-01-02', '25');
insert into Weather (Id, RecordDate, Temperature)
values ('3', '2015-01-03', '20');
insert into Weather (Id, RecordDate, Temperature)
values ('4', '2015-01-04', '30');

SELECT W1.id AS Id
FROM Weather AS W1,
     Weather AS W2
WHERE W1.RecordDate = DATE_ADD(W2.RecordDate, INTERVAL 1 DAY)
  AND W1.Temperature > W2.Temperature;
