using System;
using System.Collections.Generic;

public class Solution
{
    public int[] solution(int n, int[] numlist)
    {
        var check = new List<int>();
        int cnt = 0;
        for (int i = 0; i < numlist.Length; i++)
        {
            if (numlist[i] % n == 0)
            {
                cnt++;
                check.Add(numlist[i]);
            }
        }
        int[] answer = new int[cnt];

        for (int i = 0; i < answer.Length; i++)
        {
            answer[i] = check[i];
        }
        return answer;
    }
}