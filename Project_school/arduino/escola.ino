// arduino/escola.ino
// Código do Arduino para controlar os LEDs da escola
// Recebe comandos do Python pelo cabo USB

// ── Definição dos pinos ──────────────────────────────
#define SALA1      2   // LED da Sala 1
#define SALA2      3   // LED da Sala 2
#define COORDENACAO 4  // LED da Coordenação
#define QUADRA1    5   // LED da Quadra 1
#define QUADRA2    6   // LED da Quadra 2
#define QUADRA3    7   // LED da Quadra 3

void setup() {
  // Inicia a comunicação serial com o Python
  // 9600 é a velocidade — tem que ser igual no Python!
  Serial.begin(9600);

  // Define todos os pinos como saída
  pinMode(SALA1,       OUTPUT);
  pinMode(SALA2,       OUTPUT);
  pinMode(COORDENACAO, OUTPUT);
  pinMode(QUADRA1,     OUTPUT);
  pinMode(QUADRA2,     OUTPUT);
  pinMode(QUADRA3,     OUTPUT);

  // Garante que tudo começa apagado
  digitalWrite(SALA1,       LOW);
  digitalWrite(SALA2,       LOW);
  digitalWrite(COORDENACAO, LOW);
  digitalWrite(QUADRA1,     LOW);
  digitalWrite(QUADRA2,     LOW);
  digitalWrite(QUADRA3,     LOW);

  Serial.println("Arduino pronto!");
}

void loop() {
  // Fica esperando comandos do Python
  if (Serial.available() > 0) {
    // Lê o comando até encontrar \n
    String comando = Serial.readStringUntil('\n');
    comando.trim(); // remove espaços e \r

    Serial.print("Recebi: ");
    Serial.println(comando);

    // ── Sala 1 ──────────────────────────────────────
    if (comando == "LIGA_SALA1") {
      digitalWrite(SALA1, HIGH);
      Serial.println("Sala 1 ligada!");
    }
    else if (comando == "APAGA_SALA1") {
      digitalWrite(SALA1, LOW);
      Serial.println("Sala 1 apagada!");
    }

    // ── Sala 2 ──────────────────────────────────────
    else if (comando == "LIGA_SALA2") {
      digitalWrite(SALA2, HIGH);
      Serial.println("Sala 2 ligada!");
    }
    else if (comando == "APAGA_SALA2") {
      digitalWrite(SALA2, LOW);
      Serial.println("Sala 2 apagada!");
    }

    // ── Coordenação ─────────────────────────────────
    else if (comando == "LIGA_COORD") {
      digitalWrite(COORDENACAO, HIGH);
      Serial.println("Coordenação ligada!");
    }
    else if (comando == "APAGA_COORD") {
      digitalWrite(COORDENACAO, LOW);
      Serial.println("Coordenação apagada!");
    }

    // ── Quadra ──────────────────────────────────────
    else if (comando == "LIGA_QUADRA") {
      digitalWrite(QUADRA1, HIGH);
      digitalWrite(QUADRA2, HIGH);
      digitalWrite(QUADRA3, HIGH);
      Serial.println("Quadra ligada!");
    }
    else if (comando == "APAGA_QUADRA") {
      digitalWrite(QUADRA1, LOW);
      digitalWrite(QUADRA2, LOW);
      digitalWrite(QUADRA3, LOW);
      Serial.println("Quadra apagada!");
    }

    // ── Tudo junto ──────────────────────────────────
    else if (comando == "LIGA_TUDO") {
      digitalWrite(SALA1,       HIGH);
      digitalWrite(SALA2,       HIGH);
      digitalWrite(COORDENACAO, HIGH);
      digitalWrite(QUADRA1,     HIGH);
      digitalWrite(QUADRA2,     HIGH);
      digitalWrite(QUADRA3,     HIGH);
      Serial.println("Tudo ligado!");
    }
    else if (comando == "APAGA_TUDO") {
      digitalWrite(SALA1,       LOW);
      digitalWrite(SALA2,       LOW);
      digitalWrite(COORDENACAO, LOW);
      digitalWrite(QUADRA1,     LOW);
      digitalWrite(QUADRA2,     LOW);
      digitalWrite(QUADRA3,     LOW);
      Serial.println("Tudo apagado!");
    }

    else {
      Serial.print("Comando desconhecido: ");
      Serial.println(comando);
    }
  }
}