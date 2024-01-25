using System;

public class Solution {
    public int solution(int age) {
        int answer = 0;
        if(age<2000){
          answer=2022-age+1;
        }else{
          answer=age-2022-1;
        }
        return answer;
    }
}