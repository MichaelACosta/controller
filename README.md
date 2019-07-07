# Controller

Este layer é utilizado para interpretar os comandos passado pelo ROS e comunicar com os arduinos para fornecer os movimentos necessários, toda controle de movimento está descrito neste layer.

## Theta

Possui 0,34cm de diametro nas rodas e 0,45cm de distancia entre as rodas.
Assim, sua roda possui aproximadamente 1,0676cm de circunferencia.
O odômetro possui um total de 300 pulsos, onde um pulso movimenta 0,003cm.
Para movimentar 360 graus deve ser movimentada 3,39292cm uma das rodas, este valor equivale a 952 pulsos do odômetro.

## Go Ahead

Será zerado o contador interno do arduino para iniciar o movimento para frente, para isto será publicado um true no canal pattern.
Publicando o valor 175 no channel_y você obtera o movimento para frente.
Os canais left_sensor e right_sensor obtém a contagem de pulsos obtidas no odômetro pelo arduino.
O comando go ahead movimento o Theta por 1 metro, assim obtendo 300 pulsos nos dois canais de odometria.

### Stop GO Ahead

Para o controle de parada os canais left_sensor e right_sensor são utilizados.
O cálculo para isto é (value/300.0)*circumference >= distance.
Sendo que distance é 1, referente a 1 metro, a circumference é 3,14*0,34 e value é o número de pulsos obtidos por cada canal.
Este cálculo deve ser executado para cada pulso obtido pelos dois canais.

## Turn Left e Turn Hight

Os comandos Turn Left e Turn Hight evetuam o movimento de girar 90 graus para esquerda e direita.
Será zerado o contador interno do arduino para iniciar os movimentos, para isto será publicado um true no canal pattern.

Para o turn left é aplicado o valor 170 no channel_x.
Para o turn right é aplicado o valor 100 no channel_x.

### Stop Turn Left e Turn Hight

Para parar o movimento é avaliado o valor de odometria da roda aposta ao lado que deseja movimentar.
O cálculo parar parar é, value >= 100, sendo value os pulsos passado pelo odometro.

## Valores de PWM

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
