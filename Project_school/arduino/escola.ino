// arduino/escola.ino
// Código do Arduino para controlar os LEDs da escola
// Recebe comandos do Python pelo cabo USB

// ── Definição dos pinos ──────────────────────────────
#define SALA1       2   // LED da Sala 1
#define SALA2       3   // LED da Sala 2
#define COORDENACAO 4   // LED da Coordenação
#define QUADRA1     5   // LED da Quadra
#define PATIO       6   // LED Pátio
#define PORTAO1     7   // LED Portão 
#define PORTA_COORD 8   // LED Porta Coordenação

void setup() {
  Serial.begin(9600);

  // Define todos os pinos como saída
  pinMode(SALA1,       OUTPUT);
  pinMode(SALA2,       OUTPUT);
  pinMode(COORDENACAO, OUTPUT);
  pinMode(QUADRA1,     OUTPUT);
  pinMode(PATIO,       OUTPUT);
  pinMode(PORTAO1,     OUTPUT);
  pinMode(PORTA_COORD, OUTPUT);

  // Garante que tudo começa apagado
  digitalWrite(SALA1,       LOW);
  digitalWrite(SALA2,       LOW);
  digitalWrite(COORDENACAO, LOW);
  digitalWrite(QUADRA1,     LOW);
  digitalWrite(PATIO,       LOW);
  digitalWrite(PORTAO1,     LOW);
  digitalWrite(PORTA_COORD, LOW);

  Serial.println("Arduino pronto!");
}

void loop() {
  if (Serial.available() > 0) {
    String comando = Serial.readStringUntil('\n');
    comando.trim();

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

    // ── Quadra (1 LED) ───────────────────────────────
    else if (comando == "LIGA_QUADRA") {
      digitalWrite(QUADRA1, HIGH);
      Serial.println("Quadra ligada!");
    }
    else if (comando == "APAGA_QUADRA") {
      digitalWrite(QUADRA1, LOW);
      Serial.println("Quadra apagada!");
    }

    // ── Pátio ────────────────────────────────────────
    else if (comando == "LIGAR_PATIO") {
      digitalWrite(PATIO, HIGH);
      Serial.println("Pátio ligado!");
    }
    else if (comando == "APAGA_PATIO") {
      digitalWrite(PATIO, LOW);
      Serial.println("Pátio apagado!");
    }

    // ── Portão (1 LED) ───────────────────────────────
    else if (comando == "ABRIR_PORTAO") {
      digitalWrite(PORTAO1, HIGH);
      Serial.println("Portão aberto!");
    }
    else if (comando == "FECHAR_PORTAO") {
      digitalWrite(PORTAO1, LOW);
      Serial.println("Portão fechado!");
    }

    // ── Porta Coordenação ────────────────────────────
    else if (comando == "ABRIR_COORD") {
      digitalWrite(PORTA_COORD, HIGH);
      Serial.println("Porta coordenação aberta!");
    }
    else if (comando == "FECHAR_COORD") {
      digitalWrite(PORTA_COORD, LOW);
      Serial.println("Porta coordenação fechada!");
    }

    // ── Tudo junto ───────────────────────────────────
    else if (comando == "LIGA_TUDO") {
      digitalWrite(SALA1,       HIGH);
      digitalWrite(SALA2,       HIGH);
      digitalWrite(COORDENACAO, HIGH);
      digitalWrite(QUADRA1,     HIGH);
      digitalWrite(PATIO,       HIGH);
      digitalWrite(PORTAO1,     HIGH);
      digitalWrite(PORTA_COORD, HIGH);
      Serial.println("Tudo ligado!");
    }
    else if (comando == "APAGA_TUDO") {
      digitalWrite(SALA1,       LOW);
      digitalWrite(SALA2,       LOW);
      digitalWrite(COORDENACAO, LOW);
      digitalWrite(QUADRA1,     LOW);
      digitalWrite(PATIO,       LOW);
      digitalWrite(PORTAO1,     LOW);
      digitalWrite(PORTA_COORD, LOW);
      Serial.println("Tudo apagado!");
    }

    else {
      Serial.print("Comando desconhecido: ");
      Serial.println(comando);
    }
  }
}