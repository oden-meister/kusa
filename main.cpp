#include <opencv2/opencv.hpp>
#include <bits/stdc++.h>

cv::Mat faceFind(cv::Mat &image,std::string &cascade_file){
    cv::CascadeClassifier cascade;
    cascade.load(cascade_file);

    std::vector<cv::Rect> faces;
    cascade.detectMultiScale(image, faces, 1.1,3,0,cv::Size(20,20));
    std::cout << "Faces " << faces.size() << std::endl;

    for (int i = 0; i < faces.size(); i++){
        rectangle(image, cv::Point(faces[i].x,faces[i].y),cv::Point(faces[i].x + faces[i].width,faces[i].y + faces[i].height),cv::Scalar(0,200,0),3,CV_AA);
    }
    return image;
}

int main(){
    cv::Mat image = cv::imread("/home/megane/Downloads/sample.jpg",cv::IMREAD_COLOR);
    if(image.empty()){
        std::cout << "Image file isn't found." << std::endl;
        return 0;
    }
    std::string filename = "haarcascade_frontalface_default.xml";
    cv::Mat detectFaceImage = faceFind(image, filename);
    cv::imshow("detect face",detectFaceImage);
    cv::waitKey(0);

    return 0;
}
