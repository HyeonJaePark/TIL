import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 선분_교차_2_17387 {
    static class Point {
        long x, y;

        public Point(long x, long y) {
            this.x = x;
            this.y = y;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        
        Point[] point = new Point[4];
        
        long x1, y1, x2, y2, x3, y3, x4, y4;
        st = new StringTokenizer(br.readLine());
        x1 = Long.parseLong(st.nextToken());
        y1 = Long.parseLong(st.nextToken());
        x2 = Long.parseLong(st.nextToken());
        y2 = Long.parseLong(st.nextToken());
        st = new StringTokenizer(br.readLine());
        x3 = Long.parseLong(st.nextToken());
        y3 = Long.parseLong(st.nextToken());
        x4 = Long.parseLong(st.nextToken());
        y4 = Long.parseLong(st.nextToken());

        point[0] = new Point(x1, y1);
        point[1] = new Point(x2, y2);
        point[2] = new Point(x3, y3);
        point[3] = new Point(x4, y4);

        if (ccw(point[0], point[1], point[2]) * ccw(point[0], point[1], point[3]) == 0 &&
            ccw(point[2], point[3], point[0]) * ccw(point[2], point[3], point[1]) == 0) {
                if (Math.min(point[0].x, point[1].x) <= Math.max(point[2].x, point[3].x) &&
                    Math.min(point[2].x, point[3].x) <= Math.max(point[0].x, point[1].x) &&
                    Math.min(point[0].y, point[1].y) <= Math.max(point[2].y, point[3].y) &&
                    Math.min(point[2].y, point[3].y) <= Math.max(point[0].y, point[1].y)) {
                        System.out.println(1);
                    }
                else {
                    System.out.println(0);
                }
        } 
        else if(ccw(point[0], point[1], point[2]) * ccw(point[0], point[1], point[3]) <= 0 &&
                ccw(point[2], point[3], point[0]) * ccw(point[2], point[3], point[1]) <= 0) {
                    System.out.println(1);
        }
        else {
            System.out.println(0);
        }
    }
    public static int ccw(Point p1, Point p2, Point p3) {
        long cross_product = (p1.x * p2.y + p2.x * p3.y + p3.x * p1.y) - (p2.x * p1.y + p3.x * p2.y + p1.x * p3.y);
        if(cross_product > 0)
            return 1;
        else if(cross_product < 0)
            return -1;
        else 
            return 0;
    }
}
