#!bin/sh

curl -L -o "data.csv" "https://docs.google.com/spreadsheets/d/${GDRIVE_DOCUMENT_ID}/export?format=csv&gid=${GDRIVE_SHEET_ID}"

python3 formatter.py

members=$(cat members.json)

cd /pelican
pelican -d content
