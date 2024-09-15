import xlsxwriter

# IP adresleri ve bunlara karşılık gelen hostname'leri içeren bir sözlük oluştur

xxx yerine iP yaz 
ip_hostname_map = {
    "(xxx.xxx.xxx.xxx)" : "hostname"
}

# Excel dosyasını oluştur
workbook = xlsxwriter.Workbook('nmap_scan_results.xlsx')
worksheet = workbook.add_worksheet()

# Başlık satırını ekle
worksheet.write('A1', 'IP Adresi')
worksheet.write('B1', 'Hostname')
worksheet.write('C1', 'Port Durumu')

# İlk satırdan başla
row = 1

# IP adreslerini ve port bilgilerini Excel dosyasına ekle
with open('nmap_scan_results.txt', 'r') as file:
    ip_address = ''
    port_list = []
    for line in file:
        if 'Nmap scan report' in line:
            # Bir sonraki IP adresine geçildiğinde, mevcut IP adresini ve port bilgilerini Excel dosyasına ekle
            if ip_address:
                hostname = ip_hostname_map.get(ip_address, "Unknown")
                worksheet.write(row, 0, ip_address)
                worksheet.write(row, 1, hostname)
                worksheet.write(row, 2, ', '.join(port_list))
                row += 1
                port_list = []

            ip_address = line.split()[-1]
        elif 'open' in line:
            port = line.split('/')[0]
            port_list.append(port)

    # Dosyanın sonunda, mevcut IP adresini ve port bilgilerini Excel dosyasına ekle
    if ip_address:
        hostname = ip_hostname_map.get(ip_address, "Unknown")
        worksheet.write(row, 0, ip_address)
        worksheet.write(row, 1, hostname)
        worksheet.write(row, 2, ', '.join(port_list))

# Excel dosyasını kapat
workbook.close()

print('Excel dosyası güncellendi: nmap_scan_results.xlsx')
