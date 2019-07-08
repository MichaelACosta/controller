# Controller

Este layer é utilizado para interpretar os comandos passado pelo ROS e comunicar com os arduinos para fornecer os movimentos necessários, toda controle de movimento está descrito neste layer.

O arquivo controller.py é responsavel por receber os valores do ROS comunicar com arduino e calcular o valor do stop.

## Entrada

As publicações dos comandos são feitas no canal walk em formato de string.

Para um Go Ahead é passado por exemplo a string 'goAhead 1 175', onde goAhead é o comando, 1 é o valor em metros e 175 é o valor a ser passado para o PWM.
Para um Turn Left é passado por exemplo a string 'turnLeft 90', onde turnLeft é o comando e 90 o valor em graus.
Para um Turn Right é passado por exemplo a string 'turnRight 30', onde turnRight é o comando e 30 o valor em graus.

O menor valor passado para um Go Ahead pode ser 0,003 que é equivalente a 0,3cm.

## Theta

Possui 0,34cm de diametro nas rodas e 0,45cm de distancia entre as rodas.
Assim, sua roda possui aproximadamente 1,0676cm de circunferencia.
O odômetro possui um total de 300 pulsos, onde um pulso movimenta 0,003cm.
Para movimentar 360 graus deve ser movimentada 3,39292cm uma das rodas, este valor equivale a 952 pulsos do odômetro.

### Go Ahead

Será zerado o contador interno do arduino para iniciar o movimento para frente, para isto será publicado um true no canal pattern.
Publicando o valor passado como parametro, pwmValue, no channel_y você obterá o movimento para frente.
Para garantir que o comando movimente o Theta para frente, é feito um controle que não permite valores abaixo de 175 nem acima de 205.
Os canais left_sensor e right_sensor obtém a contagem de pulsos obtidas no odômetro pelo arduino.
O comando go ahead movimento o Theta por 1 metro, assim obtendo 300 pulsos nos dois canais de odometria.

#### Stop Go Ahead

Para o controle de parada os canais left_sensor e right_sensor são utilizados.
O cálculo para isto é (value/300.0)*circumference >= distance.
Sendo que distance é 1, referente a 1 metro, a circumference é 3,14*0,34 e value é o número de pulsos obtidos por cada canal.
Este cálculo deve ser executado para cada pulso obtido pelos dois canais.

### Turn Left e Turn Hight

Os comandos Turn Left e Turn Hight evetuam o movimento de girar a quantidade de graus passado pelo comando para esquerda ou para direita.
Será zerado o contador interno do arduino para iniciar os movimentos, para isto será publicado um true no canal pattern.

Para o turn left é aplicado o valor 170 no channel_x.
Para o turn right é aplicado o valor 100 no channel_x.

O valor passado em graus é convertido para metros e é movimentado esta metragem com a roda oposta a direção de movimento.

#### Conversão de graus para metros

Para converter o valor de graus para metros é utilizado o valor da circunferência percorrida pelo Theta em uma volta de 360 graus.
Considerando o diametro de 1,08cm para rotacionar 360 graus será percorrido 3,3912cm em torno de uma das rodas.
Portanto, o calculo (3,3912\*degre)/360, sendo degre o valor em graus para rotacionar, indica o valor em metros a ser percorrido.

#### Stop Turn Left e Turn Hight

Para parar o movimento é utilizado o mesmo cálculo do stop go ahead, passando a metragem calculada a partir do valor em graus.
Para movimentar para esquerda é calculado o movimento da roda direita.
Para movimentar para direita é calculado o movimento da roda esquerda.

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
