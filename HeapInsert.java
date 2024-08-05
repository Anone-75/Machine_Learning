
import java.util.Scanner;
public class MaxHeap {
   
int size = 10 ;
int  Elements  [] = new int [size];
int n = 9;
    // public void size(int a){
    //     this.size = a;
    //     int Elements [] = new int[size];
            
    // }
    public void Insert(){
        Scanner sc = new Scanner(System.in);
        for (int i=0; i<size ; i++ ){
            Elements[i] = sc.nextInt();
        }
        sc.close();
        HeapInsert(Elements, n);
    }

        public static void HeapInsert(int [] Elements, int n ){
            int i ,j;
                int item;
                j = n;
                i = n / 2;
                item = Elements[n];

                while((i<0) && (Elements[i] < item)){
                    Elements[j] = Elements[i];
                    j = i;
                    i = i / 2;

                }
                Elements[j]= item;
        }
   
    public void Display(){
        System.out.println("Elements in array :");
        for (int i = 0; i<size ; i++){
            System.out.print(Elements[i] + "\t");
        }
    }
    public static void main(String[] args) {
        MaxHeap heap = new MaxHeap();
        //heap.size(5);
        heap.Insert();
        heap.Display();
        
        
      
    }
}
