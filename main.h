#ifndef MAIN_H
#define MAIN_H

#include <opencv2/opencv.hpp>
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <unistd.h>
#include <ctime>

extern int countf=0;//認識した顔の総数
extern std::string RASPNUMBER="5";//ラズベリーパイの個体番号
extern std::string IP="http://127.0.0.1:8000";//IPアドレス
extern std::string TOKEN="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Im1pbmZhb3gzIiwiZXhwIjoxNTUwMTQyODI2LCJlbWFpbCI6InNwZGxjaTMwQGdtYWlsLmNvbSJ9.i7Ogj1sjWMdL3Y1SHIQ6aLW3Hnv2gqu1Mx6ybnfPYd4";
//↑トークン
//curl http://XXX.XX.XX.XXX:XXXX/api-auth/ -d "username=XXXXXXX&password=XXXXXXXX"
//で取得できる

#endif // MAIN_H
