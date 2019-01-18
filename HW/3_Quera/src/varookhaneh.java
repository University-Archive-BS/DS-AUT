import java.util.*;

public class varookhaneh
{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        System.out.println(shortest(input));
    }

    public static String shortest(String input)
    {
        int input_length = input.length();
        if (input_length == 1 || isVarooKhaneh(input))
        {
            return input;
        }

        char begin = input.charAt(0);
        char end = input.charAt(input_length - 1);

        if (begin == end)
        {
            return begin + shortest(input.substring(1, input_length - 1)) + end;
        }
        else
        {
            String same_head = shortest(input.substring(1, input_length));
            String varookhaneh1 = begin + same_head + begin;
            int hazineh1 = same_head.length() - (input_length - 1) + 2;

            String same_tail = shortest(input.substring(0, input_length - 1));
            String varookhaneh2 = end + same_tail + end;
            int hazineh2 = same_tail.length() - (input_length - 1) + 2;

            if (hazineh1 > hazineh2)
            {
                return varookhaneh2;
            }
            if (hazineh1 < hazineh2)
            {
                return varookhaneh1;
            }
            return (varookhaneh1.compareTo(varookhaneh2) < 0 ? varookhaneh1 : varookhaneh2);
        }
    }

    protected static boolean isVarooKhaneh(String input)
    {
        int input_length = input.length();
        int left = 0;
        int right = (input_length - 1) - left;

        while (left <= right)
        {
            if (input.charAt(left) != input.charAt(right))
            {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}
