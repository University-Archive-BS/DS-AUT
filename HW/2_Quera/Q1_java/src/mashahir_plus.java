import java.util.ArrayList;
import java.util.Scanner;

public class mashahir_plus
{
    public static class Node
    {
        public int value, count;
        public Node left, right;

        public Node(int value)
        {
            this.value = value;
            left = null;
            right = null;
            count = 0;
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
            if (root == null)
            {
                root = new Node(value);
            }
            else
            {
                insertNode(new Node(value));
            }
        }

        public void insertNode(Node newNode)
        {
            Node traversal_node = root;
            Node current_node = root;
            while (traversal_node != null)
            {
                current_node = traversal_node;
                if (newNode.value < traversal_node.value)
                {
                    traversal_node.count++;
                    traversal_node = traversal_node.left;
                }
                else
                {
                    traversal_node = traversal_node.right;
                }
            }
            if (newNode.value < current_node.value)
            {
                current_node.left = newNode;
            }
            else
            {
                current_node.right = newNode;
            }
        }

        public int Kth_smallest(int k)
        {
            int ret = -1;
            Node traverse_node = root;
            while (traverse_node != null)
            {
                if (traverse_node.count == (k - 1))
                {
                    ret = traverse_node.value;
                    break;
                }
                else if (traverse_node.count < k)
                {
                    k = k - (traverse_node.count + 1);
                    traverse_node = traverse_node.right;
                }
                else
                {
                    traverse_node = traverse_node.left;
                }
            }
            return ret;
        }
    }

    public static void main(String[] args)
    {
        BinarySearchTree tree = new BinarySearchTree();

        Scanner in = new Scanner(System.in);

        int n = Integer.parseInt(in.nextLine());
        ArrayList<String> commands = new ArrayList<>();
        int values = 0;
        for (int i = 0; i < n; i++)
        {
            commands.add(in.nextLine());
            if (commands.get(i).length() == 1)
            {
                if (values < 3)
                {
                    System.out.println("No reviews yet");
                }
                else
                {
                    System.out.println(tree.Kth_smallest(values - values / 3 + 1));
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
