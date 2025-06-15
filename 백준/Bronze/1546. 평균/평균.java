import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int strLen = Integer.parseInt(br.readLine());
        String str = br.readLine();
        String[] nums = str.split(" ");
        double answer = 0.0;
        double max = getMax(nums, strLen);
        for(int i=0; i < strLen; i++){
            double num = Double.parseDouble(nums[i]) / max * 100;
            answer += num;
        }
        answer /= strLen;
        System.out.println(answer);

    }

    public static double getMax(String[] nums, int n){
        double max = 0.0;
        for(int i = 0; i < n; i++){
            double num = Double.parseDouble(nums[i]);
            if (max < num) {
                max = num;
            }
        }
        return max;
    }
}