# Controller

Este layer é utilizado para interpretar os comandos passado pelo ROS e comunicar com os arduinos para fornecer os movimentos necessários, toda controle de movimento está descrito neste layer.

O arquivo controller.py é responsavel por receber os valores do ROS comunicar com arduino.

## Entrada

As publicações dos comandos são feitas no canal walk em formato de string.

Para um Go Ahead é passado por exemplo a string 'goAhead 1 175', onde goAhead é o comando, 1 é o valor em metros e 175 é o valor a ser passado para o PWM.
Para um Turn Left é passado por exemplo a string 'turnLeft 90', onde turnLeft é o comando e 90 o valor em graus.
Para um Turn Right é passado por exemplo a string 'turnRight 30', onde turnRight é o comando e 30 o valor em graus.

O menor valor passado para um Go Ahead pode ser 0,00089 que é equivalente a 0,08cm.

## Theta

### Configuração

#### Roda

Possui 0,34m de diametro nas rodas e 0,45m de distancia entre as rodas.
Assim, sua roda possui aproximadamente 1,0676m de circunferencia.

#### Odometro

O odômetro possui um total de 1200 pulsos, onde um pulso movimenta 0,00089m.
Para movimentar 360 graus deve ser movimentada 1,69646003m em uma das rodas, este valor é aproximadamente 1898 pulsos do odômetro.

### Go Ahead

Será zerado o contador interno do arduino para iniciar o movimento para frente, para isto será publicado um true no canal pattern.
O valor, pulseValue, será publicado no canal pulse do ros para o controle da distância percorrida ser feito pelo arduino.
Publicando o valor passado como parametro, pwmValue, no channel_y você obterá o movimento para frente.
Para garantir que o comando movimente o Theta para frente, é feito um controle que não permite valores abaixo de 175 nem acima de 205.

### Turn Left e Turn Hight

Os comandos Turn Left e Turn Hight evetuam o movimento de girar a quantidade de graus passado pelo comando para esquerda ou para direita.
Será zerado o contador interno do arduino para iniciar os movimentos, para isto será publicado um true no canal pattern.
O valor, pulseValue, será publicado no canal pulse do ros para o controle da distância percorrida ser feito pelo arduino.

Para o turn left é aplicado o valor 170 no channel_x.
Para o turn right é aplicado o valor 100 no channel_y.

O valor passado em graus é convertido para metros e é movimentado esta metragem com a roda oposta a direção de movimento.
Para o arduino controlar o momento de parar o movimento o valor convertido em metros é novamente convertido em pulsos.

#### Conversão de graus para metros

Para converter o valor de graus para metros é utilizado o valor da circunferência percorrida pelo Theta em uma volta de 360 graus.
Considerando o diametro de 0,54m para rotacionar 360 graus será percorrido 1,69646003m em torno de uma das rodas.
Portanto, o calculo (1,6964\*degre)/360, sendo degre o valor em graus para rotacionar, indica o valor em metros a ser percorrido.

### Conversão de metros para pulsos

Para converter o valor de metros para pulsos é utilizado o valor da circunferência da roda, diâmetro\*pi (0,34\*3,14).
Considerando o diametro de 0,34m.
Portanto, o calculo é (distance/1,0681415)\*1200, sendo distance o valor em metros a ser percorrido.

### Valores de PWM

pwmX movimento para os lados

pwmY movimento para frente e ré

---

pwm +-135 --> parado

---

pwm 55 --> máximo ré e direita

pwm 100 --> mínimo ré e direita

---

pwm 170 --> mínimo frente e esquerda

pwm 205 --> máximo frente e esquerda
