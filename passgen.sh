#!/bin/bash

echo "Enter password length:"

python3 passgen.py | grep -v ":" > newpass.txt

cat newpass.txt

echo "Copy your password"
