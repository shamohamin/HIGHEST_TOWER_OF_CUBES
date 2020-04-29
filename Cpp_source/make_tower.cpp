#include <iostream>
#include <vector>
#include <map>
#include <string>
using namespace std;

//side1 = down , side6 = up , side2 = right , side3 = left , side4 = back , side5 = front
struct cube {
    int wieght, side1, side2, side3, side4, side5, side6;
    cube(int wieght) : wieght(wieght) ,
            side1(1),side2(2), side3(3), side4(4), side5(5), side6(6) {};
};

bool compare(const cube p1 , const cube p2){
    return p1.wieght < p2.wieght ;
}

void permutation(vector<cube> &cubes);
void make_tower(vector<cube> cubes);
string set_hash(cube c);

int main(){
    vector<cube> cubes ;
    cube cube1(1);
    cube cube2(2);
    cube cube3(3);
    cubes.push_back(cube1);
    cubes.push_back(cube2);
    cubes.push_back(cube3);
    permutation(cubes) ;
    make_tower(cubes) ;
}

void permutation(vector<cube> &cubes){
    for(cube c : cubes){
        cube hold = c;

        swap(c.side1, c.side2);
        swap(c.side6, c.side3);
        hold = c ;
        cubes.push_back(hold) ;
        swap(c.side1, c.side2);
        swap(c.side6, c.side3);

        swap(c.side1, c.side3);
        swap(c.side6, c.side2);
        hold = c ;
        cubes.push_back(hold);
        swap(c.side1, c.side3);
        swap(c.side6, c.side2);

        swap(c.side1, c.side4);
        swap(c.side6, c.side5);
        hold = c ;
        cubes.push_back(hold);
        swap(c.side1, c.side4);
        swap(c.side6, c.side5);

        swap(c.side1, c.side5);
        swap(c.side6, c.side4);
        hold = c;
        cubes.push_back(hold);
        swap(c.side1, c.side5);
        swap(c.side6, c.side4);

        swap(c.side1, c.side6);
        hold = c;
        cubes.push_back(hold);
        swap(c.side1, c.side6);
    }
}

void make_tower(vector<cube> cubes){
    vector<vector<cube> > sol ;
    sort(cubes.begin(), cubes.end(), compare);

    for(cube c : cubes){
            cout << "[" << c.wieght << " " << c.side1 << " " << c.side2 << " " << c.side3 << " " <<  c.side4 << " " << c.side5 << " " << c.side6 << "] " ;
    }
    map<string, vector<cube> > memory ;

    for(int i = 0 ; i < cubes.size(); i++){
        cube up = cubes.at(i);
        vector<cube> holder ;
        holder.push_back(up);
        for(int j = i - 1  ; j >= 0; j--) {
            if(memory.find(set_hash(cubes.at(j))) == memory.end()){
                if( up.side1 == cubes.at(j).side6 &&
                    up.wieght > cubes.at(j).wieght
                    ){
                    holder.push_back(cubes.at(j)) ;
                    up = cubes.at(j) ;
                }
            }else{
                vector<cube> memoize = memory.find(set_hash(cubes.at(j)))->second ;
                cout << "hello" << endl ;
                //copy memoize array
                for(auto c : memoize){
                    if(c.wieght < up.wieght)
                        holder.push_back(c) , up = c ;
                }
                break ;
            }
        }
        memory[set_hash(holder[0])] = holder ;
        sol.push_back(holder) ;
    }

    for(vector<cube> s: sol){
        for(cube c : s){
            cout << "[" << c.wieght << " " << c.side1 << " " << c.side2 << " " << c.side3 << " "
                            <<  c.side4 << " " << c.side5 << " " << c.side6 << "] " ;
        }
        cout << endl ;
    }

    map<string, vector<cube> >::iterator itr ;

    for(itr = memory.begin(); itr != memory.end() ; itr++){
        cout << "code :" << itr->first << " " ;
        for(auto c : itr->second){
            cout << "[" << c.wieght << " " << c.side1 << " " << c.side2 << " " << c.side3 << " " <<  c.side4 << " " <<
                                                c.side5 << " " << c.side6 << "] " ;
        }
        cout << endl;
    }

}

string set_hash(cube c){
    string code = "" ;
    code += to_string(c.side1) ;
    code += to_string(c.side6) ;
    code += to_string(c.wieght) ;
    return code ;
}