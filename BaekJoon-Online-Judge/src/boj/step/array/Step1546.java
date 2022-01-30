package boj.step.array;

import java.util.Scanner;

public class Step1546 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int num = sc.nextInt();			//과목 수
		int[] scores = new int[num];	//원래 점수
		double max = 0.0;				//최댓값
		
		for(int i = 0; i < scores.length; i++) {
			scores[i] = sc.nextInt();
			if(max < scores[i]) {
				max = scores[i];
			}
		}
		
		double total = 0.0;
		double avg = 0.0;
		
		//모든 점수를 점수/M*100 로 변경 후 합
		for(int i = 0; i < scores.length; i++) {
			total += scores[i] / max * 100;
		}
		
		avg = total / num;	//변경 후 평균 점수
		System.out.println(avg);
	}

}
