import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class derakht
{
    public static class Node
    {
        public int value;
        public Node next;

        public Node(int value)
        {
            this.value = value;
            next = null;
        }

    }

    public static class Graph
    {
        public ArrayList<Node> nodes;

        public Graph(int size)
        {
            this.nodes = new ArrayList<>();
            for (int i =0; i < size; i++)
            {
                this.nodes.add(null);
            }
        }

        public void add(int v, int u)
        {
            if (nodes.get(v) == null)
            {
                nodes.set(v, new Node(u));
            }
            else
            {
                Node temp = nodes.get(v);
                while (temp.next != null)
                {
                    temp = temp.next;
                }
                temp.next = nodes.get(u);
            }
        }

        public int[] bfs(int v)
        {
            boolean[] visited = new boolean[nodes.size()];
            Arrays.fill(visited, false);
            ArrayList<Integer> queue = new ArrayList<>();
            int[] distance = new int[nodes.size()];
            Arrays.fill(distance, -1);
            visited[v] = true;
            queue.add(v);
            int u = 0;
            distance[v] = 0;
            int maximum = 0;
            while (queue.size() != 0)
            {
                u = queue.get(queue.size() - 1);
                Node element = nodes.get(u);
                while (element != null)
                {
                    if (!visited[element.value])
                    {
                        visited[element.value] = true;
                        queue.add(element.value);
                        distance[element.value] = distance[u] + 1;

                    }
                    element = element.next;
                }
            }
            for (int i = 0; i < nodes.size(); i++)
            {
                if (distance[i] > maximum)
                {
                    maximum = distance[i];
                    u = i;
                }
            }
            int[] my_return = new int[2];
            my_return[0] = u;
            my_return[1] = maximum;
            return my_return;
        }
    }

    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        int n = Integer.parseInt(scanner.nextLine());

        Graph graph = new Graph(n);
        for (int i = 0; i < n - 1; i++)
        {
            String[] edges = scanner.nextLine().split(" ");
            graph.add(Integer.parseInt(edges[0]) - 1, Integer.parseInt(edges[1]) - 1);
            graph.add(Integer.parseInt(edges[1]) - 1, Integer.parseInt(edges[0]) - 1);
        }
        System.out.println(graph.nodes.get(3).next.value);
        System.out.println(graph.bfs(graph.bfs(0)[0])[1]);
    }
}
