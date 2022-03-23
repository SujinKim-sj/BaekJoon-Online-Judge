package boj.step.array;

import java.util.Scanner;

public class Step8958 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int num = sc.nextInt();					// 테스트 케이스의 개수
		String[] result = new String[num];		// 테스트 케이스를 담을 배열
		
		for(int i = 0; i < result.length; i++) {
			result[i] = sc.next();
		}
		
		for(int i = 0; i < result.length; i++) {
			int score = 0;							
			int total = 0;							// 테스트 케이스의 총점

			for(int j = 0; j < result[i].length(); j++) {
				if(result[i].charAt(j) == 'O') {
					score++;						// O이면 1씩 증가
				} else {
					score = 0;						// X이면 다시 score 초기화
				}
				total += score;						
			}
			System.out.println(total);
		}
		
	}

}
