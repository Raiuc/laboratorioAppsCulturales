#pragma once

#include "ofMain.h"
#include "ofxFaceTracker.h"

class ofApp : public ofBaseApp {
public:
	void setup();
	void update();
	void draw();
	void keyPressed(int key);
    void audioIn(float * input, int bufferSize, int nChannels);

	ofVideoGrabber cam;
	ofxFaceTracker tracker;
	ExpressionClassifier classifier;
    
    
    // Audio
    vector <float> left;
    vector <float> right;
    
    int 	bufferCounter;
    int 	drawCounter;
    
    float smoothedVol;
    float scaledVol;
    
    ofSoundStream soundStream;
    ofTrueTypeFont fuente;
    
    ofImage ojoI, ojoD;
    ofImage nariz;
    ofImage boca;
    ofImage cuernos;
    ofImage cuerpo;

    
};
