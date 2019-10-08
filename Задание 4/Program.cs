using System;

namespace Задание_4
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Меняю местами цифры");
            Console.Write("x=");
            int x = int.Parse(Console.ReadLine());
            Console.Write("y=");
            int y = int.Parse(Console.ReadLine());
            x = x + y;
            y = x - y;
            x = x - y;
            Console.WriteLine("x=" + x); 
            Console.WriteLine("y=" + y);
        }
    }
}
