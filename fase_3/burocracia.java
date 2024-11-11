// pontuação: 28/100

import java.util.Scanner;

public class burocracia {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		
		int[] v = new int[n];
		
		for (int i = 1; i < n; i++) {
			v[i] = sc.nextInt();
		}
		
		int numop = sc.nextInt();
		
		boolean aux = false;
		
		String saida = "";
		
		for(int i = 0; i < numop; i++) {
			int op = sc.nextInt();
			
			int nobre = sc.nextInt();
				
			int niveis = 0;
			
			if(op == 1) {
				niveis = sc.nextInt();
				
				int f = v[nobre-1];
				
				for(int j = 0; j < niveis-1; j++) {
					f = v[f-1];
				}
				
				if(aux == true)
					saida+=String.format("\n%d", f);
				else
					saida+=String.format("%d", f);
				aux = true;
			}
			
			if(op == 2){
				for (int j = nobre-1; j < n; j++) {
					if(v[j] == nobre) {
						for(int k = v[j]; k < n; k++) {
							if (v[k] == j+1) {
								v[k] = nobre;
							}
						}
					}
				}
			}
		}
		
		System.out.println(saida);
		
		sc.close();
	}

}
