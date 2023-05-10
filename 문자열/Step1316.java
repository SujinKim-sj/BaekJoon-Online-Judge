package boj.step.string;

import java.util.Scanner;

public class Step1316 {

	// 문자열 10단계 - 그룹 단어 체커
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();		//그룹단어 입력 개수
		int count = num;			//최종 그룹단어의 개수 출력
		
		for(int i = 0; i < num; i++) {
			
			String word = sc.next();
			boolean[] arr = new boolean[26];
			
			for(int j = 0; j < word.length(); j++) {
				
				if(arr[word.charAt(j) - 'a'] == false) {
					arr[word.charAt(j) - 'a'] = true;
					
				} else if(word.charAt(j) != word.charAt(j - 1)){
					//알파벳이 arr에 있는데 앞단어와 같지 않으면 그룹단어가 아님
					count--;
					break;
				}
			}
		}
		
		System.out.println(count);
	}

}
