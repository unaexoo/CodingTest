using System;

public class Solution {
    public string solution(string my_string) {
string answer = "";
        foreach (var str in my_string)
        {
            if (str == 'a' || str == 'e' || str == 'i' || str == 'o' || str == 'u')
            {
                answer += "";
            }
            else
            {
                answer += str;
            }
        }
        return answer;
    }
}