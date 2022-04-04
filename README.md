# TicTacToe
package rockpaperscissorsgame;

import java.util.Scanner;
import java.util.Random;

public class Main {
	private static char[][] TicTacToeGrid= {{'_','|','_','|','_'},
											{'_','|','_','|','_'},
											{' ','|',' ','|',' '}};
	
	private static int player;
	
	
	public static void main(String[] args) {
		
		    printGrid(TicTacToeGrid);
		    boolean gameOver = gameCondition();

		    while(!gameOver) {
		    		playerMove();
		    		gameOver = gameCondition();
		    	if(gameOver) {
		    		break;
		    	}
		    		computerMove();
		    		gameOver = gameCondition();
		    		
		    }
		 }
		    	



public static void printGrid(char[][] TicTacToeGrid) {
	for(char[] row: TicTacToeGrid) {
		for(char c : row){
			System.out.print(c);
		}
        System.out.println();
  }
 }

public static void updateBoard(int position, int player) {
	
	char character;
	
	if(player == 1) {
		character = 'X';
	}else {
		character = 'O';
  }
	
	
	
	switch (position) {
	
		case 1: 
			TicTacToeGrid[0][0] = character;
			printGrid(TicTacToeGrid);
			break;
		case 2: 
			TicTacToeGrid[0][2] = character;
			printGrid(TicTacToeGrid);
			break;
		case 3: 
			TicTacToeGrid[0][4] = character;
			printGrid(TicTacToeGrid);
			break;
		case 4: 
			TicTacToeGrid[1][0] = character;
			printGrid(TicTacToeGrid);
			break;
		case 5: 
			TicTacToeGrid[1][2] = character;
			printGrid(TicTacToeGrid);
			break;
		case 6: 
			TicTacToeGrid[1][4] = character;
			printGrid(TicTacToeGrid);
			break;
		case 7: 
			TicTacToeGrid[2][0] = character;
			printGrid(TicTacToeGrid);
			break;
		case 8: 
			TicTacToeGrid[2][2] = character;
			printGrid(TicTacToeGrid);
			break;
		case 9: 
			TicTacToeGrid[2][4] = character;
			printGrid(TicTacToeGrid);
			break;
		default:
			break;
  }
 }


public static void playerMove() {
	player = 1;
	System.out.println("Please enter a number from 1-9.");

	Scanner scan = new Scanner(System.in);
	int move = scan.nextInt();

	
	boolean result = isValidMove(move);
	while(!result) {
//		while space has a x or an o in it 
		System.out.println("Please enter a correct value."); 
		move = scan.nextInt();
		result = isValidMove(move);
	}
		updateBoard(move, player);
 }

public static boolean isValidMove(int move) {
		switch(move) {
		case 1:
			if(TicTacToeGrid[0][0] == '_') {
				return true;
			}else {
				return false;
			}
//	 false: space has a x or o in it
//	 true: space has a "_" or a " "
		case 2:
			if(TicTacToeGrid[0][2] == '_') {
				return true;
			}else {
				return false;
			}
			
		case 3:
			if(TicTacToeGrid[0][4] == '_') {
				return true;
			}else {
				return false;
			}
			
		case 4:
			if(TicTacToeGrid[1][0] == '_') {
				return true;
			}else {
				return false;
			}
		case 5:
			if(TicTacToeGrid[1][2] == '_') {
				return true;
			}else {
				return false;
			}
		case 6:
			if(TicTacToeGrid[1][4] == '_') {
				return true;
			}else {
				return false;
			}
			
		case 7:
			if(TicTacToeGrid[2][0] == ' ') {
				return true;
			}else {
				return false;
			}
			
		case 8:
			if(TicTacToeGrid[2][2] == ' ') {
				return true;
			}else {
				return false;
			}
			
		case 9:
			if(TicTacToeGrid[2][4] == ' ') {
				return true;
			}else {
				return false;
			}
		default:
			return false;
			
		}
	
	}


public static void computerMove() {
	Random rand = new Random(); 
	int max = rand.nextInt(10);
	player = 2;
	
	int move = max;
	boolean result = isValidMove(move);
	while(!result) {
		move = rand.nextInt(10);
		result = isValidMove(move);
	}
	updateBoard(move, player);
}


public static boolean gameCondition() {
// Horizontal wins 
	if(TicTacToeGrid[0][0] == 'X' && TicTacToeGrid[0][2] == 'X' && TicTacToeGrid[0][4] == 'X') {
		System.out.println("Player wins!");
		return true;
	}
	
	if(TicTacToeGrid[0][0] == 'O' && TicTacToeGrid[0][2] == 'O' && TicTacToeGrid[0][4] == 'O') {
		System.out.println("Computer wins!");
		return true;
	}
	
	if(TicTacToeGrid[1][0] == 'X' && TicTacToeGrid[1][2] == 'X' && TicTacToeGrid[1][4] == 'X') {
		System.out.println("Player wins!");
		return true;
	}
	
	if(TicTacToeGrid[1][0] == 'O' && TicTacToeGrid[1][2] == 'O' && TicTacToeGrid[1][4] == 'O') {
		System.out.println("Computer wins!");
		return true;
	}

	if(TicTacToeGrid[2][0] == 'X' && TicTacToeGrid[2][2] == 'X' && TicTacToeGrid[2][4] == 'X') {
		System.out.println("Player wins!");
		return true;
	}
	
	if(TicTacToeGrid[2][0] == 'O' && TicTacToeGrid[2][2] == 'O' && TicTacToeGrid[2][4] == 'O') {
		System.out.println("Computer wins!");
		return true;
	}

//	VERTICAL WINS
	if(TicTacToeGrid[0][0] == 'X' && TicTacToeGrid[1][0] == 'X' && TicTacToeGrid[2][0] == 'X') {
		System.out.println("Player wins!");
		return true;
	}
	if(TicTacToeGrid[0][0] == 'O' && TicTacToeGrid[1][0] == 'O' && TicTacToeGrid[2][0] == 'O') {
		System.out.println("Computer wins!");
		return true;
	}
//	vertical in index 1 COLUMN
	if(TicTacToeGrid[0][2] == 'O' && TicTacToeGrid[1][2] == 'O' &&  TicTacToeGrid[2][2] == 'O') {
		System.out.println("Computer wins!");
		return true;
	}
	if(TicTacToeGrid[0][2] == 'X' && TicTacToeGrid[1][2] == 'X' &&  TicTacToeGrid[2][2] == 'X') {
		System.out.println("Player wins!");
		return true;
	}
//	vertical in index 2 column
	if(TicTacToeGrid[0][4] == 'O' && TicTacToeGrid[1][4] == 'O' &&  TicTacToeGrid[2][4] == 'O') {
		System.out.println("Computer wins!");
		return true;
	}
	if(TicTacToeGrid[0][4] == 'X' && TicTacToeGrid[1][4] == 'X' &&  TicTacToeGrid[2][4] == 'X') {
		System.out.println("Player wins!");
		return true;
	}

//	DIAGONAL WINS
	if(TicTacToeGrid[0][0] == 'X' && TicTacToeGrid[1][2] == 'X' &&  TicTacToeGrid[2][4] == 'X') {
		System.out.println("Player wins!");
		return true;
	}
	
	if(TicTacToeGrid[0][0] == 'O' && TicTacToeGrid[1][2] == 'O' &&  TicTacToeGrid[2][4] == 'O') {
		System.out.println("Computer wins!");
		return true;
	}
	if(TicTacToeGrid[0][4] == 'O' && TicTacToeGrid[1][2] == 'O' &&  TicTacToeGrid[2][0] == 'O') {
		System.out.println("Computer wins!");
		return true;
	}
	if(TicTacToeGrid[0][4] == 'X' && TicTacToeGrid[1][2] == 'X' &&  TicTacToeGrid[2][0] == 'X') {
		System.out.println("Player wins!");
		return true;
	}
	if(TicTacToeGrid[0][0] != '_' && TicTacToeGrid[0][2] != '_' && TicTacToeGrid[0][4] != '_'
	   && TicTacToeGrid[1][0] != '_' && TicTacToeGrid[1][2] != '_' && TicTacToeGrid[1][4] != '_'
	   && TicTacToeGrid[2][0] != ' ' && TicTacToeGrid[2][2] != ' ' && TicTacToeGrid[2][4] != ' ') {
		System.out.println("Tied game!");
		return true;
	}
	return false;
 }
}
