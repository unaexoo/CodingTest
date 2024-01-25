using System;

public class Solution {
    public int solution(int[] array) {
     int answer = 0;
        double len = array.Length;
        double center = Math.Ceiling(len/2)-1;
        Array.Sort(array);
        for (int i = 0; i < len; i++)
        {
            answer = array[(int)center];
        }
        return answer;
    }
}