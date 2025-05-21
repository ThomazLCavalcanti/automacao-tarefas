# ⚙️ Automação de Tarefas com Python

Este projeto foi desenvolvido para automatizar tarefas rotineiras no sistema, como organização de arquivos, backups, cliques automáticos e agendamentos programados.

---

## 🚀 Funcionalidades

- 🗂️ Organização de arquivos por tipo
- 💾 Backup automático de diretórios
- 🖱️ Simulação de cliques com `pyautogui`
- ⏰ Execução periódica com `schedule`

---

## 🧰 Tecnologias Utilizadas

- [Python 3](https://www.python.org/)
- [`schedule`](https://pypi.org/project/schedule/) – agendador de tarefas
- [`pyautogui`](https://pypi.org/project/PyAutoGUI/) – automação de mouse/teclado
- Bibliotecas padrão: `os`, `shutil`, `datetime`, `time`

---

## 🛠️ Pré-requisitos

- Python 3 instalado (recomenda-se Python 3.10+)
- Git (opcional, para clonar o repositório)

---

## ⚙️ Instalação e Execução

### 1. Clone o repositório:

```bash
git clone https://github.com/ThomazLCavalcanti/automacao-tarefas-python.git
cd automacao-tarefas-python
```

### 2. Crie e ative o ambiente virtual:

```bash
python3 -m venv venv
venv\Scripts\activate
```

### 3. Instale as dependências:

```bash
pip install -r requirements.txt
```

### 4. Execute o programa:

```bash
python automacao_tarefas.py
```

---

## 🧪 Observações

- O script precisa rodar continuamente para as tarefas agendadas funcionarem.
- `pyautogui` simula cliques, então evite mexer no mouse enquanto ele estiver ativo.
- Edite os caminhos das pastas no código conforme sua máquina.

---

## 📄 Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

---

## 🤝 Contato

Feito por Thomaz — entre em contato pelo GitHub: [@ThomazLCavalcanti](https://github.com/ThomazLCavalcanti/)
