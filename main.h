#ifndef MAIN_H
#define MAIN_H

#include <opencv2/opencv.hpp>
#include <iostream>
#include <vector>
#include <string>
#include<fstream>
#include <sstream>
#include <unistd.h>
#include <ctime>
#include<sys/stat.h>

extern int countf=0;//認識した顔の総数
extern std::string username=getenv("USER"),userdir="/home/"+username+"/";
extern std::string RASPNUMBER="";
extern std::string IP="";
extern std::string TOKEN="";

#endif // MAIN_H
