#!/bin/bash

#$1 = url

while true
do
    #curl $1/export/txt > livegraphviz.dot
    #dot -Tpng livegraphviz.dot -O
    dot -Tpng adversarial-design.dot > adversarial-design.png
    sleep 5
done
