package boj.step;

import java.util.Scanner;

public class Step3052 {
	
	//단계별로 풀어보기 - 배열
	//3052번. 나머지
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int[] arr = new int[10];
		int result = 0;
		
		for(int i = 0; i < arr.length; i++) {
			arr[i] = sc.nextInt();
			arr[i] %= 42;
		}
		
		for(int i = 0; i < arr.length; i++) {
			int count = 0;
			for(int j = i + 1; j < arr.length; j++) {
				if(arr[i] == arr[j]) { // 값이 같으면
					count++;
				}
			}
			if(count == 0) {	//값이 다르면
				result++;
			}
			
		}
		
		System.out.println(result);
	}

}
