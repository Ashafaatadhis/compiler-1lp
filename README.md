# 1L Programming Language Compiler

Compiler sederhana untuk bahasa **1L**, dibangun menggunakan **Python + SLY** (library modern berbasis Lex/Yacc).  
Tujuan project ini adalah mempelajari dasar-dasar pembangunan compiler: mulai dari _lexing_, _parsing_, _AST_, hingga _interpretation_.

---

## 🚀 1. Overview

Compiler ini memproses program 1L melalui beberapa tahap:

```
Program → Lexer → Token → Parser → AST → Interpreter → Output
```

1. **Frontend**

   - Lexer (tokenizer)
   - Parser (AST builder)
   - Grammar rules

2. **Backend**
   - Interpreter (eksekusi)
   - (Opsional) Code generation

---

## 📚 2. Tata Bahasa (Grammar)

Grammar bahasa 1L ditulis dalam bentuk Context-Free Grammar (CFG):

```
Stm     → Stm ; Stm
Stm     → id := Exp
Stm     → print(ExpList)

Exp     → id
Exp     → num
Exp     → Exp Binop Exp
Exp     → (Stm , Exp)

ExpList → Exp , ExpList
ExpList → Exp

Binop   → + | - | * | /
```

---

## 🧩 3. Struktur Proyek

```
compiler-1lp/
│
├── lexer.py
├── parser.py
├── interpreter.py
├── main.py
│
├── examples/
│   └── sample1.1l
│
└── README.md
```

---

## 🔍 4. Frontend Compiler

### 4.1 Lexer

Lexer bertugas membaca karakter input dan mengubahnya menjadi token.

### 4.2 Parser

Parser mengubah token menjadi AST sesuai grammar.

---

## 🌳 5. Abstract Syntax Tree (AST)

AST adalah representasi struktur logis program.

---

## ⚙️ 6. Backend — Interpreter

Interpreter membaca AST dan menjalankan program dengan menggunakan environment variabel.

---

## 📝 7. Contoh Program Bahasa 1L

### Contoh 1

```
x := 10 + 5;
y := x * 2;
print(x, y)
```

Output:

```
15 30
```

---

### Contoh 2 — Esequent Expression

```
x := (print(3, 4), 10);
print(x)
```

Output:

```
3 4
10
```

---

## ▶️ 8. Cara Menjalankan

### Install dependencies:

```
pip install sly
```

### Jalankan compiler:

```
python main.py
```

---

## 🌟 10. Pengembangan Lanjut

- IF / ELSE
- WHILE
- Functions
- Code generation

---

## 🏁 11. Kesimpulan

Compiler ini menunjukkan dasar-dasar konstruksi sebuah compiler:

✔ Lexer  
✔ Parser  
✔ AST  
✔ Interpreter

---
