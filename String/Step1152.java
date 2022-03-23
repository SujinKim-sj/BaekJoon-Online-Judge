package boj.step.string;

import java.util.Scanner;

public class Step1152 {

	//문자열 6단계 - 1152번 단어의 개수
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String str = sc.nextLine().trim();		//앞뒤 공백 제거
		
		if(str.isEmpty()) {
			System.out.println(0);
		} else {
			//공백을 기준으로 문자열 나누기
			System.out.println(str.split(" ").length);		//단어의 개수 출력
		}
	}

}
