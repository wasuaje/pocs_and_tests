// reading a text file
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main () {
  string line;
  string str2;
  ifstream myfile ("pruebalog.log");
  if (myfile.is_open())
  {
    while ( myfile.good() )
    {
      getline (myfile,line);
      std::string str2 = line.substr (1,12); 
      cout << str2 << endl;
    }
    myfile.close();
  }

  else cout << "Unable to open file"; 

  return 0;
}
