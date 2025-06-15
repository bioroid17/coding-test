import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        int[] nums = new int[n];
        for(int i=0; i < n; i++){
            nums[i] = Integer.parseInt(br.readLine());
        }
        int count = 1;
        while(count != 0){
            count = 0;
            for(int j=0; j<n-1; j++){
                if(nums[j] >= nums[j+1]){
                    int temp = nums[j];
                    nums[j] = nums[j+1];
                    nums[j+1] = temp;
                    count++;
                }
            }
        }
        for(int k=0; k < n; k++){
            bw.write(nums[k]+"\n");
        }
        bw.flush();
    }
}
