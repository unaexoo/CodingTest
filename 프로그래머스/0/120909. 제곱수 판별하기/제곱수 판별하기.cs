using System;

public class Solution {
    public int solution(int n) {
        int answer = 0;
        for (int i = 1; i <= n; i++)
        {
            if (i * i == n)
            {
                return answer = 1;
            }
            answer = 2;

        }
        return answer;
    }
}