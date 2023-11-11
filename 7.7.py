so_tien_muon_doi = 1375000
so_to_1 = so_tien_muon_doi // 500000
tien_con_lai = so_tien_muon_doi % 500000
so_to_2 = tien_con_lai // 200000
tien_con_lai = tien_con_lai % 200000
so_to_3 = tien_con_lai // 100000
tien_con_lai = tien_con_lai % 100000
so_to_4 = tien_con_lai // 50000
tien_con_lai = tien_con_lai % 50000 
print('đổi tiền 1375000=', so_to_1, so_to_2, so_to_3, so_to_4)
print('tiền còn lại:', tien_con_lai)
