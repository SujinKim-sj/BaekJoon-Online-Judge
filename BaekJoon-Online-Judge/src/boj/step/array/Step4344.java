package boj.step.array;

import java.util.Scanner;

public class Step4344 {
	
	//배열 7단계. 4344번 평균은 넘겠지
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int num = sc.nextInt();		//테스트 케이스의 개수
		int[] arr;
		
		for(int i = 0; i < num; i++) {
			
			//각 테스트 케이스마다 학생의 수 입력
			int stuNum = sc.nextInt();
			arr = new int[stuNum];
			
			double total = 0;
			
			for(int j = 0; j < stuNum; j++) {
				arr[j] = sc.nextInt();	
				total += arr[j];
			}
			
			double avg = total / stuNum;
			
			int count = 0;			//평균 넘는 학생들의 수
			for(int k = 0; k < stuNum; k++) {
				if(arr[k] > avg) {
					count++;
				}
			}
			
			//평균 넘는 학생들의 비율 최종 출력
			float result = (float)count / stuNum * 100;		
			System.out.println(String.format("%.3f", result) + "%");
		}
		
		
		
	}

}
