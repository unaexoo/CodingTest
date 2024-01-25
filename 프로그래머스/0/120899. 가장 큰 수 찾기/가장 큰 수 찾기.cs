using System;

public class Solution {
    public int[] solution(int[] array) {
        int[] answer = new int[2];
        for (int i = 0; i < array.Length; i++)
        {
            for (int j = 0; j < array.Length; j++)
            {
                if (array[i] < array[j])
                {
                    answer[0] = array[j];
                    answer[1] = j;
                }
            }
        }
        return answer;
    }
}