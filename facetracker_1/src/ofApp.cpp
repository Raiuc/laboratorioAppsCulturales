#include "ofApp.h"

using namespace ofxCv;
using namespace cv;

//--------------------------------------------------------------
void ofApp::setup() {
	ofSetVerticalSync(true);
    ofSetFrameRate(60);
    cam.listDevices();
    cam.setDeviceID(0);
	cam.initGrabber(640, 480);
	
	tracker.setup();
	tracker.setRescale(.5);
    
    fuente.load("fonts/verdana.ttf", 6);
    
    // Audio
    //soundStream.printDeviceList();
    //soundStream.setDeviceID(3);
    int bufferSize = 256;

    left.assign(bufferSize, 0.0);
    right.assign(bufferSize, 0.0);
    
    scene           = 0;
    bufferCounter	= 0;
    drawCounter		= 0;
    contador        = 0;
    offset[0].x     = 300;
    offset[0].y     = 350;

    offset[1].x     = 300;
    offset[1].y     = 350;
    
    smoothedVol     = 0.0;
    scaledVol		= 0.0;
    listening       = TRUE;
    

    soundStream.setup(this, 0, 2, 44100, bufferSize, 4);
    
    
    
    ojoI.load("png/ojoI.png");
    ojoD.load("png/ojoD.png");

    boca.load("png/boca.png");


}

//--------------------------------------------------------------
void ofApp::update() {
    
    contador++;
    if(contador > 60){
        contador = 0;
        listening = TRUE;
    }
    
    
	cam.update();
	if(cam.isFrameNew()) {
		if(tracker.update(toCv(cam))) {
			classifier.classify(tracker);
		}		
	}
    
    scaledVol = ofMap(smoothedVol, 0.0, 0.05, 0, 1, true);
    //cout << scaledVol << " ";
}

//--------------------------------------------------------------
void ofApp::draw() {

    ofSetColor(255);
    cam.draw(0, 0);
    ofPushStyle();

        //tracker.draw();
        ofVec2f v = tracker.getPosition();
        vector<ofVec2f> puntos = tracker.getImagePoints();
        
        for(int i = 0; i < puntos.size(); i++){
            ofDrawCircle(puntos[i].x + 640, puntos[i].y, 5);
            fuente.drawString(ofToString(i), puntos[i].x + 640, puntos[i].y - 5);
        }
    
        if (puntos.size()) {
            float angle = puntos[0].angle(puntos[16]);
            
            // Dibujar nariz
            ofPushStyle();
                ofSetColor(255, 0, 0);
                ofDrawCircle(v.x + offset[0].x, v.y + offset[0].y, 20 + scaledVol * 100);
            ofPopStyle();
            
            
            // Dibujar ojo izquierdo
            ofPushMatrix();
                ofTranslate(puntos[17].x, puntos[17].y);
                //ofRotateZ(angle);
                ojoI.draw(offset[1].x, offset[1].y,
                          abs(puntos[17].x - puntos[21].x) * (1 + scaledVol),
                          abs(puntos[17].y - puntos[41].y) * (1 + scaledVol));
            
            ofPopMatrix();

            // Dibujar ojo derecho
            ofPushMatrix();
                ofTranslate(puntos[22].x, puntos[22].y);
                //ofRotateZ(angle);
                ojoD.draw(offset[1].x, offset[1].y,
                          abs(puntos[22].x - puntos[26].x) * (1 + scaledVol),
                          abs(puntos[22].y - puntos[47].y) * (1 + scaledVol));
            
            ofPopMatrix();
            
            // Dibujar boca
            ofPushMatrix();
            
                ofTranslate(puntos[48].x, puntos[48].y);
                //ofRotateZ(angle);
                boca.draw(offset[1].x, offset[1].y,
                          abs(puntos[54].x - puntos[48].x) * (1 + scaledVol),
                          abs(puntos[50].y - puntos[57].y) * (1 + scaledVol));

            ofPopMatrix();
            //cout << angle << " \n";
        }

    ofPopStyle();
    
    
	int w = 100, h = 12;
    
	ofPushStyle();
        ofPushMatrix();
            ofTranslate(5, 10);
            int n = classifier.size();
            int primary = classifier.getPrimaryExpression();
            if (n && primary == 0 && listening) {
                ofSystem("/Users/pulso8/instrucciones.sh");
                listening = FALSE;
            }
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
		"e - agregar expresi\u00F3n\n" +
		"a - agregar muestra\n" +
		"s - guardar expresiones\n"
		"l - cargar expresiones",
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


