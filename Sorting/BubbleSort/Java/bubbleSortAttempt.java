package Java;
import java.util.Scanner;

public class bubbleSortAttempt extends java.lang.Object {
    public static void main(String args[]){
        //Initialize variables
        int size = 0;
        Scanner in = new Scanner(System.in);

        //Get the array size. Can be passed in as first arg or entered by user
        if(args.length > 0){
            System.out.println("Received argument size of: " + args[0]);
            size = Integer.parseInt(args[0]);
        }
        else{
            System.out.println("Please enter the size of the array to be sorted. Then press enter.");
            size = in.nextInt();
        }

        //Instantiate an array of said size
        int[] unsortedArray = new int[size];

        //Fill array with elements. If by args, checks if user passed in sufficient arguments
        if(args.length == size+1){
            for(int i=1;i<=size;i++){
                unsortedArray[i-1] = Integer.parseInt(args[i]);
            }
        }
        else{
            boolean completed = false;
            while(!completed){
                System.out.println("Please enter the values for the array, sepereated by a space. Then press enter.");
                String input = in.nextLine();
                String[] inputs = input.split(" ");
                if(inputs.length != size){
                    System.out.println("The number of imputs is incorrect.");
                }
                else{
                    for(int i=0;i<size;i++){
                        unsortedArray[i] = Integer.parseInt(inputs[i]);
                    }
                    completed = true;
                }
            }
        }
        in.close();
        
        //Begin sorting algorithm
        boolean sorted = false;
        long startTime = System.nanoTime();
        //Sort the algorithm until value returned is true for sorted. O(1) time to check if boolean is true
        //HELP: Could use pointers to directly update sorted array instead of by updating variables
        while(!sorted){
            unsortedArray = bubbleSort(unsortedArray);
            sorted = sortCheck(unsortedArray);
        }
        long endTime   = System.nanoTime();
        long totalTime = endTime - startTime;

        //Print out array and time in seconds to run sorting algorithm
        System.out.println("Total Run Time in seconds: " + (float)totalTime/1000000000);
        for(int i : unsortedArray){
            System.out.print(i + " ");
        }
    }

    //O(n) run time for sorting algorithm. Runs through 1D array a single time and switches adjacent values
    public static int[] bubbleSort(int[] arrayToSort){
        for(int i=0;i<arrayToSort.length-1;i++){
            if(arrayToSort[i] > arrayToSort[i+1]){
                int temp = arrayToSort[i];
                arrayToSort[i] = arrayToSort[i+1];
                arrayToSort[i+1] = temp;
            }
        }
        return arrayToSort;
    }

    //O(n) run time for checking algorithm. Runs through 1D array with no backtracking (compare by temp value) to see if all values are sorted
    public static boolean sortCheck(int[] anArray){
        int prev = 0;
        for(int i : anArray){
            if(i < prev){
                return false;
            }
            else{
                prev = i;
            }
        }
        return true;
    }
}