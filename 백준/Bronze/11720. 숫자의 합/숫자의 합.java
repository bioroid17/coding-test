import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int strLen = Integer.parseInt(br.readLine());
        String str = br.readLine();
        String[] nums = str.split("");
        int answer = 0;
        for(int i=0; i < strLen; i++){
            answer += Integer.parseInt(nums[i]);
        }
        System.out.println(answer);

    }
}