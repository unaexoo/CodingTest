using System;

public class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = new int[2];
        int odd = 1, even = 1;
        for (int i = 0; i < num_list.Length; i++)
        {
            if (num_list[i] % 2 == 0)
            {
                answer[0] = even++;
            }
            else
            {
                answer[1] = odd++;
            }
        }

        for (int i = 0; i < answer.Length; i++)
        {
            Console.WriteLine(answer[i]);
        }
        return answer;
    }
}