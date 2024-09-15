#!/bin/bash


rm nmap_scan_results.txt

#liste=(xxx.xxx.xxx.xxx yyy.yyy.yyy.yyy)

for IP_adresi in "${liste[@]}"; do


        IP="$IP_adresi"
        # Tarama sonuçlarını tutacak bir dosya oluştur
        output_file="nmap_scan.txt"
        last="nmap_scan_results.txt"
        echo "$IP adresi icin tarama baslatildi"
        # Nmap ile port taraması yap
        nmap_output=$(nmap -p- -T4 -Pn $IP)


        # Açık portları filtrele ve dosyaya yaz
        echo "$nmap_output" | awk '/^PORT/ || /open/ || /^Nmap scan/ {print}' | grep -iv "Discovered"  > "$output_file"

        # Açık port sayısını belirle
        open_ports=$(cat "$output_file" | grep open | wc -l)

        echo -e "\nToplam $open_ports adet açık port bulunmaktadır.\n\n" >> $output_file

        if grep -q "open" "$output_file"; then

                cat "$output_file" >> "$last"
        fi



done
echo -e "\n\n"
cat "$last"
