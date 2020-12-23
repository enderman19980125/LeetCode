cat words.txt | tr -s ' ' | tr ' ' '\n' | tr -s '\n' | sort | uniq -c | sort -r | awk '{print $2,$1}'
