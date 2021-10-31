nama = str(input("Nama Pegawai    : ")) 
jam = int(input("jumlah jam kerja  :")) 
upah = int(input("upah perjam      :")) 

if jam >= 8 : 
    lembur = jam - 8
    rumus= 8 * jam * upah + 8 * upah 
else :
        rumus = jam + upah 
total = upah * jam + 8* upah *6 
        
print ("jumlah Gaji lembur Per Hari     :",rumus) 
print("jumlah gaji lembur satu minggu    :",total) 
print("Keterangan") 
print("jumlah jam lembur setiap harinya adalah dalam satu minggu")
