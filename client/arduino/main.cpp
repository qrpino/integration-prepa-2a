/* Stern ADAI 2A Final Project, © Team3 - All rights reserved. */
/* Intended to be used on an Arduino UNO board. */
#include <Arduino.h>
// To get this code compiling correctly, you will need to download the following libraries :
// - ArduinoJson
// - Chrono
// - Servo
// These libraries are available at PlatformIo's Libraries section.
#include <ArduinoJson.hpp>
#include <Chrono.h>
#include <Servo.h>

#define NB_MOTORS 6

// Declare an ArdunoJson object which can store up to 512 bytes of data.
// A dire pendant l'oral : Je dois allouer beaucoup d'espace pour la suite de points
// Avec 512 octets alloués en ArduinoJson, ma limite de points est de 8.
// Elle était de 3 à 256 octets, l'Arduino n'a que 2048 octets.
ArduinoJson::StaticJsonDocument<512> json;
// Declare Chrono instance which will be used to get a time based timer, to send regularly the motors values.
Chrono dt;
// Declare array of Servo pointers, and initialize their instance.
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
        //motors[0].write(json["motor"][0].as<int>());
        for (size_t i = 0; i < NB_MOTORS; i++)
        {
          // Since C++ is a strongly typed language, and ArduinoJson is dynamically typed, we need to cast the values
          // corresponding.
          motors[i].write(json["motors"][i].as<int>()); 
        }
      }
      // Run the positions sequence.
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
      /*
      else if(json.containsKey("arc-circle"))
      {
        Serial.write("Not Handling arc-circle at this moment.");
      }
    }
  }
  */
  // If 2 seconds have passed since the Chrono variable initialization, let's reset the serial buffer, send the motors 
  // values to the serial port and finally restart the Chrono variable.
  }
  else if(dt.hasPassed(2000))
  {
    String values = "{'motors':[";
    for (size_t i = 0; i < NB_MOTORS; i++)
    {
      i < NB_MOTORS - 1 ? values += String(String(motors[i].read()) + String(", ")) : values += String(String(motors[i].read()) + String("]}"));
    }
    Serial.flush();
    Serial.write(values.c_str());
    dt.restart();
  }
  /*
  else
  {
    json.clear();
  }
  */
}}