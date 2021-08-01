#include <iostream>
using namespace std;

struct Pair
{
    int max;
    int min;
};

//returns struc pair : function getMinMax
struct Pair getMinMax(int arr[],int n){
    struct Pair minmax;
    int i;

    //if there is only one element
    if(n==1){
        minmax.max = arr[0];
        minmax.min = arr[0];
    }
     if(arr[0]>arr[1]){
         minmax.max = arr[0];
         minmax.min = arr[1];
     }else{
         minmax.max = arr[1];
         minmax.min = arr[0];
     }

     for(i=2;i<n;i++){
         if(arr[i]<minmax.min)
            minmax.min = arr[i];

        else if (arr[i] > minmax.max)
         minmax.max = arr[i];
     }
     return minmax;
}

//Driver code 
int main(){
    int arr[] = {1000,11,446,789,2342,-2322,-2343};
    int arr_size = 7;

    struct Pair minmax = getMinMax(arr,arr_size);
    cout << "Minimum elemet is " << minmax.min << endl;
    cout << "Maximum element is "<< minmax.max;
    return 0;
}