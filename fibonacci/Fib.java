import java.util.Scanner;

public class Fib {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        System.out.println("Please specify fibonacci number: ");
        Scanner sc = new Scanner(System.in);
        try {
            int fibNumber = Integer.parseInt(sc.next());
            System.out.println("Please specify operation to perform: 1 - get value, 2 - get last digit: ");
            int optNumber = Integer.parseInt(sc.next());
            if(optNumber != 1 && optNumber != 2) {
                throw new Exception("Unavailable option");
            }
            
            int result = -1;
            if(optNumber == 1){
                result = fib(fibNumber);
            }
            if(optNumber == 2){
                result = fib_last_digit(fibNumber);
            }
            System.out.println("Result: " + result);
        } catch(NumberFormatException ex) {
            System.out.println("That's not an int!");
        } catch(Exception ex){
            System.out.println(ex.getMessage());
        }
    }

    public static int fib(int n) {
        if(n <= 1) {
            return n;
        } else {
            int[] F = new int[n+1];
            F[0] = 0;
            F[1] = 1;
            for(int i = 2; i <= n; i++){
                F[i] = F[i-1] + F[i-2];
            }
            return F[n];
        }
    }
    
     public static int fib_last_digit(int n) {
        if(n <= 1) {
            return n;
        } else {
            int[] F = new int[n+1];
            F[0] = 0;
            F[1] = 1;
            for(int i = 2; i <= n; i++){
                F[i] = (F[i-1] + F[i-2])%10;
            }
            return F[n];
        }
    }   
    
}
