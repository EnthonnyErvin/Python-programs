# Python-programs

# Gerador de CPF

Este projeto em Python gera números de CPF válidos conforme as regras de validação adotadas no Brasil.

## 🖍 Descrição
O programa realiza os cálculos necessários para gerar os dois dígitos verificadores de um CPF com base nos nove primeiros dígitos gerados aleatoriamente. Ele utiliza as regras definidas pela Receita Federal para garantir que o CPF gerado seja válido.

### Principais Etapas:
1. Geração aleatória dos **nove primeiros dígitos** do CPF.
2. Cálculo do **primeiro dígito verificador**.
3. Cálculo do **segundo dígito verificador**.
4. Combinação dos valores para formar um CPF válido.

---

## Validador de CPF

Este programa em Python valida um CPF fornecido pelo usuário, verificando se ele segue as regras de formação oficial do Brasil.

### Principais Etapas:
1. Recebe um CPF inserido pelo usuário.
2. Remove quaisquer caracteres não numéricos.
3. Verifica se todos os dígitos do CPF são iguais (sequenciais), caso em que é considerado inválido.
4. Calcula os dois dígitos verificadores com base nos nove primeiros dígitos fornecidos.
5. Compara o CPF fornecido pelo usuário com o CPF gerado pelo cálculo para determinar sua validade.

---

## 🚀 Como Executar

1. Certifique-se de que você tem o Python instalado no seu computador.
2. Salve o código em um arquivo chamado `gerador_cpf.py` ou `validador_cpf.py`, conforme o objetivo.
3. Execute o script no terminal com o seguinte comando:

### Para o gerador:
```bash
python gerador_cpf.py
```

### Para o validador:
```bash
python validador_cpf.py
```

### Exemplo de Saída do Validador:

```text
CPF: 123.456.789-09

CPF recebido: 123.456.789-09
O primeiro dígito do CPF é: 0
O segundo dígito do CPF é: 9
O CPF 123.456.789-09 é validado!
```

---

## 📦 Dependências

Nenhuma biblioteca externa é necessária. Ambos os códigos utilizam apenas bibliotecas nativas do Python.

---

## 🔧 Personalização
Se desejar personalizar o programa, você pode:
- Modificar a lógica para validar múltiplos CPFs em uma lista.
- Adaptar o código para salvar os resultados em um arquivo.

---

## 📌 Objetivos de Estudo

Este código foi criado como um estudo de caso para praticar:
- Lógica de programação.
- Manipulação de strings.
- Uso de loops e cálculos matemáticos.
- Validação de entrada do usuário.

---

## 🛡️ Licença

Este projeto é de uso livre e não possui licença específica. Sinta-se à vontade para modificar, reutilizar ou distribuir.

---

### 🌟 Autor
- **[Enthonny Ervin]**