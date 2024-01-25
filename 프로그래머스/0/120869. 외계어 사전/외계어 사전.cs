using System;

public class Solution {
    public int solution(string[] spell, string[] dic) {
        int answer = 0;

            foreach(string dict in dic){
                bool check = true;
                foreach(string sll in spell)
                {
                    if (dict.IndexOf(sll) == -1)
                    {
                        check = false;
                        answer = 2;
                        break;
                    }
                }
                if (check == true)
                {
                    answer = 1; break;
                }
            }
            return answer;
    }
}