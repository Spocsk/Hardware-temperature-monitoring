#include <LiquidCrystal.h>
#include <String.h>



LiquidCrystal lcd(8, 9, 4, 5, 6, 7);        

void setup() {
  
  lcd.begin(16, 2); 
  Serial.begin(9600);
}

void loop()
{
  lcd.setCursor(0,0);
  
  
    while(Serial.available()) {
      
         String in = Serial.readString();
         
         lcd.print("CPU ");
         lcd.setCursor(4,0);
         lcd.print(in.substring(0,2));
         
         lcd.setCursor(8,0);
         lcd.print("GPU ");
         lcd.setCursor(12,0);
         lcd.print(in.substring(2,4));


          lcd.setCursor(0,1);
          lcd.print("RAM ");
          lcd.setCursor(4,1);
          lcd.print(in.substring(5,9));
          lcd.setCursor(9,1);
          lcd.print("/");
          lcd.setCursor(11,1);
          lcd.print(in.substring(9));
          
          
    }   
}
