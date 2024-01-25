using System;

public class Solution {
    public string solution(string rsp) {
        string answer = "";
        char[] ch = rsp.ToCharArray();
        var tmp = new char[ch.Length];
        for (int i = 0; i < rsp.Length; i++)
        {
            if (ch[i] == '2') tmp[i] = '0';
            else if (ch[i] == '0') tmp[i] = '5';
            else tmp[i] = '2';
        }
        answer = new String(tmp);
        return answer;
    }
}