package boj.step.string;

import java.util.Scanner;

public class Step5622 {

	//문자열 8단계 - 5622번 다이얼 
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String str = sc.next();	//할머니가 입력한 단어
		int time = 0;			//전화 거는데 걸리는 최소 시간
		
		for(int i = 0; i < str.length(); i++) {
			switch (str.charAt(i)) {
			case 'A': case 'B': case 'C':
				time += 3;
				break;
			case 'D': case 'E': case 'F':
				time += 4;
				break;
			case 'G': case 'H': case 'I':
				time += 5;
				break;
			case 'J': case 'K': case 'L':
				time += 6;
				break;
			case 'M': case 'N': case 'O':
				time += 7;
				break;
			case 'P': case 'Q': case 'R': case 'S':
				time += 8;
				break;
			case 'T': case 'U': case 'V':
				time += 9;
				break;
			case 'W': case 'X': case 'Y': case 'Z':
				time += 10;
				break;
			}
			
		}
		
		System.out.println(time);
	}

}
