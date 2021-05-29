# SET 대입 연산자 :=,
# SQL에서 비교연산자는 무조건 = 임
SET @hour := -1;

SELECT (@hour := @hour+1) as 'HOUR'
      ,(SELECT count(*) FROM ANIMAL_OUTS WHERE HOUR(DATETIME) = @hour) as hour
FROM ANIMAL_OUTS 
WHERE @hour < 23;
