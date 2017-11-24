#include "ofApp.h"

using namespace ofxCv;
using namespace cv;

//--------------------------------------------------------------
void ofApp::setup() {
	ofSetVerticalSync(true);
    cam.setDeviceID(0);
	cam.initGrabber(640, 480);
	
	tracker.setup();
	tracker.setRescale(.5);
    
    fuente.load("fonts/verdana.ttf", 6);
    
    // Audio
    soundStream.printDeviceList();
    soundStream.setDeviceID(0);
    int bufferSize = 256;

    left.assign(bufferSize, 0.0);
    right.assign(bufferSize, 0.0);
    
    bufferCounter	= 0;
    drawCounter		= 0;
    smoothedVol     = 0.0;
    scaledVol		= 0.0;

    soundStream.setup(this, 0, 2, 44100, bufferSize, 4);
    
    
    
    ojoI.load("png/ojoI.png");
    ojoD.load("png/ojoD.png");

    boca.load("png/boca.png");




}

//--------------------------------------------------------------
void ofApp::update() {
	cam.update();
	if(cam.isFrameNew()) {
		if(tracker.update(toCv(cam))) {
			classifier.classify(tracker);
		}		
	}
    
    scaledVol = ofMap(smoothedVol, 0.0, 0.05, 10, 100, true);

}

//--------------------------------------------------------------
void ofApp::draw() {
	ofSetColor(255);
	cam.draw(0, 0);
	//tracker.draw();
    ofVec2f v = tracker.getPosition();
    vector<ofVec2f> puntos = tracker.getImagePoints();
    
    for(int i = 0; i < puntos.size(); i++){
        ofDrawCircle(puntos[i].x, puntos[i].y, 5);
        fuente.drawString(ofToString(i), puntos[i].x, puntos[i].y - 5);
    }
    
    ofPushStyle();
    
        //ofSetColor(255, 0, 0);
        //ofDrawCircle(v.x, v.y, scaledVol);
        if (puntos.size()) {
            float angle = puntos[0].angle(puntos[16]);
            
            // Dibujar ojo izquierdo
            ofPushMatrix();
                ofTranslate(puntos[17].x, puntos[17].y);
                //ofRotateZ(angle);
                ojoI.draw(0, 0,
                          abs(puntos[17].x - puntos[21].x),
                          abs(puntos[17].y - puntos[41].y));
            
            ofPopMatrix();

            // Dibujar ojo derecho
            ofPushMatrix();
                ofTranslate(puntos[22].x, puntos[22].y);
                //ofRotateZ(angle);
                ojoD.draw(0, 0,
                          abs(puntos[22].x - puntos[26].x),
                          abs(puntos[22].y - puntos[47].y));
            
            ofPopMatrix();
            
            // Dibujar boca
            ofPushMatrix();
            
                ofTranslate(puntos[48].x, puntos[48].y);
                //ofRotateZ(angle);
                boca.draw(0, 0,
                          abs(puntos[54].x - puntos[48].x),
                          abs(puntos[50].y - puntos[57].y));

            ofPopMatrix();
            cout << angle << " \n";
        }

    ofPopStyle();
    
    
	int w = 100, h = 12;
    
	ofPushStyle();
        ofPushMatrix();
            ofTranslate(5, 10);
            int n = classifier.size();
            int primary = classifier.getPrimaryExpression();
            for(int i = 0; i < n; i++){
                ofSetColor(i == primary ? ofColor::red : ofColor::black);
                ofDrawRectangle(0, 0, w * classifier.getProbability(i) + .5, h);
                ofSetColor(255);
                ofDrawBitmapString(classifier.getDescription(i), 5, 9);
                ofTranslate(0, h + 5);
            }
            ofPopMatrix();
    ofPopStyle();
	
	ofDrawBitmapString(ofToString((int) ofGetFrameRate()), ofGetWidth() - 20, ofGetHeight() - 10);
	ofDrawBitmapStringHighlight(
		string() +
		"r - reset\n" +
		"e - add expression\n" +
		"a - add sample\n" +
		"s - save expressions\n"
		"l - load expressions",
		14, ofGetHeight() - 7 * 12);
}

//--------------------------------------------------------------
void ofApp::audioIn(float * input, int bufferSize, int nChannels){
    
    float curVol = 0.0;
    
    // samples are "interleaved"
    int numCounted = 0;
    
    //lets go through each sample and calculate the root mean square which is a rough way to calculate volume
    for (int i = 0; i < bufferSize; i++){
        left[i]		= input[i*2]*0.5;
        right[i]	= input[i*2+1]*0.5;
        
        curVol += left[i] * left[i];
        curVol += right[i] * right[i];
        numCounted+=2;
    }
    
    //this is how we get the mean of rms :)
    curVol /= (float)numCounted;
    
    // this is how we get the root of rms :)
    curVol = sqrt( curVol );
    
    smoothedVol *= 0.93;
    smoothedVol += 0.07 * curVol;
    
    bufferCounter++;
    
}


//--------------------------------------------------------------
void ofApp::keyPressed(int key) {
	if(key == 'r') {
		tracker.reset();
		classifier.reset();
	}
	if(key == 'e') {
		classifier.addExpression();
	}
	if(key == 'a') {
		classifier.addSample(tracker);
	}
	if(key == 's') {
		classifier.save("expressions");
	}
	if(key == 'l') {
		classifier.load("expressions");
	}
}
