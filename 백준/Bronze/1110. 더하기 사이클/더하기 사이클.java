import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		int result = num;
		int cycle = 0;
		
		while(true){
			int a = result/10, b = result%10;
			result = b * 10 + (a + b)%10;
			cycle++;
			if(result == num)
				break;
		}
		System.out.println(cycle);
		sc.close();
	}
}
