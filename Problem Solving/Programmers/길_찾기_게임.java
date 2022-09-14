import java.util.*;

public class 길_찾기_게임 {
    public static void main(String[] args) {
        int[][] nodeinfo = {{5,3},{11,5},{13,3},{3,5},{6,1},{1,3},{8,6},{7,2},{2,2}};
        Solution s = new Solution();
        s.solution(nodeinfo);
    }
    // answer code
    static class Solution {
        static int[][] answer;
        static int ansidx = 0;

        public int[][] solution(int[][] nodeinfo) {
            Node[] node = new Node[nodeinfo.length];
            for (int i = 0; i < nodeinfo.length; i++) {
                node[i] = new Node(nodeinfo[i][0], nodeinfo[i][1], i + 1);
            }

            Arrays.sort(node, (o1, o2) -> {
                if (o1.y == o2.y) {
                    return o1.x - o2.x;
                }
                else {
                    return o2.y - o1.y;
                }
            });

            Node root = node[0];
            for (int i = 1; i < node.length; i++) {
                insertNode(root, node[i]);
            }

            answer = new int[2][nodeinfo.length];
            ansidx = 0;
            preorder(node[0]);
            ansidx = 0;
            postorder(node[0]);

            return answer;
        }
        class Node {
            int x, y, idx;
            Node left, right;

            Node(int x, int y, int idx) {
                this.x = x;
                this.y = y;
                this.idx = idx;
                left = null;
                right = null;
            }
        }

        void insertNode(Node parent, Node child) {
            if (parent.x > child.x) {
                if (parent.left == null) {
                    parent.left = child;
                }
                else {
                    insertNode(parent.left, child);
                }
            }
            else {
                if (parent.right == null) {
                    parent.right = child;
                }
                else {
                    insertNode(parent.right, child);
                }
            }
        }

        void postorder(Node node) {
            if (node != null) {
                postorder(node.left);
                postorder(node.right);
                answer[1][ansidx++] = node.idx;
            }
        }

        void preorder(Node node) {
            if (node != null) {
                answer[0][ansidx++] = node.idx;
                preorder(node.left);
                preorder(node.right);
            }
        }
    }
    // answer code
}
