/* Stern ADAI 2A Final Project, © Team3 - All rights reserved. */
/* Intended to be used on an Arduino UNO board. */
#include <Arduino.h>

// To get this code compiling correctly, you will need to download the following libraries :
// - ArduinoJson
// - Chrono
// - Servo
// These libraries are available at PlatformIo's Libraries section.
#include "../.pio/libdeps/uno/ArduinoJson/ArduinoJson.h"
// #include <ArduinoJson.hpp>
#include "../.pio/libdeps/uno/Chrono/Chrono.h"
//#include <Chrono.h>
#include "../.pio/libdeps/uno/Servo/src/Servo.h"
//#include <Servo.h>

#define NB_MOTORS 6

// Declare an ArdunoJson object which can store up to 512 bytes of data.
// Remember that the Arduino that we're using has only 2048 bytes of RAM, you have to find the right balance.
ArduinoJson::StaticJsonDocument<512> json;
// Declare Chrono instance which will be used to get a time based timer, to send regularly the motors values.
Chrono dt;
// Declare array of Servo, and initialize their instance.
Servo motors[6] = {Servo()};
// Declare a pointer to a Servo object, which will be further.
Servo* currentMotor = nullptr;

Servo base;

void setup() {
  // Set the baud rate to 9600.
  Serial.begin(9600);
  // Power up the signal pins for the motors.
  motors[0].attach(11);
  motors[1].attach(10);
  motors[2].attach(9);
  motors[3].attach(6);
  motors[4].attach(5);
  motors[5].attach(3);
}

void loop() {
  // If serial data size is greater than 0.
  if(Serial.available() > 0)
  {
    String message = Serial.readString();
    // Check if the readed serial data syntax is a correct JSON representation.
    ArduinoJson::DeserializationError error = ArduinoJson::deserializeJson(json, message);
    // If JSON representation is correct, we can proceed to the instruction received.
    if(!error)
    {
      // If we have "motors" keyword, loop on the array of the pointers to the motors and set their value accordingly
      // to the received message.
      if(json.containsKey("motors"))
      { 
        for (size_t i = 0; i < NB_MOTORS; i++)
        {
          // Since C++ is a strongly typed language, and ArduinoJson is dynamically typed, we need to cast the values
          // corresponding.
          motors[i].write(json["motors"][i].as<int>()); 
        }
      }
      // Run the registered positions sequence on the client.
      else if(json.containsKey("points-sequence"))
      {
        for(size_t i = 0; i < json["points-sequence"].size(); i++)
        {
          for(int j = 0; j < NB_MOTORS; j++)
          {
            motors[j].write(json["points-sequence"][i][j].as<int>());
          }
          delay(1500);
        }
      }
  // If 2 seconds have passed since the Chrono variable initialization, let's reset the serial buffer, send the motors 
  // values to the serial port and finally restart the Chrono variable.
  }
  else if(dt.hasPassed(2000))
  {
    // Let's create the message that we want to send to the serial port.
    String values = "{'motors':[";
    for (size_t i = 0; i < NB_MOTORS; i++)
    {
      i < NB_MOTORS - 1 ? values += String(String(motors[i].read()) + String(", ")) : values += String(String(motors[i].read()) + String("]}"));
    }
    Serial.flush();
    Serial.write(values.c_str());
    dt.restart();
  }
}}