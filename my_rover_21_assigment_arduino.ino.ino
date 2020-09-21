
int MD1, MS1, MD2, MS2, MD3, MS3, MD4, MS4, M1, M2, M3, M4,number;
String Str;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {

  // put your main code here, to run repeatedly:
  M1 = random(-255, 256);
  M2 = random(-255, 256);
  M3 = random(-255, 256);
  M4 = random(-255, 256);
  
  if (M1>=0){
    MD1=1;}
  else{
    MD1 = 0;};
  if (M2>=0){
    MD2=1;}
  else{
    MD2 = 0;};
  if (M3>=0){
    MD3=1;}
  else{
    MD3 = 0;};
  if (M4>=0){
    MD4=1;}
  else{
    MD4 = 0;};
  MS1= abs(M1);
  MS2= abs(M2);
  MS3= abs(M3);
  MS4= abs(M4);

  Serial.println('S'+String(MD1)+sifirci(MS1)+
                 String(MD2)+sifirci(MS2)+
                 String(MD3)+sifirci(MS3)+
                 String(MD4)+sifirci(MS4)+'F');
  delay(500);
}

String sifirci(int number) {
  String result;
  if (number>99){
    result= String(number);}
    else if(number>9){
      result= ("0"+String(number));}
      else{
        result=("00"+String(number));};
   return result;     }
