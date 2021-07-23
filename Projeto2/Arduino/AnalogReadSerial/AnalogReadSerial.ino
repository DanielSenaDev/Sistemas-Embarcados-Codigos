void setup() {
  // Definindo os pins 8, 9, 10 e 11 como entrada
  pinMode(8, INPUT_PULLUP);
  pinMode(9, INPUT_PULLUP);
  pinMode(10, INPUT_PULLUP);
  pinMode(11, INPUT_PULLUP);

  // Iniciar comunicacao serial a 9600 bits por segundos
  Serial.begin(9600);
}

// Loop que ira verificar se um botao foi acionado e enviar um codigo atraves da porta serial caso verdade
void loop() {
  // Leitura para saber se o botao foi pressionado
  int bt1 = digitalRead(8);
  int bt2 = digitalRead(9);
  int bt3 = digitalRead(10);
  int bt4 = digitalRead(11);

  //Funcoes que irao enviar um codigo especifico para cada botao pressionado atraves da porta serial
  
  //Button1
  if(bt1==0){
    Serial.println("bt1");
  }

  //Button2
  if(bt2==0){
    Serial.println("bt2");
  }

  //Button3
  if(bt3==0){
    Serial.println("bt3");
  } 

  //Button4
  if(bt4==0){
    Serial.println("bt4");
  }  
  
  _delay_ms(100); //Delay que irá ajudar a não ocorrer spam quando apertar um botão
}
