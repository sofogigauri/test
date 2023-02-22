name: sofo

on: 
push:
branches: [ "main", ]
pull_request:
branchs: [ "main"]





jobs:
hello:

runs-on: ubuntu-latest


steps:
- name: hello step
  run : echo "hello forom github actions!"
  
  
bye:
runs-on ubuntu-latest
steps:
- name: bye step
 run : echo "bye bye!"
