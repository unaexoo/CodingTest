using System;

public class Solution {
    public int solution(string message) {
        int answer = 0;
        char[] ch = message.ToCharArray();
        for (int i = 0; i < ch.Length; i++)
        {
            answer++;
        }
        answer *= 2;
        return answer;
    }
}