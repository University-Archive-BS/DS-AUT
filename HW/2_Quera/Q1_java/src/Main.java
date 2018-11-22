import java.util.ArrayList;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Main
{
    public static void main(String[] args)
    {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<Integer>(new Comparator<Integer>()
        {
            @Override
            public int compare(Integer a, Integer b)
            {
                return b - a;
            }
        });

        Scanner in = new Scanner(System.in);

        int n = Integer.parseInt(in.nextLine());
        ArrayList<String> commands = new ArrayList<>();
        for (int i = 0; i < n; i++)
        {
            commands.add(in.nextLine());
        }

        for (int i = 0; i < n; i++)
        {
            if (commands.get(i).length() == 1)
            {
                if (i < 3)
                {
                    System.out.println("No reviews yet");
                }
                else
                {
                    Object[] result = maxHeap.toArray();
                    int res = (maxHeap.size() / 3) - 1;
                    System.out.println(Integer.parseInt(String.valueOf(result[res])));
//                    int result = (maxHeap.size() / 3);
//                    int[] temp = new int[result];
//                    for (int j = 0; j < result; j++)
//                    {
//                        temp[j] = maxHeap.poll();
//                    }
//                    System.out.println(temp[result - 1]);
//                    for (int j = 0; j < result; j++)
//                    {
//                        maxHeap.add(temp[j]);
//                    }
                }
            }
            else
            {
                maxHeap.add(Integer.valueOf(commands.get(i).substring(2)));
            }
        }
    }
}

