# Problem Statement:
Write source code in Python that will do following:
There are 2 strings S and C. String S represents a table in CSV format, where rows are separated by newline characters ('\n') and each row consists of one or more fields separated by commas (',').

The first row contains the names of columns and the following row contains the values.

For example, the table below is presented by the following string S: "id,name,age,gender,room,dep.\n1,Joe,54,M,12,8\n17,Betty,29,F,15,6".

+--+------+----+--------+------+------+<br />
| id  |   name   |  age  | gender | room | dep. |<br />
+--+------+----+--------+------+------+<br />
| &nbsp; 1 | &nbsp; &nbsp;   Joe   |   54  |&nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;     M   |  &nbsp;  &nbsp;  12 | &nbsp;  &nbsp; &nbsp;   8 |<br />
| &nbsp; 7 | &nbsp;  Betty   |   29  |&nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;     F   |  &nbsp;  &nbsp;  15 | &nbsp;  &nbsp; &nbsp;   6 |<br />
+--+------+----+--------+------+------+<br />

String C is the name of the column described by S that contains only integers. The requirement is to find the maximum value in that column. In the example above, for C = "age" , the maximum value is 54.

I have written a function:<br />
<code> class Solution { public int solution(String S, String C); }</code><br />
which, given 2 strings S and C consisting of N and M characters, respectively, returns the maximum value in column C of the table described by S.

Examples:<br/>
1. Given S = "area,land,\n3722,CN\n6612,RU\n3855,CA\n3797,USA" and C="area"

+-------+-------+<br />
|  &nbsp;  area &nbsp;  | &nbsp;  land &nbsp;|<br />
+-------+-------+<br />
| &nbsp; 3722 &nbsp;| &nbsp; CN &nbsp; | <br />
| &nbsp; 6612 &nbsp;| &nbsp; RU &nbsp; | <br />
| &nbsp; 3855 &nbsp;| &nbsp; CA &nbsp; | <br />
| &nbsp; 3797 &nbsp;|  USA &nbsp; | <br />
+-------+-------+<br />

the function will return 6612

2. Given S = "city,temp2,temp\nParis,7,-3\nKarachi,4,-4\nPorto,-1,-2" and C="temp"

+--------+---------+--------+<br />
|  &nbsp;  city &nbsp; &nbsp;  | &nbsp;  temp2 &nbsp;| &nbsp;  temp &nbsp;|<br />
+--------+---------+--------+<br />
| &nbsp; Paris &nbsp;  &nbsp; | &nbsp; &nbsp; 7 &nbsp;  &nbsp; &nbsp; | &nbsp; &nbsp; -3 &nbsp; &nbsp; | <br />
| &nbsp; Karachi &nbsp; | &nbsp; &nbsp; 4  &nbsp; &nbsp; | &nbsp; &nbsp; -4 &nbsp; &nbsp; | <br />
| &nbsp; Proto &nbsp;  &nbsp; | &nbsp; -1 &nbsp;  &nbsp; &nbsp; | &nbsp; &nbsp; -2 &nbsp; &nbsp; | <br />
+--------+---------+---------+<br />

the function with return -2


## Keywords:
Python, Source Code, Algorithm, SpreadSheet, CSV Format to Array/List conversion, Find in List, Minium Value
