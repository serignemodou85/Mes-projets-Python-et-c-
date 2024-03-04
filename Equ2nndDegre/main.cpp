#include<iostream>
#include<cmath>
using namespace std;

int main()
{
   float a,b,c,delta;
    cout << "veuiller saisir les coeff a, b et c : " << endl;
    cin>>a>>b>>c;
    if (a==0){
        if (b==0){
            if (c==0)
                cout<<"S=R";
            else
                cout<<"pas de solution";
        }else
            cout<<"x= "<<-c/b<<endl;
        }
    else{
        delta=b*b-4*a*c;
        if (delta>0){
            cout<<"x1= "<<(-b-sqrt(delta))/(2*a);
            cout<<"x2= "<<(-b+sqrt(delta))/(2*a);
        }else{
            if(delta==0)
                cout<<"x0= "<<-b/(2*a);
            else
                cout<<"pas de solution";
        }
    }
return 0;
}
