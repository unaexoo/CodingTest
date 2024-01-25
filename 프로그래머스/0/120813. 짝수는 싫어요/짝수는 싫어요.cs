using System;

public class Solution {
    public int[] solution(int n) {
        int[] answer;
            if (n % 2 == 0)
            {
                answer = new int[n / 2];
            }
            else
            {
                answer = new int[n/2+1];
            }
            int cnt = 0;
            for(int i=n; i>0; i--)
            {
                if (i % 2 != 0)
                {
                    answer[cnt++] = i;
                }
            }
        Array.Sort(answer);
            return answer;
    }
}