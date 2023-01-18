//Sort first then use two pointer techniques


#include <iostream>
#include <vector>
#include <algorithm>



using namespace std;

vector<int> twoSum(vector<int>& nums, int target) 
    {
        cout << "function call " << endl;
    }




int main()
{

    vector<int> usin = {15,7,2,11};
    int target = 9;
    
    sort(usin.begin(),usin.end());

    for (auto i = usin.begin(); i != usin.end(); ++i)
    {
        cout << *i << " ";
    }

    cout << endl;

    int leftPointer = usin[0];
    int rightPointer = usin[usin.size()-1];
    cout << leftPointer << " " << rightPointer << endl;
    int sum = leftPointer + rightPointer;

    vector<int>::iterator it;

    

    return 0;

    // while (sum!=target)
    // {
    //     if (sum > target)
    //     {
    //         return 0;
    //     }
    //     else if (sum < target)
    //     {
    //         return 0;
    //     }
    // }

}



