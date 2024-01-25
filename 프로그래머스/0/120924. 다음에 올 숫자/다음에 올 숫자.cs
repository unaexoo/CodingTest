using System;

public class Solution {
    public int solution(int[] common) {
         int answer = 0;
            int n = common[1]-common[0];
            if(common[1]+n == common[2])
            {
                answer = common[common.Length - 1] + n;
            }
            else
            {
                n = common[1] / common[0];
                answer = common[common.Length - 1] * n;
            }
            return answer;
    }
}