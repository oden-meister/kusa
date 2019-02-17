#include "main.h"

cv::Mat faceFind(cv::Mat &image,std::string &cascade_file){
    cv::CascadeClassifier cascade;
    cascade.load(cascade_file);
    std::vector<cv::Rect> faces;
    cascade.detectMultiScale(image, faces, 1.1,3,0,cv::Size(20,20));
    std::cout << "Faces " << faces.size() << std::endl;
    countf+=faces.size();
    for (int i = 0; i < faces.size(); i++){
        rectangle(image, cv::Point(faces[i].x,faces[i].y),cv::Point(faces[i].x + faces[i].width,faces[i].y + faces[i].height),cv::Scalar(0,200,0),3,CV_AA);
    }
    return image;
}

int main(){
    //ここにループの回数を入力(負の数で無限)
    int time = -1,roop=0;
    //
    std::string bfrc;
    std::ifstream ifs(userdir+".kusarc");
    if(ifs.fail()){
        ifs.close();
        std::ofstream ofs(userdir+".kusarc");
        ofs<<"#\n#kusa\n#\n\n#Change 'X' to right number or character.\n\n";
        ofs<<"IP=XXX.XXX.XXX.XXX:XXXX\n";
        ofs<<"RASPNUMBER=X\n";
        ofs<<"TOKEN=XXXXX\n";
        ofs.close();
        std::cout<<"Check "<<userdir<<".kusarc"<<std::endl;
        exit(0);
    }
    else{
        while (std::getline(ifs,bfrc)) {
            if((bfrc[0]!='#')&&bfrc.empty()!=true){
                if(bfrc.find("IP=")==0){IP=bfrc.erase(0,3);std::cout<<"IP="<<IP<<std::endl;}
                if(bfrc.find("RASPNUMBER=")==0){RASPNUMBER=bfrc.erase(0,11);std::cout<<"RASPNUMBER="<<RASPNUMBER<<std::endl;}
                if(bfrc.find("TOKEN=")==0){TOKEN=bfrc.erase(0,6);std::cout<<"TOKEN="<<TOKEN<<std::endl;}
            }
        }
        ifs.close();
    }
    cv::VideoCapture cap(0);
    if(!cap.isOpened()){
        std::cout<<"CAN NOT OPEN CAMERA\n";
        cap = cv::VideoCapture();
        while(!cap.isOpened()){}
    }
    std::string cmd;
    int64 start=cv::getTickCount();
    int64 end;
    std::stringstream sout;
    for(int i = time;i != 0;i--){
        /*cv::Mat image = cv::imread("/home/megane/Downloads/sample.jpg",cv::IMREAD_COLOR);
        if(image.empty()){
            std::cout << "Image file isn't found." << std::endl;
            return 0;
        }*/
        //↓↓ここから
        cv::Mat frame;
        bool success = cap.read(frame);
        if(!success){
            std::cout<<"Can not read a frame from video stream."<<std::endl;
        }
        //↑↑ここまでを上のコメントアウト(/**/)の中と交換する(画像相手なら)あとframeを全部imageに変える
        std::time_t t =std::time(0);
        std::tm* now=std::localtime(&t);
        end=cv::getTickCount();
        double elapsedMsec=(end-start)*1000/cv::getTickFrequency();
        if(elapsedMsec>=1000){
            std::string filename = "haarcascade_frontalface_default.xml";
            cv::Mat detectFaceImage = faceFind(frame, filename);
            cv::imshow("detect face",detectFaceImage);
            start=cv::getTickCount();
            roop++;
        }
        if(roop==10){
            cmd="curl -X POST "+IP+"/api/SmileIs/ -d \"rasp="+RASPNUMBER+"\" -d \"smileic=";
            cmd+=std::to_string(countf);
            cmd+="\" -d \"pushed_dateI=";
            sout<<now->tm_year+1900<<"-"<<std::setfill('0')<<std::setw(2)<<now->tm_mon+1<<"-"<<std::setfill('0')<<std::setw(2)<<now->tm_mday<<"T"<<std::setfill('0')<<std::setw(2)<<now->tm_hour<<":"<<std::setfill('0')<<std::setw(2)<<now->tm_min<<":"<<std::setfill('0')<<std::setw(2)<<now->tm_sec;
            cmd+=sout.str();
            cmd+="\" -H \"Authorization: JWT "+TOKEN+"\"";
            std::cout<<cmd<<std::endl;
            system(cmd.c_str());
            std::cout<<std::endl;
            cmd.clear();
            sout.str("");
            sout.clear(std::stringstream::goodbit);
            roop=0;
            countf=0;
        }
    }
    std::cout << "Program is ended" << std::endl;
    return 0;
}
