using System;

public class Solution {
    public int solution(int[] sides) {
        int answer = 2;
        Array.Sort(sides);
        for (int i = 0; i < sides.Length; i++)
        {
            Console.WriteLine(sides[i]);
        }
        if (sides[0] + sides[1] > sides[2])
        {
            answer = 1;
        }

        return answer;
    }
}