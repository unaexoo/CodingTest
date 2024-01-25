using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace 제로
{
    internal class Program
    {

        static void Main(string[] args)
        {
            int total=int.Parse(Console.ReadLine());
            int sum = 0;
            int num;
            List<int> list = new List<int>();

            for(int i = 0; i < total; i++)
            {
                num=int.Parse(Console.ReadLine().Trim());

                if (num != 0)
                {
                    list.Add(num);

                }
                else
                {
                    list.RemoveAt(list.Count - 1);
                }
            }

            foreach(int element in list)
            {
                sum+=element;
            }
            Console.WriteLine(sum);
        }
        
    }
}
