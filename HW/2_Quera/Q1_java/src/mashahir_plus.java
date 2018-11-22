import java.util.ArrayList;
import java.util.Scanner;

public class mashahir_plus
{
    public static class Node
    {
        public int value;
        public Node left, right;

        public Node(int value)
        {
            this.value = value;
            left = null;
            right = null;
        }
    }

    public static class BinarySearchTree
    {
        Node root;

        public BinarySearchTree()
        {
            root = null;
        }

        public void insert(int value)
        {
            this.root = this.insertRec(this.root, value);
        }

        public Node insertRec(Node node, int value)
        {
            if (node == null)
            {
                this.root = new Node(value);
                return this.root;
            }

            if (value == node.value)
            {
                return node;
            }

            if (value < node.value)
            {
                node.left = this.insertRec(node.left, value);
            }
            else
            {
                node.right = this.insertRec(node.right, value);
            }
            return node;
        }

        public class count
        {
            int c = 0;
        }

        void kthLargestUtil(Node node, int k, count C)
        {
            if (node == null || C.c >= k)
            {
                return;
            }

            this.kthLargestUtil(node.right, k, C);

            C.c++;

            if (C.c == k)
            {
                System.out.println(node.value);
                return;
            }

            this.kthLargestUtil(node.left, k, C);
        }

        void kthLargest(int k)
        {
            count c = new count();
            this.kthLargestUtil(this.root, k, c);
        }
    }
    public static void main(String[] args)
    {
        BinarySearchTree tree = new BinarySearchTree();

        Scanner in = new Scanner(System.in);

        int n = Integer.parseInt(in.nextLine());
        ArrayList<String> commands = new ArrayList<>();
        for (int i = 0; i < n; i++)
        {
            commands.add(in.nextLine());
        }

        int values = 0;
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
                    int res = (values / 3);
                    tree.kthLargest(res);
                }
            }
            else
            {
                tree.insert(Integer.valueOf(commands.get(i).substring(2)));
                values++;
            }

        }
    }
}
