var lines = File.ReadAllLines("day1_2.txt");
int result = 0;

List<Tuple<char, string, int>> digits = new List<Tuple<char, string, int>>();
digits.Add(new Tuple<char, string, int>('o', "one", 1));
digits.Add(new Tuple<char, string, int>('t', "two", 2));
digits.Add(new Tuple<char, string, int>('t', "three", 3));
digits.Add(new Tuple<char, string, int>('f', "four", 4));
digits.Add(new Tuple<char, string, int>('f', "five", 5));
digits.Add(new Tuple<char, string, int>('s', "six", 6));
digits.Add(new Tuple<char, string, int>('s', "seven", 7));
digits.Add(new Tuple<char, string, int>('e', "eight", 8));
digits.Add(new Tuple<char, string, int>('n', "nine", 9));


foreach (string line in lines)
{
    result += FindFirstAndLast(line);
}
Console.WriteLine(result);


int FindFirstAndLast(string line)
{
    int index = 0;
    int first = 0;
    int last = 0;
    bool found = false;
    while(index < line.Length)
    {
        bool set = false;
        if (Char.IsDigit(line[index]))
        {
            last = line[index] - '0';
            set = true; 
        }
        else
        {
            foreach (Tuple<char, string, int> d in digits)
            {
                if (line[index] == d.Item1
                    && line.Length >= index + d.Item2.Length
                    && line.Substring(index, d.Item2.Length).Equals(d.Item2))
                {
                    last = d.Item3;
                    index += d.Item2.Length-1;
                    set = true;
                    break;
                }
            }
        }
        if (set && !found)
        {
            first = last;
            found = true;
        }
        index += 1;
    }
    return first * 10 + last;
}